# Review av aktivitet 3.4 -- «Lage prognose og anbefalinger»

**Reviewer:** CLAUDE
**Dato:** 2026-03-25
**Aktivitetsmappe:** `006 analysis/aktiviteter/3_4_lage_prognose_og_anbefalinger/`
**Planreferanse:** Aktivitet ACT-3.4, planlagt 2026-03-25 til 2026-04-10

---

## Sammendrag

Aktivitet 3.4 leverer en 12-måneders prognose basert på refitting av SARIMA(0,1,1)(0,1,1)₁₂ på hele datasettet, med tilhørende prediksjonsintervall, biaskorreksjon, oppsummeringstabeller og kapasitetsplanlegging. Arbeidet er organisert i to skript, én figur og åtte resultatfiler. Rapportens kapittel 8.2 er skrevet med god faglig flyt. Reviewen identifiserer 5 styrker, 3 svakheter og 4 forbedringsforslag.

---

## Styrker

- **S1.** Ryddig todelt skriptstruktur: ett skript for prognosemodellering og ett for oppsummering og anbefalinger. Klar separasjon av faglig modellarbeid og beslutningsstøtte.
- **S2.** Biaskorreksjon er implementert korrekt og omtalt med faglig forståelse i rapporten. Beslutningen om å ikke bruke den som hovedprognose er godt begrunnet med henvisning til den positive nivåbiasen fra testsettvalideringen.
- **S3.** Tallene i rapporten er konsistente med de genererte artefaktene. Alle 12 punktprognoser, prediksjonsintervaller, totalt salg, gjennomsnitt, topp/bunnmåned og PI-bredde er verifisert og stemmer.
- **S4.** Rapportteksten i 8.2 har god narrativ struktur med naturlig overgang fra refitting, via parameterstabilitet, til prognoseresultater og videre til implikasjoner for diskusjonskapitlet.
- **S5.** Figuren er lesbar med gode fargevalg, norske aksetitler og legende, og følger prosjektets figurstandard (sentrert, 80 % bredde, figurtekst).

---

## Del 1 -- Metodikk (beregninger og kode)

### 1.1 Refitting og prognose (01_lage_prognose.py)

Skriptet laster hele datasettet (210 observasjoner), log-transformerer, fitter SARIMA(0,1,1)(0,1,1)₁₂ med `statsmodels.tsa.arima.model.ARIMA`, og genererer 12-stegs prognose med `get_forecast(steps=12)`. Tilbaketransformering skjer med `np.exp()` for punktprognose og prediksjonsintervall, og med `np.exp(forecast + sigma2/2)` for biaskorrigert prognose.

- **Modellspesifikasjon**: ORDER=(0,1,1) og SEASONAL_ORDER=(0,1,1,12) er korrekt og konsistent med ACT-3.2.
- **Data**: Hele datasettet (210 obs) brukes, som forventet for endelig prognose etter validering.
- **Parameterstabilitet**: Refittede parametere ($\theta_1 = -0.82$, $\Theta_1 = -0.62$, $\hat{\sigma}^2 = 0.012$) er nær treningsestimatene ($\theta_1 = -0.82$, $\Theta_1 = -0.60$, $\hat{\sigma}^2 = 0.015$), noe som bekrefter stabilitet.
- **Tilbaketransformering**: `np.exp(forecast_log)` gir medianprognosen, som er korrekt. Prediksjonsintervallet tilbaketransformeres med `np.exp()` på log-skala CI-grensene, som gir asymmetriske intervaller på originalskala. Dette er metodisk riktig.

**Vurdering:** Korrekt og reproduserbar.

### 1.2 Biaskorreksjon

Biaskorreksjon beregnes som `np.exp(forecast_log + sigma2/2)` der `sigma2 = result.params["sigma2"]`, altså innovasjonsvariansen fra den refittede modellen. For en lognormal fordeling gir $\exp(\mu + \sigma^2/2)$ forventningsverdien, mens $\exp(\mu)$ gir medianen.

Implementeringen bruker innovasjonsvariansen $\hat{\sigma}^2 = 0.0115$ som korreksjonsfaktor for alle 12 horisontledd. Strengt tatt er dette kun eksakt for ett-stegs-prognosen. For multi-stegs prognoser vokser prognosefeilens varians med horisonten, slik at den korrekte biaskorreksjonsfaktoren ville være $\exp(\hat{\sigma}^2_h/2)$ der $\hat{\sigma}^2_h$ er prognosefeilens varians ved horisont $h$. Denne informasjonen er tilgjengelig i `get_forecast().se_mean` eller kan utledes fra konfidensintervallene. I praksis er forskjellen marginal for denne modellen (den konstante korreksjonsfaktoren er 1.006, og den horisontspesifikke ville variere fra ca. 1.006 til ca. 1.008 over 12 steg).

