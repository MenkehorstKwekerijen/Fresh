# Fresh-skillprofiel

Fresh gebruikt twee lokale projectskills, gebaseerd op geselecteerde principes.
Dit is een aangepaste werkwijze, geen ongewijzigde installatie van vier pakketten.
De [bronregistratie](../.agents/sources.json) bewaart de onderzochte upstream
revisies en bestanden. De lokale teksten zijn zelfstandig geformuleerd; zij
roepen geen upstream scripts, agents of verborgen afhankelijkheden aan.

## Selectie en gebruik

| Taak | Lokale ingang | Invloed van bronnen |
| --- | --- | --- |
| Begrippen, nieuwe eisen en ketengedrag | [fresh-spec](../.agents/skills/fresh-spec/SKILL.md) | Superpowers ontwerp; Matt domeinmodellering; l-gevity dependencies; pstack schrijven |
| Uitvoering, diagnose, review en bewijs | [fresh-deliver](../.agents/skills/fresh-deliver/SKILL.md) | Superpowers uitvoering; Matt gedragstests; l-gevity teststrategie; pstack impact en echte appcontrole |

De root [AGENTS.md](../AGENTS.md) wijst expliciet naar de lokale bestanden.
Automatische ontdekking verschilt per agentomgeving. Als de skill niet in de
omgeving verschijnt, leest de agent de gekoppelde SKILL.md rechtstreeks. Test
ontdekking afzonderlijk in iedere gebruikte client; een leesproef bewijst alleen
de lokale leesroute. Download upstream documenten niet opnieuw bij iedere taak.

## Bewuste afwijkingen

- Specificaties staan in de repository. Uitvoeringsplannen en besluiten staan in
  kleine issues; geen dubbele planbestanden, Projects of voortgangsdocumenten.
- Eén uitvoerder en één onafhankelijke eindreview zijn standaard; geen verplichte
  agent per deelstap of integratiebranch voor iedere functie.
- Vragen beperken zich tot beslissingen die uitkomst of moeilijk omkeerbare
  keuzes veranderen. Technische uitvoering gaat door binnen de gegeven opdracht.
- Kleine mechanische wijzigingen krijgen gerichte controles, geen kunstmatig TDD.
- Documentatie en tests blijven risicogericht. Geen verplichte volledige
  requirementsgraaf, formele TLA+-modellen of aparte verificatiecatalogus.
- Pstack-principes voor autonoom werken geven geen toestemming bedrijfsbetekenis
  te raden. Betekenisverschillen gaan terug naar een expliciet gebruikersbesluit.
- Verificatierecepten verwijzen naar criteria. Zij worden pas opgesteld en
  uitgevoerd wanneer een echte applicatieroute bestaat; geen lege verificatieskill.

## Onderhoud

Wijzig het projectprofiel via een PR. Lees gewijzigde upstream bronnen op een
vaste revisie, beoordeel nieuwe dependencies en conflicten en pas uitsluitend de
gekozen lokale werkwijze aan. Werk de bronregistratie mee bij. Geen automatische
upstream updates. Neem bij letterlijke overname ook toepasselijke licenties mee.

Beproef na een verandering aan triggers of leesroute een concrete opdracht in een
nieuwe sessie, zonder gewenste antwoorden mee te geven. Leg bewijs bij de PR.
Een terugkerende fout wordt waar mogelijk een gerichte uitvoerbare controle;
betekenisvragen blijven inhoudelijke review.
