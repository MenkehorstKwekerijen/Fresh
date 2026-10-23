---
id: prijzen
status: draft
depends_on: []
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

Bij een vaste verkoopprijs is het expliciet ingestelde bedrag de verkoopprijs.
Een brutomargepercentage over de verkoopprijs is niet als prijswijze gekozen.
Hoe beide gekozen prijswijzen in de margegroep of op het product worden
vastgelegd, is nog te bepalen; de wens voor een vaste verkoopprijs blijft gelden.

### Standaardmarge per leverancier

Bij het inlezen van voorraadlijsten in Fresh wordt de ingestelde standaardmarge
van de betreffende leverancier toegepast op diens inkoopprijzen. Bijvoorbeeld:
zonder afwijkende productinstellingen geeft EUR 10,00 inkoop bij leverancier A
met 30 procent opslag een berekende verkoopprijs van EUR 13,00. Hetzelfde
product met EUR 10,00 inkoop bij leverancier B met 40 procent opslag geeft
EUR 14,00. De leveranciersinstelling van A geldt niet voor B.

De standaardmarge en een expliciet gekozen margegroep zijn onderscheiden
instellingen. Of een productgroep de standaardmarge vervangt, en of de
standaardmarge zelf als margegroep wordt beheerd, moet nog worden besloten.
Er wordt geen optelling of andere combinatie van marges aangenomen.

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
groepen bij verschillende leveranciers zijn geen conflict. De eerdere
voorrangsvolgorde product, leverancier, hoofdstuk geldt niet. De verhouding
tot de standaardmarge moet nog worden bepaald.

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

Deze afspraak gaat over het wijzigen van expliciete groepstoewijzingen. Wat er
gebeurt als de standaardmarge of de prijsinstellingen binnen een al gekoppelde
margegroep wijzigen, is nog open.

## Keten en herstel

De leveranciersberekening gebruikt de inkoopprijs van de betreffende leverancier.
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

## Open keuzes

De verhouding tussen standaardmarge en expliciete margegroep, beheer van de
standaardmarge (los percentage of margegroep), herberekening na wijzigingen en
gedrag bij ontbrekende standaardmarge moeten nog worden bepaald. Concrete
verkoopfilters, combinatie met actueel aanbod en leveranciersbereik van een
hoofdstukactie blijven open. Automatische uitbreiding van een handmatige
selectie is niet gekozen; nieuwe voorraad valt onder de leveranciersstandaard,
waarbij samenloop met bestaande productinstellingen nog uitwerking vraagt.
Inhoud van margegroepen en de plaats van vaste verkoopprijzen, gedrag bij geen
kandidaat of een nog open keuze, gevolgen van gewijzigde groepsinhoud, afronding,
de basis van bedragen (zoals belasting en bijkomende kosten), ontbrekende
inkoopprijzen en de hierboven genoemde ketengevolgen worden uitgewerkt in
[issue #6](https://github.com/MenkehorstKwekerijen/Fresh/issues/6).
