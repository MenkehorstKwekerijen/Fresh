---
id: voorraad
status: draft
depends_on: []
---
# Actuele voorraad en bronvoorrang

## Doel en scope

Deze specificatie bezit welke voorraad actueel is bij vervanging van een lijst en
samenloop van fictief en TCM. Dit geldt voor de vier voorraadsoorten uit de
[glossary](../glossary.md). Historische verkopen, basisstam- en catalogusupdates
vallen buiten deze vervangingsregel. De importbediening, matching, prijsvalidatie
en exportvrijgave hebben hun eigen specificaties.

De bestaande voorraadregels zijn uit voorraadimport verplaatst, met behoud van
hun criterium-ID's en betekenis. De specificatie blijft draft; open keuzes staan
in [issue #12](https://github.com/MenkehorstKwekerijen/Fresh/issues/12).
Lees gericht: [vervangen](#voorraad-vervangen) ·
[bronvoorrang](#leveranciers-en-mogelijke-dubbele-aanlevering) ·
[V1-referentie](#eenmalige-v1-referentie) · [keten en open keuzes](#keten-en-open-keuzes).

<a id="gedrag-en-gegevens"></a>

## Voorraad vervangen

Een nieuwe definitief verwerkte lijst vervangt de vorige voor dezelfde leverancier of bron,
zonder oude regels bij te mengen. Historische bewaring is een aparte open keuze.

<a id="ac-voorraadimport-001"></a>

### De nieuwe stand vervangt de vorige

Gegeven een vorige stand van 20 planten en een nieuw bestand met 12 planten voor dezelfde regel en
leverancier of bron, is de actuele stand na vervanging 12, niet 32. Dit geldt voor elk van de vier
voorraadsoorten in scope.

<a id="ac-voorraadimport-002"></a>

### Ontbrekende regels vervallen uit de actuele voorraad

Gegeven een vorige lijst met regels A en B en een nieuwe lijst met alleen A, behoort B na vervanging
niet meer tot de actuele voorraad van die leverancier of bron. Dit bepaalt niet of historische
gegevens worden bewaard.

## Leveranciers en mogelijke dubbele aanlevering

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

<a id="ac-voorraadimport-003"></a>

### De voorraaddatum bepaalt de bronvoorrang

Gegeven hetzelfde aanbod van één leverancier via beide routes, met één regel van 20 planten in TCM
met datum 20 oktober 2026 in het Excelbestand en 12 planten in fictief ingelezen in Fresh op 22
oktober 2026, is fictief leidend en is de gebruikte voorraad 12, ook als het TCM-bestand op 23
oktober wordt ingelezen. Staat bij dezelfde TCM-voorraad in het Excelbestand 23 oktober, dan is TCM
leidend en is de gebruikte voorraad 20.

<a id="ac-voorraadimport-004"></a>

### Bronkeuze geldt voor de volledige leverancierslijst

Gegeven een oudere TCM-lijst met regels A en B en een nieuwere fictieve lijst met alleen A voor
dezelfde leverancier, wordt de fictieve lijst gebruikt. B wordt niet aangevuld vanuit de oudere
TCM-lijst. Bij een nieuwere TCM-lijst geldt dezelfde regel met TCM als gekozen bron.

<a id="ac-voorraadimport-005"></a>

### Gelijke datum en inhoud vragen geen handmatige keuze

Gegeven fictief en TCM voor dezelfde leverancier met dezelfde geldige datum en dezelfde
voorraadinhoud, vraagt Fresh geen bronkeuze aan de gebruiker. De voorraad wordt niet dubbel geteld.

<a id="ac-voorraadimport-006"></a>

### Verschillende inhoud op dezelfde datum vraagt één bronkeuze

Gegeven fictief en TCM voor dezelfde leverancier met dezelfde geldige datum, maar respectievelijk 12
en 20 planten voor dezelfde regel, toont Fresh één aandachtspunt waarin de gebruiker de te gebruiken
bron kiest.

<a id="ac-voorraadimport-007"></a>

### Een ontbrekende of ongeldige datum vraagt één bronkeuze

Gegeven samenloop van fictief en TCM voor dezelfde leverancier, waarbij een benodigde datum
ontbreekt of ongeldig is, toont Fresh één aandachtspunt waarin de gebruiker de te gebruiken bron
kiest.

## Eenmalige V1-referentie

Onder de [onderzoeksgrens](../architecture/overview.md#eenmalige-v1-referentie)
zijn drie verschillen vastgesteld. Ze wijzigen de Fresh-vervangingsregel niet.

| Onderwerp | Aangetroffen V1-werking | Nog aan de gebruiker voor te leggen |
| --- | --- | --- |
| Activeringsmoment | Na succesvolle bestandsverwerking kan V1 de oude lijst vervangen terwijl de nieuwe lijst nog open matchregels bevat. Die onopgeloste regels worden voorraadproblemen; de oude voorraad blijft niet als aanvulling staan. [Verwerken][v1-activation], [activeren][v1-stock]. | Fresh wacht tot stap 5 en blokkeert op ongematchte regels zonder uitzondering. Advies: deze expliciete Fresh-afspraak behouden; eerder vervangen kan tijdelijk minder bruikbare voorraad geven. |
| Vervangen of aanvullen | V1 kent volledige vervanging en een expliciet gekozen aanvullende lijst. Bij aanvulling blijven niet-genoemde producten staan; overlap vraagt een keuze, zonder aantallen automatisch op te tellen. [Lifecycle][v1-stock], [overlap][v1-overlap]. | Fresh heeft volledige vervanging gekozen. Is een aparte aanvullende lijst werkelijk nodig? Voorstel: niet toevoegen zonder concrete behoefte. |
| Kwaliteitsvarianten | Binnen leverancier + naamcode + maatcode onderscheidt de voorraadlaag bewezen externe tekst na normalisatie van hoofdletters en witruimte. Andere tekst, ook alleen een ander leesteken, vormt een andere variant; onbekende tekst is niet hetzelfde als bewezen leeg. Gelijke of onzekere dubbele regels worden als probleem behandeld. [Variantvergelijking][v1-variant], [gelezen tests][v1-variant-test]. | Dit is geen herkenningsgeheugen dat tekstwijzigingen aan dezelfde uitvoering koppelt. Fresh heeft daarvoor al controle gekozen; het omgaan met bewezen leeg, onbekend en echte dubbele regels is nog te bepalen. |

[v1-activation]: https://github.com/MenkehorstKwekerijen/WinTree-Tools/blob/209846776a450dabbe29dc32322e60a1c986243e/app/main.py#L2209
[v1-stock]: https://github.com/MenkehorstKwekerijen/WinTree-Tools/blob/209846776a450dabbe29dc32322e60a1c986243e/app/storage/supplier_imports.py#L413
[v1-overlap]: https://github.com/MenkehorstKwekerijen/WinTree-Tools/blob/209846776a450dabbe29dc32322e60a1c986243e/app/storage/supplier_imports.py#L666
[v1-variant]: https://github.com/MenkehorstKwekerijen/WinTree-Tools/blob/209846776a450dabbe29dc32322e60a1c986243e/app/storage/supplier_imports.py#L12
[v1-variant-test]: https://github.com/MenkehorstKwekerijen/WinTree-Tools/blob/209846776a450dabbe29dc32322e60a1c986243e/tests/test_supplier_import_variant_overlap.py#L43

## Keten en open keuzes

Prijzen en leveranciersselecties gebruiken deze voorraadbetekenis.
[Voorraadimport](voorraadimport.md#stappen-van-de-leveranciersimport) bepaalt
wanneer een voorbereide lijst definitief wordt verwerkt; prijsvoorwaarden staan
in [prijzen](prijzen.md#prijsvoorwaarden-bij-import). Deze verwijzingen beschrijven
afnemers en integratie, geen prerequisites van de voorraadbetekenis.

De exacte bron-/leveranciersidentificatie, inhoudsvergelijking, ontbrekende of
ongeldige velden, oudere of herhaalde bestanden binnen dezelfde bron en behoud
van een bronkeuze vragen nog afspraken. Ook overlap tussen andere voorraadsoorten,
historische bewaring en het actualiseringsmoment van afnemers zijn nog open.
Zie [issue #12](https://github.com/MenkehorstKwekerijen/Fresh/issues/12) en de
[gegevensketen](../architecture/overview.md). Vervallen aanbod mag bij herstel of
gelijktijdige wijzigingen niet opnieuw actueel worden.
