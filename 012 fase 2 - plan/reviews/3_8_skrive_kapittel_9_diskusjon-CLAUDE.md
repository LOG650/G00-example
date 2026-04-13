# Review av aktivitet 3.8 – «Skrive kapittel 9 Diskusjon»

**Reviewer:** CLAUDE
**Dato:** 2026-04-13
**Aktivitetsmappe:** Ingen dedikert mappe. Artefakter gjenbrukt fra `006 analysis/aktiviteter/3_4_lage_prognose_og_anbefalinger/`
**Planreferanse:** Aktivitet ACT-3.8, planlagt 2026-04-10 til 2026-04-15

---

## Sammendrag

Kapittel 9 Diskusjon er ferdigskrevet med seks seksjoner (9.1–9.6), to tabeller (Tabell 9.1 og 9.2) og én figur (Figur 9.1). Kapittelet drøfter modellvalg, residualdiagnostikk, prognoseevne og bias, kapasitetsimplikasjoner, begrensninger og samlet vurdering opp mot problemstillingen. Alle fire forbedringsforslag (F1–F4) fra ACT-3.4-reviewen er innarbeidet. Kapitlet holder jevnt over god faglig kvalitet med klar struktur og et reflektert språk. Reviewen identifiserer 5 styrker, 2 svakheter og 4 forbedringsforslag.

---

## Styrker

- **S1.** Kapitlet har en gjennomtenkt disposisjon der hver seksjon bygger logisk på de foregående. Progresjonen fra modellvalg (9.1), via diagnostikk (9.2) og empirisk ytelse (9.3), til praktiske implikasjoner (9.4), begrensninger (9.5) og samlet vurdering (9.6) gir leseren en naturlig oppbygging.
- **S2.** Diskusjonen av biaskorreksjon i seksjon 9.3 er faglig presis og viser god forståelse. Argumentasjonen for at medianprognosen forsvares som pragmatisk tilnærming fordi biaskorreksjon ville forsterket den positive nivåbiasen, er overbevisende og nyansert. Horisontavhengig varians (F1 fra ACT-3.4) er kommentert med konkrete tall (0.6 % til 0.8 %).
- **S3.** Seksjon 9.5 Begrensninger er forbilledlig i sin bredde og ærlighet. Den dekker seks begrensninger — univariat tilnærming, historisk analyseperiode, trendekstrapolering, residualdiagnostikk, modellomfang og statisk prognose — uten å overdramatisere eller bagatellisere.
- **S4.** Alle fire forbedringsforslag fra ACT-3.4-reviewen er innarbeidet på en relevant måte: F1 i seksjon 9.3 (biaskorreksjon med horisontavhengig varians), F2 som Tabell 9.1 (refittet parametertabell), F3 som Tabell 9.2 (kapasitetsplanleggingstabell med sesongkategorisering) og F4 som Figur 9.1 (helhetsfigur).
- **S5.** Tallene i Tabell 9.1 og 9.2 er verifisert mot artefaktene (`tab_01_modellparametere_refittet.csv` og `tab_04_kapasitetsplanlegging.csv`) og stemmer eksakt. Konsistensen mellom genererte artefakter og rapporttekst er gjennomgående god.

---

## Del 1 – Metodikk (beregninger og kode)

### 1.1 Tabell 9.1 – Refittede parametere

Tabell 9.1 viser de refittede parameterne for SARIMA$(0,1,1)(0,1,1)_{12}$ estimert på hele datasettet. Verdiene er sammenlignet med `tab_01_modellparametere_refittet.csv`:

| Parameter | Rapport | Artefakt | Stemmer |
|:----------|--------:|---------:|:--------|
| $\theta_1$ | -0.8215 | -0.821528 | Ja (avrundet) |
| SE($\theta_1$) | 0.0240 | 0.023955 | Ja (avrundet) |
| $\Theta_1$ | -0.6228 | -0.622829 | Ja (avrundet) |
| $\sigma^2$ | 0.0115 | 0.011536 | Ja (avrundet) |

