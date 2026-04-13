# Review av aktivitet 3.7 – «Skrive kapittel 3 Teori»

**Reviewer:** Claude (automatisert review)
**Dato:** 2026-04-13
**Aktivitetsmappe:** `006 analysis/aktiviteter/3_7_skrive_teorikapittel/`
**Planreferanse:** Aktivitet ACT-3.7, planlagt 2026-04-10 til 2026-04-15, faktisk ferdig 2026-04-10 (commit 9e3f626)

---

## Sammendrag

Kapittel 3 Teori er et solid og velstrukturert teorikapittel som dekker alle nødvendige konsepter for den etterfølgende SARIMA-analysen: tidsseriedekomponering, stasjonaritet, ARIMA/SARIMA-rammeverket, modellidentifikasjon med ACF/PACF og informasjonskriterier, samt validering og prognoseevaluering med biaskorreksjon. Teksten er faglig presis, godt forankret i anerkjente kilder, og har tydelige fremoverreferanser til metode-, analyse- og diskusjonskapitlene. Fire pedagogiske figurer med syntetiske data illustrerer teorien effektivt. Reviewen identifiserer 7 styrker, 2 svakheter og 5 forbedringsforslag.

---

## Styrker

- **S1.** Kapitlet bygger en klar logisk progresjon fra grunnleggende tidsseriekonsepter (3.1) via stasjonaritet og transformasjoner (3.2) til modellrammeverket (3.3), identifikasjonsverktøy (3.4) og validering (3.5). Hvert avsnitt bygger naturlig videre på det foregående, noe som gir god pedagogisk flyt.
- **S2.** Alle formler og definisjoner er matematisk korrekte. Stasjonaritetsbetingelsene, differensieringsoperatorene, SARIMA-ligningen, Ljung-Box-statistikken, AIC/BIC, feilmålene og biaskorreksjonsformelen er riktig gjengitt med korrekt notasjon.
- **S3.** Fremoverreferansene til kapittel 6.3 (SARIMA-spesifikasjon), 7.1 (stasjonaritetstesting), 7.2 (ACF/PACF-analyse), 8.1 (testsettvalidering) og 9 (diskusjon av biaskorreksjon) er alle verifisert til å peke til eksisterende seksjoner. Dette sikrer at teorikapitlet fungerer som et reelt fundament for resten av rapporten, i tråd med CLAUDE.md sin sjekkliste.
- **S4.** Referansene er faglig solide og dekker feltet godt: tre etablerte lærebøker (Box et al., 2015; Hyndman & Athanasopoulos, 2021; Shumway & Stoffer, 2017) og fem seminalartikler (Dickey & Fuller, 1979; Kwiatkowski et al., 1992; Ljung & Box, 1978; Engle, 1982; Jarque & Bera, 1987). Alle åtte referansene finnes i kapittel 11 Bibliografi med fullstendig APA7-formatering, og alle har tilhørende oppsummeringsfiler i `003 references/`.
- **S5.** De fire figurene er generert med et reproduserbart Python-skript som bruker syntetiske data med fast seed (`np.random.default_rng(42)`). Skriptet er selvforklarende, godt kommentert og kan kjøres fra tomt miljø med standard Python-avhengigheter (numpy, matplotlib, scipy).
- **S6.** Biaskorreksjonsseksjonen (3.5) er et faglig sterkt tilskudd som mange studentrapporter på dette nivået utelater. Forklaringen av Jensens ulikhet, median vs. gjennomsnittsprognose, og den eksplisitte formelen $E[y_{T+h}] = \exp(\hat{z}_{T+h} + \sigma_h^2/2)$ gir et solid grunnlag for diskusjonen i kapittel 9.
- **S7.** Alle figurer følger CLAUDE.md-standarden korrekt: HTML-format med `width="80%"`, sentrert med `<div align="center">`, og figurtekst i sentrert, liten skrift og kursiv.

---

## Del 1 – Metodikk (beregninger og kode)

### 1.1 Matematiske formler og definisjoner

Alle sentrale formler er gjennomgått:

