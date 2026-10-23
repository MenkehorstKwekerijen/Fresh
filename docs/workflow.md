# Ontwikkelwerkwijze

Dit document bezit het ontwikkelproces van Fresh. Het legt geen productgedrag of
technologische applicatiekeuzes vast. Zie [documentafspraken](documentation.md)
voor informatie-eigenaarschap en [skillprofiel](skills.md) voor de gekozen bronnen.

## Ontwikkelcyclus

1. **Begrijpen.** Onderzoek de bron, relevante glossarybegrippen en bestaande
   specificaties. Benoem het gebruikersresultaat, de eenvoudigste oplossing en
   reële alternatieven. Alleen ontbrekende keuzes die de uitkomst veranderen
   vragen een gebruikersbesluit. Registreer dat besluit op het issue.
2. **Specificeren.** Werk de owning specificatie bij. Leg concrete invoer,
   verwachte uitkomst, foutgedrag en ketengevolgen vast. Een voorstel blijft
   `draft` totdat het bevoegde gebruikersbesluit is vastgelegd. Reeds expliciet
   opgedragen gedrag hoeft niet nogmaals te worden goedgekeurd.
   Leg de [documentatiekeuze](documentation.md#documentatie-bij-uitbreidingen)
   vast vóór bouwen en herbeoordeel haar bij een scopewijziging.
3. **Plannen.** Maak een klein uitvoeringsissue met verwijzingen naar criteria,
   echte afhankelijkheden en een korte technische checklist waar nodig. Een
   onbekende haalbaarheid krijgt een begrensde proef met een stopcriterium.
4. **Bouwen.** Implementeer één complete gedragsstap tegelijk. Gebruik bij
   bedrijfslogica en bugfixes een relevante test die eerst het ontbrekende of
   foutieve gedrag laat zien. Maak de minimale implementatie en controleer haar.
   Een tekstcorrectie of opmaakwijziging vraagt geen kunstmatige gedragstest.
5. **Beoordelen.** Controleer criteria, eenvoud, documentatie en gevolgen buiten
   de diff. Verifieer kritieke aannames via de echte relevante systeemgrens.
6. **Opleveren.** Rapporteer uitgevoerde controles, revisie en beperkingen in de
   PR. Sluit alleen de aantoonbaar afgeronde scope.

Een bugfix die een bestaande afspraak herstelt gebruikt de bestaande specificatie.
Een zuiver mechanische wijziging kan direct naar uitvoering en gerichte controle.
Splits een taak als zij meerdere onafhankelijk opleverbare resultaten bevat of
niet meer met haar relevante context te begrijpen en te verifiëren is.

## Kleine issues en voortgang

### Scope tijdens vragenrondes

Begin ieder issue en iedere PR met één concreet resultaat en een korte grens:
wat hoort erbij, wat valt erbuiten? Toets bij een onderwerpwissel, nieuwe
afnemer of extra zelfstandig resultaat of het nog binnen die grens past.
Een raakvlak alleen is geen afhankelijkheid.

| Uitkomst | Handeling |
| --- | --- |
| Verduidelijkt het afgesproken resultaat | Werk de bestaande afspraak bij |
| Is noodzakelijk voor dat resultaat | Houd het erbij en benoem de concrete afhankelijkheid in issue en PR |
| Levert een zelfstandig resultaat | Verwerk het in een passend klein issue; maak een eigen PR zodra het werk start |
| Is een toekomstidee | Noteer het kort op het passende issue; werk nog geen specificatie uit |

Meld een scopeverschuiving kort aan de gebruiker. Vraag alleen een keuze als
productwerking of prioriteit onduidelijk is; routine-indeling vereist geen
nieuwe toestemming. Hervat de vraag bij het juiste onderwerp. Kopieer geen
gesprek naar meerdere issues: link naar de owning afspraak en bewaar alleen
besluitreden en open vragen bij het issue.

Splits bestaand werk voordat meer zelfstandige scope wordt toegevoegd. Bewaar
besloten inhoud, criterium-ID's en herleidbare geschiedenis. Nieuwe PR's tonen
alleen hun eigen wijziging. Gebruik bij echte afhankelijkheden een expliciete
base-branch en mergevolgorde; werk na merge de volgende base bij en controleer
de diff opnieuw. Sluit de oude verzamel-PR pas wanneer alle opvolgers vindbaar
zijn; sluit daarmee geen onvoltooide productissues.

### Voortgang zonder extra register

Gebruik [het issuesjabloon](../.github/ISSUE_TEMPLATE/task.md). Eén issue bezit één
resultaat; opslag, verwerking, scherm en tests mogen daarvoor samen veranderen.
Maak maximaal twee niveaus: een kort overkoepelend issue en uitvoeringsissues.
Gebruik native sub-issues wanneer beschikbaar, anders alleen links, zonder een
tweede afvinklijst. Beschrijf blokkades bij het betreffende uitvoeringsissue.

| Signaal | Betekenis |
| --- | --- |
| Open issue | Werk is open; zonder PR is niet zeker of het al gestart is |
| Startnotitie | De uitvoerder is met onderzoek of uitvoering begonnen |
| Concept-PR | De implementatie is zichtbaar en nog in uitvoering |
| PR klaar voor review | De auteur heeft de vereiste voorbereidingen afgerond |
| Blokkadenotitie, eventueel label `blocked` | Concrete ontbrekende beslissing, afhankelijkheid of omgeving |
| Gesloten issue | Lees de reden: uitgevoerd, vervallen of vervangen |

Gebruik `Closes #nummer` alleen als merge de afgesproken afrondingsgrens bereikt.
Blijft een vereiste praktijkproef open, verwijs met `Refs #nummer` en houd het
issue open. Implementatie, verificatie, release en productiegebruik zijn
verschillende feiten. Een ouderissue sluit pas na beoordeling van zijn eigen
scope; een telling van gesloten sub-issues is geen acceptatiebewijs.

Voortgang volgt uit issues en PR's, zonder Projects of apart roadmapbestand.
Bij een chatwissel verzorgt [fresh-handoff](../.agents/skills/fresh-handoff/SKILL.md)
één korte hervattingsnotitie op het actieve issue of de PR en een startprompt.
Wissel op verzoek of bij onoverzichtelijke context op een logisch tussenpunt;
wacht niet op een gegarandeerde melding over een vol contextvenster. De nieuwe
sessie controleert eerst de actuele bronnen. Geen extra statusbestand of taak.

## Ketencontrole

Bij gewijzigde gegevens of bedrijfsregels bepaal je:

- herkomst, identiteit, betekenis, eigenaar en actualiteit van de gegevens;
- directe en indirecte afnemers, inclusief bestanden en externe systemen;
- gevolgen van wijzigen, ontbreken, veroudering en dubbele verwerking;
- gedrag bij onderbreking en, indien relevant, gelijktijdige wijzigingen;
- herstel wanneer uitvoer al door een afnemer is gebruikt.

Leg alleen toepasselijke risico's vast. Onduidelijke betekenis is een open
productkeuze. Een onbewezen technische aanname is een onderzoekstaak. Controleer
wat de veiligheid van de wijziging werkelijk bepaalt; een lijst aanroepers is
geen bewijs. Gebruik een toestandstabel bij processen met relevante overgangen.

## Review en afronding

Eén uitvoerende agent is standaard. Functionele opleveringen en wijzigingen aan
de procesbasis krijgen een onafhankelijke reviewer met opdracht, specificatie,
base/head-revisies en bewijs. Geef geen gewenste conclusie mee. Extra parallelle
agents zijn alleen nuttig bij onafhankelijk werk of gerichte risicoanalyse.

De reviewer controleert ook of diff en open vragen bij het ene PR-resultaat
horen, of echte afhankelijkheden zijn benoemd en of productregels bij hun eigenaar
staan zonder onnodige kopieën. Controleer glossary-impact, geraakte verwijzingen
en of nieuwe modules/functies de juiste eigenaar en een vindbare leesroute hebben,
en onvoorziene ketengevolgen. Los belangrijke bevindingen op. Herhaal gerichte
controles na fixes; doe een nieuwe review wanneer nieuwe wijzigingen of resterend
risico dit rechtvaardigen. Is onafhankelijke review niet beschikbaar, rapporteer
dat als ontbrekend bewijs, niet als geslaagde fresh pass.

Gebruik [het PR-sjabloon](../.github/pull_request_template.md). Een onderdeel is
afgerond wanneer de criteria zijn aangetoond, belangrijke bevindingen zijn
opgelost en documentatie overeenkomt met de bedoelde werking. Tests vermelden hun
revisie en relevante omgeving. Repareer een foute testverwachting alleen met een
inhoudelijke onderbouwing; verander geen afspraak om een test groen te krijgen.

Voer tijdens bouwen snelle gerichte controles uit en bij oplevering de benodigde
bredere controles. Kies de kleinste test die het risico betrouwbaar ziet. Test
databases, bestandsformaten en externe compatibiliteit echt wanneer juist hun
semantiek het risico is. Leg ontbrekende praktijk- of platformproeven expliciet vast.

## Aanmaakvolgorde

Deze volgorde is een inrichtingprocedure, geen handmatig voortgangsregister.

| Pakket | Inhoud | Afrondingsvoorwaarde |
| --- | --- | --- |
| A | README, AGENTS, werkwijze, documentafspraken en sjablonen | Een nieuwe agent vindt de eigenaar en leesroute |
| B | Projectskills, bronrevisies, doccontrole en CI | Positieve en negatieve controles plus een onafhankelijke leesproef slagen |
| C | `docs/project.md`, `docs/glossary.md`, `docs/architecture/overview.md` | Doel, betekenis, keten en open keuzes zijn expliciet |
| D | Eerste productspecificatie en klein uitvoeringsissue | Eén praktijkroute is voldoende bepaald om te bouwen |

Maak geen lege productdocumenten voor pakket C. Maak ze zodra besliste inhoud
beschikbaar is. Handleidingen ontstaan bij de werkelijk geïmplementeerde route.
Verificatie-instructies beschrijven starten, beginsituatie, bediening, bewijs en
opruimen en worden zelf uitgevoerd. Voeg controles op terugkerende fouten toe
waar dat beter werkt dan meer instructietekst.