**Vurdering:** Tilnærmingen er funksjonelt akseptabel fordi korreksjonsfaktoren er marginal og ikke brukes som hovedprognose, men det er en metodisk forenkling som bør nevnes i diskusjonskapitlet. Se F1.

### 1.3 Oppsummering og anbefalinger (02_oppsummere_anbefalinger.py)

Skriptet leser prognosetabellen, beregner nøkkeltall (totalprognose, gjennomsnitt, topp/bunn, amplitude, PI-bredde) og produserer en kapasitetsplanleggingstabell med sesongkategorisering.

- **Nøkkeltall er verifisert**: Total 100 413, gjennomsnitt 8 368, toppmåned desember 1981 (19 483), bunnmåned august 1981 (2 694), amplitude 16 789, gjennomsnittlig PI-bredde 3 844. Alle stemmer med manuell kontroll.
- **Sesongkategorisering**: Funksjonen `classify_season()` definerer lavsesong som juni-august, høysesong som november-januar og resten som normalsesong. Se V2 under svakheter.

**Vurdering:** Beregningene er korrekte, men sesongklassifiseringen har faglige svakheter.

### Gjenstående metodiske observasjoner

- Prognosen er en ren ekstrapolering uten reestimering eller rullerende oppdatering. Dette er konsistent med tilnærmingen i ACT-3.3, men betyr at den positive nivåbiasen identifisert i testsettvalideringen sannsynligvis også er til stede i den endelige prognosen. Rapporten nevner dette riktig.
- Artefaktene er ikke committet til git ennå (scripts, figurer og resultater er untracked). Se V3.

---

## Del 2 -- Språk, innhold og figurer

### 2.1 Rapporttekst -- kapittel 8.2

Kapittel 8.2 er det eneste nye rapportkapitlet i denne aktiviteten. Teksten er velskrevet og følger rapportstrukturen i CLAUDE.md.

**Språk:** Godt norsk fagspråk uten skrivefeil. Setningene er klare og konsise. Begrepet «refittet» (norsk bøying av engelsk stamme) brukes konsekvent og er akseptabelt i fagsammenheng.

**Faglig innhold:** Kapitlet dekker refitting, parameterstabilitet, prognoseresultater med usikkerhet, biaskorreksjon og implikasjoner. Teksten gjør et godt poeng av at biaskorreksjon ville forsterke den positive nivåbiasen. Overgangen til kapittel 9 (diskusjon) er naturlig og tydelig. Teksten nevner «detaljert drøfting av praktiske implikasjoner og modellbegrensninger følger i kapittel 9» -- dette er et løfte som må innfris i ACT-3.5.

### 2.2 Figurer -- rapportklarhet

| Figur | Tittel i figur | Vurdering |
|:------|:---------------|:----------|
| 8.2 | «12-måneders prognose for SARIMA(0,1,1)(0,1,1)₁₂» | Lesbar figur med gode farger (grønn for historisk, oransje for prognose), norske legendetekster og ryddig x-akse. Historisk salg vises fra 1978 og fremover, noe som gir god kontekst uten å overbelaste figuren. |

Figuren viser historisk salg, prognosekurve og 95 % prediksjonsintervall. Den vertikale stiplede linjen ved prognoseopprinnelsen er nyttig for å skille historikk fra prognose.

Figurteksten i rapporten er: «Figur 8.2 12-måneders prognose for SARIMA$(0,1,1)(0,1,1)_{12}$ med 95 % prediksjonsintervall (juli 1981 til juni 1982).» Denne er informativ og følger prosjektets standard.

### 2.3 Tabeller -- konsistens og lesbarhet

Rapporten inneholder én ny tabell (Tabell 8.2) med 12 rader for punktprognose og prediksjonsintervall. Tallene er verifisert mot `tab_02_prognose_12_maaneder.csv` og stemmer eksakt.

Tabellen i rapporten bruker mellomrom som tusenskilletegn (f.eks. «6 159»), som er god norsk praksis og gjør tabellen lettlest. Kolonnene «Nedre 95 %» og «Øvre 95 %» er klare. Biaskorreksjon-kolonnen er utelatt fra rapporttabellen, noe som er et godt valg siden den ikke brukes som hovedprognose.

Oppsummeringstabellene (tab_03, tab_04) er kun i artefaktene og ikke i rapporten. Disse kunne vært nyttige som støttetabeller i diskusjon eller vedlegg. Se F3.

