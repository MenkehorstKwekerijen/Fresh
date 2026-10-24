---
id: voorraadimport
status: draft
depends_on: [voorraad, prijzen]
---
# Voorraadimport

## Doel en scope

Deze specificatie bezit de importstappen, kolomtoewijzing, matching en wachtlijst.
De [voorraadbasis](voorraad.md) bepaalt vervanging en bronvoorrang voor fictieve
voorraad, eigen voorraad, eigen externe voorraad en TCM. Import vereist daarnaast
de [prijsvoorwaarden](prijzen.md#prijsvoorwaarden-bij-import); beide zijn expliciete
prerequisites. Geen prijsberekening of uitwerking van exportvrijgave.
Deze conceptafspraken zijn nog niet volledig genoeg voor implementatie.
Besluiten en open keuzes: [issue #12](https://github.com/MenkehorstKwekerijen/Fresh/issues/12).
Eerdere basisbesluiten staan in [issue #4](https://github.com/MenkehorstKwekerijen/Fresh/issues/4).

Lees gericht: [voorraadbasis](voorraad.md) · [importstappen](#stappen-van-de-leveranciersimport) · [kolommen](#kolomtoewijzing-in-stap-2) ·
[productherkenning](#herkenning-bij-volgende-leverancierslijsten) ·
[naam- en maatkoppelingen](#naam--en-maatkoppelingen-hergebruiken) ·
[uitsluiten en matching](#uitsluiten-vanuit-voor-controle) · [wachtlijst](#wachtlijst-voor-stamcodes) ·
[V1-referentie](#eenmalige-v1-referentie) · [keten en open keuzes](#keten-en-open-keuzes).

## Stappen van de leveranciersimport

| Stap | Handeling |
| --- | --- |
| 1 | Bestand en leverancier selecteren |
| 2 | Kolommen toewijzen, leveranciersmapping controleren en waarschuwingen behandelen |
| 3 | Bestand uitlezen, controleren en automatisch proberen te matchen |
| 4 | Resterende regels handmatig matchen met naam- en maatcodes |
| 5 | Import definitief verwerken: nieuwe stand opslaan en vorige vervangen |

Controles, prijscorrecties en matches tijdens de voorbereiding wijzigen de actuele voorraad
niet. Prijsvoorwaarden staan bij [prijzen](prijzen.md#prijsvoorwaarden-bij-import):
[standaardmarge vooraf](prijzen.md#ac-prijzen-046), [prijsvalidatie](prijzen.md#ac-prijzen-049)
en [herstel per regel](prijzen.md#ac-prijzen-050). De matchuitzonderingen hieronder heffen
prijsblokkades niet op.

<a id="ac-voorraadimport-011"></a>

### Alleen stap 5 vervangt de actuele voorraad

Gegeven een actuele leverancierslijst met 20 planten en een nieuw bestand met 12 planten voor
dezelfde regel, leest en controleert stap 3 het nieuwe bestand en probeert Fresh automatisch naam-
en maatcodes te matchen. Stap 4 laat de gebruiker resterende matches oplossen. De actuele voorraad
blijft tijdens deze voorbereiding 20. Na succesvolle definitieve verwerking in stap 5 is de actuele
voorraad 12; het nieuwe bestand vervangt dan de vorige stand.

## Kolomtoewijzing in stap 2

[Kolomtoewijzing](../glossary.md#term-kolomtoewijzing) wordt per leverancier onthouden.
Nieuwe bestanden worden opnieuw gecontroleerd. De gebruiker kan prijsfouten
[direct in Fresh herstellen](prijzen.md#ac-prijzen-051); de waarschuwing bij mapping
is geen toestemming om een blokkade te negeren.

<a id="ac-voorraadimport-008"></a>

### De tweede importstap wijst bestandskolommen toe

Gegeven een geselecteerd leveranciersbestand, kan de gebruiker in stap 2 de kolommen voor plantnaam,
maat en inkoopprijs aan de overeenkomstige gegevens in Fresh toewijzen, vóór verwerking tot actuele
voorraad.

<a id="ac-voorraadimport-009"></a>

### Prijsproblemen zijn al bij de kolomtoewijzing zichtbaar

Gegeven stap 2 met een niet-toegewezen inkoopprijskolom of een toegewezen kolom met een lege of
ongeldige prijs op regel 12, toont Fresh daar al een waarschuwing met toegang tot respectievelijk de
toewijzing of de betreffende foutregel en herstelactie. Verwerking blijft geblokkeerd zolang het
prijsprobleem bestaat.

<a id="ac-voorraadimport-010"></a>

### Kolomtoewijzing wordt per leverancier hergebruikt

Gegeven een vastgelegde kolomtoewijzing voor leverancier A, vult Fresh die in stap 2 alvast in bij
een volgend bestand van A met dezelfde kolomstructuur. De gebruiker kan haar controleren en
aanpassen. Fresh controleert de inhoud van dit nieuwe bestand opnieuw; de toewijzing van A wordt
niet als instelling voor een andere leverancier gebruikt.

## Herkenning bij volgende leverancierslijsten

Een [productuitvoering](../glossary.md#term-productuitvoering) wordt niet volledig
onderscheiden door leverancier, naamcode en maatcode. De leverancier heeft geen
eigen artikelcode beschikbaar; kwaliteitsverschillen staan in de extra tekst,
die ook gewone opmerkingen kan bevatten en doorgaans gelijk blijft. De gebruiker
koos daarom beperkte tekstvergelijking, zonder automatische kwaliteitsanalyse
of slimme gelijkstelling van verschillende omschrijvingen. Besluitbasis:
[issue #12](https://github.com/MenkehorstKwekerijen/Fresh/issues/12).

Voor opeenvolgende bestanden van dezelfde leverancier binnen dezelfde bron
vergelijkt Fresh de aangeleverde plantnaam, maat en extra tekst. Alleen
hoofdletters, spaties aan begin/eind en herhaalde spaties worden genegeerd.
Getallen, bereiken, leestekens en afkortingen worden niet weggelaten of gelijkgesteld.
Prijs en voorraadhoeveelheid bepalen niet of het dezelfde uitvoering is.
De herkenningsregel hieronder betreft een eenduidige voorganger; dubbelzinnige
gevallen en gegevens buiten deze drie velden vragen nog uitwerking.

| Vergelijking met de vorige lijst | Afhandeling |
| --- | --- |
| Plantnaam, maat en extra tekst gelijk na deze beperkte normalisatie | Dezelfde uitvoering herkennen |
| Een van deze teksten inhoudelijk anders | Vorige uitvoering als voorstel tonen; gebruiker kiest dezelfde of een andere uitvoering |
| Gebruiker bevestigt dezelfde uitvoering | Bestaande instellingen behouden en de nieuwe brongegevens gebruiken |
| Gebruiker kiest een andere uitvoering | Afzonderlijk behandelen; begininstellingen blijven een open keuze |

Herkenning en de bestaande naam-/maatcodematch zijn verschillende stappen:
twee uitvoeringen kunnen dezelfde codes delen zonder hun instellingen te delen.
Herkenning bewaart een bestaande match, maar maakt geen match voor een wachtende
regel. De [wachtlijst](#wachtlijst-voor-stamcodes) blijft de actuele lijst volgen.
[Prijsinstellingen](prijzen.md#prijsinstellingen-bij-volgende-imports) en
[exportuitsluitingen](wintree-export.md#uitsluiting-per-uitvoering-en-volgende-import)
hebben hun eigen behoudregels. Geen van deze voorbereidingskeuzes vervangt de
actuele voorraad vóór stap 5 of geeft automatisch exportvrijgave.

<a id="ac-voorraadimport-020"></a>

### Hoofdletters en overtollige spaties verhinderen herkenning niet

Gegeven één eerdere uitvoering bij leverancier A met plantnaam `Plant P`, maat
`100-125` en extra tekst `3-jarige kroon`, herkent Fresh de volgende regel van A
binnen dezelfde bron met `plant p`, ` 100-125 ` en `3-JARIGE  KROON` als dezelfde
uitvoering. Een gewijzigde hoeveelheid of inkoopprijs verhindert die herkenning niet.

<a id="ac-voorraadimport-021"></a>

### Een gewijzigde omschrijving vraagt een keuze over de uitvoering

Gegeven een eerdere uitvoering met extra tekst `3-jarige kroon`, toont Fresh bij
dezelfde leverancier en verder gelijke gegevens de vorige uitvoering als voorstel
wanneer de nieuwe tekst `3-jarige kroon, aanbieding` of `3 jr kroon` is. Fresh
neemt niet zelf aan dat dit dezelfde uitvoering is. Ook `2-jarige kroon` tegenover
`3-jarige kroon` en `2-3 tak` tegenover `4-5 tak` worden niet automatisch gelijkgesteld.
Een gewijzigde plantnaam of maat volgt dezelfde controleroute.

<a id="ac-voorraadimport-022"></a>

### Dezelfde uitvoering behoudt haar bestaande codematch

Gegeven een uitvoering met een bestaande naam-/maatcodematch waarvan de stamcodes
ongewijzigd beschikbaar zijn, blijft die match bij de volgende import behouden
wanneer Fresh dezelfde uitvoering volgens de tekstvergelijking herkent of de
gebruiker dit na een tekstwijziging bevestigt. De gebruiker hoeft diezelfde match
niet opnieuw in te stellen. Een wachtende regel zonder match krijgt hierdoor
geen codes; daarvoor blijft de wachtlijstroute gelden.

<a id="ac-voorraadimport-023"></a>

### Een andere uitvoering blijft afzonderlijk

Gegeven een voorgestelde eerdere uitvoering `2-jarige kroon` en een nieuwe regel
`3-jarige kroon`, behandelt Fresh de nieuwe regel afzonderlijk wanneer de gebruiker
kiest voor een andere uitvoering, ook bij gelijke naam- en maatcodes. De oude en
nieuwe uitvoering worden niet samengevoegd. Welke begininstellingen de nieuwe
uitvoering krijgt, is hiermee niet besloten.

## Naam- en maatkoppelingen hergebruiken

Bevestigde koppelingen naar een [naamcode](../glossary.md#term-naamcode) en een
[maatcode](../glossary.md#term-maatcode) worden binnen dezelfde leverancier
afzonderlijk onthouden en hergebruikt. De gebruiker heeft dit bevestigd in
[issue #12](https://github.com/MenkehorstKwekerijen/Fresh/issues/12).
Een bevestigde naamkoppeling kan daardoor ook bij een andere maat worden gebruikt;
een bevestigde maatkoppeling ook bij een andere plantnaam, zolang dezelfde
maatbetekenis geldt. De andere helft van de match moet afzonderlijk beschikbaar
zijn; één geleerde koppeling maakt niet vanzelf een volledige productmatch.

Dit hergebruik beslist niet of twee regels dezelfde
[productuitvoering](#herkenning-bij-volgende-leverancierslijsten) zijn.
[Prijsinstellingen](prijzen.md#prijsinstellingen-bij-volgende-imports) en
[exportuitsluitingen](wintree-export.md#uitsluiting-per-uitvoering-en-volgende-import)
blijven per uitvoering gelden. Een gedeelde codematch is geen reden om die
instellingen te kopiëren, uitvoeringen samen te voegen of export vrij te geven.
De bestaande wachtlijstroute voor ontbrekende stamcodes blijft gelden.

De onderstaande criteria betreffen eenduidige, eerder bevestigde koppelingen
met ongewijzigd beschikbare stamcodes en ongewijzigde naam- of maatbetekenis.
Exact dezelfde gegevens voor de betreffende naam- of maatkoppeling hergebruiken
de vorige match, ongeacht de kolom waarin ze zijn aangeleverd. De inhoud is
leidend, niet de kolomnaam of kolompositie. Dit geldt ook voor aanvullende
kenmerken zoals pot/kluit, potmaat of vorm: die mogen niet buiten de vergelijking
vallen omdat ze in extra tekst in plaats van een aparte kolom staan.
Alleen dezelfde losse maataanduiding is dus geen bewijs dat alle maatgegevens
gelijk zijn. Het afzonderlijke naam-/maatgeheugen blijft gelden; prijs en
voorraadhoeveelheid zijn geen gegevens voor deze codematch.

Het uitlezen van gegevens uit verschillende kolommen, de afbakening van
naam-/maatkenmerken tegenover overige opmerkingen, tekstvarianten, conflicterende
koppelingen, correcties en gewijzigde stamcodes vragen nog uitwerking.
Dit besluit kiest geen V1-normalisatie of technisch geheugenschema.

<a id="ac-voorraadimport-024"></a>

### Een bevestigde naamkoppeling werkt ook bij een andere maat

Gegeven een bevestigde koppeling van leveranciersnaam `Plant P` naar naamcode N
bij leverancier A, gebruikt Fresh N opnieuw voor dezelfde naam bij A wanneer
de maat van `100-125` naar `125-150` verschilt. De naam hoeft niet opnieuw te worden
gekoppeld. De maatcode volgt haar eigen match; hergebruik van N beslist niet over
de identiteit van de uitvoering of haar begininstellingen.

<a id="ac-voorraadimport-025"></a>

### Een bevestigde maatkoppeling werkt ook bij een andere plantnaam

Gegeven een bevestigde koppeling van maat `100-125` naar maatcode M bij leverancier
A, gebruikt Fresh M opnieuw bij een andere plantnaam van A met dezelfde volledige
maatbetekenis en ongewijzigde relevante context. Die maat hoeft niet opnieuw te
worden gekoppeld; de naamcode wordt afzonderlijk bepaald.

<a id="ac-voorraadimport-026"></a>

### Geleerde koppelingen blijven bij de leverancier

Gegeven alleen een bevestigde naam- of maatkoppeling bij leverancier A, gebruikt
Fresh die niet als geleerde koppeling bij leverancier B, ook bij dezelfde
brontekst. B volgt de eigen matchroute; dezelfde uiteindelijke stamcode blijft
mogelijk zonder de leveranciersgeheugens te delen.

<a id="ac-voorraadimport-027"></a>

### Dezelfde matchgegevens mogen in andere kolommen staan

Gegeven leverancier A met een bevestigde maatmatch voor `100-125` en `kluit`,
waarbij `kluit` eerst in een aparte pot/kluitkolom staat, gebruikt Fresh dezelfde
maatmatch opnieuw wanneer `kluit` in de volgende lijst in de extra tekst staat
en de overige maatgegevens exact gelijk zijn. Ook verplaatsen of hernoemen van
de bronkolommen verandert de match niet. De kolomtoewijzing en inhoud blijven
onderworpen aan de bestaande importcontrole. Verandering van `kluit` naar `pot`
valt niet onder dit hergebruik op basis van exact dezelfde gegevens.

## Uitsluiten vanuit Voor controle

Vanuit 'Voor controle' kunnen ook gematchte regels bewust van WinTree-export worden
uitgesloten. De inkoper kan dit ook later doen, vóór vrijgave van die export.
[Exportuitsluiting](../glossary.md#term-uitsluiten-wintree-export) laat intern gebruik voor
catalogusbeheer, verkoop en assortimentsanalyse intact. Een uitsluiting vult geen codes in;
het concrete interne gebruik zonder productmatch staat nog open.

| Regel | Matchvoorwaarde van stap 5 |
| --- | --- |
| Naam- en maatcode gematcht | Voldaan |
| Bewust uitgesloten van WinTree-export | Ontbrekende match blokkeert niet |
| Op de wachtlijst voor ontbrekende stamcodes | Ontbrekende match blokkeert overige regels niet |
| Ongematcht zonder deze uitzonderingen | Definitieve verwerking geblokkeerd |

<a id="ac-voorraadimport-012"></a>

### Voor controle biedt uitsluiten ongeacht de matchstatus

Gegeven een nog niet gematchte regel A en een al gematchte regel B in 'Voor controle', kan de
gebruiker zowel A als B direct uitsluiten van de WinTree-export. Een geslaagde match is geen
belemmering om B uit te sluiten. De [exportspecificatie](wintree-export.md#ac-wintree-export-002) bepaalt het
resultaat in het exportbestand.

<a id="ac-voorraadimport-013"></a>

### Ongematchte regels zonder uitzondering blokkeren afronding

Gegeven een verder geldige import met één ongematchte regel die niet bewust is uitgesloten en niet
op de wachtlijst voor stamcodes staat, blijft stap 5 geblokkeerd en blijft de actuele voorraad
ongewijzigd.

<a id="ac-voorraadimport-014"></a>

### Uitgesloten en wachtende regels blokkeren niet op matching

Gegeven een verder geldige import met gematchte regels, één bewust uitgesloten ongematchte regel en
één wachtende regel waarvoor een stamcode ontbreekt, kan stap 5 doorgaan zonder eerst die twee
regels te matchen. De wachtende regel blijft bewaard voor latere verwerking; de uitgesloten regel
wordt niet verwijderd vanwege zijn exportuitsluiting.

## Wachtlijst voor stamcodes

De [wachtlijst](../glossary.md#term-wachtlijst-stamcodes) bewaart regels waarvoor een
naamcode of maatcode ontbreekt in de actuele WinTree-basisstam. Deze regels gaan nog niet
mee in de WinTree-export en blokkeren de overige export niet. De prijscontroles blijven gelden.

Een stamupdate start automatisch een nieuwe matchpoging; eenduidige matches kunnen verder
worden verwerkt. Onduidelijke matches blijven ter controle; ontbrekende codes blijven wachten.
De inkoper houdt de exportvrijgave. Later matchen heft een bewuste uitsluiting niet op.
Bij definitieve voorraadvervanging volgt de actieve wachtlijst dezelfde leverancier en bron:
ontbrekende regels vervallen, terugkerende regels gebruiken de nieuwste gegevens.

<a id="ac-voorraadimport-015"></a>

### Nieuwe stamcodes maken verwerking van wachtende regels mogelijk

Gegeven een wachtende regel waarvan de naamcode of maatcode ontbreekt en waarvan het
leveranciersbestand nog niet is vervangen, wanneer de benodigde codes via een basisstamupdate uit
WinTree beschikbaar komen, kan die bewaarde regel worden gematcht en verwerkt. Een eventuele bewuste
exportuitsluiting blijft behouden.

<a id="ac-voorraadimport-016"></a>

### Een stamupdate start automatisch een nieuwe matchpoging

Gegeven een wachtlijst bij een nog actuele leverancierslijst, wanneer de WinTree-basisstam in Fresh
wordt geactualiseerd, probeert Fresh die wachtende regels opnieuw te matchen zonder aparte
startactie door de gebruiker.

<a id="ac-voorraadimport-017"></a>

### Onduidelijke matches blijven ter controle

Gegeven een automatische matchpoging na een stamupdate die voor een wachtende regel geen eenduidige
match oplevert, blijft die regel ter controle staan en wordt geen willekeurige match vastgelegd.
Ontbreken de benodigde codes nog, dan blijft de regel wachten.

<a id="ac-voorraadimport-018"></a>

### Ontbrekende wachtregels vervallen bij een nieuwe lijst

Gegeven een actieve wachtende regel A en een nieuw bestand van dezelfde leverancier en bron waarin A
ontbreekt, blijft A tijdens de importvoorbereiding op de actieve wachtlijst. Na succesvolle
vervanging in stap 5 vervalt A uit die lijst. Als de benodigde stamcodes later beschikbaar komen,
verwerkt Fresh A niet alsnog vanuit de oude lijst als actueel aanbod.

<a id="ac-voorraadimport-019"></a>

### Terugkerende wachtregels gebruiken de nieuwste gegevens

Gegeven een wachtende regel met 20 planten en inkoopprijs EUR 10,00, wanneer deze regel terugkomt in
de nieuwe leverancierslijst met 12 planten en inkoopprijs EUR 11,00 en die lijst definitief is
verwerkt, gebruikt latere verwerking na een stamupdate de 12 planten en EUR 11,00 uit de nieuwste
lijst. De oude gegevens worden niet teruggezet of erbij opgeteld. De
[herkenningsroute](#herkenning-bij-volgende-leverancierslijsten) bepaalt of het dezelfde
uitvoering is, ook wanneer stamcodes nog ontbreken.

## Eenmalige V1-referentie

Deze vergelijking volgt de [vastgezette onderzoeksgrens](../architecture/overview.md#eenmalige-v1-referentie).
De bronnen hieronder zijn V1-waarnemingen, geen aanvullende Fresh-eisen.
De besloten herkenningsroute hierboven blijft staan; nieuwe keuzes horen bij
[issue #12](https://github.com/MenkehorstKwekerijen/Fresh/issues/12).

| Onderwerp | Aangetroffen V1-werking | Betekenis voor de keuze in Fresh |
| --- | --- | --- |
| Bestandsinrichting | Excel/CSV met werkblad-, kopregel- en kolomkeuze; profiel per leverancier. Bij ontbrekende voorraadkolom kan een expliciet standaardaantal worden gebruikt. Een gemapte voorraadkolom blijft leidend, ook bij een lege cel. [Parser/profiel][v1-parser], [verwerking][v1-process]. | Profielhergebruik is al besloten. Afzonderlijke pot-/kluit- en hoogtevelden, structuurherstel en een standaardaantal zijn nog te kiezen; geen V1-beginwaarde overnemen. |
| Volledige productmatch onthouden | De sleutel gebruikt leverancier, genormaliseerde plantnaam, bronmaat, potmaat en hoogte exclusief pot. Extra omschrijving, prijs, hoeveelheid en artikelcode zitten niet in die sleutel. De normalisatie is ruimer dan alleen hoofdletters/spaties. [Sleutel][v1-key], [toepassing][v1-prepare]. | Geen geschikte overname als identiteit voor kwaliteitsgebonden instellingen: twee kronen kunnen hetzelfde matchgeheugen delen. Fresh houdt het reeds gekozen onderscheid van uitvoeringen. |
| Naam en maat apart onthouden | Handmatig bevestigde volledige leveranciersnamen en veilige volledige bronmaten worden apart geleerd. Naamkennis kan over maten en maatkennis over planten worden hergebruikt, binnen dezelfde leverancier. Vorm-/stamhoogtecontext begrenst breed maatleren; een afwijkende bestaande koppeling vraagt bevestiging. [Geheugen][v1-memory]. | Afzonderlijk hergebruik is expliciet gekozen; de Fresh-afspraak en nog open grenzen staan bij [naam- en maatkoppelingen](#naam--en-maatkoppelingen-hergebruiken). De overige V1-geheugenregels zijn hiermee niet overgenomen. |
| Nieuwe of gewijzigde codematch | V1 maakt naam-/maatvoorstellen, controleert de actuele stam en de dekking van maatkenmerken. Eerder veilig geleerd gedrag kan direct bevestigd terugkomen; nieuwe volledig zekere voorstellen kunnen met een expliciete bulkactie worden goedgekeurd. [Voorbereiding][v1-prepare], [bulkselectie][v1-certain], [gelezen regressietest][v1-reimport-test]. | De Fresh-regel voor uitvoeringherkenning kiest nog geen fuzzy matcher, scores of bulkgoedkeuring. Bepaal die codematchbediening apart; neem geen V1-drempels stil over. |
| Wachten op codes | Naam en maat kunnen afzonderlijk wachten. Een officiële stamupload start hercontrole; alleen eenduidige volledig zekere matches worden automatisch opgelost. V1 biedt ook handmatig toepassen van een bestaande code of lokale stamkopie. [Hercontrole][v1-wait], [handmatige toepassing][v1-wait-apply]. | Automatische hercontrole is al besloten in Fresh. Groepsbediening en lokale stamkopieën zijn nog te kiezen; een lokale kopie maakt geen code in WinTree. |

De Fresh-afspraak voor dezelfde matchgegevens ongeacht hun bronkolom staat bij
[naam- en maatkoppelingen](#naam--en-maatkoppelingen-hergebruiken).
Het vervangingsmoment staat bij [voorraad](voorraad.md#eenmalige-v1-referentie);
de verschillende soorten uitsluiting staan bij [export](wintree-export.md#eenmalige-v1-referentie).

[v1-parser]: https://github.com/MenkehorstKwekerijen/WinTree-Tools/blob/209846776a450dabbe29dc32322e60a1c986243e/app/supplier_file.py#L364
[v1-process]: https://github.com/MenkehorstKwekerijen/WinTree-Tools/blob/209846776a450dabbe29dc32322e60a1c986243e/app/main.py#L2160
[v1-key]: https://github.com/MenkehorstKwekerijen/WinTree-Tools/blob/209846776a450dabbe29dc32322e60a1c986243e/app/importer.py#L1542
[v1-prepare]: https://github.com/MenkehorstKwekerijen/WinTree-Tools/blob/209846776a450dabbe29dc32322e60a1c986243e/app/workflow.py#L317
[v1-memory]: https://github.com/MenkehorstKwekerijen/WinTree-Tools/blob/209846776a450dabbe29dc32322e60a1c986243e/app/workflow.py#L863
[v1-certain]: https://github.com/MenkehorstKwekerijen/WinTree-Tools/blob/209846776a450dabbe29dc32322e60a1c986243e/app/main.py#L2276
[v1-reimport-test]: https://github.com/MenkehorstKwekerijen/WinTree-Tools/blob/209846776a450dabbe29dc32322e60a1c986243e/tests/test_v225_identical_reimport.py
[v1-wait]: https://github.com/MenkehorstKwekerijen/WinTree-Tools/blob/209846776a450dabbe29dc32322e60a1c986243e/app/main.py#L185
[v1-wait-apply]: https://github.com/MenkehorstKwekerijen/WinTree-Tools/blob/209846776a450dabbe29dc32322e60a1c986243e/app/main.py#L2805

## Keten en open keuzes

Leveranciersvoorkeuren, assortimentsanalyses en uitvoer naar WinTree of website gebruiken
voorraadgegevens. Hun actualiseringsmoment is nog niet bepaald. Vervallen aanbod mag ook
bij een onderbroken import of gelijktijdige stamupdate niet opnieuw actueel worden.

Nog te bepalen in [issue #12](https://github.com/MenkehorstKwekerijen/Fresh/issues/12):

- Bestandsvelden, leveranciers- en bronherkenning, gewijzigde kolommen/volgorde/structuur,
  bestanden met meerdere leveranciers, lege bestanden en overige bestandsfouten.
- Nieuwe naam-/maatcodematches; uitlezen en afbakenen van naam-/maatkenmerken
  tegenover opmerkingen, tekstvarianten, conflicten en correcties; gewijzigde of vervallen
  stamcodes, intern gebruik zonder match, verdere wachtlijstbediening en plaats
  van 'Voor controle'.
- Grenzen van productherkenning: geen of meerdere mogelijke voorgangers, dubbele regels,
  kenmerken in afzonderlijke velden zoals pot/kluit, terugkeer na een ontbrekende lijst,
  bronwissels en onthouden van eerder bevestigde tekstvarianten. Begininstellingen voor
  een andere uitvoering en de afhandeling van een nog open herkenningskeuze zijn ook open.
- Inhoudsvergelijking, ouder of opnieuw ingelezen bestand binnen dezelfde bron, gedrag bij
  open bronkeuze en bewaren/herbeoordelen van die keuze bij een volgende import.
- Historische bewaring, herstel, gelijktijdigheid en behoud van menselijke keuzes.

Exportvrijgave en behoud of opheffen van exportuitsluitingen horen bij de
[exportspecificatie](wintree-export.md) en
[issue #13](https://github.com/MenkehorstKwekerijen/Fresh/issues/13).
