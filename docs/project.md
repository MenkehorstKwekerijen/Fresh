# Productbasis van Fresh

Dit document bezit productdoel, gebruikers, scope en algemene kwaliteitseisen.
Het bevat de eerste gebruikersbesluiten uit [issue #4](https://github.com/MenkehorstKwekerijen/Fresh/issues/4).
Open keuzes zijn nog geen productregels of bouwopdrachten.

## Doel

Fresh moet [externe fictieve voorraad](glossary.md#term-externe-fictieve-voorraad)
efficiënt en snel kunnen inlezen, marges laten bepalen en uitvoer leveren voor
[WinTree](glossary.md#term-wintree).

Daarnaast moet Fresh voorraadgegevens en historische verkoopgegevens gebruiken
om leveranciersvoorkeuren te bepalen en keuzes en analyses voor het assortiment
van de online catalogus te ondersteunen. De gegevensbronnen en afnemers staan
in het [ketenoverzicht](architecture/overview.md).

Herhaaldelijke menselijke keuzes moeten slim worden geautomatiseerd. De aandacht
van de gebruiker moet uitgaan naar aandachtspunten en noodzakelijke controles.
Welke keuzes automatisch mogen worden uitgevoerd, vraagt concrete afspraken;
er is nog geen algoritme of leertechniek gekozen.

## Gebruikers en gebruik

| Werkzaamheid | Gebruiker |
| --- | --- |
| Voorraad inlezen | De persoon die voorraadbestanden verwerkt |
| Marges en import in WinTree controleren | De inkoper |
| Commerciële keuzes voor het websiteassortiment maken | De assortimentsbeheerder |

Meerdere mensen moeten gelijktijdig acties kunnen uitvoeren: ongeveer drie tot
vier wijzigende gebruikers, met daarnaast gebruikers die alleen lezen. Deze
werkzaamheden leggen nog geen accounts, autorisaties of goedkeuringsstappen vast.

## Eerste bruikbare versie

De gebruiker heeft de volgende werkzaamheden genoemd:

- Leveranciersbestanden en overige voorraadbronnen inlezen.
- Externe fictieve voorraad omzetten naar de naamcodes en maatcodes uit de
  [WinTree-basisstam](glossary.md#term-wintree-basisstam), zodat deze voorraad
  later snel in WinTree kan worden ingelezen.
- Leveranciersvoorkeuren vastleggen.
- [Prijsinstellingen](specs/prijzen.md) voor opslag op inkoop en vaste
  verkoopprijzen vastleggen; margegroepen aanmaken en toewijzen voor individuele
  producten, zelf geselecteerde producten binnen een leverancier en hele
  catalogushoofdstukken, ook met een bulkactie. Bij de leveranciersselectie
  gebruikt de gebruiker filters op actueel fictief/TCM-aanbod en verkoopgeschiedenis.
  Uitgangspunt is één actieve margegroep per product; de reikwijdte bij hetzelfde
  product van meerdere leveranciers vraagt nog verduidelijking.
  Verschillende kandidaten vragen een eenmalige keuze. Een gekozen groep blijft
  gekoppeld; gewijzigde toewijzingsregels vragen expliciete herbeoordeling van
  bestaande producten.
- [Catalogusbeheer](glossary.md#term-catalogusbeheer): producten en hun gegevens
  beheren, inclusief hun weergave op de website, hoofdstukken, Duitse en Engelse
  vertalingen en filters.
- Productupdates via Excel-lijsten verwerken en afzonderlijke producten toevoegen.
- Catalogusgegevens via CSV aan de website overdragen, aansluitend op de huidige
  importwerkwijze van de website. Een API-koppeling volgt als latere uitbreiding.

Export naar WinTree hoort bij het productdoel. De exacte exportafspraak en de
inhoud en verwerking van de website-CSV's moeten nog worden uitgewerkt. Ook de
eerste oplevering van verkoopanalyse en automatisering en overige uitgestelde
functies zijn nog niet afgebakend.

## Algemene kwaliteitseisen

- Inlezen en dagelijks werk moeten efficiënt en snel verlopen. Aantallen en
  meetbare responstijden worden bepaald met representatieve werkvoorbeelden.
- Gelijktijdig werken moet worden ondersteund; conflictgedrag wordt gespecificeerd
  voordat gedeelde gegevens kunnen worden gewijzigd.
- Terugkerend handwerk moet afnemen, met gerichte aandacht voor noodzakelijke
  menselijke keuzes en controles.

Technische voorstellen staan bij de [architectuurkeuzes](architecture/overview.md#technische-richting).
Open productvragen en besluiten worden behandeld in
[issue #4](https://github.com/MenkehorstKwekerijen/Fresh/issues/4).
