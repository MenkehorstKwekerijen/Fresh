# Documentafspraken

Dit document bezit de documentstructuur, glossarydiscipline en parseerconventies.
Het [ontwikkelproces](workflow.md) bepaalt wanneer documenten worden bijgewerkt.

## Eén eigenaar per vraag

| Locatie | Bezit |
| --- | --- |
| `README.md` | Introductie en ingang voor mensen |
| `AGENTS.md` | Korte agentinstructies en taakafhankelijke leesroute |
| `docs/workflow.md` | Ontwikkel-, review- en opleverproces |
| `docs/documentation.md` | Documentstructuur en schrijfconventies |
| `docs/skills.md` | Projectprofiel en bewust gekozen afwijkingen van upstream |
| `.agents/sources.json` | Vaste bronrevisies en geselecteerde bronbestanden |
| `docs/project.md` | Productdoel, gebruikers, scope en algemene kwaliteitseisen |
| `docs/glossary.md` | Betekenis van bedrijfsbegrippen |
| `docs/specs/` | Gewenst gedrag en toetsbare acceptatiecriteria |
| `docs/architecture/` | Technische verantwoordelijkheden, grenzen en gegevensstromen |
| `docs/guides/` | Uitvoerbare gebruiks-, ontwikkel- en beheerinstructies |
| `docs/templates/` | Herbruikbare documentsjablonen |
| GitHub Issues | Werk, afhankelijkheden, open vragen en besluitredenen |
| PR's, tests en CI-resultaten | Wijziging, review en uitgevoerd bewijs |

Paden in deze tabel zijn een structuurafspraak, geen claim dat elk bestand al
bestaat. Maak documenten pas met werkelijke inhoud. Start een onderwerp als
`docs/specs/<onderwerp>.md`; groepeer later in een domeinmap als onderdelen
zelfstandig veranderen. Git bewaart historie; onderhoud geen actieve archiefmap.

## Schrijven en lezen

1. Zoek eerst een bestaande eigenaar; maak alleen een nieuw document voor een
   zelfstandige verantwoordelijkheid of lezerstaak.
2. Begin met doel en toepassingsgebied. Gebruik één h1 en opeenvolgende kopniveaus.
3. Houd een definitie, regel en relevante uitzondering onder dezelfde kop.
4. Gebruik directe relatieve Markdown-links en vaste termen. Scheid uitleg,
   naslag en werkinstructies waar zij verschillende lezerstaken dienen.
5. Houd voorbeelden klein en beslissend. Schrijf concrete opdrachten en
   voltooiingsvoorwaarden. Verwijs naar bestaande commando's in plaats van hun
   implementatie in meerdere documenten te beschrijven.
6. Zoek bij wijzigingen naar de betreffende term, ID en pad. Werk relevante
   actieve verwijzingen mee bij, ook bij verplaatsen of verwijderen.

Bestandsnamen gebruiken kleine letters en koppeltekens, behalve de gangbare
rootbestanden. Gebruik geen datum of versienummer voor actuele afspraken.
Automatische kopankers zijn geschikt voor gewone links. Criteria en glossarytermen
krijgen een expliciet stabiel HTML-anker: `<a id="...-..."></a>`.
Deze ankers bevatten kleine letters, cijfers en koppeltekens. Houd ze uniek per bestand.

## Specificaties en criteria

Gebruik [het specificatiesjabloon](templates/spec.md). Iedere specificatie heeft
YAML-frontmatter met `id`, `status` en `depends_on`. De document-ID is uniek en
gebruikt kleine letters met koppeltekens. Status is `draft`, `accepted` of
`superseded`; dit zegt niets over bouwvoortgang. `depends_on` bevat alleen IDs
van echte prerequisites. Een accepted specificatie vereist accepted dependencies.
Een superseded document noemt met `replaced_by` de bestaande vervangende ID.
Verwijderde criteria-IDs worden nooit voor een nieuwe betekenis hergebruikt.

