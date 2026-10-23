---
id: prijzen
status: draft
depends_on: []
---
# Prijsinstellingen en margegroepen

## Doel en scope

Fresh ondersteunt [opslag op inkoop](../glossary.md#term-opslag-op-inkoop) en
een [vaste verkoopprijs](../glossary.md#term-vaste-verkoopprijs).
[Margegroepen](../glossary.md#term-margegroep) moeten kunnen worden aangemaakt en
toegewezen voor individuele producten, leveranciers en catalogushoofdstukken,
ook via een [bulkactie](../glossary.md#term-bulkactie). Dit gebruikersbesluit staat in
[issue #6](https://github.com/MenkehorstKwekerijen/Fresh/issues/6).
De specificatie is nog niet volledig genoeg voor implementatie.

## Gedrag en gegevens

Bij procentuele opslag geldt:

`verkoopprijs = inkoopprijs × (1 + opslagpercentage / 100)`

Bij een vaste verkoopprijs is het expliciet ingestelde bedrag de verkoopprijs.
Een brutomargepercentage over de verkoopprijs is niet als prijswijze gekozen.

Margegroepen kunnen worden aangemaakt. Toewijzing is beschikbaar voor individuele
producten, leveranciers en catalogushoofdstukken, ook als bulkactie op een
selectie. De inhoud van een groep en de voorrang tussen groepsinstellingen en
afzonderlijke instellingen zijn nog niet bepaald.

De toewijzing aan een leverancier of hoofdstuk is blijvend. Ook later toegevoegde
producten vallen automatisch onder de toepasselijke margegroep, zonder een
nieuwe bulkactie. Welke instelling uiteindelijk geldt bij meerdere toepasselijke
toewijzingen, wordt bepaald door nog vast te stellen voorrangsregels.

Als die regels geen eenduidige prijsinstelling opleveren, toont Fresh een duidelijk
aandachtspunt met de betrokken instellingen en hun herkomst. Fresh kiest in dat
geval niet stilzwijgend een instelling. Wat vóór oplossing gebeurt met een reeds
bestaande prijs of een export, moet nog worden bepaald.

## Keten en herstel

De prijsberekening gebruikt een inkoopprijs. Welke prijs geldt bij meerdere
leveranciers of voorraadbronnen en of deze keuze samenhangt met de
leveranciersvoorkeur moet nog worden besloten.

WinTree-export en catalogus/website zijn relevante afnemers binnen het
[productdoel](../project.md). Welke prijsvelden elke afnemer krijgt, moet nog
worden uitgewerkt. Ook herberekening bij nieuwe inkoopprijzen, wijzigingen van
groepen, gelijktijdige wijzigingen en herstel vragen nog concrete afspraken.

## Acceptatiecriteria

<a id="ac-prijzen-001"></a>

### Opslag wordt over de inkoopprijs berekend

Gegeven een inkoopprijs van EUR 10,00 en een ingestelde opslag van 30 procent,
is de berekende verkoopprijs EUR 13,00.

<a id="ac-prijzen-002"></a>

### De vaste verkoopprijs bepaalt het verkoopbedrag

Gegeven een toepasselijke instelling met vaste verkoopprijs EUR 15,00 en een
inkoopprijs van EUR 10,00, is de verkoopprijs EUR 15,00.

<a id="ac-prijzen-003"></a>

### Toewijzing ondersteunt de drie gekozen doelgroepen

De gebruiker kan een margegroep aanmaken en toewijzing uitvoeren voor individuele
producten, leveranciers en catalogushoofdstukken.

<a id="ac-prijzen-004"></a>

### Een bulkactie past de toewijzing toe op de selectie

Gegeven drie beschikbare onderdelen A, B en C, waarbij de gebruiker A en B
selecteert, kan de gebruiker met één bulkactie een margegroep voor A en B
toewijzen. De directe toewijzing van het niet-geselecteerde onderdeel C verandert niet.

<a id="ac-prijzen-005"></a>

### Nieuwe producten vallen onder blijvende toewijzingen

Gegeven een leverancier of hoofdstuk met toegewezen margegroep G, valt een later
toegevoegd product dat bij die leverancier of dat hoofdstuk hoort automatisch
onder G, zonder een nieuwe toewijzingsactie. Eventuele andere toepasselijke
instellingen worden volgens de nog vast te stellen voorrangsregels beoordeeld.

<a id="ac-prijzen-006"></a>

### Onduidelijke voorrang wordt een zichtbaar aandachtspunt

Gegeven een product waarop meerdere prijsinstellingen van toepassing zijn en
waarvoor de vastgestelde voorrangsregels geen eenduidige keuze opleveren, toont
Fresh een aandachtspunt met de betrokken instellingen en hun herkomst. Er wordt
niet stilzwijgend één van die instellingen gekozen.

## Open keuzes

Inhoud van margegroepen, voorrangsregels, gedrag zolang een prijskeuze openstaat,
afronding, de basis van
bedragen (zoals belasting en bijkomende kosten), ontbrekende inkoopprijzen en
de hierboven genoemde ketengevolgen worden uitgewerkt in
[issue #6](https://github.com/MenkehorstKwekerijen/Fresh/issues/6).