- **Dekomponering** (additiv og multiplikativ): Korrekt. Log-transformasjonens konvertering fra multiplikativ til additiv struktur er riktig forklart.
- **Stasjonaritetsbetingelser** (seksjon 3.2): De tre betingelsene for svak stasjonaritet er korrekt gjengitt etter Shumway & Stoffer (2017).
- **Differensieringsoperatorer**: Forsinkelsesoperatoren $B$ og differensieringsoperatorene $(1-B)$ og $(1-B^s)$ er korrekt definert og illustrert.
- **SARIMA-ligning** (seksjon 3.3): Den kompakte formen $\Phi(B^s)\,\phi(B)\,(1-B)^d(1-B^s)^D y_t = \Theta(B^s)\,\theta(B)\,\varepsilon_t$ er korrekt.
- **ACF/PACF-signaturmønstre** (seksjon 3.4): Beskrivelsen av kutoff- og avfallsmønstre for AR, MA og ARMA er korrekt.
- **AIC/BIC** (seksjon 3.4): Formlene er korrekt gjengitt.
- **Ljung-Box** (seksjon 3.5): Teststatistikken og frihetsgrader ($m - p - q$) er korrekt. Merknad om sesonglag er relevant.
- **Feilmål** (MAE, RMSE, MAPE): Formlene er korrekte.
- **Biaskorreksjon** (seksjon 3.5): Formelen $E[y_{T+h}] = \exp(\hat{z}_{T+h} + \sigma_h^2/2)$ er korrekt utledet fra log-normalfordelingens egenskaper med riktig forklaring via Jensens ulikhet.

**Vurdering:** Ingen feil identifisert i formler eller definisjoner.

### 1.2 Figurgenereringskode – reproduserbarhet

Skriptet `01_generate_theory_figures.py` er gjennomgått:

- Bruker `np.random.default_rng(42)` for reproduserbar generering.
- Alle fire figurer bruker syntetiske data, ingen avhengighet til prosjektdata.
- Avhengigheter (numpy, matplotlib, scipy) er standard.
- Manuell ACF/PACF-beregning (`_compute_acf`, `_compute_pacf`) er korrekt implementert. Durbin-Levinson-algoritmen i `_compute_pacf` er riktig.
- Figurene lagres med `dpi=150`, som gir god oppløsning.

**Vurdering:** Koden er reproduserbar og korrekt. Én mindre observasjon: skriptet bruker `matplotlib.use("Agg")` for headless rendering, men `plt.rcParams.update(...)` etter `use()` er riktig rekkefølge. Ingen feil.

### 1.3 Konsistens mellom figurer og rapporttekst

Alle fire figurer er visuelt kontrollert mot teksten:

| Figur | Tekstreferanse | Konsistens |
|:------|:---------------|:-----------|
| 3.1 | Linje 172: «Figur 3.1 illustrerer prinsippet med en syntetisk tidsserie som er dekomponert i sine tre additive komponenter.» | OK – figuren viser fire paneler: observert serie, trend, sesong og restledd |
| 3.2 | Linje 201: «Figur 3.2 viser effekten av ulike differensieringsstrategier på en syntetisk ikke-stasjonær serie med trend og sesong.» | OK – figuren viser fire paneler med original, ordinær, sesong- og kombinert differensiering |
| 3.3 | Linje 252: «Figur 3.3 illustrerer de karakteristiske mønstrene med syntetiske AR(1)- og MA(1)-prosesser.» | OK – figuren viser fire paneler med ACF og PACF for AR(1) og MA(1) med tydelige kutoff-annoteringer |
| 3.4 | Linje 309: «Figur 3.4 illustrerer forskjellen mellom median og gjennomsnitt for en log-normalfordelt prognose.» | OK – figuren viser log-normalfordeling med markerte median- og gjennomsnittslinjer |

**Vurdering:** God konsistens mellom figurer og tekst. Figurene illustrerer presist det teksten beskriver.

### 1.4 Referanser – faglig kvalitet og sporbarhet

Alle åtte referanser er kontrollert:

