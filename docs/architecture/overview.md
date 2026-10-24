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
[conceptspecificatie actuele voorraad](../specs/voorraad.md#gedrag-en-gegevens).

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

Een [wachtlijst voor stamcodes](../specs/voorraadimport.md#wachtlijst-voor-stamcodes)
verbindt leveranciersregels met latere basisstamupdates. De voorraadimportspecificatie
bezit matching, vervanging en behoud van de actuele wachtlijst.

Naamcode en maatcode onderscheiden niet alle kwaliteitsuitvoeringen bij een
leverancier. [Productherkenning bij volgende leverancierslijsten](../specs/voorraadimport.md#herkenning-bij-volgende-leverancierslijsten)
gebruikt aangeleverde tekst en gebruikerskeuzes; een codematch is niet hetzelfde
als herkenning van de uitvoering. De rol van afzonderlijke pot-/kluitvelden,
bronwissels en het gebruik van codes in historische verkopen blijven open.

## Verwerking en afnemers

De operationele route omvat voorraad inlezen, fictieve voorraad naar WinTree-codes
omzetten, marges bepalen en exporteren naar WinTree. De inkoper controleert marges
en de import in WinTree. De [exportspecificatie](../specs/wintree-export.md) bezit
inkopersvrijgave en selectie van exportregels. Het formaat en de bevestiging van
verwerking in WinTree zijn nog te bepalen; exportuitsluiting is geen interne aanbodfilter.

De [prijsspecificatie](../specs/prijzen.md) bezit berekening, groepstoewijzing en
prijsvalidatie. De berekening gebruikt leverancier, productkoppeling en inkoopprijs.
Groepstoewijzing gebruikt daarnaast aanbod uit fictief/TCM en gekoppelde
verkoopgeschiedenis. Instellingen volgen de herkende productuitvoering bij een
leverancier. De verdere herkenningsgrenzen, verkoopkoppeling, uiteindelijke
catalogusprijs en prijsvelden voor elke afnemer zijn nog te bepalen.

De commerciële route gebruikt voorraadbronnen en historische verkoopgegevens
voor leveranciersvoorkeuren en assortimentskeuzes. Catalogusbeheer omvat de
productgegevens en websiteweergave uit de projectbasis. De website leest nu
CSV-bestanden in; Fresh sluit in de eerste versie op die route aan. Welke velden
worden aangeleverd en hoe de website wijzigingen verwerkt, vraagt nog een
expliciete interfaceafspraak. Een API-koppeling is de gewenste latere uitbreiding;
deze is niet nodig voor de eerste CSV-route.

Deze routes delen gegevens. De bekende samenloop tussen leveranciersbestanden
en TCM en het onderscheid met dezelfde soort en maat bij verschillende leveranciers
staan in de [conceptspecificatie actuele voorraad](../specs/voorraad.md#leveranciers-en-mogelijke-dubbele-aanlevering).
De bronvoorrang voor deze samenloop staat bij het
[criterium over de voorraaddatum](../specs/voorraad.md#ac-voorraadimport-003).
Uitzonderingen op de datumvergelijking staan in dezelfde specificatie. De
technische bestandsvalidatie en overige combinatieregels zijn nog uit te werken.

## Eenmalige V1-referentie

Op expliciet verzoek van de gebruiker is op 24 oktober 2026 WinTree-Tools V1
eenmalig alleen-lezen onderzocht op main
[`209846776a450dabbe29dc32322e60a1c986243e`](https://github.com/MenkehorstKwekerijen/WinTree-Tools/commit/209846776a450dabbe29dc32322e60a1c986243e).
De opdracht en afbakening staan in [issue #20](https://github.com/MenkehorstKwekerijen/Fresh/issues/20).
Dit is een vastgezette referentie, geen blijvende bronafhankelijkheid van Fresh.
Er is geen V1-code overgenomen of gewijzigd. Documentatie, code en aanwezige tests
zijn statisch gelezen; de applicatie en praktijkbestanden zijn niet uitgevoerd.

De waarnemingen en nog voor te leggen keuzes staan bij
[import en herkenning](../specs/voorraadimport.md#eenmalige-v1-referentie),
[voorraadvervanging](../specs/voorraad.md#eenmalige-v1-referentie),
[prijsinstellingen](../specs/prijzen.md#eenmalige-v1-referentie) en
[export](../specs/wintree-export.md#eenmalige-v1-referentie).
V1 heeft verschillende sleutels voor matchgeheugen, voorraadvarianten en prijzen;
die vormen niet gezamenlijk één reeds gekozen Fresh-identiteit. Ook bestaan in
V1 zowel een directe bulkexportroute als een inkopersreviewroute. De vergelijking
benoemt daarom welke route is onderzocht. Alleen een expliciet gebruikersbesluit
verandert de Fresh-afspraken; referentiegedrag en aanbevelingen zijn geen acceptatie.

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
