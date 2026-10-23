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

Nog te verduidelijken is of leverancier en hoofdstuk dienen als selectie van
producten voor een eenmalige toewijzing, of als blijvende toewijzingsregel die
ook op later toegevoegde producten werkt. Er is nog geen overervingsmodel gekozen.

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
producten, leveranciers en catalogushoofdstukken. Het precieze effect van
leverancier- en hoofdstuktoewijzing op toekomstige producten staat nog open.

<a id="ac-prijzen-004"></a>

### Een bulkactie past de toewijzing toe op de selectie

Gegeven drie beschikbare onderdelen A, B en C, waarbij de gebruiker A en B
selecteert, kan de gebruiker met één bulkactie een margegroep voor A en B
toewijzen. De toewijzing van het niet-geselecteerde onderdeel C verandert niet.

## Open keuzes

Inhoud en blijvende werking van margegroepen, voorrangsregels, afronding, de basis van
bedragen (zoals belasting en bijkomende kosten), ontbrekende inkoopprijzen en
de hierboven genoemde ketengevolgen worden uitgewerkt in
[issue #6](https://github.com/MenkehorstKwekerijen/Fresh/issues/6).
