---
id: prijzen
status: draft
depends_on: []
---
# Prijsinstellingen en margegroepen

## Doel en scope

Fresh ondersteunt [opslag op inkoop](../glossary.md#term-opslag-op-inkoop) en
een [vaste verkoopprijs](../glossary.md#term-vaste-verkoopprijs). Een product heeft
na toewijzing één actieve [margegroep](../glossary.md#term-margegroep).
Leverancier en catalogushoofdstuk helpen bij de automatische toewijzing.
Handmatige toewijzing en keuze zijn ook beschikbaar als
[bulkactie](../glossary.md#term-bulkactie).

Het actuele gebruikersbesluit staat in
[issue #6](https://github.com/MenkehorstKwekerijen/Fresh/issues/6).
De specificatie is nog niet volledig genoeg voor implementatie.

## Gedrag en gegevens

### Prijswijzen

Bij procentuele opslag geldt:

`verkoopprijs = inkoopprijs × (1 + opslagpercentage / 100)`

Bij een vaste verkoopprijs is het expliciet ingestelde bedrag de verkoopprijs.
Een brutomargepercentage over de verkoopprijs is niet als prijswijze gekozen.
Hoe beide gekozen prijswijzen in de margegroep of op het product worden
vastgelegd, is nog te bepalen; de wens voor een vaste verkoopprijs blijft gelden.

### Eén actieve groep en kandidaten voor toewijzing

Margegroepen kunnen worden aangemaakt en aan producten toegewezen. Instellingen
bij leverancier en hoofdstuk leveren [kandidaat-margegroepen](../glossary.md#term-kandidaat-margegroep)
voor automatische toewijzing bij nieuwe producten. Er is geen voorrangsvolgorde
tussen product, leverancier en hoofdstuk voor de prijsberekening.

Bij één kandidaat wordt die groep automatisch gekoppeld. Wanneer leverancier
en hoofdstuk dezelfde groep opleveren, is dat één kandidaat. Bij verschillende
kandidaten krijgt de gebruiker een duidelijk aandachtspunt en kiest die eenmaal,
eventueel voor meerdere producten met een bulkactie.

De gekozen groep blijft aan het product gekoppeld. Een volgende prijsberekening
vraagt niet opnieuw om dezelfde keuze. Leverancier en hoofdstuk blijven dus niet
bij elke berekening concurrerende prijsinstellingen leveren.

### Herbeoordeling na gewijzigde toewijzingsregels

Een wijziging van de toewijzingsregels bij leverancier of hoofdstuk overschrijft
de gekozen groep van bestaande producten niet automatisch. Bestaande producten
vragen een expliciete herbeoordeling. Een andere groep wordt pas gekoppeld als
die herbeoordeling tot die keuze leidt.

Deze afspraak gaat over het wijzigen van toewijzingsregels. Wat er gebeurt als
de prijsinstellingen binnen een al gekoppelde margegroep wijzigen, is nog open.

## Keten en herstel

De prijsberekening gebruikt een inkoopprijs. Welke prijs geldt bij meerdere
leveranciers of voorraadbronnen en of deze keuze samenhangt met de
leveranciersvoorkeur moet nog worden besloten.

WinTree-export en catalogus/website zijn relevante afnemers binnen het
[productdoel](../project.md). Welke prijsvelden elke afnemer krijgt, moet nog
worden uitgewerkt. Herberekening bij nieuwe inkoopprijzen of gewijzigde
groepsinhoud, gelijktijdige wijzigingen en herstel vragen nog afspraken.

## Acceptatiecriteria

<a id="ac-prijzen-001"></a>

### Opslag wordt over de inkoopprijs berekend

Gegeven een inkoopprijs van EUR 10,00 en een ingestelde opslag van 30 procent,
is de berekende verkoopprijs EUR 13,00.

<a id="ac-prijzen-002"></a>

### De vaste verkoopprijs bepaalt het verkoopbedrag

Gegeven een toepasselijke instelling met vaste verkoopprijs EUR 15,00 en een
inkoopprijs van EUR 10,00, is de verkoopprijs EUR 15,00.

<a id="ac-prijzen-004"></a>

### Een bulkactie past de toewijzing toe op de selectie

Gegeven drie beschikbare onderdelen A, B en C, waarbij de gebruiker A en B
selecteert, kan de gebruiker met één bulkactie een margegroep voor A en B
toewijzen. De directe toewijzing van het niet-geselecteerde onderdeel C verandert niet.

<a id="ac-prijzen-008"></a>

### Eén kandidaat wordt automatisch gekoppeld

Gegeven een nieuw product waarvoor de leveranciers- en hoofdstukinstellingen
samen alleen groep G opleveren, wordt G automatisch de actieve margegroep.
Dit geldt ook wanneer beide instellingen dezelfde groep G aanwijzen.

<a id="ac-prijzen-009"></a>

### Verschillende kandidaten vragen een eenmalige keuze

Gegeven een nog niet toegewezen product met kandidaat G via de leverancier en
H via het hoofdstuk, toont Fresh de kandidaten en hun herkomst. De gebruiker
kan eenmaal een groep kiezen, ook in bulk. Na keuze voor H is alleen H actief.

<a id="ac-prijzen-010"></a>

### Een gekozen koppeling blijft behouden

Gegeven een product waarvoor de gebruiker bij kandidaten G en H groep H heeft
gekozen, blijft H bij volgende berekeningen actief zonder een herhaalde
keuzevraag over dezelfde kandidaten.

<a id="ac-prijzen-011"></a>

### Gewijzigde toewijzingsregels vereisen expliciete herbeoordeling

Gegeven een product met actieve groep G, blijft G gekoppeld wanneer de
leveranciers- of hoofdstukinstelling een andere groep H gaat voorstellen.
Wijziging van de productkoppeling naar H vereist expliciete herbeoordeling.

## Open keuzes

Inhoud van margegroepen en de plaats van vaste verkoopprijzen, gedrag bij geen
kandidaat of een nog open keuze, gevolgen van gewijzigde groepsinhoud, afronding,
de basis van bedragen (zoals belasting en bijkomende kosten), ontbrekende
inkoopprijzen en de hierboven genoemde ketengevolgen worden uitgewerkt in
[issue #6](https://github.com/MenkehorstKwekerijen/Fresh/issues/6).