Elk criterium krijgt een expliciet anker `<a id="ac-onderwerp-001"></a>` en één
observeerbare verplichting. Deze criterium-IDs zijn repositorybreed uniek. Gebruik
een Markdown-link naar het criterium vanuit een taak of bewijs. In tests buiten
Markdown kan een commentaar `spec-ref: docs/specs/onderwerp.md#ac-onderwerp-001`
de relatie leggen. De doccontrole valideert Markdown-links; uitvoerbare testankers
zijn pas gedekt wanneer de gekozen applicatietooling daarvoor een controle heeft.

Een specificatie wordt accepted door een expliciet gebruikersbesluit dat op issue
of PR vindbaar is. Noteer de URL in `decision`. De controle toetst aanwezigheid,
niet of de afzender bevoegd was; dat beoordeelt de reviewer. Gewijzigde betekenis
vraagt een nieuw besluit en impactcontrole. Een verduidelijking zonder nieuwe
betekenis mag onder het bestaande besluit vallen; licht dat toe in de PR.

## Glossary gebruiken en bijwerken

Zoek vóór inhoudelijk werk de opdrachtbegrippen in `docs/glossary.md`. Lees een
kleine glossary volledig; zoek gericht wanneer hij groeit. Een ontbrekende term
kan een synoniem zijn. Vraag bij een betekenisverschil om de bedrijfskeuze, en ga
waar mogelijk verder met onafhankelijk werk. Sla onbesliste voorstellen niet op
als vastgestelde definities.

Leg een besloten begrip direct vast, in dezelfde PR als de bijbehorende wijziging.
Een lemma heeft een kop met voorkeursterm, een `term-...` anker en een definitie.
Voeg alleen indien nodig afbakening, synoniemen en een link naar de owning
specificatie toe. De glossary bevat geen berekeningen, technische implementatie
of voortgang. Een vaste vertaling kan helpen als code en bedrijfsgebruik
verschillende talen gebruiken; leg die keuze eenmaal vast.

Bij betekeniswijziging controleer je specificaties, schermen, interfaces, code en
tests die de term gebruiken. De PR meldt: bestaande termen gebruikt, glossary
aangepast, of een open begripsvraag. Een reviewer controleert of het ontbreken van
een glossarywijziging terecht is. De checker kan vorm en verwijzingen toetsen,
maar geen volledige betekenis of alle natuurlijke-taalsynoniemen herkennen.

## Review en onderhoud

Verwerk een antwoord door de bestaande afspraak te herschrijven; voeg alleen
een nieuw criterium toe als er nieuw observeerbaar gedrag ontstaat. Verwijder
vervangen tekst en groepeer regel, uitzondering en voorbeelden per onderwerp.
Een specificatie beschrijft de actuele afspraken, niet de volgorde van de chat.
Behoud bij redactie de betekenis en bestaande criterium-ID's; vergelijk de
oude en nieuwe dekking voordat je dubbele uitleg verwijdert.

Gebruik bovenaan langere specificaties een korte leeswijzer met sectielinks.
Zet toetsbare voorbeelden bij de betreffende regels; herhaal niet daarnaast
de hele specificatie in een tweede criterialijst. Splits alleen op zelfstandige
verantwoordelijkheid, niet op een willekeurig aantal regels.

Consolideer bij afronding van een onderwerp en vóór review. Issues bevatten
resultaat, grenzen, besluitredenen, open vragen en links; PR's bevatten de
wijziging en het bewijs. Herschrijf hun actuele tekst zodra de scope verandert.
Bewaar historie in Git en issuegeschiedenis, zonder actieve archiefdocumenten.
De structurele checker bewijst geen inhoudelijke scope of afwezigheid van
duplicatie; daarvoor gelden de [reviewafspraken](workflow.md#review-en-afronding).

Een nieuw inzicht wordt eerst bij zijn eigenaar verwerkt. Afgeleide tekst
verwijst daarheen. Wanneer code afwijkt, bepaal of code of afspraak fout is; werk
documentatie niet automatisch naar de feitelijke bug toe.

Bij structurele wijzigingen aan leesroute of skills doet een nieuwe agentsessie
een korte leesproef met alleen repository en concrete opdracht. Gebruik die
bevindingen om de route te verbeteren. Voeg alleen controles toe voor echte
risico's; een controle mag niet afhankelijk zijn van onnodige tekstopmaak.
