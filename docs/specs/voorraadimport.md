---
id: voorraadimport
status: draft
depends_on: []
---
# Voorraadimport

## Doel en scope

Voorraadbestanden vervangen de actuele stand in Fresh. Dit geldt voor fictieve voorraad,
eigen voorraad, eigen externe voorraad en TCM. De leveranciersroute voegt kolomtoewijzing,
matching en een wachtlijst toe. Historische verkopen, basisstam- en catalogusupdates vallen
buiten deze vervangingsregel. Geen prijsberekening of uitwerking van exportvrijgave.
Deze conceptafspraken zijn nog niet volledig genoeg voor implementatie.
Besluiten en open keuzes: [issue #12](https://github.com/MenkehorstKwekerijen/Fresh/issues/12).
Eerdere basisbesluiten staan in [issue #4](https://github.com/MenkehorstKwekerijen/Fresh/issues/4).

Lees gericht: [vervangen](#voorraad-vervangen) · [bronvoorrang](#leveranciers-en-mogelijke-dubbele-aanlevering) ·
[importstappen](#stappen-van-de-leveranciersimport) · [kolommen](#kolomtoewijzing-in-stap-2) ·
[uitsluiten en matching](#uitsluiten-vanuit-voor-controle) · [wachtlijst](#wachtlijst-voor-stamcodes) ·
[keten en open keuzes](#keten-en-open-keuzes).

<a id="gedrag-en-gegevens"></a>

## Voorraad vervangen

Een nieuwe definitief verwerkte lijst vervangt de vorige voor dezelfde leverancier of bron,
zonder oude regels bij te mengen. Historische bewaring is een aparte open keuze.

<a id="ac-voorraadimport-001"></a>

### De nieuwe stand vervangt de vorige

Gegeven een vorige stand van 20 planten en een nieuw bestand met 12 planten voor dezelfde regel en
leverancier of bron, is de actuele stand na vervanging 12, niet 32. Dit geldt voor elk van de vier
voorraadsoorten in scope.

<a id="ac-voorraadimport-002"></a>

### Ontbrekende regels vervallen uit de actuele voorraad

Gegeven een vorige lijst met regels A en B en een nieuwe lijst met alleen A, behoort B na vervanging
niet meer tot de actuele voorraad van die leverancier of bron. Dit bepaalt niet of historische
gegevens worden bewaard.

## Leveranciers en mogelijke dubbele aanlevering

Dezelfde soort en maat kunnen bij verschillende leveranciers beschikbaar zijn.
Dat is op zichzelf geen dubbele aanlevering van dezelfde voorraad.

De gebruiker heeft geen overlap bevestigd tussen eigen voorraad, eigen externe
voorraad en de andere voorraadsoorten. Wel kan één leverancier in theorie zowel
via een fictief voorraadbestand als via TCM worden ingelezen. Daar komt hetzelfde
aanbod via twee routes binnen. De aanlevering vermeldt expliciet of het om TCM of
"inkoop aanbieding" (fictief) gaat. Bij deze samenloop is de bron met de meest
recente [voorraaddatum](../glossary.md#term-voorraaddatum) leidend. De datum wordt
per bron als volgt bepaald:

| Bron | Datum voor de vergelijking |
| --- | --- |
| Fictief | De [importdatum](../glossary.md#term-importdatum): het bestand inlezen via de importeerfunctie in Fresh |
| TCM | De datum per leverancier die in het TCM-Excelbestand staat; diens regels worden in één keer naar WinTree overgedragen |

Het moment waarop het TCM-bestand in Fresh wordt ingelezen vervangt de datum
uit dat bestand niet. De keuze tussen fictief en TCM geldt voor de volledige
voorraadlijst van dezelfde leverancier, niet afzonderlijk per productregel.
De overlappende voorraad wordt niet opgeteld en regels uit de oudere lijst
worden niet bijgemengd in de gekozen nieuwere lijst.

Bij de datumvergelijking gelden de volgende uitzonderingen:

| Situatie bij dezelfde leverancier | Gedrag |
| --- | --- |
| Gelijke geldige datum en gelijke inhoud | Geen gebruikersactie nodig; de voorraad blijft enkelvoudig |
| Gelijke geldige datum, maar verschillende inhoud | Eén aandachtspunt waarin de gebruiker de bron kiest |
| Een benodigde datum ontbreekt of is ongeldig | Eén aandachtspunt waarin de gebruiker de bron kiest |

De exacte veldnamen, herkenning van dezelfde leverancier en vergelijking van
inhoud moeten nog worden uitgewerkt en aan bestanden getoetst. Dit besluit gaat
over samenloop van fictief en TCM, niet over de verwerking van een ouder bestand
binnen dezelfde bron. Ook het opnieuw inlezen van hetzelfde fictieve bestand
vraagt nog een expliciete afspraak.

<a id="ac-voorraadimport-003"></a>

### De voorraaddatum bepaalt de bronvoorrang

Gegeven hetzelfde aanbod van één leverancier via beide routes, met één regel van 20 planten in TCM
met datum 20 oktober 2026 in het Excelbestand en 12 planten in fictief ingelezen in Fresh op 22
oktober 2026, is fictief leidend en is de gebruikte voorraad 12, ook als het TCM-bestand op 23
oktober wordt ingelezen. Staat bij dezelfde TCM-voorraad in het Excelbestand 23 oktober, dan is TCM
leidend en is de gebruikte voorraad 20.

<a id="ac-voorraadimport-004"></a>

### Bronkeuze geldt voor de volledige leverancierslijst

Gegeven een oudere TCM-lijst met regels A en B en een nieuwere fictieve lijst met alleen A voor
dezelfde leverancier, wordt de fictieve lijst gebruikt. B wordt niet aangevuld vanuit de oudere
TCM-lijst. Bij een nieuwere TCM-lijst geldt dezelfde regel met TCM als gekozen bron.

<a id="ac-voorraadimport-005"></a>

### Gelijke datum en inhoud vragen geen handmatige keuze

Gegeven fictief en TCM voor dezelfde leverancier met dezelfde geldige datum en dezelfde
voorraadinhoud, vraagt Fresh geen bronkeuze aan de gebruiker. De voorraad wordt niet dubbel geteld.

<a id="ac-voorraadimport-006"></a>

### Verschillende inhoud op dezelfde datum vraagt één bronkeuze

Gegeven fictief en TCM voor dezelfde leverancier met dezelfde geldige datum, maar respectievelijk 12
en 20 planten voor dezelfde regel, toont Fresh één aandachtspunt waarin de gebruiker de te gebruiken
bron kiest.

<a id="ac-voorraadimport-007"></a>

### Een ontbrekende of ongeldige datum vraagt één bronkeuze

Gegeven samenloop van fictief en TCM voor dezelfde leverancier, waarbij een benodigde datum
ontbreekt of ongeldig is, toont Fresh één aandachtspunt waarin de gebruiker de te gebruiken bron
kiest.

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
lijst. De oude gegevens worden niet teruggezet of erbij opgeteld. De herkenning van dezelfde regel
moet afzonderlijk worden gespecificeerd.

## Keten en open keuzes

Leveranciersvoorkeuren, assortimentsanalyses en uitvoer naar WinTree of website gebruiken
voorraadgegevens. Hun actualiseringsmoment is nog niet bepaald. Vervallen aanbod mag ook
bij een onderbroken import of gelijktijdige stamupdate niet opnieuw actueel worden.

Nog te bepalen in [issue #12](https://github.com/MenkehorstKwekerijen/Fresh/issues/12):

- Bestandsvelden, leveranciers- en bronherkenning, gewijzigde kolommen/volgorde/structuur,
  bestanden met meerdere leveranciers, lege bestanden en overige bestandsfouten.
- Exacte matchregels, codeproblemen, productidentiteit, herkenning van terugkerende regels,
  intern gebruik zonder match, verdere wachtlijstbediening en plaats van 'Voor controle'.
- Inhoudsvergelijking, ouder of opnieuw ingelezen bestand binnen dezelfde bron, gedrag bij
  open bronkeuze en bewaren/herbeoordelen van die keuze bij een volgende import.
- Historische bewaring, herstel, gelijktijdigheid en behoud van menselijke keuzes.

Exportvrijgave en hergebruik van exportuitsluitingen horen bij de
[exportspecificatie](wintree-export.md) en
[issue #13](https://github.com/MenkehorstKwekerijen/Fresh/issues/13).