**Vurdering:** Korrekt og konsistent. Avrundingen er passende for rapportformatet.

### 1.2 Tabell 9.2 – Kapasitetsplanlegging

Tabell 9.2 er sammenlignet med `tab_04_kapasitetsplanlegging.csv`. Alle 12 rader med punktprognoser, prediksjonsintervall og sesongkategorier stemmer eksakt. Sesongkategoriseringen er den reviderte, dataforankrede versjonen fra V2-fiksen i ACT-3.4.

**Vurdering:** Korrekt og konsistent.

### 1.3 Figur 9.1 – Helhetsfigur

Figuren er generert av `03_helhetsfigur.py` i ACT-3.4-mappen. Skriptet laster hele tidsserien (210 observasjoner) og 12-måneders prognosen, og produserer en figur med historisk salg, prognosekurve og 95 % prediksjonsintervall. Koden er lesbar og reproduserbar.

**Vurdering:** Korrekt. Figuren gir god visuell kontekst for diskusjonen i seksjon 9.5.

### 1.4 Kryssreferanser til andre kapitler

Kapittel 9 refererer til resultater fra kapittel 7.2 (Tabell 7.2, modellkandidater), 7.3 (Tabell 7.3, treningsestimater), 7.4 (residualdiagnostikk), 8.1 (testsettvalidering), 8.2 (prognoseresultater), 4.4 (sesongvariasjon i casebeskrivelsen) og 1.1 (problemstilling). Alle disse kryssreferansene er verifisert som korrekte — de refererte tabellene, figurene og seksjonene finnes i rapporten.

**Vurdering:** Alle kryssreferanser er korrekte.

### 1.5 Kravoppfyllelse

| Krav | Relevant del av kap. 9 | Status |
|:-----|:----------------------|:-------|
| REQ-004 (validering) | Seksjon 9.2 drøfter residualdiagnostikk; seksjon 9.3 drøfter prognosekvalitet | Oppfylt |
| REQ-005 (logistisk tolkning) | Seksjon 9.4 oversetter prognosen til kapasitetsplanlegging | Oppfylt |
| REQ-006 (norsk fagspråk) | Hele kapitlet bruker norsk fagterminologi konsekvent | Oppfylt |
| REQ-008 (reproduserbarhet) | Tabeller og figur er sporbare til artefakter | Oppfylt |

**Vurdering:** Alle relevante krav er oppfylt gjennom diskusjonskapitlet.

### Gjenstående metodiske observasjoner

- Kapittel 9 er et rendyrket skrivekapittel uten ny analyse. Det er ingen nye skript, modellkjøringer eller beregninger utover det som allerede ble produsert i ACT-3.4. Tabellene og figuren i kapittel 9 gjenbruker eksisterende artefakter, noe som er faglig korrekt.

---

## Del 2 – Språk, innhold og figurer

### 2.1 Rapporttekst – kapittel 9

**Språk:** Godt norsk fagspråk gjennom hele kapitlet. Setningene er klare og varierer i lengde. Fagbegreper brukes presist (parsimoni, heteroskedastisitet, biaskorreksjon, innovasjonsvarians). Ingen skrivefeil identifisert.

**Faglig innhold:** Kapitlet er faglig solid og veldisponert. Særlig sterke avsnitt er drøftingen av biaskorreksjon i 9.3 og begrensningskapitlet i 9.5.

Én innholdsmessig observasjon: Seksjon 9.6 oppsummerer problemstillingen som «to spørsmål», men problemstillingen i 1.1 er formulert som ett sammensatt spørsmål med tre delproblemer (1.2). Det tredje delspørsmålet (implikasjoner for kapasitetsplanlegging) nevnes i 9.4 men omtales ikke eksplisitt i den samlede vurderingen 9.6. Se V1.