### 2.4 Bildereferanse med feil URL-koding

Figur 8.2 i rapporten bruker `../006 analysis/aktiviteter/...` (med literal mellomrom), mens alle tidligere figurer bruker `../006%20analysis/aktiviteter/...` (med URL-kodet mellomrom). Dette er inkonsistent og kan føre til at figuren ikke vises i enkelte Markdown-renderere. Se V1.

---

## Svakheter og forbedringsforslag

### V1. Inkonsistent URL-koding i figursti

**Alvorlighetsgrad:** Middels
**Kategori:** Språk og innhold

Figur 8.2 refereres med `../006 analysis/...` mens alle andre figurer i rapporten bruker `../006%20analysis/...`. Mellomrom i URL-stier kan føre til at figuren ikke vises i noen Markdown-renderere (f.eks. GitHub, VS Code preview). Stien bør endres til `../006%20analysis/aktiviteter/3_4_lage_prognose_og_anbefalinger/figurer/fig_01_prognose_12_maaneder.png` for konsistens.

### V2. Sesongklassifisering i kapasitetsplanleggingstabell er ikke dataforankret

**Alvorlighetsgrad:** Middels
**Kategori:** Metodikk

Funksjonen `classify_season()` definerer lavsesong som juni-august, høysesong som november-januar og normalsesong som resten. Denne klassifiseringen stemmer dårlig med historiske data:

- **Januar** er klassifisert som «Høysesong», men har et historisk gjennomsnitt på 4 466 -- rangert som 7. høyeste måned. Oktober (rang 3, gjennomsnitt 7 161) er derimot klassifisert som «Normalsesong».
- **Juni** er klassifisert som «Lavsesong», men har et historisk gjennomsnitt på 5 121 -- rangert som 6. høyeste måned, altså over mediannivået.
- De tre historisk svakeste månedene er august (2 003), februar (3 856) og juli (4 420), men bare to av disse er klassifisert som lavsesong.

Selv om tabellen bare ligger i artefaktene og ikke i rapporten, er den beskrevet i README og kan bli brukt av andre uten kontekst. En mer dataforankret tilnærming ville klassifisere basert på kvartiler eller standardavvik fra gjennomsnittet.

### V3. Artefakter er ikke committet til git

**Alvorlighetsgrad:** Middels
**Kategori:** Metodikk

Scripts, figurer og resultatfiler fra ACT-3.4 er utrackede i git. Rapport, README og status.md er modifiserte men ikke stagede. For sporbarhet og reproduserbarhet bør arbeidet committes før aktiviteten lukkes. I tillegg er `schedule.json` ikke oppdatert -- den viser fortsatt ACT-3.4 som `"not-started"` med `percentComplete: 0`, mens `status.md` angir at aktiviteten er fullført per 2026-03-25.

### F1. Biaskorreksjon bør nyanseres med horisontavhengig varians

**Alvorlighetsgrad:** Lav
**Kategori:** Metodikk

Biaskorreksjon-kolonnen i `tab_02_prognose_12_maaneder.csv` bruker konstant $\hat{\sigma}^2 = 0.0115$ for alle 12 horisontledd. Strengt tatt vokser prognosefeilens varians med horisonten, slik at den korrekte korreksjonsfaktoren er horisontspesifikk. I praksis er forskjellen svært liten for denne modellen (0.6 % vs. ca. 0.8 % ved horisont 12), men det kan være verdt å kommentere denne forenklingen i diskusjonskapitlet som en del av den metodiske nyansen som allerede er planlagt.

### F2. Rapporttekst mangler henvisning til refittede parametere i tabellform

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Rapporten omtaler refittede parametere inline ($\theta_1 = -0.82$, $\Theta_1 = -0.62$, $\hat{\sigma}^2 = 0.012$), men inkluderer ikke den fulle parametertabellen fra `tab_01_modellparametere_refittet.md`. Denne tabellen inneholder konfidensintervaller og z-verdier som dokumenterer estimatenes presisjon i den refittede modellen. En kort tabell (som tabell 7.3 for treningsestimater) kunne styrke dokumentasjonen, eventuelt som vedlegg.

### F3. Oppsummeringstabeller ikke brukt i rapporten

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Artefaktene inneholder to oppsummeringstabeller (tab_03 prognoseoppsummering og tab_04 kapasitetsplanlegging) som gir nyttig beslutningsstøtte, men ingen av dem er referert i rapporten. Tab_03 (nøkkeltall) kunne styrke kapittel 8.2 eller 9, og tab_04 (kapasitetsplanlegging med sesongkategorier -- etter korrigering, se V2) kunne fungere som beslutningsstøtte i diskusjonskapitlet.