| Referanse | I kap. 3 | I kap. 11 | Oppsummering i `003 references/` | PDF i `003 references/` |
|:----------|:---------|:----------|:----------------------------------|:------------------------|
| Box et al. (2015) | Ja (3.3, 3.4) | Ja | `ref_box_et_al_2015.md` | `box_et_al_2015_tsa5.pdf` |
| Hyndman & Athanasopoulos (2021) | Ja (3.1, 3.5) | Ja | `ref_hyndman_athanasopoulos_2021.md` | Nei (open access nettbok) |
| Shumway & Stoffer (2017) | Ja (3.2, 3.3) | Ja | `ref_shumway_stoffer_2017.md` | `shumway_stoffer_2017_tsa4.pdf` |
| Dickey & Fuller (1979) | Ja (3.2) | Ja | `ref_dickey_fuller_1979.md` | Nei |
| Kwiatkowski et al. (1992) | Ja (3.2) | Ja | `ref_kwiatkowski_et_al_1992.md` | `kwiatkowski_et_al_1992_kpss.pdf` |
| Ljung & Box (1978) | Ja (3.5) | Ja | `ref_ljung_box_1978.md` | `ljung_box_1978.pdf` |
| Engle (1982) | Ja (3.5) | Ja | `ref_engle_1982.md` | `engle_1982_arch.pdf` |
| Jarque & Bera (1987) | Ja (3.5) | Ja | `ref_jarque_bera_1987.md` | `jarque_bera_1987_normality.pdf` |

**Vurdering:** Komplett sporbarhet. Alle referanser brukt i kapittel 3 finnes i bibliografien og har oppsummeringsfiler. Hyndman & Athanasopoulos og Dickey & Fuller mangler PDF i `003 references/`, men førstnevnte er en open access-nettbok og sistnevnte er en kort artikkel – dette er akseptabelt.

### Gjenstående metodiske observasjoner

- KPSS-testen (seksjon 3.2) beskrives som å dekomponere serien i «en deterministisk trend, en tilfeldig vandring og et stasjonært feilledd». Dette er en forenklet, men dekkende beskrivelse av testens underliggende modell. For et LOG650-kurs er presisjonsnivået passende.
- Ljung-Box-testens frihetsgrader oppgis som $m - p - q$. Noen lærebøker bruker $m - p - q - P - Q$ for SARIMA-modeller. Formuleringen i teksten er den vanligste og konsistent med Ljung & Box (1978), men det kan diskuteres om sesongparameterne bør trekkes fra. Se F3.

---

## Del 2 – Språk, innhold og figurer

### 2.1 Rapporttekst – Introduksjonsavsnittet (linje 152)

**Språk:** Godt norsk fagspråk. Setningen er lang men velstrukturert og gir en nyttig veikart for kapitlet.

**Faglig innhold:** Introduksjonen ramser opp alle fem seksjonene og kobler dem eksplisitt til «analysemetodene som brukes i kapittel 6 til 8». Dette følger CLAUDE.md sin sjekkliste om at teorikapitlet skal gi «et faktisk grunnlag for metodevalg og tolkning senere i rapporten».

### 2.2 Rapporttekst – Seksjon 3.1 Tidsserier og dekomponering

**Språk:** Klart og pedagogisk. Forklaringen av temporal avhengighet og overgangen fra additiv til multiplikativ modell via log-transformasjon er godt formulert. Riktig bruk av norske fagtermer: «trendkomponent», «sesongkomponent», «restkomponent».

**Faglig innhold:** Solid. Bindeleddet mellom multiplikativ dekomponering og log-transformasjon er elegant og forbereder leseren for seksjon 3.2. Referansen til Hyndman & Athanasopoulos (2021) er passende.

### 2.3 Rapporttekst – Seksjon 3.2 Stasjonaritet og transformasjoner

**Språk:** Godt. Differensieringsformuleringene med forsinkelsesoperatoren er presist formulert. ADF- og KPSS-beskrivelsene er korte og dekkende.

**Faglig innhold:** Solid. Komplementariteten mellom ADF (nullhypotese: enhetsrot) og KPSS (nullhypotese: stasjonaritet) er tydelig forklart. Fremoverreferansen til kapittel 7.1 er verifisert.

### 2.4 Rapporttekst – Seksjon 3.3 ARIMA- og SARIMA-modeller

**Språk:** Godt. Progresjonen fra AR via MA og ARMA til ARIMA og deretter SARIMA er ryddig forklart. Box-Jenkins-metodikkens tre steg er presist formulert.

