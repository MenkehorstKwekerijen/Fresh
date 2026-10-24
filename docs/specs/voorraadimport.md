---
id: voorraadimport
status: draft
depends_on: [voorraad, prijzen]
---
# Voorraadimport

## Doel en scope

Deze specificatie bezit de importstappen, kolomtoewijzing, matching en wachtlijst.
De [voorraadbasis](voorraad.md) bepaalt vervanging en bronvoorrang voor fictieve
voorraad, eigen voorraad, eigen externe voorraad en TCM. Import vereist daarnaast
de [prijsvoorwaarden](prijzen.md#prijsvoorwaarden-bij-import); beide zijn expliciete
prerequisites. Geen prijsberekening of uitwerking van exportvrijgave.
Deze conceptafspraken zijn nog niet volledig genoeg voor implementatie.
Besluiten en open keuzes: [issue #12](https://github.com/MenkehorstKwekerijen/Fresh/issues/12).
Eerdere basisbesluiten staan in [issue #4](https://github.com/MenkehorstKwekerijen/Fresh/issues/4).

Lees gericht: [voorraadbasis](voorraad.md) · [importstappen](#stappen-van-de-leveranciersimport) · [kolommen](#kolomtoewijzing-in-stap-2) ·
[uitsluiten en matching](#uitsluiten-vanuit-voor-controle) · [wachtlijst](#wachtlijst-voor-stamcodes) ·
[keten en open keuzes](#keten-en-open-keuzes).

## Stappen van de leveranciersimport

| Stap | Handeling |
| --- | --- |
| 1 | Bestand en leverancier selecteren |
| 2 | Kolommen toewijzen, leveranciersmapping controleren en waarschuwingen behandelen |
| 3 | Bestand uitlezen, controleren en automatisch proberen te matchen |
| 4 | Resterende regels handmatig matchen met naam- en maatcodes |
| 5 | Import definitief verwerken: nieuwe stand opslaan en vorige vervangen |

Controles, prijscorrecties en matches tijdens de voorbereiding wijzigen de actuele voorraad
niet. Prijsvoorwaarden staan bij [prijzen](prijzen.md#prijsvoorwaarden-bij-import):
[standaardmarge vooraf](prijzen.md#ac-prijzen-046), [prijsvalidatie](prijzen.md#ac-prijzen-049)
en [herstel per regel](prijzen.md#ac-prijzen-050). De matchuitzonderingen hieronder heffen
prijsblokkades niet op.

<a id="ac-voorraadimport-011"></a>

### Alleen stap 5 vervangt de actuele voorraad

Gegeven een actuele leverancierslijst met 20 planten en een nieuw bestand met 12 planten voor
dezelfde regel, leest en controleert stap 3 het nieuwe bestand en probeert Fresh automatisch naam-
en maatcodes te matchen. Stap 4 laat de gebruiker resterende matches oplossen. De actuele voorraad
blijft tijdens deze voorbereiding 20. Na succesvolle definitieve verwerking in stap 5 is de actuele
voorraad 12; het nieuwe bestand vervangt dan de vorige stand.

## Kolomtoewijzing in stap 2

[Kolomtoewijzing](../glossary.md#term-kolomtoewijzing) wordt per leverancier onthouden.
Nieuwe bestanden worden opnieuw gecontroleerd. De gebruiker kan prijsfouten
[direct in Fresh herstellen](prijzen.md#ac-prijzen-051); de waarschuwing bij mapping
is geen toestemming om een blokkade te negeren.

<a id="ac-voorraadimport-008"></a>

### De tweede importstap wijst bestandskolommen toe

Gegeven een geselecteerd leveranciersbestand, kan de gebruiker in stap 2 de kolommen voor plantnaam,
maat en inkoopprijs aan de overeenkomstige gegevens in Fresh toewijzen, vóór verwerking tot actuele
voorraad.

<a id="ac-voorraadimport-009"></a>

### Prijsproblemen zijn al bij de kolomtoewijzing zichtbaar

Gegeven stap 2 met een niet-toegewezen inkoopprijskolom of een toegewezen kolom met een lege of
ongeldige prijs op regel 12, toont Fresh daar al een waarschuwing met toegang tot respectievelijk de
toewijzing of de betreffende foutregel en herstelactie. Verwerking blijft geblokkeerd zolang het
prijsprobleem bestaat.

<a id="ac-voorraadimport-010"></a>

### Kolomtoewijzing wordt per leverancier hergebruikt

Gegeven een vastgelegde kolomtoewijzing voor leverancier A, vult Fresh die in stap 2 alvast in bij
een volgend bestand van A met dezelfde kolomstructuur. De gebruiker kan haar controleren en
aanpassen. Fresh controleert de inhoud van dit nieuwe bestand opnieuw; de toewijzing van A wordt
niet als instelling voor een andere leverancier gebruikt.

## Uitsluiten vanuit Voor controle

Vanuit 'Voor controle' kunnen ook gematchte regels bewust van WinTree-export worden
uitgesloten. De inkoper kan dit ook later doen, vóór vrijgave van die export.
[Exportuitsluiting](../glossary.md#term-uitsluiten-wintree-export) laat intern gebruik voor
catalogusbeheer, verkoop en assortimentsanalyse intact. Een uitsluiting vult geen codes in;
het concrete interne gebruik zonder productmatch staat nog open.

| Regel | Matchvoorwaarde van stap 5 |
| --- | --- |
| Naam- en maatcode gematcht | Voldaan |
| Bewust uitgesloten van WinTree-export | Ontbrekende match blokkeert niet |
| Op de wachtlijst voor ontbrekende stamcodes | Ontbrekende match blokkeert overige regels niet |
| Ongematcht zonder deze uitzonderingen | Definitieve verwerking geblokkeerd |

<a id="ac-voorraadimport-012"></a>

### Voor controle biedt uitsluiten ongeacht de matchstatus

Gegeven een nog niet gematchte regel A en een al gematchte regel B in 'Voor controle', kan de
gebruiker zowel A als B direct uitsluiten van de WinTree-export. Een geslaagde match is geen
belemmering om B uit te sluiten. De [exportspecificatie](wintree-export.md#ac-wintree-export-002) bepaalt het
resultaat in het exportbestand.

<a id="ac-voorraadimport-013"></a>

### Ongematchte regels zonder uitzondering blokkeren afronding

Gegeven een verder geldige import met één ongematchte regel die niet bewust is uitgesloten en niet
op de wachtlijst voor stamcodes staat, blijft stap 5 geblokkeerd en blijft de actuele voorraad
ongewijzigd.

<a id="ac-voorraadimport-014"></a>

### Uitgesloten en wachtende regels blokkeren niet op matching

Gegeven een verder geldige import met gematchte regels, één bewust uitgesloten ongematchte regel en
één wachtende regel waarvoor een stamcode ontbreekt, kan stap 5 doorgaan zonder eerst die twee
regels te matchen. De wachtende regel blijft bewaard voor latere verwerking; de uitgesloten regel
wordt niet verwijderd vanwege zijn exportuitsluiting.

## Wachtlijst voor stamcodes

De [wachtlijst](../glossary.md#term-wachtlijst-stamcodes) bewaart regels waarvoor een
naamcode of maatcode ontbreekt in de actuele WinTree-basisstam. Deze regels gaan nog niet
mee in de WinTree-export en blokkeren de overige export niet. De prijscontroles blijven gelden.

Een stamupdate start automatisch een nieuwe matchpoging; eenduidige matches kunnen verder
worden verwerkt. Onduidelijke matches blijven ter controle; ontbrekende codes blijven wachten.
De inkoper houdt de exportvrijgave. Later matchen heft een bewuste uitsluiting niet op.
Bij definitieve voorraadvervanging volgt de actieve wachtlijst dezelfde leverancier en bron:
ontbrekende regels vervallen, terugkerende regels gebruiken de nieuwste gegevens.

<a id="ac-voorraadimport-015"></a>

### Nieuwe stamcodes maken verwerking van wachtende regels mogelijk

Gegeven een wachtende regel waarvan de naamcode of maatcode ontbreekt en waarvan het
leveranciersbestand nog niet is vervangen, wanneer de benodigde codes via een basisstamupdate uit
WinTree beschikbaar komen, kan die bewaarde regel worden gematcht en verwerkt. Een eventuele bewuste
exportuitsluiting blijft behouden.

<a id="ac-voorraadimport-016"></a>

### Een stamupdate start automatisch een nieuwe matchpoging

Gegeven een wachtlijst bij een nog actuele leverancierslijst, wanneer de WinTree-basisstam in Fresh
wordt geactualiseerd, probeert Fresh die wachtende regels opnieuw te matchen zonder aparte
startactie door de gebruiker.

<a id="ac-voorraadimport-017"></a>

### Onduidelijke matches blijven ter controle

Gegeven een automatische matchpoging na een stamupdate die voor een wachtende regel geen eenduidige
match oplevert, blijft die regel ter controle staan en wordt geen willekeurige match vastgelegd.
Ontbreken de benodigde codes nog, dan blijft de regel wachten.

<a id="ac-voorraadimport-018"></a>

### Ontbrekende wachtregels vervallen bij een nieuwe lijst

Gegeven een actieve wachtende regel A en een nieuw bestand van dezelfde leverancier en bron waarin A
ontbreekt, blijft A tijdens de importvoorbereiding op de actieve wachtlijst. Na succesvolle
vervanging in stap 5 vervalt A uit die lijst. Als de benodigde stamcodes later beschikbaar komen,
verwerkt Fresh A niet alsnog vanuit de oude lijst als actueel aanbod.

<a id="ac-voorraadimport-019"></a>

### Terugkerende wachtregels gebruiken de nieuwste gegevens

Gegeven een wachtende regel met 20 planten en inkoopprijs EUR 10,00, wanneer deze regel terugkomt in
de nieuwe leverancierslijst met 12 planten en inkoopprijs EUR 11,00 en die lijst definitief is
verwerkt, gebruikt latere verwerking na een stamupdate de 12 planten en EUR 11,00 uit de nieuwste
lijst. De oude gegevens worden niet teruggezet of erbij opgeteld. De herkenning van dezelfde regel
moet afzonderlijk worden gespecificeerd.

## Keten en open keuzes

Leveranciersvoorkeuren, assortimentsanalyses en uitvoer naar WinTree of website gebruiken
voorraadgegevens. Hun actualiseringsmoment is nog niet bepaald. Vervallen aanbod mag ook
bij een onderbroken import of gelijktijdige stamupdate niet opnieuw actueel worden.

Nog te bepalen in [issue #12](https://github.com/MenkehorstKwekerijen/Fresh/issues/12):

- Bestandsvelden, leveranciers- en bronherkenning, gewijzigde kolommen/volgorde/structuur,
  bestanden met meerdere leveranciers, lege bestanden en overige bestandsfouten.
- Exacte matchregels, codeproblemen, productidentiteit, herkenning van terugkerende regels,
  intern gebruik zonder match, verdere wachtlijstbediening en plaats van 'Voor controle'.
- Inhoudsvergelijking, ouder of opnieuw ingelezen bestand binnen dezelfde bron, gedrag bij
  open bronkeuze en bewaren/herbeoordelen van die keuze bij een volgende import.
- Historische bewaring, herstel, gelijktijdigheid en behoud van menselijke keuzes.

Exportvrijgave en hergebruik van exportuitsluitingen horen bij de
[exportspecificatie](wintree-export.md) en
[issue #13](https://github.com/MenkehorstKwekerijen/Fresh/issues/13).
