---
id: voorraadimport
status: draft
depends_on: []
---
# Voorraadimport

## Doel en scope

Nieuwe voorraadbestanden actualiseren de voorraad in Fresh. Deze eerste
conceptspecificatie legt de besloten vervangingsregel vast; de volledige
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

### Leveranciers en mogelijke dubbele aanlevering

Dezelfde soort en maat kunnen bij verschillende leveranciers beschikbaar zijn.
Dat is op zichzelf geen dubbele aanlevering van dezelfde voorraad.

De gebruiker heeft geen overlap bevestigd tussen eigen voorraad, eigen externe
voorraad en de andere voorraadsoorten. Wel kan één leverancier in theorie zowel
via een fictief voorraadbestand als via TCM worden ingelezen. Daar kan dezelfde
voorraad dus via twee routes binnenkomen. Of de twee lijsten dan hetzelfde
volledige aanbod bevatten en welke bron moet worden gebruikt, is nog niet bepaald.

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

## Open keuzes

Verdere afbakening, de afhandeling van een leverancier die zowel via fictief
als TCM binnenkomt en de hierboven genoemde import- en herstelvragen worden behandeld in
[issue #4](https://github.com/MenkehorstKwekerijen/Fresh/issues/4).
