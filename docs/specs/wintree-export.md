---
id: wintree-export
status: draft
depends_on: [voorraadimport, prijzen]
---
# WinTree-export

## Doel en scope

Leveranciersvoorraad met WinTree-codes en prijzen gecontroleerd kunnen exporteren
naar WinTree. Deze eerste afspraken betreffen uitsluiten en inkoperscontrole,
besloten in [issue #6](https://github.com/MenkehorstKwekerijen/Fresh/issues/6).
De volledige exportafspraak is nog niet voldoende bepaald om te bouwen.

## Gedrag en gegevens

Vóór vrijgave van de WinTree-export krijgt de inkoper een
[inkoperscontrole](../glossary.md#term-inkoperscontrole). Daar kan de inkoper
alsnog regels [uitsluiten](../glossary.md#term-uitsluiten-wintree-export), ook als
deze al met naam- en maatcodes gematcht zijn. Een geslaagde match betekent dus
niet dat de regel verplicht in de export komt.

Regels die vanuit
['Voor controle'](voorraadimport.md#uitsluiten-vanuit-voor-controle) of tijdens de
inkoperscontrole zijn uitgesloten, komen niet in de vrijgegeven WinTree-export.
Import definitief verwerken en export vrijgeven zijn afzonderlijke handelingen;
stap 5 van de import vervangt deze inkoperscontrole niet.

## Keten en herstel

WinTree is de afnemer van de export. Of een uitgesloten regel beschikbaar blijft
voor voorraadweergave, leveranciersvoorkeuren of catalogusbeheer in Fresh, is nog
open. Dit besluit legt evenmin vast wat er met eerder naar WinTree geëxporteerde
regels gebeurt; het beschrijft welke regels de nieuwe export bevat.

## Acceptatiecriteria

<a id="ac-wintree-export-001"></a>

### De inkoper controleert vóór vrijgave

Gegeven een voorbereide WinTree-export met een gematchte regel A, krijgt de
inkoper vóór vrijgave de inkoperscontrole en kan hij A daar alsnog uitsluiten.
Een voltooide import of match omzeilt deze controle niet.

<a id="ac-wintree-export-002"></a>

### Uitgesloten regels ontbreken in de export

Gegeven regel A uitgesloten vanuit 'Voor controle' en gematchte regel B
uitgesloten tijdens de inkoperscontrole, bevat de vrijgegeven WinTree-export
geen A en geen B.

## Open keuzes

Het effect op voorraad en commerciële afnemers in Fresh, opnieuw opnemen van
regels, geldigheid van uitsluitingen bij een volgend bestand, overige
controlepunten, wijzigingen na controle, gelijktijdige wijzigingen, exportformaat
en verwerking of herstel in WinTree moeten nog worden bepaald. De eerstvolgende
keuze staat in [issue #6](https://github.com/MenkehorstKwekerijen/Fresh/issues/6).
