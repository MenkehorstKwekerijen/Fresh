# Werken aan Fresh

## Begin gericht

Lees de opdracht, de actuele branch/diff en het bijbehorende issue. Gebruik geen
eerdere chats of oude WinTree-regels als onuitgesproken productbesluit.
Lees daarna alleen de bronnen die bij de taak horen:

| Taak | Lees vóór uitvoering |
| --- | --- |
| Nieuw gedrag, veranderde betekenis of nieuwe begrippen | [fresh-spec](.agents/skills/fresh-spec/SKILL.md) |
| Implementeren, bugfix, testen of opleveren | [fresh-deliver](.agents/skills/fresh-deliver/SKILL.md) |
| Chat overdragen of werk hervatten | [fresh-handoff](.agents/skills/fresh-handoff/SKILL.md) |
| Documentatie of glossary aanpassen | [documentafspraken](docs/documentation.md) |
| Werkwijze, issues of PR's inrichten | [werkwijze](docs/workflow.md) |
| Skillselectie of skillwijziging | [skillprofiel](docs/skills.md) |

Zoek bij inhoudelijk werk de relevante begrippen in `docs/glossary.md`, wanneer
dat bestand bestaat. Ontbrekende productbetekenis wordt eerst beslist; verzin geen
definities om alvast code te kunnen schrijven. Volg de gekoppelde specificatie en
haar directe afhankelijkheden. Laad niet standaard alle documentatie of skills.

## Uitvoeren en afronden

- Werk op een taakbranch. Kies de kleinste complete, controleerbare oplevering.
- Bepaal bij een module of functie de [documentatiekeuze](docs/documentation.md#documentatie-bij-uitbreidingen)
  vóór bouwen; leg scope en owning bronnen vast in issue en PR.
- Volg de [ontwikkelcyclus](docs/workflow.md#ontwikkelcyclus). Reeds geautoriseerd
  werk gaat door; leg een nieuwe bedrijfskeuze voor als die de uitkomst verandert.
- Houd betekenis en gedrag bij hun documenteigenaar. Werk gewijzigde afspraken,
  glossarybetekenissen en geraakte verwijzingen in dezelfde PR bij.
- Onderzoek verschillen tussen code en specificatie; maak een productfout niet
  onzichtbaar door alleen de specificatie aan te passen.
- Draai de toepasselijke [controles](docs/guides/checks.md). Claim alleen bewezen
  resultaten; vermeld ontbrekende omgeving, bewijs of bevoegdheid.
- Een functionele oplevering krijgt een onafhankelijke eindreview. Zie de
  [reviewafspraken](docs/workflow.md#review-en-afronding); een eigen tweede lezing
  is geen onafhankelijke review.
- Gebruik bij een chatwissel [fresh-handoff](.agents/skills/fresh-handoff/SKILL.md)
  voor één hervattingsnotitie op het actieve issue of de PR.

## Prioriteit en grenzen

Binnen repository-afspraken is het [Fresh-profiel](docs/skills.md) leidend boven
upstream skillprocedures. Hogere platforminstructies en expliciete opdrachten
blijven leidend. Een ontbrekende automatische skillregistratie wordt opgevangen
door de bovenstaande lokale `SKILL.md` direct te lezen.

Lees een onderliggende `AGENTS.md` wanneer de geraakte map die bevat. Voeg zo'n
bestand alleen toe voor blijvende regels die uitsluitend in die map gelden.
Bedrijfsdata, credentials en lokale uitvoer horen niet in dit publieke repository.