### 2.2 Figurer – rapportklarhet

| Figur | Tittel i figur | Vurdering |
|:------|:---------------|:----------|
| 9.1 | «Historisk salg og 12-måneders prognose for SARIMA(0,1,1)(0,1,1)₁₂» | Figuren er lesbar med gode farger og norske aksetitler. Den viser hele tidsserien fra 1964, noe som gir verdifull kontekst. Figurformatet følger CLAUDE.md-standarden (sentrert, 80 %, figurtekst). |

Figurteksten er informativ: «Figur 9.1 Historisk månedlig traktorsalg (1964–1981) og 12-måneders prognose med 95 % prediksjonsintervall.» Den følger prosjektets figurstandard.

### 2.3 Tabeller – konsistens og lesbarhet

**Tabell 9.1 (refittede parametere):** Ryddig og konsistent. Kolonneoverskrifter er klare. Tallene bruker punktum som desimaltegn, som er akseptabelt i teknisk sammenheng. Tabellen har korrekt tabelltekst under.

**Tabell 9.2 (kapasitetsplanlegging):** Godt presentert med mellomrom som tusenskilletegn. Sesongkategorier er tydelige. Tabellen har introduksjonssetning i brødteksten og tabelltekst under.

Én observasjon: Tabell 9.2 gjentar punktprognoser og prediksjonsintervall fra Tabell 8.2. Forskjellen er tilleggskolonnen med sesongkategori. Repetisjon av alle tallene gjør at to tabeller i rapporten inneholder nesten identisk informasjon. Se F1.

### 2.4 Funn fra andre reviewer

| # | Funn | Alvorlighetsgrad | Status | Tilhører denne aktiviteten? |
|:--|:-----|:-----------------|:-------|:----------------------------|
| F1 | Nyansere biaskorreksjon med horisontavhengig varians (ACT-3.4) | Lav | Lukket | Ja – innarbeidet i seksjon 9.3 |
| F2 | Vurdere refittet parametertabell (ACT-3.4) | Lav | Lukket | Ja – innarbeidet som Tabell 9.1 |
| F3 | Vurdere oppsummeringstabeller i rapport (ACT-3.4) | Lav | Lukket | Ja – innarbeidet som Tabell 9.2 |
| F4 | Vurdere helhetsfigur med hele tidsserien (ACT-3.4) | Lav | Lukket | Ja – innarbeidet som Figur 9.1 |

Alle fire forbedringsforslag fra ACT-3.4-reviewen er implementert og kan lukkes.

### 2.5 Strukturell observasjon – manglende litteraturreferanser

Diskusjonskapitlet nevner «airline-modellen» (seksjon 9.1, 9.2) uten å referere til Box et al. (2015) som introduserte den. Kapitlet drøfter diagnostiske tester (Ljung-Box, Jarque-Bera, ARCH-LM) uten kildehenvisninger, selv om disse er oppgitt i kapittel 7.4. Det nevnes heller ingen litteratur for å støtte påstandene om at residualbrudd er vanlige for reelle økonomiske tidsserier. En diskusjon bør normalt forankre sine vurderinger i litteraturen. Se V2.

---

## Svakheter og forbedringsforslag

### V1. Seksjon 9.6 dekker ikke alle tre delproblemer eksplisitt

**Alvorlighetsgrad:** Middels
**Kategori:** Språk og innhold

Seksjon 9.6 oppsummerer problemstillingen som «to spørsmål» (hvordan modellere og i hvilken grad modellen gir beslutningsgrunnlag), men problemstillingen i 1.2 har tre delproblemer: (1) mønstre i trend og sesong, (2) modellspesifikasjon og ytelse, (3) implikasjoner for produksjon og lager. Delspørsmål 3 er grundig behandlet i seksjon 9.4, men den samlede vurderingen i 9.6 inkluderer det bare implisitt via formuleringen «kapasitetsplanlegging». For fullstendighetens skyld bør enten seksjon 9.6 eksplisitt nevne alle tre delproblemer, eller teksten bør tydeliggjøre at de to spørsmålene i 9.6 samler opp de tre delspørsmålene fra 1.2.

