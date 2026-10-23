"""Validate the documented Markdown subset and spec/skill metadata, offline."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml
from markdown_it import MarkdownIt

SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
ANCHOR = re.compile(r'<a\s+id=[\"\']([a-z0-9-]+)[\"\']\s*>')
MD = MarkdownIt("commonmark", {"html": True})
COMMENTS = re.compile(r"<!--.*?(?:-->|\Z)", re.DOTALL)
PR_SECTIONS = (
    "Resultaat", "Specificatie", "Documentatie en begrippen",
    "Ketengevolgen", "Bewijs", "Open punten",
)


class UniqueLoader(yaml.SafeLoader):
    """Duplicate YAML keys are mistakes, not silent overrides."""


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"dubbele YAML-sleutel: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


@dataclass
class Document:
    path: Path
    meta: dict
    anchors: set[str]
    links: list[str]
    criteria: list[str]


def parse(path: Path, text: str) -> Document:
    meta = {}
    lines = text.splitlines()
    if lines and lines[0] == "---":
        try:
            end = lines.index("---", 1)
        except ValueError as exc:
            raise ValueError("frontmatter mist afsluitende ---") from exc
        meta = yaml.load("\n".join(lines[1:end]), Loader=UniqueLoader)
        if not isinstance(meta, dict):
            raise ValueError("frontmatter moet een mapping zijn")
        text = "\n".join(lines[end + 1:])
    anchors, links, criteria = set(), [], []
    heading_counts = {}
    tokens = MD.parse(text)
    for index, token in enumerate(tokens):
        if token.type == "heading_open":
            inline = tokens[index + 1]
            label = "".join(t.content for t in (inline.children or [])
                            if t.type in {"text", "code_inline"})
            slug = re.sub(r"[^\w\- ]", "", label.lower()).replace(" ", "-")
            count = heading_counts.get(slug, 0)
            heading_counts[slug] = count + 1
            anchors.add(slug if count == 0 else f"{slug}-{count}")
        for child in [token, *(token.children or [])]:
            if child.type in {"link_open", "image"}:
                links.append(child.attrGet("href") or child.attrGet("src") or "")
            if child.type in {"html_inline", "html_block"}:
                for anchor in ANCHOR.findall(COMMENTS.sub("", child.content)):
                    if anchor in anchors:
                        raise ValueError(f"dubbel anker: {anchor}")
                    anchors.add(anchor)
                    if anchor.startswith("ac-"):
                        criteria.append(anchor)
    return Document(path, meta, anchors, links, criteria)


def documents(root: Path) -> list[Path]:
    """Only maintained documentation, not environments or ignored scratch."""
    paths = [root / name for name in ("README.md", "AGENTS.md") if (root / name).exists()]
    for folder in ("docs", ".agents/skills", ".github"):
        paths.extend((root / folder).rglob("*.md"))
    return sorted(set(paths))


def check(root: Path) -> list[str]:
    root = root.resolve()
    errors, docs = [], {}
    for path in documents(root):
        try:
            docs[path.resolve()] = parse(path, path.read_text(encoding="utf-8"))
        except (ValueError, TypeError, yaml.YAMLError) as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")

    specs, criteria = {}, {}
    for path, doc in docs.items():
        rel = path.relative_to(root).as_posix()
        for link in doc.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue  # external availability is deliberately not a network gate
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not target.is_relative_to(root) or not target.exists():
                errors.append(f"{rel}: ongeldig lokaal doel: {link}")
                continue
            if url.fragment:
                if target not in docs:
                    errors.append(f"{rel}: ankerdoel valt buiten gecontroleerde Markdown: {link}")
                elif unquote(url.fragment) not in docs[target].anchors:
                    errors.append(f"{rel}: onbekend anker: {link}")
        if rel.startswith("docs/specs/"):
            meta = doc.meta
            ident = meta.get("id")
            if not isinstance(ident, str) or not SLUG.fullmatch(ident):
                errors.append(f"{rel}: ontbrekende of ongeldige specificatie-ID")
                continue
            if ident in specs:
                errors.append(f"{rel}: dubbele specificatie-ID {ident}")
            specs[ident] = doc
            if meta.get("status") not in {"draft", "accepted", "superseded"}:
                errors.append(f"{rel}: ongeldige status")
            deps = meta.get("depends_on")
            if not isinstance(deps, list) or any(not isinstance(d, str) for d in deps):
                errors.append(f"{rel}: depends_on moet een lijst IDs zijn")
            if meta.get("status") == "accepted":
                decision = meta.get("decision", "")
                if not isinstance(decision, str) or not decision.startswith("https://"):
                    errors.append(f"{rel}: accepted mist decision-URL")
                if not doc.criteria:
                    errors.append(f"{rel}: accepted mist expliciete ac-criteria")
            for criterion in doc.criteria:
                if criterion in criteria:
                    errors.append(f"{rel}: dubbel criterium {criterion}")
                criteria[criterion] = rel
        if rel.startswith(".agents/skills/") and path.name == "SKILL.md":
            if doc.meta.get("name") != path.parent.name or not SLUG.fullmatch(path.parent.name):
                errors.append(f"{rel}: skillnaam moet overeenkomen met mapnaam")
            description = doc.meta.get("description")
            if not isinstance(description, str) or not 1 <= len(description) <= 1024:
                errors.append(f"{rel}: ongeldige skillbeschrijving")

    graph = {}
    for ident, doc in specs.items():
        deps = doc.meta.get("depends_on", [])
        if not isinstance(deps, list) or any(not isinstance(d, str) for d in deps):
            continue
        graph[ident] = deps
        for dep in deps:
            if dep not in specs:
                errors.append(f"{ident}: onbekende dependency {dep}")
            elif doc.meta.get("status") == "accepted" and specs[dep].meta.get("status") != "accepted":
                errors.append(f"{ident}: accepted vereist accepted dependency {dep}")
        if doc.meta.get("status") == "superseded":
            replacement = doc.meta.get("replaced_by")
            if not isinstance(replacement, str) or replacement == ident or replacement not in specs:
                errors.append(f"{ident}: superseded mist bestaande replaced_by-ID")
        if doc.meta.get("status") != "superseded":
            for link in doc.links:
                target = (doc.path.parent / unquote(urlsplit(link).path)).resolve()
                other = docs.get(target)
                if other and other.meta.get("status") == "superseded":
                    errors.append(f"{ident}: actieve specificatie linkt vervallen specificatie: {link}")

    visiting, visited = set(), set()

    def visit(ident):
        if ident in visiting:
            errors.append(f"{ident}: dependencycyclus")
            return
        if ident in visited:
            return
        visiting.add(ident)
        for dep in graph.get(ident, []):
            visit(dep)
        visiting.remove(ident)
        visited.add(ident)

    for ident in graph:
        visit(ident)
    return errors


def check_pr(body: str, root: Path | None = None,
             changed_files: list[str] | None = None) -> list[str]:
    tokens = MD.parse(body)
    sections = {}
    field_sections = {}
    active = None
    heading_content = False
    for index, token in enumerate(tokens):
        if token.type == "heading_open" and token.tag == "h2" and token.level == 0:
            active = tokens[index + 1].content
            sections[active] = []
            field_sections[active] = []
            heading_content = True
        elif token.type == "heading_close":
            heading_content = False
        elif active and not heading_content:
            if token.type == "inline":
                value = "".join("\n" if child.type in {"softbreak", "hardbreak"} else
                                COMMENTS.sub("", child.content)
                                if child.type == "html_inline" else child.content
                                for child in (token.children or []))
                sections[active].append(value)
                field_sections[active].append(value)
            elif token.type in {"fence", "code_block", "html_block"}:
                value = COMMENTS.sub("", token.content) if token.type == "html_block" else token.content
                sections[active].append(value)
    errors = []
    for title in PR_SECTIONS:
        value = "\n".join(sections.get(title, [])).strip()
        if not value or value.lower() in {"todo", "tbd", "..."}:
            errors.append(f"PR: vul sectie {title} in")

    def field(section: str, label: str) -> str:
        # Ignore code fences and HTML comments: examples are not declarations.
        if not "\n".join(sections.get(section, [])).strip():
            return ""  # the missing section was already reported
        values = re.findall(r"^" + re.escape(label) + r":[ \t]*([^\n]*)$",
                            "\n".join(field_sections.get(section, [])), re.MULTILINE)
        if len(values) != 1 or not values[0].strip() or values[0].strip().lower() in {
                "todo", "tbd", "...", "n.v.t.", "nvt"}:
            errors.append(f"PR: vul {label} eenmaal concreet in onder {section}")
            return ""
        return values[0].strip()

    field("Resultaat", "Binnen scope")
    field("Resultaat", "Buiten scope")
    choice = field("Documentatie en begrippen", "Documentatiekeuze")
    sources = field("Documentatie en begrippen", "Documentatiebronnen")
    field("Documentatie en begrippen", "Toelichting")
    if choice and choice not in {"bijgewerkt", "bestaand-volstaat"}:
        errors.append("PR: Documentatiekeuze moet bijgewerkt of bestaand-volstaat zijn")
    source_paths = []
    for source in sources.split(",") if sources else []:
        source = source.strip()
        url = urlsplit(source)
        path = Path(unquote(url.path))
        if (url.scheme or url.netloc or url.query or path.is_absolute()
                or ".." in path.parts or path.suffix != ".md"
                or not (path.as_posix() in {"AGENTS.md", "README.md"}
                        or path.parts[0] in {"docs", ".agents", ".github"})):
            errors.append(f"PR: ongeldige documentatiebron: {source}")
            continue
        source_paths.append(path.as_posix())
        if root is not None:
            target = (root / path).resolve()
            if not target.is_relative_to(root.resolve()) or not target.is_file():
                errors.append(f"PR: ontbrekende documentatiebron: {source}")
            elif url.fragment:
                try:
                    doc = parse(target, target.read_text(encoding="utf-8"))
                    if unquote(url.fragment) not in doc.anchors:
                        errors.append(f"PR: onbekend anker in documentatiebron: {source}")
                except (ValueError, TypeError, yaml.YAMLError):
                    errors.append(f"PR: onleesbare documentatiebron: {source}")
    if choice == "bijgewerkt" and changed_files is not None:
        if not set(source_paths).intersection(changed_files):
            errors.append("PR: bijgewerkt vereist minstens één gewijzigde documentatiebron in deze diff")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--pr-event", type=Path)
    args = parser.parse_args()
    errors = check(args.root)
    if args.pr_event:
        event = json.loads(args.pr_event.read_text(encoding="utf-8"))
        if "pull_request" in event:
            pr = event["pull_request"]
            base = pr.get("base", {}).get("sha", "")
            changed_files = None
            if not re.fullmatch(r"[0-9a-f]{40}", base):
                errors.append("PR: base-SHA ontbreekt voor documentatiecontrole op de diff")
            else:
                result = subprocess.run(["git", "diff", "--name-only", base, "HEAD"],
                                        cwd=args.root, text=True, capture_output=True)
                if result.returncode:
                    errors.append("PR: diff niet beschikbaar; haal de base-commit op")
                else:
                    changed_files = result.stdout.splitlines()
            errors.extend(check_pr(pr.get("body") or "", args.root, changed_files))
    for error in errors:
        print(error)
    print(f"Documentatiecontrole: {'FAIL' if errors else 'PASS'} ({len(errors)} fouten)")
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
