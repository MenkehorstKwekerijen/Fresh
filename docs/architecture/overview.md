# Gegevensketen en systeemgrenzen

Dit overzicht bezit de bekende gegevensstromen en technische grenzen van Fresh.
Het beschrijft de productrichting, geen reeds gebouwde architectuur. Doel,
gebruikers en scope staan in [de projectbasis](../project.md); betekenis staat
in [de glossary](../glossary.md).

## Inkomende gegevens

| Bron | Bekende aanlevering | Nog te bepalen grens |
| --- | --- | --- |
| [WinTree-basisstam](../glossary.md#term-wintree-basisstam) | Excel/CSV uit WinTree met naamcodes, maatcodes en bijbehorende omschrijvingen | Bestandsindeling, actualisering en verwerking van gewijzigde codes |
| [Externe fictieve voorraad](../glossary.md#term-externe-fictieve-voorraad) | Excel of CSV, ritme verschilt per leverancier | Bestandsinhoud, bronafbakening en actualiteit |
| [Eigen voorraad](../glossary.md#term-eigen-voorraad) | Periodiek vanuit WinTree via Excel of CSV | Bestandsinhoud, bronafbakening en actualiteit |
| [Eigen externe voorraad](../glossary.md#term-eigen-externe-voorraad) | Periodiek vanuit WinTree via Excel of CSV | Bestandsinhoud, bronafbakening en actualiteit |
| [TCM-voorraad](../glossary.md#term-tcm-voorraad) | Periodiek vanuit WinTree via Excel of CSV | Bestandsinhoud, bronafbakening en actualiteit |
| Historische verkoopgegevens | Periodiek vanuit WinTree via Excel of CSV | Bestandsinhoud, periode, detailniveau en herhaalde aanlevering |
| Catalogusupdates | Excel-lijsten en afzonderlijke producten toevoegen | Identificatie van bestaande producten en betekenis van wijzigingen |

De automatische ontvangst van TCM betreft de aanlevering aan WinTree. De route
van WinTree naar Fresh gebruikt periodieke bestanden, net als de andere hierboven
genoemde WinTree-bronnen. Frequentie en handmatige of automatische bediening van
die bestandsoverdracht zijn nog niet bepaald. De besloten vervangingsregel voor
de vier voorraadsoorten staat in de
[conceptspecificatie voorraadimport](../specs/voorraadimport.md#gedrag-en-gegevens).

## Omzetting naar WinTree-codes

De catalogus en de overige voorraadbronnen gebruiken de naamcodes en maatcodes uit de
[WinTree-basisstam](../glossary.md#term-wintree-basisstam). Externe fictieve
voorraad wordt aangeleverd met plantnamen, maten en pot-/kluitgegevens. Fresh moet
deze gegevens omzetten naar de bijbehorende WinTree-naamcodes en -maatcodes voor
de latere import in het ERP.

De basisstam is daarmee een noodzakelijke referentie voor deze omzetting en is
beschikbaar als Excel/CSV met de codes en bijbehorende omschrijvingen. Hoe Fresh
deze referentie actueel houdt en gewijzigde codes verwerkt, is nog te bepalen. De regels
voor herkenning, meerdere mogelijke codes, ontbrekende codes en hergebruik van
menselijke keuzes horen in de eerste relevante productspecificatie.

Het gebruik van naamcodes en maatcodes bepaalt nog niet of hun combinatie een
volledige productidentiteit vormt. De precieze rol van pot-/kluitgegevens en het
gebruik van codes in historische verkopen moeten nog worden bevestigd.

## Verwerking en afnemers

De operationele route omvat voorraad inlezen, fictieve voorraad naar WinTree-codes
omzetten, marges bepalen en exporteren naar WinTree. De inkoper controleert marges
en de import in WinTree. Exportformaat,
controlepunten en bevestiging van verwerking in het ERP zijn nog te specificeren.

De gekozen prijswijzen en open vragen over margegroepen staan in de
[conceptspecificatie prijzen](../specs/prijzen.md). Ingelezen leveranciersvoorraad
krijgt de standaardmarge van die leverancier op diens inkoopprijs. Afzonderlijke
margegroeptoewijzingen gelden per product en leverancier en vervangen voor die
combinatie de standaardmarge, zonder stapeling. Hoe leveranciersprijzen naar een catalogusprijs
leiden en welke prijzen naar afnemers gaan, moet nog worden uitgewerkt.

Voor margegroeptoewijzing selecteert de gebruiker producten binnen een leverancier
met filters op actueel fictief/TCM-aanbod en verkoopgeschiedenis. Deze route
vereist betrouwbare koppeling van verkoopgegevens aan producten en waar nodig
leveranciers; de beschikbare velden en filterbetekenis moeten nog worden bepaald.

De commerciële route gebruikt voorraadbronnen en historische verkoopgegevens
voor leveranciersvoorkeuren en assortimentskeuzes. Catalogusbeheer omvat de
productgegevens en websiteweergave uit de projectbasis. De website leest nu
CSV-bestanden in; Fresh sluit in de eerste versie op die route aan. Welke velden
worden aangeleverd en hoe de website wijzigingen verwerkt, vraagt nog een
expliciete interfaceafspraak. Een API-koppeling is de gewenste latere uitbreiding;
deze is niet nodig voor de eerste CSV-route.

Deze routes delen gegevens. De bekende samenloop tussen leveranciersbestanden
en TCM en het onderscheid met dezelfde soort en maat bij verschillende leveranciers
staan in de [conceptspecificatie voorraadimport](../specs/voorraadimport.md#leveranciers-en-mogelijke-dubbele-aanlevering).
De bronvoorrang voor deze samenloop staat bij het
[criterium over de voorraaddatum](../specs/voorraadimport.md#ac-voorraadimport-003).
Uitzonderingen op de datumvergelijking staan in dezelfde specificatie. De
technische bestandsvalidatie en overige combinatieregels zijn nog uit te werken.

## Technische richting

De gebruiker stelt PostgreSQL voor als database. Dit is een technische
voorkeursrichting; inrichting, applicatiestack en hosting zijn nog niet besloten.
Het gebruiksprofiel staat in [de projectbasis](../project.md#gebruikers-en-gebruik).

Een gedeelde database bepaalt niet zelfstandig hoe gelijktijdige imports en
wijzigingen met elkaar omgaan. Transactiegrenzen, conflictdetectie en herstel
moeten aansluiten op het nog te specificeren gedrag.

## Uitwerking per praktijkroute

Bij de eerste productspecificatie worden voor de geraakte ketenonderdelen
identiteit, herkomst, actualiteit, controle, foutgedrag, herhaling en herstel
uitgewerkt volgens de [ketencontrole](../workflow.md#ketencontrole).
Een onbesliste bronbetekenis wordt niet door een technische standaard ingevuld.
De vervolgbesluiten worden verzameld in
[issue #4](https://github.com/MenkehorstKwekerijen/Fresh/issues/4).