### V2. Diskusjonskapitlet mangler litteraturreferanser

**Alvorlighetsgrad:** Middels
**Kategori:** Språk og innhold

Kapittel 9 inneholder ingen eksplisitte kildehenvisninger, til tross for at det drøfter faglige begreper (airline-modellen, parsimoni, informasjonskriterier) og gjør påstander om hva som er «vanlig» for reelle tidsserier. Prosjektets rapportsjekkliste i CLAUDE.md sier at diskusjonskapitlet skal knytte funn til litteratur. Minst følgende steder bør ha referanser:
- Seksjon 9.1: «airline-modellen» bør referere til Box et al. (2015)
- Seksjon 9.2: Påstanden om at residualbrudd «ikke er uvanlige» bør underbygges
- Seksjon 9.3: Biaskorreksjon med $\exp(\mu + \sigma^2/2)$ bør referere til relevant kilde
- Seksjon 9.5: Nevning av ETS og GARCH som alternativer bør refereres

### F1. Tabell 9.2 gjentar innholdet i Tabell 8.2

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Tabell 9.2 inneholder punktprognoser og prediksjonsintervall som er identiske med Tabell 8.2, pluss sesongkategori-kolonnen. En mer kompakt løsning kan være å kun vise sesongkategoriene som en enkel tilleggstabell eller å referere til Tabell 8.2 for de numeriske verdiene og bare tilføye sesongkategoriene.

### F2. Seksjon 9.4 kan styrkes med konkrete handlingsanbefalinger

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Seksjon 9.4 drøfter kapasitetsimplikasjoner på et overordnet nivå, men gir ingen spesifikke handlingsanbefalinger for PowerHorse. For eksempel nevnes det at «bedriften må bygge opp lager i forkant av høysesongen», men det konkretiseres ikke når oppbyggingen bør starte eller i hvilket omfang. Et kort avsnitt med mer spesifikke anbefalinger knyttet til prognosetallene ville styrke det praktiske bidraget.

### F3. Figur 9.1 er plassert i seksjon 9.5 (Begrensninger) men tjener hele kapitlet

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Figur 9.1 (helhetsfigur) er plassert i slutten av seksjon 9.5 Begrensninger, men den illustrerer modellens utgangspunkt og er relevant for hele diskusjonen. Figuren kunne hatt en mer naturlig plassering i seksjon 9.1 (modellvalg) eller i innledningen til kapittel 9, der den ville sette kontekst for alle de påfølgende drøftingene.

### F4. Innholdsfortegnelsen har en gjenværende parentesbemerkning

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Innholdsfortegnelsen viser «5. Metode og data (kan splittes i to)», og selve kapitteloverskriften i rapporten lyder «## 5 Metode og data (kan splittes i to)». Parentesbemerkningen er et internt notat og bør fjernes før endelig innlevering. Selv om dette strengt tatt ikke hører til ACT-3.8, ble det oppdaget under kryssreferansesjekk av kapittel 9 og bør noteres for ACT-3.10.

---

## Avhukningsliste – tiltak

| # | Tiltak | Kategori | Status | Kommentar |
|:--|:-------|:---------|:-------|:----------|
| V1 | Tydeliggjøre koblingen mellom 9.6 og de tre delspørsmålene i 1.2 | Språk og innhold | [x] | Seksjon 9.6 omskrevet til tre delspørsmål |
| V2 | Legge inn litteraturreferanser i diskusjonskapitlet | Språk og innhold | [x] | Referanser lagt inn i 9.1, 9.2, 9.3 og 9.5 |
| F1 | Vurdere å redusere overlapp mellom Tabell 9.2 og 8.2 | Språk og innhold | [x] | Tabell 9.2 komprimert, refererer til Tabell 8.2 |
| F2 | Vurdere mer konkrete handlingsanbefalinger i seksjon 9.4 | Språk og innhold | [x] | Konkrete tall for lageroppbygging lagt til |
| F3 | Vurdere å flytte Figur 9.1 til innledning av kap. 9 eller seksjon 9.1 | Språk og innhold | [x] | Figur 9.1 flyttet til innledning av kap. 9 |
| F4 | Fjerne parentesbemerkningen «(kan splittes i to)» fra kap. 5 | Språk og innhold | [x] | Fjernet fra overskrift og innholdsfortegnelse |

