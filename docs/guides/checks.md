# Documentatie controleren

Deze handleiding controleert de procesbasis. Python 3.12 is tooling voor deze
controles en bepaalt niet de toekomstige applicatiestack.

## Lokaal uitvoeren

Voer vanuit de repositoryroot uit, bij voorkeur in een eigen virtuele omgeving:

```sh
python -m pip install -r requirements-docs.txt
python -m unittest discover -s tests -v
python tools/check_docs.py
```

De tests bewijzen onder andere dat ongeldige links en metadata worden afgewezen.
De checker meldt per fout het bestand of de specificatie-ID. Exitcode 0 betekent
dat de structurele controles slagen; andere exitcodes vragen onderzoek.

## Dekking en beperkingen

De checker leest root README/AGENTS, `docs/`, `.agents/skills/` en `.github/`.
Hij gebruikt een Markdown-parser en YAML-parser. Inline-, image- en opgeloste
referentielinks worden gecontroleerd. Voor fragmenten ondersteunt hij kopankers
met gewone tekst/code en expliciete `<a id="kleine-letters"></a>`-ankers.
Gebruik Markdown-links, geen HTML-href-links of dynamische MDX. Codevoorbeelden
worden niet als links geïnterpreteerd. Externe URLs worden niet op bereikbaarheid
gecontroleerd. Bestanden buiten de genoemde scope vereisen uitbreiding van de scan.

Specificaties krijgen ID-, status-, dependency-, cyclus- en criteriumcontroles.
Skillnaam en beschrijving worden gecontroleerd. PR-events controleren aanwezigheid
van de zes ingevulde secties uit het PR-sjabloon. De controle bewijst geen
inhoudelijke volledigheid, autorisatie van een besluit, juiste glossarybetekenis,
uitgevoerde applicatietest of onafhankelijke review. Dat blijft reviewwerk.

## GitHub-beveiliging instellen en bewijzen

De [workflow](../../.github/workflows/docs.yml) draait op PR-wijzigingen, wijzigingen
aan de PR-beschrijving en pushes naar main. Er zijn geen padfilters die een
verplichte controle onbedoeld overslaan. PR-tekst wordt via JSON gelezen en niet
in een shellcommando geïnterpoleerd. De workflow heeft uitsluitend leesrechten.

Na de eerste geslaagde run stelt een repositorybeheerder bescherming van `main`
in: wijzigingen via PR, de daadwerkelijk getoonde `docs-check` als verplichte
statuscheck, en bewust gekozen bypassrechten. Kies een streng actuele branch of
een passende mergecontrole, zodat bewijs bij de samengevoegde code hoort.
Een onafhankelijke agentsreview is niet automatisch een GitHub-approval van een
andere account; stel geen onuitvoerbare reviewervereiste in.

Bewijs de inrichting met een tijdelijke PR met een kapotte link: de check moet
falen en samenvoegen moet geblokkeerd zijn. Herstel de link en controleer groen.
Sluit de proef zonder de fout naar main te brengen. Leg het resultaat op de PR
of het inrichtingsissue vast. Claim bescherming pas na controle van de instelling
en deze proef. Ontbrekende rechten worden als aparte blokkade geregistreerd.

## Leesroute beproeven

Geef een nieuwe agent alleen de checkout en een concrete opdracht: een nieuwe
bedrijfsbetekenis, een bugfix of een wijziging aan documentatie. Laat hem aangeven
welke bron, ontbrekende keuze en controle nodig is. Geef geen verwachte conclusie
mee. Vergelijk de route met de owning afspraken en verbeter alleen gevonden
tekortkomingen. Een geslaagde leesproef bewijst geen automatische skillregistratie
in andere agentclients.
