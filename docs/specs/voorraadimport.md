---
id: voorraadimport
status: draft
depends_on: []
---
# Voorraadimport

## Doel en scope

Nieuwe voorraadbestanden actualiseren de voorraad in Fresh. Deze eerste
conceptspecificatie legt de besloten vervangingsregel en bronvoorrang vast; de volledige
importroute is nog niet voldoende bepaald om te bouwen.

De regel geldt voor [externe fictieve voorraad](../glossary.md#term-externe-fictieve-voorraad),
[eigen voorraad](../glossary.md#term-eigen-voorraad),
[eigen externe voorraad](../glossary.md#term-eigen-externe-voorraad) en
[TCM-voorraad](../glossary.md#term-tcm-voorraad).
Het gebruikersbesluit is vastgelegd in
[issue #4](https://github.com/MenkehorstKwekerijen/Fresh/issues/4).

## Gedrag en gegevens

Een nieuw voorraadbestand vervangt de vorige voorraad van dezelfde leverancier
of bron volledig. Het bestand bevat de nieuwe voorraadstand, geen aanvulling
op de vorige stand. Regels die ontbreken in het nieuwe bestand behoren na
vervanging niet meer tot de actuele voorraad van die leverancier of bron.

Deze afspraak bepaalt geen vervangingsgedrag voor historische verkoopgegevens,
de WinTree-basisstam of catalogusupdates. De bestandsvelden die bepalen bij welke
leverancier of bron een bestand hoort, moeten nog worden uitgewerkt.

Voor leveranciersvoorraadlijsten geldt vóór het inlezen de
[controle op een ingestelde standaardmarge](prijzen.md#ac-prijzen-046).
Bij deze blokkade vindt geen vervanging van de bestaande voorraad plaats.
De afhandeling van een bestand met meerdere leveranciers wordt nog uitgewerkt.

### Leveranciers en mogelijke dubbele aanlevering

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

## Keten en herstel

Leveranciersvoorkeuren, assortimentsanalyses en uitvoer naar WinTree of website
kunnen door de nieuwe voorraadstand worden geraakt. Wanneer deze afnemers
worden bijgewerkt, is nog niet besloten.

De vervangingsregel bepaalt evenmin het gedrag bij een ongeldig of leeg bestand,
onbekende codes, een onderbroken import of gelijktijdige wijzigingen. Dat moet
worden gespecificeerd vóór implementatie, inclusief herstel en de gevolgen voor
eerder vastgelegde menselijke keuzes.

## Acceptatiecriteria

<a id="ac-voorraadimport-001"></a>

### De nieuwe stand vervangt de vorige

Gegeven een vorige stand van 20 planten en een nieuw bestand met 12 planten voor
dezelfde regel en leverancier of bron, is de actuele stand na vervanging 12,
niet 32. Dit geldt voor elk van de vier voorraadsoorten in scope.

<a id="ac-voorraadimport-002"></a>

### Ontbrekende regels vervallen uit de actuele voorraad

Gegeven een vorige lijst met regels A en B en een nieuwe lijst met alleen A,
behoort B na vervanging niet meer tot de actuele voorraad van die leverancier
of bron. Dit bepaalt niet of historische gegevens worden bewaard.

<a id="ac-voorraadimport-003"></a>

### De voorraaddatum bepaalt de bronvoorrang

Gegeven hetzelfde aanbod van één leverancier via beide routes, met één regel
van 20 planten in TCM met datum 20 oktober 2026 in het Excelbestand en 12 planten
in fictief ingelezen in Fresh op 22 oktober 2026, is fictief leidend en is de
gebruikte voorraad 12, ook als het TCM-bestand op 23 oktober wordt ingelezen.
Staat bij dezelfde TCM-voorraad in het Excelbestand 23 oktober, dan is TCM
leidend en is de gebruikte voorraad 20.

<a id="ac-voorraadimport-004"></a>

### Bronkeuze geldt voor de volledige leverancierslijst

Gegeven een oudere TCM-lijst met regels A en B en een nieuwere fictieve lijst
met alleen A voor dezelfde leverancier, wordt de fictieve lijst gebruikt.
B wordt niet aangevuld vanuit de oudere TCM-lijst. Bij een nieuwere TCM-lijst
geldt dezelfde regel met TCM als gekozen bron.

<a id="ac-voorraadimport-005"></a>

### Gelijke datum en inhoud vragen geen handmatige keuze

Gegeven fictief en TCM voor dezelfde leverancier met dezelfde geldige datum en
dezelfde voorraadinhoud, vraagt Fresh geen bronkeuze aan de gebruiker. De voorraad
wordt niet dubbel geteld.

<a id="ac-voorraadimport-006"></a>

### Verschillende inhoud op dezelfde datum vraagt één bronkeuze

Gegeven fictief en TCM voor dezelfde leverancier met dezelfde geldige datum,
maar respectievelijk 12 en 20 planten voor dezelfde regel, toont Fresh één
aandachtspunt waarin de gebruiker de te gebruiken bron kiest.

<a id="ac-voorraadimport-007"></a>

### Een ontbrekende of ongeldige datum vraagt één bronkeuze

Gegeven samenloop van fictief en TCM voor dezelfde leverancier, waarbij een
benodigde datum ontbreekt of ongeldig is, toont Fresh één aandachtspunt waarin
de gebruiker de te gebruiken bron kiest.

## Open keuzes

Verdere afbakening, de vergelijking van inhoud, het gedrag zolang een bronkeuze
openstaat en het bewaren en opnieuw beoordelen van die keuze bij nieuwe import,
en de hierboven genoemde import- en herstelvragen worden behandeld in
[issue #4](https://github.com/MenkehorstKwekerijen/Fresh/issues/4).