**Faglig innhold:** Solid. Den multiplikative strukturen i SARIMA er korrekt beskrevet. Omtalen av SARIMA$(0,1,1)(0,1,1)_{12}$ som «flypassasjermodellen» er historisk korrekt og nyttig som referansepunkt. Henvisningen til kapittel 6.3 for «den fullstendige utledningen med alle polynomdefinisjoner» er verifisert.

### 2.5 Rapporttekst – Seksjon 3.4 Modellidentifikasjon og modellvalg

**Språk:** Godt. Signaturmønstrene er forklart kompakt men tilstrekkelig. Parsimonprinsippet er greit formulert.

**Faglig innhold:** Solid. Koblingen fra visuell ACF/PACF-tolkning til systematisk AIC/BIC-sammenligning gir en naturlig arbeidsflyt. Fremoverreferansen til kapittel 7.2 er verifisert.

### 2.6 Rapporttekst – Seksjon 3.5 Validering og prognoseevaluering

**Språk:** Generelt godt, men det finnes én grammatisk feil: «Denne biaskorreksjon gir» (linje 309) burde være «Denne biaskorreksjonen gir» (bestemt form). Se V1.

**Faglig innhold:** Den mest innholdsrike seksjonen. Dekker residualdiagnostikk (Ljung-Box, ARCH-LM, Jarque-Bera), prognosefeilmål (MAE, RMSE, MAPE), hold-out-validering og biaskorreksjon. Alle teststatistikker er korrekt gjengitt med riktige referanser. Biaskorreksjonsformelen med Jensens ulikhet er et sterkt tilskudd.

### 2.7 Figurer – rapportklarhet

| Figur | Tittel i figur | Format | Vurdering |
|:------|:---------------|:-------|:----------|
| 3.1 | «Additiv dekomponering: $y_t = T_t + S_t + \varepsilon_t$» | OK (HTML, 80%, sentrert, kursiv figurtekst) | God pedagogisk figur. Fire paneler viser observert serie, trend, sesong og restledd tydelig. Norske aksetitler. |
| 3.2 | «Differensiering for å oppnå stasjonaritet» | OK (HTML, 80%, sentrert, kursiv figurtekst) | Effektiv sammenstilling av fire differensieringsstrategier. Nullinjen i differensierte paneler hjelper tolkningen. |
| 3.3 | «Signaturmønstre i ACF og PACF for AR- og MA-prosesser» | OK (HTML, 80%, sentrert, kursiv figurtekst) | Tydelige kutoff-annoteringer. Konfidensgrenser synlige. Norske akselabeler. |
| 3.4 | «Biaskorreksjon ved tilbaketransformering fra log-skala» | OK (HTML, 80%, sentrert, kursiv figurtekst) | God visualisering av log-normalfordelingen med median vs. gjennomsnitt. Biaspilen er et nyttig visuelt element. |

**Samlet figurvurdering:** Alle fire figurer er konsistente i stil, oppfyller CLAUDE.md-kravene, og illustrerer teorien godt. Figurene bruker norske etiketter der det er naturlig. Se F1 for en mulig forbedring av Figur 3.2.

### 2.8 Matematisk notasjon

Inline-matematikk bruker `$...$` gjennomgående, i tråd med CLAUDE.md-kravet. Displaymatte bruker `$$...$$`. Ingen `\(...\)` er identifisert. Notasjonen er konsistent gjennom hele kapitlet.

### 2.9 Innholdsfortegnelse – konsistens

Innholdsfortegnelsen inneholder alle fem underseksjoner av kapittel 3 (3.1–3.5) med riktige titler og ankre. Verifisert OK.

**Observasjon:** Innholdsfortegnelsen sier «Modellering» for kapittel 6 (linje 85), mens den faktiske overskriften er «Modell» (linje 432). Tilsvarende sier den «Metode og data (kan splittes i to)» for kapittel 5 med parentesbemerkning som bør fjernes i en ferdig rapport. Begge er pre-eksisterende inkonsistenser som ikke tilhører ACT-3.7, men noteres for ACT-3.10.

---

## Svakheter og forbedringsforslag

