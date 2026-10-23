# Bedrijfsbegrippen

Deze glossary bezit de besloten betekenis van bedrijfsbegrippen in Fresh.
De eerste definities komen uit de gebruikersantwoorden vastgelegd in
[issue #4](https://github.com/MenkehorstKwekerijen/Fresh/issues/4).
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

## WinTree

<a id="term-wintree"></a>

Het ERP van de organisatie. WinTree is de bestemming voor de beoogde
voorraadexport en het systeem waarlangs TCM-voorraad wordt ontvangen.

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

Een procentuele verhoging van de inkoopprijs om de verkoopprijs te bepalen.
Het percentage heeft de inkoopprijs als grondslag. Berekening en voorbeelden
staan in de [prijsspecificatie](specs/prijzen.md).

## Vaste verkoopprijs

<a id="term-vaste-verkoopprijs"></a>

Een expliciet ingesteld verkoopbedrag, in plaats van een verkoopprijs die met
een opslagpercentage wordt berekend. Het toepassingsgedrag staat in de
[prijsspecificatie](specs/prijzen.md).

## Catalogusbeheer

<a id="term-catalogusbeheer"></a>

Het beheren van producten, hun gegevens en hun weergave op de website, inclusief
hoofdstukken, Duitse en Engelse vertalingen en filters. Dit omvat productupdates
via Excel-lijsten en afzonderlijke producten toevoegen. De overdracht naar de
website is een afzonderlijk uit te werken systeemgrens.