---

## Samsvar med prosjektplan og krav

| Sjekkpunkt | Status | Kommentar |
|:---|:---|:---|
| Drøfte funn opp mot problemstilling og litteratur | Delvis | Problemstilling er godt dekket. Litteraturkoblingen mangler (V2) |
| Drøfte log-transformasjon og manglende bias-korreksjon | OK | Grundig drøftet i seksjon 9.3 med horisontavhengig varians |
| Vurdere begrensninger og praktiske implikasjoner | OK | Seks begrensninger i 9.5 og kapasitetsplanlegging i 9.4 |
| Innarbeide F1 fra ACT-3.4 (biaskorreksjon med horisontavhengig varians) | OK | Innarbeidet i seksjon 9.3 |
| Innarbeide F2 fra ACT-3.4 (refittet parametertabell) | OK | Innarbeidet som Tabell 9.1 i seksjon 9.1 |
| Innarbeide F3 fra ACT-3.4 (oppsummeringstabeller) | OK | Innarbeidet som Tabell 9.2 i seksjon 9.4 |
| Innarbeide F4 fra ACT-3.4 (helhetsfigur) | OK | Innarbeidet som Figur 9.1 i seksjon 9.5 |
| ACT-3.8-C01 (kapittel ferdigskrevet) | OK | Seks seksjoner, to tabeller, én figur |
| ACT-3.8-C02 (review gjennomført) | Pågår | Denne reviewen |

---

## Samlet vurdering

### Metodikk

Det er ingen nye beregninger i ACT-3.8 — kapitlet gjenbruker artefakter fra ACT-3.4. Tallmessig konsistens mellom artefakter og rapporttekst er verifisert for begge tabeller og figuren. Alle kryssreferanser til andre kapitler er kontrollert og funnet korrekte. Kriteriene i prosjektplanen (ACT-3.8-C01) er oppfylt.

### Språk, innhold og figurer

Kapitlet er velskrevet med et reflektert og presist fagspråk. Strukturen følger en logisk progresjon og gir leseren god oversikt over modellens styrker og begrensninger. De to svakhetene som er identifisert — ufullstendig dekning av alle delproblemer i den samlede vurderingen (V1) og manglende litteraturreferanser (V2) — er begge av middels alvorlighetsgrad. V1 er rask å fikse. V2 henger sammen med at kapittel 2 Litteratur (ACT-3.6) ikke er skrevet ennå; det kan likevel legges inn referanser til kilder som allerede finnes i kapittel 11.

### Anbefalt prioritering videre

1. **(Bør)** V1 – Tydeliggjøre koblingen mellom seksjon 9.6 og de tre delspørsmålene fra 1.2.
2. **(Bør)** V2 – Legge inn litteraturreferanser i diskusjonskapitlet, i det minste for airline-modellen (Box et al., 2015).
3. **(Kan)** F3 – Vurdere å flytte Figur 9.1 til en mer sentral plassering i kapitlet.
4. **(Kan)** F1 – Vurdere å redusere overlapp mellom Tabell 9.2 og 8.2.
5. **(Kan)** F2 – Vurdere mer spesifikke handlingsanbefalinger i seksjon 9.4.
6. **(Kan)** F4 – Overføre parentesbemerkning-fiks for kap. 5 til ACT-3.10.