### V1. Grammatisk feil: «Denne biaskorreksjon» mangler bestemt form

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Linje 309 i `rapport.md` skriver «Denne biaskorreksjon gir gjennomsnittsprognosen». Korrekt norsk bøyning er «Denne biaskorreksjonen gir», ettersom «denne» krever bestemt form av substantivet.

**Anbefalt tiltak:** Rett til «Denne biaskorreksjonen gir».

### V2. Seksjon 3.5 plasserer ARCH-LM-testen under «Validering og prognoseevaluering» uten å koble den til seksjon 3.2

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

ARCH-LM-testen (Engle, 1982) undersøker om residualvariansen er konstant over tid. Seksjon 3.2 behandler stasjonaritet og kravet om konstant varians, og nevner at log-transformasjon stabiliserer variansen. Det finnes imidlertid ingen eksplisitt kobling tilbake fra ARCH-LM-beskrivelsen i 3.5 til stasjonaritetsbetingelsen om konstant varians i 3.2. En kort setning ville styrke den indre sammenhengen i kapitlet.

**Anbefalt tiltak:** Legg til en kort kryssreferanse, f.eks.: «Konstant varians er én av de tre stasjonaritetsbetingelsene beskrevet i seksjon 3.2.»

### F1. Figur 3.2 – sesongdifferensiert panel viser tydelig gjenværende trend

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

I Figur 3.2 viser det nedre venstre panelet («Sesongdifferensiert») en tydelig positiv trend som ikke er fjernet. Dette er faglig korrekt – sesongdifferensiering fjerner sesong men ikke trend – men teksten i seksjon 3.2 kunne ha kommentert dette eksplisitt for å styrke den pedagogiske verdien. Eksempel: «Som Figur 3.2 viser, fjerner sesongdifferensieringen alene sesongen men ikke trenden, noe som bekrefter behovet for å kombinere de to differensieringstypene.»

### F2. Vurder å nevne MASE som alternativ til MAPE

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Teksten nevner MAPEs svakheter (udefinert for nullverdier, asymmetrisk), men foreslår ikke et alternativ. Mean Absolute Scaled Error (MASE), som Hyndman & Athanasopoulos (2021) anbefaler som et skalauavhengig mål uten MAPEs svakheter, kunne vært nevnt som supplement. Dette er imidlertid valgfritt for et LOG650-kurs og kan vurderes av forfatteren.

### F3. Presiser frihetsgrader for Ljung-Box i SARIMA-kontekst

**Alvorlighetsgrad:** Lav
**Kategori:** Metodikk

Teksten oppgir frihetsgrader for Ljung-Box som $m - p - q$. For SARIMA-modeller bruker noen implementasjoner $m - p - q - P - Q$ (der $P$ og $Q$ er sesongparametere). Selv om $m - p - q$ er den mest siterte formuleringen og konsistent med originalartikkelen, kan en fotnote eller kommentar nevne at praksis varierer for sesongmodeller.

### F4. Vurder å legge til en kort oppsummering på slutten av kapitlet

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Kapittel 3 slutter brått etter Figur 3.4 og biaskorreksjonsavsnittet. En avsluttende setning eller to som samler trådene – for eksempel at rammeverket nå er på plass for den konkrete modelleringen i kapittel 6 – ville gi kapitlet en ryddigere avslutning og tydeliggjøre overgangen til neste kapittel.

### F5. Overføres til ACT-3.10: Innholdsfortegnelse-inkonsistenser

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Innholdsfortegnelsen har «Modellering» for kapittel 6 (faktisk: «Modell») og «Metode og data (kan splittes i to)» for kapittel 5 (parentesbemerkningen bør fjernes). Disse er pre-eksisterende og tilhører ikke ACT-3.7, men bør rettes i ACT-3.10 (sammenstilling).

---

## Avhukningsliste – tiltak

