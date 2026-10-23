---
id: voorraadimport
status: draft
depends_on: []
---
# Voorraadimport

## Doel en scope

Nieuwe voorraadbestanden actualiseren de voorraad in Fresh. Deze eerste
conceptspecificatie legt de besloten vervangingsregel en bronvoorrang vast; de volledige
importroute is nog niet voldoende bepaald om te bouwen.

De regel geldt voor [externe fictieve voorraad](../glossary.md#term-externe-fictieve-voorraad),
[eigen voorraad](../glossary.md#term-eigen-voorraad),
[eigen externe voorraad](../glossary.md#term-eigen-externe-voorraad) en
[TCM-voorraad](../glossary.md#term-tcm-voorraad).
Het gebruikersbesluit is vastgelegd in
[issue #4](https://github.com/MenkehorstKwekerijen/Fresh/issues/4).
Prijscontroles, herstel en de kolomtoewijzingsstap zijn verder besloten in
[issue #6](https://github.com/MenkehorstKwekerijen/Fresh/issues/6).

## Gedrag en gegevens

Een nieuw voorraadbestand vervangt de vorige voorraad van dezelfde leverancier
of bron volledig. Het bestand bevat de nieuwe voorraadstand, geen aanvulling
op de vorige stand. Regels die ontbreken in het nieuwe bestand behoren na
vervanging niet meer tot de actuele voorraad van die leverancier of bron.

Deze afspraak bepaalt geen vervangingsgedrag voor historische verkoopgegevens,
de WinTree-basisstam of catalogusupdates. De bestandsvelden die bepalen bij welke
leverancier of bron een bestand hoort, moeten nog worden uitgewerkt.

Voor leveranciersvoorraadlijsten geldt vóór het inlezen de
[controle op een ingestelde standaardmarge](prijzen.md#ac-prijzen-046).
Bij deze blokkade vindt geen vervanging van de bestaande voorraad plaats.
De afhandeling van een bestand met meerdere leveranciers wordt nog uitgewerkt.

Een ontbrekende of ongeldige inkoopprijs blokkeert eveneens de volledige
leverancierslijst volgens de [prijsvalidatie](prijzen.md#ac-prijzen-049).
De foutmelding biedt een [directe herstelactie per foutregel](prijzen.md#ac-prijzen-050).

### Stappen van de leveranciersimport

De gebruiker heeft de volgende volgorde gekozen:

| Stap | Handeling |
| --- | --- |
| 1 | Bestand en leverancier selecteren |
| 2 | Kolommen toewijzen, met vooringevulde leveranciersinstellingen en waarschuwingen |
| 3 | Bestand uitlezen, controleren en automatisch proberen te matchen |
| 4 | Resterende regels handmatig matchen met naamcodes en maatcodes |
| 5 | Import definitief verwerken: nieuwe voorraad opslaan en vorige stand vervangen |

Tot en met stap 4 blijft de actuele voorraad ongewijzigd. Ook controles,
prijscorrecties en handmatige matches in de importvoorbereiding vervangen de
vorige voorraad niet. Alleen de definitieve verwerking in stap 5 actualiseert
de voorraad volgens de vervangingsregel. De eerder vastgelegde prijsblokkades
blijven gelden.
Vóór stap 5 moeten alle regels gematcht zijn, behalve bewust van WinTree-export
uitgesloten regels en regels op de hieronder beschreven wachtlijst.
De automatische matchregels moeten nog worden uitgewerkt.

### Uitsluiten vanuit Voor controle

Vanuit 'Voor controle' kan de gebruiker een regel direct uitsluiten van de
WinTree-export. Dit kan zowel bij een nog niet gematchte als bij een al gematchte
regel. De inkoper kan ook na het matchen nog regels uitsluiten tijdens de
[inkoperscontrole vóór exportvrijgave](wintree-export.md#gedrag-en-gegevens).

Uitsluiten geldt alleen voor de WinTree-export; de regels blijven
[intern beschikbaar](wintree-export.md#ac-wintree-export-003).
Een bewust uitgesloten regel mag ongematcht blijven en blokkeert stap 5 niet
vanwege die ontbrekende match. Uitsluiten vult geen naam- of maatcode in.
Hoe een ongematchte regel intern wordt getoond en betrokken bij productgebonden
toepassingen, moet nog worden uitgewerkt. De eerder vastgelegde prijsblokkades
blijven gelden; uitsluiten is geen uitzondering daarop.

### Wachtlijst voor stamcodes

Een regel waarvoor de benodigde naamcode of maatcode nog ontbreekt in de actuele
WinTree-basisstam, kan op de
[wachtlijst voor stamcodes](../glossary.md#term-wachtlijst-stamcodes) komen.
Deze regel blijft bewaard voor latere verwerking. De ontbrekende match op de
wachtlijst blokkeert de definitieve import van de overige regels niet en
[blokkeert evenmin hun WinTree-export](wintree-export.md#ac-wintree-export-004).
De bestaande prijscontroles blijven gelden.

Na actualisering van de basisstam vanuit WinTree kunnen de wachtende regels
worden gematcht en verwerkt zodra de benodigde codes beschikbaar zijn.
Of Fresh dit automatisch start of de gebruiker dit start, is nog niet besloten.
Wachten op stamcodes is iets anders dan bewust uitsluiten van de export;
latere verwerking heft een bewuste exportuitsluiting niet op.

| Situatie van een regel | Gevolg voor de matchvoorwaarde van stap 5 |
| --- | --- |
| Naam- en maatcode gematcht | Matchvoorwaarde voldaan |
| Ongematcht en bewust uitgesloten van WinTree-export | Geen matchblokkade |
| Wacht op ontbrekende stamcodes en staat op de wachtlijst | Geen matchblokkade voor de overige regels; later verwerken |
| Ongematcht zonder een van deze uitzonderingen | Definitieve verwerking geblokkeerd |

### Kolomtoewijzing in stap 2

De tweede stap van de bestandsimport is
[kolomtoewijzing](../glossary.md#term-kolomtoewijzing), ook kolommapping genoemd.
De gebruiker wijst bestandskolommen toe aan gegevens in Fresh, zoals plantnaam,
maat en inkoopprijs. Deze stap vindt plaats vóór verwerking van het bestand tot
actuele voorraad.

Fresh onthoudt de kolomtoewijzing per leverancier en vult die bij een volgend
bestand van dezelfde leverancier alvast in. De gebruiker kan de toewijzing
controleren en aanpassen. De controles worden opnieuw op het nieuwe bestand
uitgevoerd; een eerdere toewijzing bewijst niet dat het nieuwe bestand geldig is.
Herkenning van gewijzigde kolomnamen, volgorde of bestandsstructuur moet nog
worden uitgewerkt.

Fresh waarschuwt in deze stap wanneer de inkoopprijskolom niet is toegewezen of
wanneer ontbrekende of ongeldige prijzen worden gevonden in de toegewezen kolom.
De waarschuwing geeft toegang tot de betreffende toewijzing of foutregels met
hun directe herstelactie. De [blokkerende prijscontrole](prijzen.md#ac-prijzen-049)
blijft gelden; een waarschuwing mag niet als toestemming om toch te verwerken
worden gebruikt. Prijzen kunnen [direct in Fresh worden gecorrigeerd](prijzen.md#ac-prijzen-051).

### Leveranciers en mogelijke dubbele aanlevering

Dezelfde soort en maat kunnen bij verschillende leveranciers beschikbaar zijn.
Dat is op zichzelf geen dubbele aanlevering van dezelfde voorraad.

De gebruiker heeft geen overlap bevestigd tussen eigen voorraad, eigen externe
voorraad en de andere voorraadsoorten. Wel kan één leverancier in theorie zowel
via een fictief voorraadbestand als via TCM worden ingelezen. Daar komt hetzelfde
aanbod via twee routes binnen. De aanlevering vermeldt expliciet of het om TCM of
"inkoop aanbieding" (fictief) gaat. Bij deze samenloop is de bron met de meest
recente [voorraaddatum](../glossary.md#term-voorraaddatum) leidend. De datum wordt
per bron als volgt bepaald:

| Bron | Datum voor de vergelijking |
| --- | --- |
| Fictief | De [importdatum](../glossary.md#term-importdatum): het bestand inlezen via de importeerfunctie in Fresh |
| TCM | De datum per leverancier die in het TCM-Excelbestand staat; diens regels worden in één keer naar WinTree overgedragen |

Het moment waarop het TCM-bestand in Fresh wordt ingelezen vervangt de datum
uit dat bestand niet. De keuze tussen fictief en TCM geldt voor de volledige
voorraadlijst van dezelfde leverancier, niet afzonderlijk per productregel.
De overlappende voorraad wordt niet opgeteld en regels uit de oudere lijst
worden niet bijgemengd in de gekozen nieuwere lijst.

Bij de datumvergelijking gelden de volgende uitzonderingen:

| Situatie bij dezelfde leverancier | Gedrag |
| --- | --- |
| Gelijke geldige datum en gelijke inhoud | Geen gebruikersactie nodig; de voorraad blijft enkelvoudig |
| Gelijke geldige datum, maar verschillende inhoud | Eén aandachtspunt waarin de gebruiker de bron kiest |
| Een benodigde datum ontbreekt of is ongeldig | Eén aandachtspunt waarin de gebruiker de bron kiest |

De exacte veldnamen, herkenning van dezelfde leverancier en vergelijking van
inhoud moeten nog worden uitgewerkt en aan bestanden getoetst. Dit besluit gaat
over samenloop van fictief en TCM, niet over de verwerking van een ouder bestand
binnen dezelfde bron. Ook het opnieuw inlezen van hetzelfde fictieve bestand
vraagt nog een expliciete afspraak.

## Keten en herstel

Leveranciersvoorkeuren, assortimentsanalyses en uitvoer naar WinTree of website
kunnen door de nieuwe voorraadstand worden geraakt. Wanneer deze afnemers
worden bijgewerkt, is nog niet besloten.

Naast de hierboven vastgelegde prijsblokkades is het gedrag bij andere fouten
in een bestand of een leeg bestand nog open, evenals bij
andere codeproblemen dan wachten op ontbrekende stamcodes, een onderbroken
import of gelijktijdige wijzigingen. Dat moet
worden gespecificeerd vóór implementatie, inclusief herstel en de gevolgen voor
eerder vastgelegde menselijke keuzes.

De verwerking van wachtende regels moet ook worden uitgewerkt voor de situatie
waarin inmiddels een nieuw leveranciersbestand de vorige lijst heeft vervangen.
De nieuwe wachtlijstafspraak verandert de bestaande vervangingsregel niet.

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

<a id="ac-voorraadimport-003"></a>

### De voorraaddatum bepaalt de bronvoorrang

Gegeven hetzelfde aanbod van één leverancier via beide routes, met één regel
van 20 planten in TCM met datum 20 oktober 2026 in het Excelbestand en 12 planten
in fictief ingelezen in Fresh op 22 oktober 2026, is fictief leidend en is de
gebruikte voorraad 12, ook als het TCM-bestand op 23 oktober wordt ingelezen.
Staat bij dezelfde TCM-voorraad in het Excelbestand 23 oktober, dan is TCM
leidend en is de gebruikte voorraad 20.

<a id="ac-voorraadimport-004"></a>

### Bronkeuze geldt voor de volledige leverancierslijst

Gegeven een oudere TCM-lijst met regels A en B en een nieuwere fictieve lijst
met alleen A voor dezelfde leverancier, wordt de fictieve lijst gebruikt.
B wordt niet aangevuld vanuit de oudere TCM-lijst. Bij een nieuwere TCM-lijst
geldt dezelfde regel met TCM als gekozen bron.

<a id="ac-voorraadimport-005"></a>

### Gelijke datum en inhoud vragen geen handmatige keuze

Gegeven fictief en TCM voor dezelfde leverancier met dezelfde geldige datum en
dezelfde voorraadinhoud, vraagt Fresh geen bronkeuze aan de gebruiker. De voorraad
wordt niet dubbel geteld.

<a id="ac-voorraadimport-006"></a>

### Verschillende inhoud op dezelfde datum vraagt één bronkeuze

Gegeven fictief en TCM voor dezelfde leverancier met dezelfde geldige datum,
maar respectievelijk 12 en 20 planten voor dezelfde regel, toont Fresh één
aandachtspunt waarin de gebruiker de te gebruiken bron kiest.

<a id="ac-voorraadimport-007"></a>

### Een ontbrekende of ongeldige datum vraagt één bronkeuze

Gegeven samenloop van fictief en TCM voor dezelfde leverancier, waarbij een
benodigde datum ontbreekt of ongeldig is, toont Fresh één aandachtspunt waarin
de gebruiker de te gebruiken bron kiest.

<a id="ac-voorraadimport-008"></a>

### De tweede importstap wijst bestandskolommen toe

Gegeven een geselecteerd leveranciersbestand, kan de gebruiker in stap 2 de
kolommen voor plantnaam, maat en inkoopprijs aan de overeenkomstige gegevens
in Fresh toewijzen, vóór verwerking tot actuele voorraad.

<a id="ac-voorraadimport-009"></a>

### Prijsproblemen zijn al bij de kolomtoewijzing zichtbaar

Gegeven stap 2 met een niet-toegewezen inkoopprijskolom of een toegewezen kolom
met een lege of ongeldige prijs op regel 12, toont Fresh daar al een waarschuwing
met toegang tot respectievelijk de toewijzing of de betreffende foutregel en
herstelactie. Verwerking blijft geblokkeerd zolang het prijsprobleem bestaat.

<a id="ac-voorraadimport-010"></a>

### Kolomtoewijzing wordt per leverancier hergebruikt

Gegeven een vastgelegde kolomtoewijzing voor leverancier A, vult Fresh die in
stap 2 alvast in bij een volgend bestand van A met dezelfde kolomstructuur.
De gebruiker kan haar controleren en aanpassen. Fresh controleert de inhoud
van dit nieuwe bestand opnieuw; de toewijzing van A wordt niet als instelling
voor een andere leverancier gebruikt.

<a id="ac-voorraadimport-011"></a>

### Alleen stap 5 vervangt de actuele voorraad

Gegeven een actuele leverancierslijst met 20 planten en een nieuw bestand met
12 planten voor dezelfde regel, leest en controleert stap 3 het nieuwe bestand
en probeert Fresh automatisch naam- en maatcodes te matchen. Stap 4 laat de
gebruiker resterende matches oplossen. De actuele voorraad blijft tijdens deze
voorbereiding 20. Na succesvolle definitieve verwerking in stap 5 is de actuele
voorraad 12; het nieuwe bestand vervangt dan de vorige stand.

<a id="ac-voorraadimport-012"></a>

### Voor controle biedt uitsluiten ongeacht de matchstatus

Gegeven een nog niet gematchte regel A en een al gematchte regel B in
'Voor controle', kan de gebruiker zowel A als B direct uitsluiten van de
WinTree-export. Een geslaagde match is geen belemmering om B uit te sluiten.
De [exportspecificatie](wintree-export.md#ac-wintree-export-002) bepaalt het
resultaat in het exportbestand.

<a id="ac-voorraadimport-013"></a>

### Ongematchte regels zonder uitzondering blokkeren afronding

Gegeven een verder geldige import met één ongematchte regel die niet bewust is
uitgesloten en niet op de wachtlijst voor stamcodes staat, blijft stap 5
geblokkeerd en blijft de actuele voorraad ongewijzigd.

<a id="ac-voorraadimport-014"></a>

### Uitgesloten en wachtende regels blokkeren niet op matching

Gegeven een verder geldige import met gematchte regels, één bewust uitgesloten
ongematchte regel en één wachtende regel waarvoor een stamcode ontbreekt,
kan stap 5 doorgaan zonder eerst die twee regels te matchen. De wachtende regel
blijft bewaard voor latere verwerking; de uitgesloten regel wordt niet verwijderd
vanwege zijn exportuitsluiting.

<a id="ac-voorraadimport-015"></a>

### Nieuwe stamcodes maken verwerking van wachtende regels mogelijk

Gegeven een wachtende regel waarvan de naamcode of maatcode ontbreekt en waarvan
het leveranciersbestand nog niet is vervangen, wanneer de benodigde codes via
een basisstamupdate uit WinTree beschikbaar komen, kan die bewaarde regel worden
gematcht en verwerkt. Een eventuele bewuste exportuitsluiting blijft behouden.
Dit criterium kiest nog niet voor automatisch of handmatig starten.

## Open keuzes

Gedrag bij gewijzigde bestandsstructuur,
automatische matching, intern gebruik van ongematchte uitgesloten of wachtende
regels, bediening van de wachtlijst en hervatten na een stamupdate of na een
nieuwer leveranciersbestand, de precieze plaats van 'Voor controle' in de importroute,
verdere afbakening, de vergelijking van inhoud, het gedrag zolang een bronkeuze
openstaat en het bewaren en opnieuw beoordelen van die keuze bij nieuwe import,
en de hierboven genoemde import- en herstelvragen worden behandeld in
[issue #4](https://github.com/MenkehorstKwekerijen/Fresh/issues/4).
