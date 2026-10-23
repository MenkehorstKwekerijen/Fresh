# Gegevensketen en systeemgrenzen

Dit overzicht bezit de bekende gegevensstromen en technische grenzen van Fresh.
Het beschrijft de productrichting, geen reeds gebouwde architectuur. Doel,
gebruikers en scope staan in [de projectbasis](../project.md); betekenis staat
in [de glossary](../glossary.md).

## Inkomende gegevens

| Bron | Bekende aanlevering | Nog te bepalen grens |
| --- | --- | --- |
| [Externe fictieve voorraad](../glossary.md#term-externe-fictieve-voorraad) | Excel of CSV, ritme verschilt per leverancier | Bestandsinhoud en vervanging of aanvulling van vorige gegevens |
| [Eigen voorraad](../glossary.md#term-eigen-voorraad) | Periodiek vanuit WinTree via Excel of CSV | Bestandsinhoud, actualiteit en vervanging of aanvulling |
| [Eigen externe voorraad](../glossary.md#term-eigen-externe-voorraad) | Periodiek vanuit WinTree via Excel of CSV | Bestandsinhoud, actualiteit en vervanging of aanvulling |
| [TCM-voorraad](../glossary.md#term-tcm-voorraad) | Periodiek vanuit WinTree via Excel of CSV | Bestandsinhoud, actualiteit en vervanging of aanvulling |
| Historische verkoopgegevens | Periodiek vanuit WinTree via Excel of CSV | Bestandsinhoud, periode, detailniveau en herhaalde aanlevering |
| Catalogusupdates | Excel-lijsten en afzonderlijke producten toevoegen | Identificatie van bestaande producten en betekenis van wijzigingen |

De automatische ontvangst van TCM betreft de aanlevering aan WinTree. De route
van WinTree naar Fresh gebruikt periodieke bestanden, net als de andere hierboven
genoemde WinTree-bronnen. Frequentie en handmatige of automatische bediening van
die bestandsoverdracht zijn nog niet bepaald.

## Verwerking en afnemers

De operationele route omvat voorraad inlezen, marges bepalen en exporteren naar
WinTree. De inkoper controleert marges en de import in WinTree. Exportformaat,
controlepunten en bevestiging van verwerking in het ERP zijn nog te specificeren.

De commerciële route gebruikt voorraadbronnen en historische verkoopgegevens
voor leveranciersvoorkeuren en assortimentskeuzes. Catalogusbeheer omvat de
productgegevens en websiteweergave uit de projectbasis. De website leest nu
CSV-bestanden in; Fresh sluit in de eerste versie op die route aan. Welke velden
worden aangeleverd en hoe de website wijzigingen verwerkt, vraagt nog een
expliciete interfaceafspraak. Een API-koppeling is de gewenste latere uitbreiding;
deze is niet nodig voor de eerste CSV-route.

Deze routes delen gegevens. Welke producten tussen bronnen bij elkaar horen en
hoe mogelijke overlap tussen voorraadbronnen wordt behandeld, moet expliciet
worden besloten voordat gegevens worden gecombineerd. Er is nog geen regel
vastgesteld voor optellen, voorrang of uitsluiten van bronnen.

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