| # | Tiltak | Kategori | Status | Kommentar |
|:--|:-------|:---------|:-------|:----------|
| V1 | Rett «Denne biaskorreksjon» til «Denne biaskorreksjonen» i rapport.md linje 309 | Språk og innhold | [x] | Rettet |
| V2 | Legg til kryssreferanse fra ARCH-LM i 3.5 til stasjonaritetsbetingelsen i 3.2 | Språk og innhold | [x] | Lagt til «et av de tre stasjonaritetskravene beskrevet i seksjon 3.2» |
| F1 | Vurder å kommentere gjenværende trend i sesongdifferensiert panel i teksten | Språk og innhold | [x] | Lagt til to setninger om at sesongdifferensiering alene ikke fjerner trenden |
| F2 | Vurder å nevne MASE som alternativ til MAPE | Språk og innhold | [x] | Lagt til kort omtale av MASE med referanse til Hyndman & Athanasopoulos (2021) |
| F3 | Vurder presisering av Ljung-Box frihetsgrader for SARIMA | Metodikk | [x] | Lagt til setning om at noen implementasjoner bruker m-p-q-P-Q for SARIMA |
| F4 | Vurder en kort oppsummerende avslutning på kapitlet | Språk og innhold | [x] | Lagt til oppsummerende avsnitt som samler trådene og peker mot kap. 6–9 |
| F5 | Overføres til ACT-3.10: Rett innholdsfortegnelse-inkonsistenser | Språk og innhold | [x] | Overført til ACT-3.10-sjekklisten i status.md |

---

## Samsvar med prosjektplan og krav

| Sjekkpunkt | Status | Kommentar |
|:---|:---|:---|
| Beskrive teoretisk rammeverk (tidsserieanalyse, SARIMA, stasjonaritet) | OK | Alle tre temaer er dekket i seksjon 3.1–3.3 |
| Koble teori til metodevalg og diskusjon | OK | Fremoverreferanser til kap. 6.3, 7.1, 7.2, 8.1 og 9 er verifisert |
| Kontrollere at alle referanser i kap. 3 finnes i kap. 11 og har oppsummeringsfil | OK | Alle 8 referanser verifisert i bibliografi og `003 references/` |
| Gjennomføre review og lukke aktiviteten | Pågår | Denne reviewen |
| ACT-3.7-C01: Kapittel 3 Teori er ferdigskrevet med rammeverk koblet til metode og diskusjon | OK | Fem seksjoner med tydelige koblinger |
| ACT-3.7-C02: Review er gjennomført og aktiviteten er lukket | Pågår | Denne reviewen |
| REQ-007: Leveranser i henhold til kursfaser | OK | Levert innen planlagt periode |
| REQ-008: Analyse skal kunne etterprøves | OK | Figurskript er reproduserbart med fast seed |

---

## Samlet vurdering

### Metodikk

Alle matematiske formler og definisjoner er korrekte og konsistente med de oppgitte kildene. Figurgenereringskoden er reproduserbar og godt strukturert. Konsistensen mellom genererte figurer og rapporttekst er god. Referansene er faglig solide og dekker feltet bredt med en god blanding av etablerte lærebøker og seminalartikler. Det er ingen metodiske feil som krever korrigering.

### Språk, innhold og figurer

Kapitlet er godt skrevet med klart norsk fagspråk og en pedagogisk oppbygging som passer for et LOG650-kurs. Den logiske progresjonen fra grunnleggende begreper til avanserte diagnostikkverktøy fungerer godt. De fire figurene er visuelt klare, korrekt formatert etter CLAUDE.md-standarden, og illustrerer teorien effektivt. De identifiserte svakhetene er begrenset til én grammatisk feil og en manglende intern kryssreferanse, begge av lav alvorlighetsgrad. Forbedringsforslalgene handler om finpuss som kan styrke kapitlet ytterligere.

### Anbefalt prioritering videre

1. **(Bør)** V1 – Rett grammatisk feil «Denne biaskorreksjon» til «Denne biaskorreksjonen»
2. **(Kan)** V2 – Legg til kryssreferanse fra ARCH-LM til stasjonaritetsbetingelsen
3. **(Kan)** F1 – Kommenter gjenværende trend i sesongdifferensiert panel
4. **(Kan)** F4 – Legg til kort oppsummering på slutten av kapitlet
5. **(Kan)** F2 – Vurder å nevne MASE
6. **(Kan)** F3 – Presiser frihetsgrader for Ljung-Box
7. **(Kan)** F5 – Overføres til ACT-3.10: Innholdsfortegnelse-inkonsistenser