### F4. Figur 8.2 viser bare historikk fra 1978

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Figur 8.2 viser historisk salg fra ca. 1978 og fremover, noe som gir god lokal kontekst rundt prognosen. Imidlertid finnes det ingen figur i rapporten som viser hele tidsserien sammen med prognosen. En slik figur kunne styrke helhetsinntrykket, spesielt i diskusjonskapitlet der modellens langsiktige trendekstrapolering drøftes. Dette er et forbedringsforslag for ACT-3.5 eller vedlegg.

---

## Avhukningsliste -- tiltak

| # | Tiltak | Kategori | Status | Kommentar |
|:--|:-------|:---------|:-------|:----------|
| V1 | Endre figursti til URL-kodet mellomrom | Språk og innhold | [x] | Fikset 2026-03-25 |
| V2 | Revidere sesongklassifisering i kapasitetstabellen | Metodikk | [x] | Dataforankret klassifisering basert på historisk månedsprofil, fikset 2026-03-25 |
| V3 | Committe artefakter og oppdatere schedule.json | Metodikk | [x] | schedule.json oppdatert og artefakter committet 2026-03-25 |
| F1 | Nyansere biaskorreksjon med horisontavhengighet i diskusjon | Metodikk | [ ] | Hører til ACT-3.5 |
| F2 | Vurdere parametertabell for refittede estimater | Språk og innhold | [ ] | |
| F3 | Vurdere oppsummeringstabeller i rapport | Språk og innhold | [ ] | Hører til ACT-3.5 |
| F4 | Vurdere helhetsfigur med hele tidsserien og prognose | Språk og innhold | [ ] | Hører til ACT-3.5 |

---

## Samsvar med prosjektplan og krav

| Sjekkpunkt | Status | Kommentar |
|:---|:---|:---|
| Lage 12-måneders prognose (ACT-3.4-C01) | OK | 12-måneders punktprognose med PI er produsert og dokumentert i rapport og artefakter |
| Tolke prognoseresultater | OK | Rapporten tolker sesongmønster, usikkerhet og biaskorreksjon |
| Vurdere konsekvenser for produksjon og lager | Delvis | Rapporten nevner kapasitetsimplikasjoner i ett avsnitt, men detaljert drøfting er utsatt til kap. 9 |
| Formulere anbefalinger til PowerHorse (ACT-3.4-C02) | Delvis | Anbefalinger er forberedt i artefaktene (tab_04), men ikke eksplisitt formulert i rapporten ennå |
| REQ-001 (12-måneders prognose) | OK | Punktprognoser per måned og samlet tolkning er levert |
| REQ-005 (Logistisk tolkning) | Delvis | Grunnlaget er lagt, men oversettelse til konkrete anbefalinger hører til kap. 9 i ACT-3.5 |
| schedule.json oppdatert | OK | ACT-3.4 oppdatert til «completed» med percentComplete 100 |
| Git-commit av artefakter | OK | Artefaktene er committet 2026-03-25 |

---

## Samlet vurdering

### Metodikk

Prognosearbeidet er faglig solid. Modellen er korrekt refittet, prognosene er riktig tilbaketransformert, og biaskorreksjon er behandlet med god forståelse. Tallmessig konsistens mellom kode, artefakter og rapport er verifisert. Den viktigste metodiske svakheten er sesongklassifiseringen i kapasitetstabellen (V2), som ikke er forankret i data og gir feilaktige kategorier for flere måneder. Denne tabellen er dog ikke i rapporten og har begrenset konsekvens for sluttresultatet.

### Språk, innhold og figurer

Rapportteksten i kapittel 8.2 er velskrevet med god faglig flyt og presist norsk fagspråk. Figuren er lesbar og følger prosjektets standard. Den viktigste svakheten er inkonsistent URL-koding i figurstien (V1), som bør fikses umiddelbart for å sikre at figuren vises korrekt.

### Anbefalt prioritering videre

1. **(Må)** V1 -- Rette figurstien til URL-kodet mellomrom for konsistens og rendering.
2. **(Må)** V3 -- Committe artefakter til git og oppdatere schedule.json til «completed».
3. **(Bør)** V2 -- Revidere sesongklassifisering i kapasitetstabellen basert på historiske data.
4. **(Kan)** F2 -- Vurdere å inkludere refittet parametertabell i rapport eller vedlegg.
5. **(Kan)** F1/F3/F4 -- Nyansering av biaskorreksjon, oppsummeringstabeller i rapport og helhetsfigur kan håndteres i ACT-3.5.
