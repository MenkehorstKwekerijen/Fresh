---
name: fresh-deliver
description: Voer een afgebakende Fresh-opdracht uit en lever controleerbaar bewijs. Gebruik bij implementatie, bugfix, debugging, ketenimpact, code review en oplevering.
---
# Fresh opleveren

1. Lees issue, branch/diff, relevante specificatie en glossarybegrippen. Gebruik
   de [ontwikkelcyclus](../../../docs/workflow.md#ontwikkelcyclus). Los ontbrekende
   bedrijfsbetekenis op voordat je afhankelijk gedrag bouwt; onafhankelijk werk
   kan doorgaan. Een mechanische taak vereist geen nieuwe productspecificatie.
2. Bepaal het kleinste complete resultaat en echte prerequisites. Zet uitsluitend
   noodzakelijke technische stappen in het issue. Maak een taakbranch en bewaar
   ander werk. Noteer start of hervatting met de actuele commit.
   Toets extra werk aan de [scopecontrole](../../../docs/workflow.md#scope-tijdens-vragenrondes)
   en splits zelfstandige resultaten voordat de PR verder groeit.
3. Reproduceer bij fouten eerst het gedrag en traceer de oorzaak. Kies per
   belangrijk risico een verwachte uitkomst uit de afspraak, niet uit de code.
   Test relevante bedrijfslogica en bugs eerst rood, bouw minimaal en test groen.
4. Controleer [ketengevolgen](../../../docs/workflow.md#ketencontrole), ook via
   data, bestanden en afnemers buiten de diff. Bewijs kritieke aannames met echte
   uitvoer waar mogelijk. Houd onbekende gevolgen zichtbaar.
5. Werk volgens de [documentafspraken](../../../docs/documentation.md) de owning
   betekenis, glossary en geraakte verwijzingen bij. Een herstel naar bestaand
   gedrag hoeft de afspraak niet te veranderen.
6. Voer de relevante [controles](../../../docs/guides/checks.md) uit. Laat de
   volledige oplevering onafhankelijk beoordelen volgens
   [review en afronding](../../../docs/workflow.md#review-en-afronding).
7. Verwerk belangrijke bevindingen en verifieer de fixes. Publiceer via een PR
   wanneer dat binnen de opdracht valt. Maak bewijs, revisie, documentatie-impact
   en ontbrekende controles zichtbaar. Sluit alleen de bewezen issue-scope.

Gebruik bij een chatwissel [fresh-handoff](../fresh-handoff/SKILL.md).
Bij ontbrekende rechten: behoud lokaal werk en rapporteer de geweigerde
handeling. Een lokale check is geen bewijs van ingestelde GitHub-bescherming.
