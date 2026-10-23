---
id: prijzen
status: draft
depends_on: [voorraadimport]
---
# Prijsinstellingen en margegroepen

## Doel en scope

Fresh ondersteunt [opslag op inkoop](../glossary.md#term-opslag-op-inkoop) en
een [vaste verkoopprijs](../glossary.md#term-vaste-verkoopprijs). Iedere leverancier
heeft een [standaardmarge](../glossary.md#term-standaardmarge-leverancier) voor
diens ingelezen voorraad. Na groepstoewijzing geldt één actieve
[margegroep](../glossary.md#term-margegroep) per product en leverancier.
Hetzelfde product kan bij verschillende leveranciers een andere marge hebben.
Toewijzing kan per individueel product, voor een zelf geselecteerde groep
producten binnen een leverancier en voor een heel catalogushoofdstuk.
Meerdere producten toewijzen kan met een [bulkactie](../glossary.md#term-bulkactie).

Het actuele gebruikersbesluit staat in
[issue #6](https://github.com/MenkehorstKwekerijen/Fresh/issues/6).
De specificatie is nog niet volledig genoeg voor implementatie.

## Gedrag en gegevens

### Prijswijzen

Bij procentuele opslag geldt:

`verkoopprijs = inkoopprijs × (1 + opslagpercentage / 100)`

Margegroepen bepalen de procentuele opslag. Een vaste verkoopprijs wordt
afzonderlijk ingesteld voor een product bij een leverancier. Dat bedrag vervangt
de procentuele berekening: er wordt geen groeps- of leveranciersopslag bovenop
toegepast. Een brutomargepercentage over de verkoopprijs is niet als prijswijze gekozen.

| Toepasselijke instelling voor product en leverancier | Verkoopprijs |
| --- | --- |
| Vaste verkoopprijs ingesteld | Het ingestelde bedrag |
| Geen vaste prijs, wel een toegewezen margegroep | Inkoopprijs met het groepspercentage |
| Geen vaste prijs of toegewezen groep | Inkoopprijs met de leveranciersstandaard |

Bij een vaste verkoopprijs van EUR 15,00 blijft de verkoopprijs EUR 15,00 als
de inkoopprijs van EUR 10,00 naar EUR 11,00 verandert. Deze instelling geldt
alleen bij die leverancier. Een bestaande margegroep blijft gekoppeld wanneer
de gebruiker een vaste prijs instelt. Fresh gebruikt het actuele groepspercentage
voor de vergelijkingsprijs; de gebruikte verkoopprijs blijft het vaste bedrag.
Bij bewust terugschakelen naar procentuele berekening gebruikt Fresh opnieuw
dezelfde groep met het actuele percentage en de actuele inkoopprijs. De gebruiker
hoeft de groep niet opnieuw te kiezen.

Zonder gekoppelde margegroep gebruikt Fresh de actuele standaardmarge van die
leverancier voor de vergelijking met een vaste prijs. Bij bewust terugschakelen
naar procentuele berekening gebruikt Fresh diezelfde leveranciersstandaard met
de actuele inkoopprijs. Fresh hoeft daarvoor geen margegroep toe te wijzen.

### Instelbare afrondingsstaffel

Voor berekende verkoopprijzen geldt de volgende
[afrondingsstaffel](../glossary.md#term-afrondingsstaffel):

| Prijsbereik | Afrondingsstap |
| --- | --- |
| Onder EUR 1,00 | EUR 0,01 |
| Vanaf EUR 1,00 tot en met EUR 10,00 | EUR 0,05 |
| Meer dan EUR 10,00 | EUR 0,25 |

De staffel moet via de instellingen kunnen worden aangepast. De genoemde
bedragen zijn de gekozen begininstelling. De richting van afronden, behandeling
van bedragen precies tussen twee stappen en het moment waarop het prijsbereik
wordt bepaald zijn nog open. Ook gevolgen van gewijzigde instellingen voor
bestaande prijzen, de vergelijking met vaste prijzen en toepassing op handmatig
ingestelde vaste prijzen moeten nog worden bepaald.

### Standaardmarge per leverancier

Bij het inlezen van voorraadlijsten in Fresh wordt de ingestelde standaardmarge
van de betreffende leverancier toegepast op diens inkoopprijzen. Bijvoorbeeld:
zonder afwijkende productinstellingen geeft EUR 10,00 inkoop bij leverancier A
met 30 procent opslag een berekende verkoopprijs van EUR 13,00. Hetzelfde
product met EUR 10,00 inkoop bij leverancier B met 40 procent opslag geeft
EUR 14,00. De leveranciersinstelling van A geldt niet voor B.

Een [individuele margeregel](../glossary.md#term-individuele-margeregel) voor
een product bij een leverancier gaat voor de standaardmarge van die leverancier.
Bij procentuele berekening vervangt een expliciet toegewezen productgroep
daarmee de standaardmarge voor die combinatie. Zonder individuele regel geldt
de standaardmarge.
De marges worden niet opgeteld en niet na elkaar toegepast. Standaard 30 procent
en een individuele regel van 40 procent bij EUR 10,00 inkoop geeft EUR 14,00.
Dit geldt ook als de individuele opslag lager is dan de standaardmarge.
De berekening geeft voorrang aan de individuele regel zonder een conflictkeuze
tussen die regel en de standaardmarge te vragen.

Of de standaardmarge zelf als margegroep wordt beheerd, moet nog worden besloten.

### Producten selecteren en toewijzen

De gebruiker kan één product bij een leverancier rechtstreeks aan een margegroep toewijzen.
Binnen een leverancier stelt de gebruiker zelf een selectie samen met filters
op actueel aanbod uit fictieve voorraad en TCM en op verkoopgeschiedenis.
Vervolgens wijst de gebruiker de geselecteerde producten met een bulkactie aan
een margegroep toe. Binnen dezelfde leverancier kunnen verschillende selecties
aan verschillende margegroepen worden toegewezen. Ook een heel hoofdstuk kan
worden toegewezen.

De filters helpen bij het selecteren; ze vormen geen opgeslagen regel die
toekomstige producten automatisch aan deze selectie toevoegt. De precieze
verkoopfilters, periode en combinatie met actueel aanbod zijn nog te bepalen.

### Eén actieve groep en conflicterende toewijzingen

Margegroepen kunnen worden aangemaakt en aan producten toegewezen. Verschillende
toewijzingen kunnen [kandidaat-margegroepen](../glossary.md#term-kandidaat-margegroep)
voor hetzelfde product bij dezelfde leverancier opleveren. Verschillende
groepen bij verschillende leveranciers zijn geen conflict. De voorrang van
een individuele regel op de leveranciersstandaard staat hierboven. Een
hoofdstuk is een route voor groepstoewijzing en vormt geen extra prijsniveau.

Wanneer toewijzingen dezelfde groep opleveren, is dat één kandidaat. Bij
verschillende kandidaten krijgt de gebruiker een duidelijk aandachtspunt en
kiest die eenmaal, eventueel voor meerdere producten met een bulkactie.
Een toewijzing die afwijkt van de bestaande actieve groep vraagt een bewuste keuze.

De gekozen groep blijft aan het product bij die leverancier gekoppeld. Een volgende prijsberekening
vraagt niet opnieuw om dezelfde keuze. Leverancier en hoofdstuk blijven dus niet
bij elke berekening concurrerende prijsinstellingen leveren.

### Herbeoordeling na gewijzigde toewijzingsregels

Een wijziging van de toewijzingsregels bij leverancier of hoofdstuk overschrijft
de gekozen groep van bestaande producten niet automatisch. Bestaande producten
vragen een expliciete herbeoordeling. Een andere groep wordt pas gekoppeld als
die herbeoordeling tot die keuze leidt.

Deze afspraak gaat over het wijzigen van expliciete groepstoewijzingen.
Het wijzigen van een percentage binnen een gekoppelde groep is een andere
handeling en werkt volgens onderstaande herberekeningsregel.

### Herberekening en aandacht voor vaste prijzen

Een gewijzigd groepspercentage wordt automatisch toegepast op de gekoppelde
producten met procentuele prijsberekening. Bij EUR 10,00 inkoop en wijziging
van 30 naar 35 procent verandert de berekende verkoopprijs van EUR 13,00 naar
EUR 13,50. De groepskoppeling verandert daarbij niet.

Een wijziging van de leveranciersstandaard werkt eveneens automatisch door
voor producten die deze standaard gebruiken. Zonder eigen groep of vaste prijs
wordt de verkoopprijs opnieuw berekend. Bij een vaste prijs zonder eigen groep
wordt de vergelijkingsprijs bijgewerkt en gelden de onderstaande aandachtregels;
de vaste prijs blijft staan. Een eigen margegroep blijft voor zowel berekening
als vergelijking leidend en wordt niet door de leverancierswijziging vervangen.

Vaste verkoopprijzen blijven gelijk. Komt de prijs op basis van het toepasselijke
percentage boven de vaste verkoopprijs, dan toont Fresh een aandachtspunt met
de vaste prijs, de berekende prijs en het verschil. Bijvoorbeeld bij EUR 10,00
inkoop, EUR 13,00 vast en 40 procent opslag: de vaste verkoopprijs blijft
EUR 13,00; de melding geeft aan dat deze EUR 1,00 onder de berekende EUR 14,00 ligt.
Bij een gelijke of lagere berekende prijs is er om deze reden geen aandachtspunt.

De gebruiker kan de vaste prijs behouden, aanpassen of teruggaan naar
procentuele berekening. Fresh verhoogt de vaste prijs niet automatisch.

Bij bewust kiezen voor 'vaste prijs behouden' verdwijnt het aandachtspunt voor
dat product bij die leverancier. Fresh onthoudt de op dat moment beoordeelde
berekende prijs. Zolang de vaste prijs niet wordt gewijzigd, wordt dezelfde
situatie niet opnieuw voorgelegd: pas als de berekende prijs boven het laatst
beoordeelde bedrag stijgt én boven de vaste prijs ligt, verschijnt opnieuw een
aandachtspunt. Een tussentijdse daling en terugkeer naar hetzelfde beoordeelde
bedrag geven geen nieuwe melding. Opnieuw behouden neemt de dan beoordeelde
berekende prijs als nieuwe grens.

Wat prijswijze- of vaste-prijswijzigingen met een eerdere behoudkeuze doen,
moet nog worden bepaald. Ook gedrag bij een ontbrekende leveranciersstandaard
zonder groepskoppeling blijft open; Fresh neemt daarvoor geen percentage aan.

## Keten en herstel

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
worden uitgewerkt. Herberekening na een groeps- of leveranciersstandaardwijziging geldt binnen Fresh;
dit besluit geeft geen automatische publicatie of aanpassing van al geëxporteerde
bestanden. Het moment van overdracht naar afnemers, herberekening bij nieuwe
inkoopprijzen, gelijktijdige wijzigingen
en herstel vragen nog afspraken.

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

<a id="ac-prijzen-009"></a>

### Verschillende kandidaten vragen een eenmalige keuze

Gegeven een nog niet toegewezen product bij leverancier A met kandidaat G via een leveranciersselectie en
H via het hoofdstuk, toont Fresh de kandidaten en hun herkomst. De gebruiker
kan eenmaal een groep kiezen, ook in bulk. Na keuze voor H is alleen H actief.

<a id="ac-prijzen-010"></a>

### Een gekozen koppeling blijft behouden

Gegeven een product bij leverancier A waarvoor de gebruiker bij kandidaten G en H groep H heeft
gekozen, blijft H bij volgende berekeningen actief zonder een herhaalde
keuzevraag over dezelfde kandidaten.

<a id="ac-prijzen-011"></a>

### Gewijzigde toewijzingsregels vereisen expliciete herbeoordeling

Gegeven een product bij leverancier A met actieve groep G, blijft G gekoppeld wanneer een
leveranciersselectie of hoofdstuktoewijzing een andere groep H gaat voorstellen.
Wijziging van de productkoppeling naar H vereist expliciete herbeoordeling.

<a id="ac-prijzen-012"></a>

### Een individueel product krijgt een margegroep

Gegeven een product bij leverancier A zonder actieve margegroep, kan de gebruiker
rechtstreeks groep G toewijzen. Daarna is G de actieve margegroep van dat product bij A.

<a id="ac-prijzen-013"></a>

### Een leveranciersselectie gebruikt aanbod en verkoopgeschiedenis

Gegeven een gekozen leverancier met ingelezen fictief/TCM-aanbod en gekoppelde
verkoopgeschiedenis, kan de gebruiker met filters op deze gegevens producten
vinden, zelf selecteren en de selectie in één bulkactie aan een margegroep
toewijzen. Welke verkoopfilters beschikbaar zijn, is nog te besluiten.

<a id="ac-prijzen-014"></a>

### Een heel hoofdstuk kan worden toegewezen

Gegeven een hoofdstuk met producten zonder actieve margegroep voor de gekozen
leveranciers, kan de gebruiker die producten met één bulkactie aan groep G
toewijzen. Daarna is G hun actieve groep bij die leveranciers.

<a id="ac-prijzen-015"></a>

### Een nieuwe import breidt een handmatige selectie niet automatisch uit

Gegeven een handmatig gekozen leveranciersselectie die aan groep G is toegewezen,
wordt een later geïmporteerd nieuw product niet uitsluitend doordat het aan
dezelfde filters voldoet onderdeel van die selectie of aan G gekoppeld.

<a id="ac-prijzen-016"></a>

### Ingelezen voorraad krijgt de standaardmarge van de leverancier

Gegeven leverancier A met standaardmarge 30 procent en een ingelezen product
met inkoopprijs EUR 10,00 zonder afwijkende productinstelling, berekent Fresh
voor dat aanbod EUR 13,00 verkoopprijs.

<a id="ac-prijzen-017"></a>

### Hetzelfde product kan per leverancier een andere marge krijgen

Gegeven hetzelfde product bij A en B, beide met inkoopprijs EUR 10,00 en zonder
afwijkende productinstelling, geeft de standaardmarge van A van 30 procent
EUR 13,00 en die van B van 40 procent EUR 14,00. De instelling van A wordt
niet gebruikt voor het aanbod van B.

<a id="ac-prijzen-018"></a>

### Een groepstoewijzing blijft beperkt tot de gekozen leverancier

Gegeven hetzelfde product bij A en B, verandert het toewijzen van groep G
aan dat product bij A de margegroeptoewijzing bij B niet.

<a id="ac-prijzen-019"></a>

### Een individuele margeregel vervangt de leveranciersstandaard

Gegeven leverancier A met standaardmarge 30 procent en een product bij A met
inkoopprijs EUR 10,00, geen vaste verkoopprijs en een toegewezen margegroep van 40 procent, berekent
Fresh EUR 14,00. Fresh stapelt de marges niet en vraagt geen conflictkeuze
tussen de productregel en de leveranciersstandaard.

<a id="ac-prijzen-020"></a>

### Een lagere individuele marge gaat ook voor

Gegeven leverancier A met standaardmarge 30 procent en een product bij A met
inkoopprijs EUR 10,00, geen vaste verkoopprijs en een toegewezen margegroep van 20 procent, berekent
Fresh EUR 12,00. De hogere leveranciersstandaard verdringt de productregel niet.

<a id="ac-prijzen-021"></a>

### Een vaste verkoopprijs vervangt de procentuele berekening

Gegeven een product bij A met inkoopprijs EUR 10,00, standaardmarge 30 procent,
een groepspercentage van 40 procent en een ingestelde vaste verkoopprijs
EUR 15,00, is de verkoopprijs EUR 15,00. De percentages worden niet toegepast.

<a id="ac-prijzen-022"></a>

### Een vaste verkoopprijs blijft gelijk bij gewijzigde inkoopprijs

Gegeven een product bij A met vaste verkoopprijs EUR 15,00, blijft de
verkoopprijs EUR 15,00 wanneer diens inkoopprijs van EUR 10,00 naar EUR 11,00
verandert.

<a id="ac-prijzen-023"></a>

### Een vaste verkoopprijs geldt alleen bij de gekozen leverancier

Gegeven hetzelfde product bij A en B, beide met inkoopprijs EUR 10,00,
waarbij B zonder individuele regel een standaardmarge van 30 procent gebruikt,
geeft het instellen van vaste verkoopprijs EUR 15,00 bij A een verkoopprijs
van EUR 15,00 bij A. De verkoopprijs bij B blijft EUR 13,00.

<a id="ac-prijzen-024"></a>

### Een groepswijziging herberekent gekoppelde procentuele prijzen

Gegeven een product bij A met inkoopprijs EUR 10,00, gekoppelde groep G met
30 procent en zonder vaste verkoopprijs, wordt de verkoopprijs automatisch
EUR 13,50 als G naar 35 procent wijzigt. Het product blijft aan G gekoppeld.

<a id="ac-prijzen-025"></a>

### Een hogere berekende prijs geeft aandacht zonder vaste prijs te wijzigen

Gegeven een product bij A met inkoopprijs EUR 10,00, vaste verkoopprijs EUR 13,00
en een toepasselijk groepspercentage dat van 30 naar 40 procent wijzigt,
blijft de verkoopprijs EUR 13,00. Fresh toont een aandachtspunt met EUR 13,00
vast, EUR 14,00 berekend en EUR 1,00 verschil.

<a id="ac-prijzen-026"></a>

### Een berekende prijs op of onder de vaste prijs geeft dit signaal niet

Gegeven een product bij A met vaste verkoopprijs EUR 13,00, geeft een toepasselijke
berekende prijs van EUR 13,00 of EUR 12,00 geen aandachtspunt voor een te lage
vaste prijs.

<a id="ac-prijzen-027"></a>

### De gebruiker kiest hoe een vaste prijs wordt behandeld

Gegeven het aandachtspunt met EUR 13,00 vast en EUR 14,00 berekend, kan de
gebruiker de vaste EUR 13,00 behouden, een ander vast bedrag instellen of
teruggaan naar de toepasselijke procentuele berekening. Alleen die keuze
wijzigt de prijswijze of de vaste prijs; het signaal doet dit niet zelfstandig.

<a id="ac-prijzen-028"></a>

### De groep blijft gekoppeld bij een vaste verkoopprijs

Gegeven een product bij A met groep G van 30 procent en inkoopprijs EUR 10,00,
blijft G gekoppeld nadat de gebruiker vaste verkoopprijs EUR 13,00 instelt.
Na wijziging van G naar 40 procent gebruikt Fresh G voor de vergelijkingsprijs
EUR 14,00; de gebruikte verkoopprijs blijft EUR 13,00.

<a id="ac-prijzen-029"></a>

### Terugschakelen gebruikt de bewaarde groep met actuele gegevens

Gegeven een product bij A met vaste verkoopprijs EUR 13,00, bewaarde groep G
met actueel 40 procent en actuele inkoopprijs EUR 10,00, geeft bewust
terugschakelen naar procentuele berekening EUR 14,00 verkoopprijs. Fresh
vraagt niet opnieuw om een groep te kiezen.

<a id="ac-prijzen-030"></a>

### Een bewust behouden vaste prijs geeft geen herhaalde melding

Gegeven vaste prijs EUR 13,00 en berekende prijs EUR 14,00 bij product P van
leverancier A, verdwijnt het aandachtspunt wanneer de gebruiker de vaste prijs
behoudt. Bij ongewijzigde vaste prijs geven berekende prijzen van EUR 14,00 of
lager geen nieuwe melding, ook niet na een daling en terugkeer naar EUR 14,00.

<a id="ac-prijzen-031"></a>

### Verdere stijging vraagt opnieuw aandacht

Gegeven een bewust behouden vaste prijs EUR 13,00 bij een beoordeelde berekende
prijs EUR 14,00, verschijnt opnieuw een aandachtspunt als de berekende prijs
EUR 14,50 wordt. Behoudt de gebruiker opnieuw EUR 13,00, dan wordt EUR 14,50 de
nieuwe beoordelingsgrens. De vaste verkoopprijs blijft EUR 13,00.

<a id="ac-prijzen-032"></a>

### Zonder groep levert de leveranciersstandaard de vergelijkingsprijs

Gegeven een product bij A zonder margegroep, met inkoopprijs EUR 10,00, vaste
verkoopprijs EUR 13,00 en leveranciersstandaard 40 procent, is de vergelijkingsprijs
EUR 14,00. Zonder eerdere behoudkeuze toont Fresh het aandachtspunt van EUR 1,00;
de gebruikte verkoopprijs blijft EUR 13,00.

<a id="ac-prijzen-033"></a>

### Terugschakelen zonder groep gebruikt de leveranciersstandaard

Gegeven een product bij A zonder margegroep, met vaste verkoopprijs EUR 13,00,
actuele inkoopprijs EUR 10,00 en actuele leveranciersstandaard 40 procent,
geeft bewust terugschakelen naar procentuele berekening EUR 14,00 verkoopprijs.
Een margegroeptoewijzing is hiervoor niet nodig.

<a id="ac-prijzen-034"></a>

### Een gewijzigde leveranciersstandaard herberekent standaardprijzen

Gegeven een product bij A met inkoopprijs EUR 10,00, zonder eigen groep of
vaste prijs, wordt de verkoopprijs automatisch EUR 13,50 wanneer de
leveranciersstandaard van 30 naar 35 procent wijzigt.

<a id="ac-prijzen-035"></a>

### Een leverancierswijziging verdringt een eigen groep niet

Gegeven een product bij A met inkoopprijs EUR 10,00 en eigen groep G van
40 procent, blijft G leidend wanneer de leveranciersstandaard van 30 naar
35 procent wijzigt. De procentuele prijs blijft EUR 14,00; bij een vaste prijs
blijft de vergelijkingsprijs op basis van G eveneens EUR 14,00.

<a id="ac-prijzen-036"></a>

### Een leverancierswijziging actualiseert de vergelijking zonder vaste prijs te wijzigen

Gegeven een product bij A zonder groep, met inkoopprijs EUR 10,00 en vaste
verkoopprijs EUR 13,00, wordt de vergelijkingsprijs EUR 13,50 als de
leveranciersstandaard van 30 naar 35 procent wijzigt. Zonder eerdere behoudkeuze
verschijnt een aandachtspunt met EUR 0,50 verschil. De verkoopprijs blijft EUR 13,00.

<a id="ac-prijzen-037"></a>

### De gekozen afrondingsstaffel is instelbaar

Gegeven de prijsinstellingen, is de beginstaffel zichtbaar met stappen van
EUR 0,01 onder EUR 1,00, EUR 0,05 vanaf EUR 1,00 tot en met EUR 10,00 en
EUR 0,25 boven EUR 10,00. De gebruiker kan de staffel via de instellingen
aanpassen. Het toepassen bij herberekening volgt de nog te bepalen afrondingsregels.

## Open keuzes

Beheer van de standaardmarge (los percentage of margegroep) en gedrag bij
ontbrekende standaardmarge moeten nog worden bepaald. Concrete
verkoopfilters, combinatie met actueel aanbod en leveranciersbereik van een
hoofdstukactie blijven open. Automatische uitbreiding van een handmatige
selectie is niet gekozen; voorraad zonder individuele regel valt onder de
leveranciersstandaard. Herkenning van bestaande productinstellingen bij nieuwe
imports vraagt nog uitwerking.
Gedrag bij geen
kandidaat of een nog open keuze, behoudkeuzes na wijzigingen van vaste prijs of prijswijze,
afrondingsrichting, grens- en middelpuntgedrag, toepassing op vaste prijzen en
doorwerking van gewijzigde afrondingsinstellingen,
de basis van bedragen (zoals belasting en bijkomende kosten), ontbrekende
inkoopprijzen en de hierboven genoemde ketengevolgen worden uitgewerkt in
[issue #6](https://github.com/MenkehorstKwekerijen/Fresh/issues/6).
