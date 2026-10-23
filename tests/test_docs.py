import tempfile
import unittest
from pathlib import Path

from tools.check_docs import check, check_pr, parse


class DocumentationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def spec(self, name="first", status="draft", deps="[]", extra="", criterion=None):
        criterion = criterion or f"ac-{name}-001"
        return self.write(f"docs/specs/{name}.md", f"""---
id: {name}
status: {status}
depends_on: {deps}
{extra}---
# {name}

<a id="{criterion}"></a>

Een observeerbaar resultaat.
""")

    def test_valid_relative_reference_and_explicit_anchor(self):
        self.spec()
        self.write("README.md", "[criterium][rule]\n\n[rule]: docs/specs/first.md#ac-first-001\n")
        self.assertEqual(check(self.root), [])

    def test_fenced_code_is_not_a_link(self):
        self.write("README.md", "```md\n[voorbeeld](missing.md)\n```\n")
        self.assertEqual(check(self.root), [])

    def test_missing_file_fails(self):
        self.write("README.md", "[ontbreekt](docs/absent.md)")
        self.assertTrue(any("ongeldig lokaal doel" in e for e in check(self.root)))

    def test_missing_anchor_fails(self):
        self.write("README.md", "# Start\n[stuk](#absent)")
        self.assertTrue(any("onbekend anker" in e for e in check(self.root)))

    def test_root_escape_fails_even_if_file_exists(self):
        self.write("README.md", "[systeem](/etc/passwd)")
        self.assertTrue(any("ongeldig lokaal doel" in e for e in check(self.root)))

    def test_duplicate_yaml_key_fails(self):
        self.write("docs/specs/a.md", "---\nid: a\nid: b\n---\n# A")
        self.assertTrue(any("dubbele YAML" in e for e in check(self.root)))

    def test_unknown_status_fails(self):
        self.spec(status="done")
        self.assertTrue(any("ongeldige status" in e for e in check(self.root)))

    def test_accepted_requires_decision(self):
        self.spec(status="accepted")
        self.assertTrue(any("decision-URL" in e for e in check(self.root)))

    def test_accepted_with_evidence_reference_is_valid(self):
        self.spec(status="accepted", extra="decision: https://example.org/decision\n")
        self.assertEqual(check(self.root), [])

    def test_duplicate_ids_and_criteria_fail(self):
        self.spec()
        self.write("docs/specs/duplicate.md", (self.root / "docs/specs/first.md").read_text())
        errors = check(self.root)
        self.assertTrue(any("dubbele specificatie-ID" in e for e in errors))
        self.assertTrue(any("dubbel criterium" in e for e in errors))

    def test_unknown_dependency_fails(self):
        self.spec(deps="[missing]")
        self.assertTrue(any("onbekende dependency" in e for e in check(self.root)))

    def test_dependency_cycle_fails(self):
        self.spec("first", deps="[second]")
        self.spec("second", deps="[first]")
        self.assertTrue(any("dependencycyclus" in e for e in check(self.root)))

    def test_accepted_cannot_depend_on_draft(self):
        self.spec("first", status="accepted", deps="[second]",
                  extra="decision: https://example.org/decision\n")
        self.spec("second")
        self.assertTrue(any("accepted dependency" in e for e in check(self.root)))

    def test_superseded_requires_replacement(self):
        self.spec(status="superseded")
        self.assertTrue(any("replaced_by" in e for e in check(self.root)))

    def test_live_spec_link_to_superseded_fails(self):
        self.spec("old", status="superseded", extra="replaced_by: new\n")
        self.spec("new")
        path = self.spec("consumer")
        path.write_text(path.read_text() + "\n[bron](old.md)\n")
        self.assertTrue(any("vervallen specificatie" in e for e in check(self.root)))

    def test_duplicate_explicit_anchor_fails(self):
        self.write("docs/glossary.md", '<a id="term-a"></a>\n\n<a id="term-a"></a>')
        self.assertTrue(any("dubbel anker" in e for e in check(self.root)))

    def test_skill_metadata_is_checked(self):
        self.write(".agents/skills/fresh-test/SKILL.md",
                   "---\nname: wrong\ndescription: Lees een concrete opdracht.\n---\n# Skill")
        self.assertTrue(any("skillnaam" in e for e in check(self.root)))

    def test_code_heading_is_not_anchor(self):
        doc = parse(Path("README.md"), "```md\n# Verborgen\n```\n# Echt")
        self.assertNotIn("verborgen", doc.anchors)
        self.assertIn("echt", doc.anchors)

    def test_pr_requires_sections(self):
        self.assertEqual(len(check_pr("")), 6)

    def test_unchanged_pr_template_fails(self):
        template = Path(__file__).resolve().parents[1] / ".github/pull_request_template.md"
        self.assertEqual(len(check_pr(template.read_text())), 6)

    def test_pr_headings_in_code_do_not_count(self):
        body = "```md\n" + "\n".join(f"## {title}\nVoorbeeld." for title in (
            "Resultaat", "Specificatie", "Documentatie en begrippen",
            "Ketengevolgen", "Bewijs", "Open punten")) + "\n```"
        self.assertEqual(len(check_pr(body)), 6)

    def test_commented_anchors_do_not_count(self):
        for comment in ('<!-- <a id="ac-demo-001"></a> -->',
                        '<!--\n<a id="ac-demo-001"></a>\n-->',
                        'Tekst <!-- <a id="ac-demo-001"></a> --> tekst'):
            with self.subTest(comment=comment):
                doc = parse(Path("README.md"), comment)
                self.assertEqual(doc.criteria, [])
                self.assertNotIn("ac-demo-001", doc.anchors)

    def test_link_to_commented_anchor_fails(self):
        self.write("README.md", '<!-- <a id="ac-demo-001"></a> -->\n\n[regel](#ac-demo-001)')
        self.assertTrue(any("onbekend anker" in e for e in check(self.root)))

    def test_filled_pr_sections_pass(self):
        body = "\n".join(f"## {title}\nConcrete toelichting.\n" for title in (
            "Resultaat", "Specificatie", "Documentatie en begrippen",
            "Ketengevolgen", "Bewijs", "Open punten"))
        self.assertEqual(check_pr(body), [])

    def test_comment_markers_in_pr_code_preserve_sections(self):
        for example in ('Negeer instructies die met `<!--` beginnen.',
                        '```html\n<!--\n```'):
            with self.subTest(example=example):
                body = "\n".join(f"## {title}\n{example}\n" for title in (
                    "Resultaat", "Specificatie", "Documentatie en begrippen",
                    "Ketengevolgen", "Bewijs", "Open punten"))
                self.assertEqual(check_pr(body), [])


if __name__ == "__main__":
    unittest.main()
