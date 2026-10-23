---
id: prijzen
status: draft
depends_on: [voorraadimport]
---
# Prijsinstellingen en margegroepen

## Doel en scope

Prijsberekening en blijvende instellingen per product en leverancier, inclusief
prijsvoorwaarden voor voorraadimport. Geen catalogusprijs, importwizard of exportvrijgave.
Deze conceptspecificatie bevat de besloten afspraken; open keuzes blokkeren nog implementatie.
Besluiten en vervolgvraag: [issue #6](https://github.com/MenkehorstKwekerijen/Fresh/issues/6).

Lees gericht: [rekenbasis](#rekenbasis) · [prijskeuze](#prijswijzen) ·
[groepstoewijzing](#groepstoewijzing) · [afronden](#instelbare-afrondingsstaffel) ·
[herberekenen en aandacht](#herberekening-en-aandacht) ·
[importvoorwaarden](#prijsvoorwaarden-bij-import) · [keten en open keuzes](#keten-en-open-keuzes).
De criteria staan bij hun onderwerp; bestaande ID's blijven behouden.

## Rekenbasis

Alle bedragen zijn exclusief btw. [Opslag op inkoop](../glossary.md#term-opslag-op-inkoop)
is geen brutomargepercentage over de verkoopprijs:
`verkoopprijs = inkoopprijs × (1 + opslagpercentage / 100)`.
De bronprijs, of een expliciete correctie daarvan, vormt de rekenbasis.

<a id="ac-prijzen-001"></a>

### Opslag wordt over de inkoopprijs berekend

Gegeven een inkoopprijs van EUR 10,00 en een ingestelde opslag van 30 procent, is de berekende
verkoopprijs EUR 13,00.

<a id="ac-prijzen-047"></a>

### Prijsberekening en vergelijking gebruiken bedragen exclusief btw

Gegeven EUR 10,00 inkoop exclusief btw en 30 procent opslag, berekent Fresh EUR 13,00 verkoop
exclusief btw. Bij een vaste prijs van EUR 12,07 exclusief btw blijft die vaste prijs gelden en is
het verschil met de berekende prijs EUR 0,93 exclusief btw. Er wordt voor deze berekening of
vergelijking geen btw aan de bedragen toegevoegd.

<a id="ac-prijzen-048"></a>

### Overige kosten worden via het opslagpercentage verwerkt

Gegeven een inkoopprijs van EUR 10,00 exclusief btw uit het leveranciersbestand en 30 procent
opslag, is de berekende verkoopprijs EUR 13,00 exclusief btw. Ook als de gebruiker daarnaast EUR
1,00 transportkosten verwacht, voegt Fresh die niet afzonderlijk aan de rekenbasis toe. De gebruiker
kan voor dekking van die kosten het toepasselijke opslagpercentage aanpassen; Fresh blijft rekenen
vanaf de inkoopprijs uit het bestand.

## Prijswijzen

Per product en leverancier geldt deze volgorde, zonder stapeling:

| Instelling | Gebruikte verkoopprijs |
| --- | --- |
| [Vaste verkoopprijs](../glossary.md#term-vaste-verkoopprijs) | Exact het ingestelde bedrag |
| Geen vaste prijs, wel [margegroep](../glossary.md#term-margegroep) | Inkoopprijs met groepspercentage |
| Geen van beide | Inkoopprijs met [leveranciersstandaard](../glossary.md#term-standaardmarge-leverancier) |

Een margegroep bevat een percentage. Een vaste prijs is een afzonderlijke instelling;
een bestaande groep blijft erachter gekoppeld voor vergelijking en terugschakelen.

<a id="ac-prijzen-045"></a>

### De leveranciersstandaard is een rechtstreeks ingesteld percentage

Gegeven leveranciers A en B, kan de gebruiker bij beide rechtstreeks 30 procent standaardopslag
instellen zonder een margegroep te kiezen of aan te maken. Bij wijziging van A naar 35 procent
blijft B op 30 procent. Producten bij A die de standaard gebruiken worden volgens de bestaande
herberekeningsregels bijgewerkt; een individueel toegewezen groep blijft voorgaan en een vaste
verkoopprijs blijft exact staan.

<a id="ac-prijzen-016"></a>

### Ingelezen voorraad krijgt de standaardmarge van de leverancier

Gegeven leverancier A met standaardmarge 30 procent en een ingelezen product met inkoopprijs EUR
10,00 zonder afwijkende productinstelling, berekent Fresh voor dat aanbod EUR 13,00 verkoopprijs.

<a id="ac-prijzen-017"></a>

### Hetzelfde product kan per leverancier een andere marge krijgen

Gegeven hetzelfde product bij A en B, beide met inkoopprijs EUR 10,00 en zonder afwijkende
productinstelling, geeft de standaardmarge van A van 30 procent EUR 13,00 en die van B van 40
procent EUR 14,00. De instelling van A wordt niet gebruikt voor het aanbod van B.

<a id="ac-prijzen-019"></a>

### Een individuele margeregel vervangt de leveranciersstandaard

Gegeven leverancier A met standaardmarge 30 procent en een product bij A met inkoopprijs EUR 10,00,
geen vaste verkoopprijs en een toegewezen margegroep van 40 procent, berekent Fresh EUR 14,00. Fresh
stapelt de marges niet en vraagt geen conflictkeuze tussen de productregel en de
leveranciersstandaard.

<a id="ac-prijzen-020"></a>

### Een lagere individuele marge gaat ook voor

Gegeven leverancier A met standaardmarge 30 procent en een product bij A met inkoopprijs EUR 10,00,
geen vaste verkoopprijs en een toegewezen margegroep van 20 procent, berekent Fresh EUR 12,00. De
hogere leveranciersstandaard verdringt de productregel niet.

<a id="ac-prijzen-002"></a>

### De vaste verkoopprijs bepaalt het verkoopbedrag

Gegeven een toepasselijke instelling met vaste verkoopprijs EUR 15,00 en een inkoopprijs van EUR
10,00, is de verkoopprijs EUR 15,00.

<a id="ac-prijzen-021"></a>

### Een vaste verkoopprijs vervangt de procentuele berekening

Gegeven een product bij A met inkoopprijs EUR 10,00, standaardmarge 30 procent, een groepspercentage
van 40 procent en een ingestelde vaste verkoopprijs EUR 15,00, is de verkoopprijs EUR 15,00. De
percentages worden niet toegepast.

<a id="ac-prijzen-022"></a>

### Een vaste verkoopprijs blijft gelijk bij gewijzigde inkoopprijs

Gegeven een product bij A met vaste verkoopprijs EUR 15,00, blijft de verkoopprijs EUR 15,00 wanneer
diens inkoopprijs van EUR 10,00 naar EUR 11,00 verandert.

<a id="ac-prijzen-023"></a>

### Een vaste verkoopprijs geldt alleen bij de gekozen leverancier

Gegeven hetzelfde product bij A en B, beide met inkoopprijs EUR 10,00, waarbij B zonder individuele
regel een standaardmarge van 30 procent gebruikt, geeft het instellen van vaste verkoopprijs EUR
15,00 bij A een verkoopprijs van EUR 15,00 bij A. De verkoopprijs bij B blijft EUR 13,00.

<a id="ac-prijzen-028"></a>

### De groep blijft gekoppeld bij een vaste verkoopprijs

Gegeven een product bij A met groep G van 30 procent en inkoopprijs EUR 10,00, blijft G gekoppeld
nadat de gebruiker vaste verkoopprijs EUR 13,00 instelt. Na wijziging van G naar 40 procent gebruikt
Fresh G voor de vergelijkingsprijs EUR 14,00; de gebruikte verkoopprijs blijft EUR 13,00.

<a id="ac-prijzen-029"></a>

### Terugschakelen gebruikt de bewaarde groep met actuele gegevens

Gegeven een product bij A met vaste verkoopprijs EUR 13,00, bewaarde groep G met actueel 40 procent
en actuele inkoopprijs EUR 10,00, geeft bewust terugschakelen naar procentuele berekening EUR 14,00
verkoopprijs. Fresh vraagt niet opnieuw om een groep te kiezen.

<a id="ac-prijzen-032"></a>

### Zonder groep levert de leveranciersstandaard de vergelijkingsprijs

Gegeven een product bij A zonder margegroep, met inkoopprijs EUR 10,00, vaste verkoopprijs EUR 13,00
en leveranciersstandaard 40 procent, is de vergelijkingsprijs EUR 14,00. Zonder eerdere behoudkeuze
toont Fresh het aandachtspunt van EUR 1,00; de gebruikte verkoopprijs blijft EUR 13,00.

<a id="ac-prijzen-033"></a>

### Terugschakelen zonder groep gebruikt de leveranciersstandaard

Gegeven een product bij A zonder margegroep, met vaste verkoopprijs EUR 13,00, actuele inkoopprijs
EUR 10,00 en actuele leveranciersstandaard 40 procent, geeft bewust terugschakelen naar procentuele
berekening EUR 14,00 verkoopprijs. Een margegroeptoewijzing is hiervoor niet nodig.

## Groepstoewijzing

De gebruiker kan margegroepen aanmaken en één actieve groep per product en leverancier
koppelen. Filters helpen bij handmatige selectie; ze vormen geen automatische toewijzingsregel.
Een hoofdstuk is een toewijzingsroute, geen prijsniveau. Gelijke kandidaten gelden als één;
verschillende groepen bij verschillende leveranciers zijn geen conflict. Een wijziging van
expliciete toewijzing vraagt een bewuste keuze; een percentagewijziging binnen de groep volgt
[herberekening](#herberekening-en-aandacht).

<a id="ac-prijzen-012"></a>

### Een individueel product krijgt een margegroep

Gegeven een product bij leverancier A zonder actieve margegroep, kan de gebruiker rechtstreeks groep
G toewijzen. Daarna is G de actieve margegroep van dat product bij A.

<a id="ac-prijzen-018"></a>

### Een groepstoewijzing blijft beperkt tot de gekozen leverancier

Gegeven hetzelfde product bij A en B, verandert het toewijzen van groep G aan dat product bij A de
margegroeptoewijzing bij B niet.

<a id="ac-prijzen-013"></a>

### Een leveranciersselectie gebruikt aanbod en verkoopgeschiedenis

Gegeven een gekozen leverancier met ingelezen fictief/TCM-aanbod en gekoppelde verkoopgeschiedenis,
kan de gebruiker met filters op deze gegevens producten vinden, zelf selecteren en de selectie in
één bulkactie aan een margegroep toewijzen. Welke verkoopfilters beschikbaar zijn, is nog te
besluiten.

<a id="ac-prijzen-014"></a>

### Een heel hoofdstuk kan worden toegewezen

Gegeven een hoofdstuk met producten zonder actieve margegroep voor de gekozen leveranciers, kan de
gebruiker die producten met één bulkactie aan groep G toewijzen. Daarna is G hun actieve groep bij
die leveranciers.

<a id="ac-prijzen-004"></a>

### Een bulkactie past de toewijzing toe op de selectie

Gegeven drie beschikbare onderdelen A, B en C, waarbij de gebruiker A en B selecteert, kan de
gebruiker met één bulkactie een margegroep voor A en B toewijzen. De directe toewijzing van het
niet-geselecteerde onderdeel C verandert niet.

<a id="ac-prijzen-009"></a>

### Verschillende kandidaten vragen een eenmalige keuze

Gegeven een nog niet toegewezen product bij leverancier A met kandidaat G via een
leveranciersselectie en H via het hoofdstuk, toont Fresh de kandidaten en hun herkomst. De gebruiker
kan eenmaal een groep kiezen, ook in bulk. Na keuze voor H is alleen H actief.

<a id="ac-prijzen-010"></a>

### Een gekozen koppeling blijft behouden

Gegeven een product bij leverancier A waarvoor de gebruiker bij kandidaten G en H groep H heeft
gekozen, blijft H bij volgende berekeningen actief zonder een herhaalde keuzevraag over dezelfde
kandidaten.

<a id="ac-prijzen-011"></a>

### Gewijzigde toewijzingsregels vereisen expliciete herbeoordeling

Gegeven een product bij leverancier A met actieve groep G, blijft G gekoppeld wanneer een
leveranciersselectie of hoofdstuktoewijzing een andere groep H gaat voorstellen. Wijziging van de
productkoppeling naar H vereist expliciete herbeoordeling.

<a id="ac-prijzen-015"></a>

### Een nieuwe import breidt een handmatige selectie niet automatisch uit

Gegeven een handmatig gekozen leveranciersselectie die aan groep G is toegewezen, wordt een later
geïmporteerd nieuw product niet uitsluitend doordat het aan dezelfde filters voldoet onderdeel van
die selectie of aan G gekoppeld.

## Instelbare afrondingsstaffel

De [afrondingsstaffel](../glossary.md#term-afrondingsstaffel) geldt voor berekende prijzen
én vergelijkingsprijzen. De onderstaande criteria bepalen de begininstelling, grenzen en
volgorde. Handmatig ingestelde vaste prijzen blijven exact.

<a id="ac-prijzen-037"></a>

### De gekozen afrondingsstaffel is instelbaar

Gegeven de prijsinstellingen, is de beginstaffel zichtbaar met stappen van EUR 0,01 onder EUR 1,00,
EUR 0,05 vanaf EUR 1,00 tot en met EUR 10,00, EUR 0,10 boven EUR 10,00 tot en met EUR 20,00 en EUR
0,25 boven EUR 20,00. De gebruiker kan de staffel via de instellingen aanpassen.

<a id="ac-prijzen-038"></a>

### Afronden kiest het dichtstbijzijnde bedrag

Gegeven de gekozen staffel, wordt een berekende verkoopprijs van EUR 12,04 afgerond naar EUR 12,00
en EUR 12,06 naar EUR 12,10. Een berekende prijs van EUR 20,14 wordt afgerond naar EUR 20,25. De
afzonderlijke middenregel staat in het criterium over bedragen precies halverwege.

<a id="ac-prijzen-040"></a>

### Precies halverwege wordt naar boven afgerond

Gegeven de gekozen staffel, wordt EUR 0,125 afgerond naar EUR 0,13, EUR 2,125 naar EUR 2,15, EUR
12,05 naar EUR 12,10 en EUR 20,125 naar EUR 20,25. Elk bedrag ligt precies tussen twee stappen van
zijn toepasselijke bereik.

<a id="ac-prijzen-044"></a>

### De onafgeronde prijs bepaalt de afrondingsstap

Gegeven de gekozen beginstaffel, geldt:

| Onafgeronde berekende prijs | Gekozen stap | Afgeronde prijs |
| --- | --- | --- |
| EUR 0,999 | EUR 0,01 | EUR 1,00 |
| EUR 1,00 | EUR 0,05 | EUR 1,00 |
| EUR 10,00 | EUR 0,05 | EUR 10,00 |
| EUR 10,04 | EUR 0,10 | EUR 10,00 |
| EUR 20,00 | EUR 0,10 | EUR 20,00 |
| EUR 20,04 | EUR 0,25 | EUR 20,00 |

Het afgeronde bedrag leidt niet tot een nieuwe keuze van de stap of een tweede afronding, ook
wanneer het bedrag op een grens van een ander prijsbereik uitkomt.

<a id="ac-prijzen-039"></a>

### Herhaald berekenen stapelt geen afronding op

Gegeven inkoopprijs EUR 10,05 en opslag 20 procent, is het onafgeronde eindbedrag EUR 12,06 en de
afgeronde verkoopprijs EUR 12,10. Iedere volgende herberekening met dezelfde invoer en staffel
gebruikt opnieuw EUR 10,05 en 20 procent en geeft EUR 12,10. Het eerder afgeronde bedrag wordt niet
als rekenbasis gebruikt.

<a id="ac-prijzen-041"></a>

### Een handmatig ingestelde vaste prijs wordt niet afgerond

Gegeven een handmatig ingestelde vaste verkoopprijs van EUR 12,07, blijft de gebruikte verkoopprijs
exact EUR 12,07 bij een staffelstap van EUR 0,10. De afrondingsstaffel wordt niet op dit vaste
bedrag toegepast.

## Herberekening en aandacht

Groepspercentages, leveranciersstandaarden en afrondingsinstellingen werken automatisch
door op de berekeningen die ervan afhangen. Vaste prijzen blijven behouden. Bij een hogere
afgeronde vergelijkingsprijs kan de gebruiker behouden, aanpassen of terugschakelen.
De behoudgrens geldt zolang de vaste prijs ongewijzigd is; wijzigingen daarvan zijn nog open.

<a id="ac-prijzen-024"></a>

### Een groepswijziging herberekent gekoppelde procentuele prijzen

Gegeven een product bij A met inkoopprijs EUR 10,00, gekoppelde groep G met 30 procent en zonder
vaste verkoopprijs, wordt de verkoopprijs automatisch EUR 13,50 als G naar 35 procent wijzigt. Het
product blijft aan G gekoppeld.

<a id="ac-prijzen-034"></a>

### Een gewijzigde leveranciersstandaard herberekent standaardprijzen

Gegeven een product bij A met inkoopprijs EUR 10,00, zonder eigen groep of vaste prijs, wordt de
verkoopprijs automatisch EUR 13,50 wanneer de leveranciersstandaard van 30 naar 35 procent wijzigt.

<a id="ac-prijzen-035"></a>

### Een leverancierswijziging verdringt een eigen groep niet

Gegeven een product bij A met inkoopprijs EUR 10,00 en eigen groep G van 40 procent, blijft G
leidend wanneer de leveranciersstandaard van 30 naar 35 procent wijzigt. De procentuele prijs blijft
EUR 14,00; bij een vaste prijs blijft de vergelijkingsprijs op basis van G eveneens EUR 14,00.

<a id="ac-prijzen-036"></a>

### Een leverancierswijziging actualiseert de vergelijking zonder vaste prijs te wijzigen

Gegeven een product bij A zonder groep, met inkoopprijs EUR 10,00 en vaste verkoopprijs EUR 13,00,
wordt de vergelijkingsprijs EUR 13,50 als de leveranciersstandaard van 30 naar 35 procent wijzigt.
Zonder eerdere behoudkeuze verschijnt een aandachtspunt met EUR 0,50 verschil. De verkoopprijs
blijft EUR 13,00.

<a id="ac-prijzen-043"></a>

### Een gewijzigde staffel herberekent bestaande prijzen en vergelijkingen

Gegeven inkoopprijs EUR 10,05 en opslag 20 procent, geeft de berekening EUR 12,06. Bij wijziging van
de stap voor dit bereik van EUR 0,10 naar EUR 0,25 verandert de berekende verkoopprijs automatisch
van EUR 12,10 naar EUR 12,00. Voor een product met dezelfde rekeninvoer en vaste prijs EUR 12,02
verandert de vergelijkingsprijs eveneens naar EUR 12,00; het aandachtspunt voor een te lage vaste
prijs vervalt. De vaste verkoopprijs blijft EUR 12,02. Dit leidt niet automatisch tot export of
publicatie en wijzigt geen eerder geëxporteerde bestanden.

<a id="ac-prijzen-025"></a>

### Een hogere berekende prijs geeft aandacht zonder vaste prijs te wijzigen

Gegeven een product bij A met inkoopprijs EUR 10,00, vaste verkoopprijs EUR 13,00 en een
toepasselijk groepspercentage dat van 30 naar 40 procent wijzigt, blijft de verkoopprijs EUR 13,00.
Fresh toont een aandachtspunt met EUR 13,00 vast, EUR 14,00 berekend en EUR 1,00 verschil.

<a id="ac-prijzen-026"></a>

### Een berekende prijs op of onder de vaste prijs geeft dit signaal niet

Gegeven een product bij A met vaste verkoopprijs EUR 13,00, geeft een toepasselijke berekende prijs
van EUR 13,00 of EUR 12,00 geen aandachtspunt voor een te lage vaste prijs.

<a id="ac-prijzen-027"></a>

### De gebruiker kiest hoe een vaste prijs wordt behandeld

Gegeven het aandachtspunt met EUR 13,00 vast en EUR 14,00 berekend, kan de gebruiker de vaste EUR
13,00 behouden, een ander vast bedrag instellen of teruggaan naar de toepasselijke procentuele
berekening. Alleen die keuze wijzigt de prijswijze of de vaste prijs; het signaal doet dit niet
zelfstandig.

<a id="ac-prijzen-030"></a>

### Een bewust behouden vaste prijs geeft geen herhaalde melding

Gegeven vaste prijs EUR 13,00 en berekende prijs EUR 14,00 bij product P van leverancier A,
verdwijnt het aandachtspunt wanneer de gebruiker de vaste prijs behoudt. Bij ongewijzigde vaste
prijs geven berekende prijzen van EUR 14,00 of lager geen nieuwe melding, ook niet na een daling en
terugkeer naar EUR 14,00.

<a id="ac-prijzen-031"></a>

### Verdere stijging vraagt opnieuw aandacht

Gegeven een bewust behouden vaste prijs EUR 13,00 bij een beoordeelde berekende prijs EUR 14,00,
verschijnt opnieuw een aandachtspunt als de berekende prijs EUR 14,50 wordt. Behoudt de gebruiker
opnieuw EUR 13,00, dan wordt EUR 14,50 de nieuwe beoordelingsgrens. De vaste verkoopprijs blijft EUR
13,00.

<a id="ac-prijzen-042"></a>

### Aandacht vergelijkt de afgeronde prijs met de exacte vaste prijs

Gegeven de gekozen staffel en een ongewijzigde vaste verkoopprijs van EUR 12,02, zonder eerdere
behoudkeuze, geldt:

| Onafgeronde berekende prijs | Afgeronde vergelijkingsprijs | Aandachtspunt |
| --- | --- | --- |
| EUR 12,04 | EUR 12,00 | Nee |
| EUR 12,06 | EUR 12,10 | Ja, met EUR 0,08 verschil |

De vaste prijs blijft in beide gevallen EUR 12,02. Bij bewust behouden van de tweede situatie wordt
EUR 12,10 de beoordeelde grens; een stijging van het onafgeronde bedrag naar EUR 12,09 geeft geen
nieuwe melding, omdat de afgeronde vergelijkingsprijs EUR 12,10 blijft.

## Prijsvoorwaarden bij import

De leverancier moet vóór het inlezen een standaardmarge hebben. Een ontbrekende of
ongeldige inkoopprijs blokkeert de hele lijst. De waarschuwing bij kolomtoewijzing en de
importroute vallen onder [voorraadimport](voorraadimport.md); deze sectie bezit prijsvalidatie
en directe prijscorrectie. Een foutmelding neemt geen prijs of percentage aan.

<a id="ac-prijzen-046"></a>

### Een ontbrekende standaardmarge blokkeert het inlezen

Gegeven een voorraadlijst voor leverancier A zonder ingestelde standaardmarge, blokkeert Fresh het
inlezen en vermeldt dat eerst een standaardmarge voor A moet worden ingesteld. Er wordt geen
percentage aangenomen en een eventuele vorige voorraadstand van A blijft behouden. Na het instellen
van de standaardmarge blokkeert deze ontbrekende instelling de import niet meer; andere importfouten
worden daardoor niet overgeslagen.

<a id="ac-prijzen-049"></a>

### Een ontbrekende of ongeldige inkoopprijs blokkeert de volledige lijst

Gegeven een leverancierslijst met geldige regels en een regel waarvan de inkoopprijs ontbreekt of
geen leesbaar bedrag is, blokkeert Fresh de volledige import van die lijst. Geen van de nieuwe
regels vervangt de vorige voorraad. Fresh toont de foutregels en neemt geen nulprijs of eerdere
prijs als vervanging. Na herstel controleert Fresh de lijst opnieuw; andere blokkerende fouten
blijven de import tegenhouden.

<a id="ac-prijzen-050"></a>

### Een prijsfout biedt een directe link naar herstel

Gegeven een ontbrekende inkoopprijs op bestandsregel 12 van leverancier A, vermeldt de foutmelding
A, regel 12, het veld inkoopprijs en de foutreden. De herstelactie brengt de gebruiker rechtstreeks
bij die regel en het op te lossen prijsprobleem. Bij meerdere foutregels heeft iedere fout een eigen
gerichte herstelactie; een link naar alleen een algemeen overzicht volstaat niet.

<a id="ac-prijzen-051"></a>

### Een prijsfout wordt rechtstreeks in Fresh gecorrigeerd

Gegeven een lege inkoopprijs op regel 12, opent de directe herstelactie die regel in Fresh. De
gebruiker ziet de lege bronwaarde en kan EUR 10,00 exclusief btw invullen zonder een nieuw bestand
te uploaden. Fresh controleert de import opnieuw en gebruikt EUR 10,00 als inkoopprijs; bij 30
procent opslag is de berekende verkoopprijs EUR 13,00 exclusief btw. De oorspronkelijke bronwaarde
blijft zichtbaar. Zolang andere blokkerende fouten bestaan, blijft de volledige import geblokkeerd
en de vorige voorraad behouden.

## Keten en open keuzes

De procentuele leveranciersberekening gebruikt de inkoopprijs van de betreffende
leverancier; een vaste verkoopprijs blijft het ingestelde bedrag.
Hoe meerdere leveranciersprijzen leiden tot een catalogusprijs en of deze keuze
samenhangt met de leveranciersvoorkeur moet nog worden besloten.

De selectieroute gebruikt actueel fictief/TCM-aanbod volgens de
[bronkeuze bij voorraadimport](voorraadimport.md#leveranciers-en-mogelijke-dubbele-aanlevering).
Verkoopgeschiedenis moet aan producten en waar nodig leveranciers gekoppeld
kunnen worden. De benodigde velden en betrouwbare koppeling zijn nog niet
bevestigd. Of ook eerder verkochte producten buiten het actuele aanbod kunnen
worden geselecteerd, is open. De margegroeptoewijzing geldt per product en
leverancier; de precieze productidentiteit en herkenning over opeenvolgende
bestanden zijn nog niet bepaald. Bij een hoofdstukactie moet duidelijk zijn
welke leveranciersaanbiedingen worden geraakt; de bediening hiervan is nog open.

WinTree-export en catalogus/website zijn relevante afnemers binnen het
[productdoel](../project.md). Welke prijsvelden elke afnemer krijgt, moet nog
worden uitgewerkt. Herberekening na wijziging van een groepspercentage,
leveranciersstandaard of afrondingsstaffel geldt binnen Fresh;
dit besluit geeft geen automatische publicatie of aanpassing van al geëxporteerde
bestanden. Het moment van overdracht naar afnemers, herberekening bij nieuwe
inkoopprijzen, gelijktijdige wijzigingen
en herstel vragen nog afspraken.

Het achteraf verwijderen van een standaardmarge bij bestaande voorraad is nog open;
Fresh neemt daarvoor geen percentage aan. De afhandeling van een bestand met meerdere
leveranciers moet nog worden bepaald. Concrete
verkoopfilters, combinatie met actueel aanbod en leveranciersbereik van een
hoofdstukactie blijven open. Automatische uitbreiding van een handmatige
selectie is niet gekozen; voorraad zonder individuele regel valt onder de
leveranciersstandaard. Herkenning van bestaande productinstellingen bij nieuwe
imports vraagt nog uitwerking.
Gedrag bij geen
kandidaat of een nog open keuze, behoudkeuzes na wijzigingen van vaste prijs of prijswijze,
bronbestanden met bedragen inclusief btw, hergebruik van prijscorrecties bij
volgende bestanden en correcties na gewijzigde kolomtoewijzing,
toegestane prijswaarden (waaronder nulprijzen) en de hierboven genoemde
ketengevolgen worden uitgewerkt in
[issue #6](https://github.com/MenkehorstKwekerijen/Fresh/issues/6).
