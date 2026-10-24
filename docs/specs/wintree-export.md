---
id: wintree-export
status: draft
depends_on: [voorraadimport, prijzen]
---
# WinTree-export

## Doel en scope

Leveranciersvoorraad met WinTree-codes en prijzen gecontroleerd kunnen exporteren
naar WinTree. Deze eerste afspraken betreffen uitsluiten en inkoperscontrole,
besloten in [issue #13](https://github.com/MenkehorstKwekerijen/Fresh/issues/13).
De volledige exportafspraak is nog niet voldoende bepaald om te bouwen.
Importwizard en prijsberekening vallen buiten deze scope.

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

Regels op de [wachtlijst voor stamcodes](voorraadimport.md#wachtlijst-voor-stamcodes)
gaan nog niet mee naar WinTree, maar blokkeren de export van de overige regels
niet. Na een stamupdate probeert Fresh ze
[automatisch opnieuw te matchen](voorraadimport.md#ac-voorraadimport-016).
Ook dan blijft de inkoperscontrole vóór exportvrijgave gelden; een geslaagde
match geeft de export niet automatisch vrij.

## Uitsluiting per uitvoering en volgende import

Een [productuitvoering](../glossary.md#term-productuitvoering) kan afzonderlijk
worden uitgesloten, ook als een andere uitvoering dezelfde naam- en maatcodes
heeft. Bij een volgende lijst blijft de uitsluiting behouden voor dezelfde
uitvoering volgens de [herkenningsroute](voorraadimport.md#herkenning-bij-volgende-leverancierslijsten).
De herkenning verleent geen exportvrijgave. Opheffen van een uitsluiting en
begininstellingen voor een andere uitvoering zijn nog open keuzes.

<a id="ac-wintree-export-006"></a>

### Uitsluiten van de ene kwaliteit sluit de andere niet uit

Gegeven leverancier A met uitvoeringen `2-jarige kroon` en `3-jarige kroon` met
dezelfde naam- en maatcodes, kan de gebruiker alleen de 2-jarige uitvoering
uitsluiten. De 3-jarige uitvoering wordt hierdoor niet uitgesloten; haar export
blijft onderworpen aan de overige controles en inkopersvrijgave.

<a id="ac-wintree-export-007"></a>

### Dezelfde uitvoering behoudt haar uitsluiting bij een volgende lijst

Gegeven een uitgesloten uitvoering bij A, blijft deze uitgesloten na definitieve
verwerking van een volgende lijst waarin zij als dezelfde uitvoering wordt herkend.
Dit geldt ook wanneer de gebruiker bij gewijzigde extra tekst, bijvoorbeeld
`3-jarige kroon, aanbieding`, bevestigt dat het dezelfde uitvoering is.
Een gewijzigde voorraad of prijs heft de uitsluiting niet op.

## Keten en herstel

WinTree is de afnemer van de export. Uitsluiten heeft alleen effect op deze
export: de regel blijft intern in Fresh beschikbaar en doet mee voor
catalogusbeheer, verkoop en assortimentsanalyse. De uitsluiting verwijdert de
regel niet uit de actuele voorraad en vormt geen interne aanbodfilter.

[Matching en intern gebruik zonder match](voorraadimport.md#keten-en-open-keuzes)
horen bij voorraadimport.
Dit besluit legt evenmin vast wat er met eerder naar WinTree geëxporteerde
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

<a id="ac-wintree-export-003"></a>

### Exportuitsluiting verandert het interne aanbod niet

Gegeven een geïmporteerde en gematchte regel A die beschikbaar is voor
catalogusbeheer, verkoop en assortimentsanalyse, wanneer A wordt uitgesloten
van de WinTree-export, blijft A voor die interne toepassingen beschikbaar en
meedoen. Alleen de opname in de WinTree-export verandert. Dit geldt voor
uitsluiten vanuit 'Voor controle' en tijdens de inkoperscontrole.

<a id="ac-wintree-export-004"></a>

### Wachten op stamcodes blokkeert de overige export niet

Gegeven gematchte, niet uitgesloten regels A en B die voldoen aan de overige
exportcontroles, en regel C op de wachtlijst wegens een ontbrekende stamcode,
kan de inkoper de export van A en B vrijgeven. C ontbreekt in dat bestand en
blijft wachten op latere verwerking.

<a id="ac-wintree-export-005"></a>

### Automatische matching geeft geen exportvrijgave

Gegeven een wachtende regel die na een stamupdate succesvol wordt gematcht,
blijft de inkoperscontrole vereist voordat die regel voor WinTree-export wordt
vrijgegeven. De automatische matchpoging veroorzaakt zelf geen exportvrijgave.

## Open keuzes

Opnieuw opnemen in de export, begininstellingen voor een andere uitvoering, behoud
bij terugkeer na afwezigheid of een bronwissel, overige
controlepunten, wijzigingen na controle, gelijktijdige wijzigingen, exportformaat
en verwerking of herstel in WinTree moeten nog worden bepaald. De eerstvolgende
keuze staat in [issue #13](https://github.com/MenkehorstKwekerijen/Fresh/issues/13).
