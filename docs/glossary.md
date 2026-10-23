# Bedrijfsbegrippen

Deze glossary bezit de besloten betekenis van bedrijfsbegrippen in Fresh.
De eerste definities komen uit de gebruikersantwoorden vastgelegd in
[issue #4](https://github.com/MenkehorstKwekerijen/Fresh/issues/4).
Prijsbegrippen worden verder besloten in
[issue #6](https://github.com/MenkehorstKwekerijen/Fresh/issues/6).
Verwerkingsregels en berekeningen horen in productspecificaties.

## Externe fictieve voorraad

<a id="term-externe-fictieve-voorraad"></a>

Externe voorraad waarvan leveranciers periodiek Excel- of CSV-bestanden
aanleveren. Het aanleverritme verschilt per leverancier, bijvoorbeeld wekelijks
of tweewekelijks.

De bronvermelding "inkoop aanbieding" duidt op deze fictieve voorraad.

## Eigen voorraad

<a id="term-eigen-voorraad"></a>

Bomen of struiken in pot van de eigen containervelden en kluitplanten van de
eigen percelen.

## Eigen externe voorraad

<a id="term-eigen-externe-voorraad"></a>

Voorraad die al is ingekocht maar nog bij een leverancier staat, bijvoorbeeld
reeds gekochte bomen.

## TCM-voorraad

<a id="term-tcm-voorraad"></a>

Voorraad die automatisch via WinTree wordt ontvangen met TreeCommerce Messenger
(TCM). De route van WinTree naar Fresh staat in het
[ketenoverzicht](architecture/overview.md#inkomende-gegevens).

## Voorraaddatum

<a id="term-voorraaddatum"></a>

De datum waarmee Fresh de actualiteit van een voorraadbron vergelijkt. De
herkomst verschilt tussen fictief en TCM en is vastgelegd in de
[specificatie voorraadimport](specs/voorraadimport.md#leveranciers-en-mogelijke-dubbele-aanlevering).

## Importdatum

<a id="term-importdatum"></a>

De datum waarop een bestand via de importeerfunctie van Fresh wordt ingelezen.

## Kolomtoewijzing

<a id="term-kolomtoewijzing"></a>

Het koppelen van kolommen uit een importbestand aan de gegevens die Fresh
verwacht, zoals plantnaam, maat en inkoopprijs. Ook kolommapping genoemd.
Het importgedrag staat in de
[voorraadimportspecificatie](specs/voorraadimport.md#kolomtoewijzing-in-stap-2).

## WinTree

<a id="term-wintree"></a>

Het ERP van de organisatie. WinTree is de bestemming voor de beoogde
voorraadexport en het systeem waarlangs TCM-voorraad wordt ontvangen.

## Inkoperscontrole

<a id="term-inkoperscontrole"></a>

De beoordeling door de inkoper vóór vrijgave van de WinTree-export, waarbij
de inkoper ook regels kan uitsluiten. Het gedrag staat in de
[exportspecificatie](specs/wintree-export.md).

## Uitsluiten van WinTree-export

<a id="term-uitsluiten-wintree-export"></a>

De bewuste keuze om een regel niet mee te nemen in de WinTree-export.
Dit begrip bepaalt op zichzelf niet of de regel in Fresh als voorraad beschikbaar
blijft. De toepassing staat in de [exportspecificatie](specs/wintree-export.md).

## WinTree-basisstam

<a id="term-wintree-basisstam"></a>

De referentiegegevens in WinTree met naamcodes en maatcodes. Deze codes worden
ook gebruikt door de catalogus en de overige voorraadbronnen naast externe
fictieve voorraad.

## Naamcode

<a id="term-naamcode"></a>

Een code uit de WinTree-basisstam voor een plantnaam.

## Maatcode

<a id="term-maatcode"></a>

Een code uit de WinTree-basisstam voor een maat. Welke kenmerken de maatcode
precies omvat, is nog niet uitgewerkt.

## Opslag op inkoop

<a id="term-opslag-op-inkoop"></a>

Een procentuele verhoging van de inkoopprijs exclusief btw om de verkoopprijs
exclusief btw te bepalen.
Het percentage heeft de inkoopprijs als grondslag. Berekening en voorbeelden
staan in de [prijsspecificatie](specs/prijzen.md).

## Vaste verkoopprijs

<a id="term-vaste-verkoopprijs"></a>

Een afzonderlijk ingesteld verkoopbedrag exclusief btw voor een product bij een leverancier,
in plaats van een verkoopprijs die met een opslagpercentage wordt berekend.
Het toepassingsgedrag staat in de
[prijsspecificatie](specs/prijzen.md).

## Afrondingsstaffel

<a id="term-afrondingsstaffel"></a>

Een instelbare indeling van prijsbereiken met per bereik een afrondingsstap.
De gekozen bedragen en toepassingsregels staan in de
[prijsspecificatie](specs/prijzen.md#instelbare-afrondingsstaffel).

## Standaardmarge van een leverancier

<a id="term-standaardmarge-leverancier"></a>

Het rechtstreeks per leverancier ingestelde opslagpercentage op de inkoopprijs
voor diens ingelezen voorraad. De verhouding tot afzonderlijk toegewezen margegroepen staat in de
[prijsspecificatie](specs/prijzen.md).

## Individuele margeregel

<a id="term-individuele-margeregel"></a>

Een expliciete prijsinstelling voor een product bij een bepaalde leverancier,
bijvoorbeeld via een toegewezen margegroep. De voorrang op de standaardmarge
van die leverancier staat in de [prijsspecificatie](specs/prijzen.md).

## Margegroep

<a id="term-margegroep"></a>

Een groep met een opslagpercentage die aan een product bij een leverancier wordt
gekoppeld. De actieve margegroep is de gekozen groep voor die combinatie. De inhoud en werking
van de toewijzing worden vastgelegd in de
[prijsspecificatie](specs/prijzen.md).

## Kandidaat-margegroep

<a id="term-kandidaat-margegroep"></a>

Een margegroep die bij een toewijzing in aanmerking komt voor een product bij een leverancier,
bijvoorbeeld vanuit een leveranciersselectie of een catalogushoofdstuk.
Een kandidaat is nog geen actieve koppeling.

## Bulkactie

<a id="term-bulkactie"></a>

Eén handeling waarmee dezelfde wijziging op meerdere geselecteerde onderdelen
wordt toegepast.

## Catalogusbeheer

<a id="term-catalogusbeheer"></a>

Het beheren van producten, hun gegevens en hun weergave op de website, inclusief
hoofdstukken, Duitse en Engelse vertalingen en filters. Dit omvat productupdates
via Excel-lijsten en afzonderlijke producten toevoegen. De overdracht naar de
website is een afzonderlijk uit te werken systeemgrens.
