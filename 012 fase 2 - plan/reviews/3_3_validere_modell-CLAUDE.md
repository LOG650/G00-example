# Review av aktivitet 3.3 – «Validere modell»

**Reviewer:** CLAUDE
**Dato:** 2026-03-23
**Aktivitetsmappe:** `006 analysis/aktiviteter/3_3_validere_modell/`
**Planreferanse:** Aktivitet ACT-3.3, planlagt 2026-03-20 til 2026-03-25

---

## Sammendrag

Aktivitet 3.3 leverer en solid modellvalidering med to ryddige skript, seks resultatfiler og én figur. Residualdiagnostikk (Ljung-Box og ARCH-LM) er korrekt gjennomført og ærlig dokumentert, og testsettvalideringen gir et tydelig bilde av modellens styrker og svakheter. Reviewen identifiserer 5 styrker, 2 svakheter og 3 forbedringsforslag.

---

## Styrker

- **S1.** Ærlig og transparent håndtering av residualtestene – modellens brudd på forutsetninger er dokumentert uten å bortforklare dem.
- **S2.** Ryddig skriptseparasjon: ett skript for residualtester, ett for testsettvalidering. Klart skille mellom analyse (kap. 7.4) og resultater (kap. 8.1).
- **S3.** Korrekt bruk av `model_df=2` i Ljung-Box-testen, som justerer frihetsgrader for de to estimerte MA-parameterne.
- **S4.** Figur 8.1 er lesbar med gode fargevalg, akseformatering og norske legender. Figur- og tabellformat følger CLAUDE.md-standarden.
- **S5.** Rapportteksten gir god narrativ flyt fra residualanalyse (7.4) til testsettresultater (8.1) med tydelige kryssreferanser fremover til diskusjonskapitlet.

---

## Del 1 – Metodikk (beregninger og kode)

### 1.1 Residualtester (01_kjore_residualtester.py)

Skriptet estimerer SARIMA(0,1,1)(0,1,1)₁₂ på log-transformerte treningsdata og kjører Ljung-Box ved lag 12 og 24 samt ARCH-LM med 12 lag. Koden er ryddig og reproduserbar.

- **model_df=2**: Korrekt – modellen har to estimerte MA-parametere (θ₁ og Θ₁).
- **Ljung-Box-lags**: 12 og 24 er sesongrelevante som spesifisert i aktivitetsplanen.
- **ARCH-LM med 12 lag**: Rimelig valg for månedlige data.
- **Resultatene stemmer**: Tabellverdiene i `tab_01_residualtester.md` er konsistente med CSV-filen og med tabell 7.4 i rapporten.

**Vurdering:** Korrekt og fullstendig.

### 1.2 Testsettvalidering (02_validere_testsett.py)

Skriptet bruker `model.filter(MODEL_PARAMS)` med hardkodede parametere `[-0.8217, -0.5998, 0.0146]` for å generere prognoser for hele testperioden (42 måneder) i ett steg.

- **Parameterne er verifisert** mot estimeringsresultatene i `tab_05_modellparametere.csv` fra ACT-3.2: ma.L1=-0.821687, ma.S.L12=-0.599819, sigma2=0.014585. Avrundingen stemmer.
- **Feilmål er verifisert**: MAE=415.17, RMSE=494.13, MAPE=5.39 % stemmer med manuell kontroll av prognosetabellen.
- **Biastelling er korrekt**: 41 av 42 måneder har positiv prognosefeil (overprognose), som rapportert i kapittel 8.1.
- **Økende feil over tid**: Gjennomsnittlig APE øker fra 4.60 % (1978) til 7.46 % (1981 H1), noe som er forventet for en ren multi-step-ahead-prognose uten reestimering.

**Vurdering:** Beregningene er korrekte. Tilnærmingen med `model.filter()` og hardkodede parametere er funksjonelt korrekt, men se V1 under svakheter.

### 1.3 Prognose uten bias-korreksjon

Prognosene genereres på log-skala og transformeres tilbake med `exp()`. Når $\hat{z}_{t+h}$ er forventet log-salg, gir $\exp(\hat{z}_{t+h})$ medianen av den tilbake-transformerte fordelingen, ikke forventningsverdien. Bias-korreksjonen $E[Y] = \exp(\mu + \sigma^2/2)$ er ikke anvendt. I dette tilfellet overprogniserer modellen likevel systematisk, slik at den manglende korreksjonen ikke forverrer bias – men det er verdt å nevne i diskusjonskapitlet at transformasjonsteknikken i seg selv kan påvirke punktprognosens fortolkning.

**Vurdering:** Akseptabelt for dette prosjektets omfang, men bør nevnes som en metodisk nyanse i kapittel 9.

### Gjenstående metodiske observasjoner

- Prognosetilnærmingen er den strengest mulige: 42-stegs-prognose fra ett enkelt tidspunkt uten rullerende reestimering. Dette er metodisk rent, men gir høyere feil enn en rullerende tilnærming ville gjort. Rapporten beskriver dette transparent.
- Gjennomsnittlig bias (412.20 enheter) er nær MAE (415.17), noe som bekrefter at nesten all feil skyldes systematisk overprognose, ikke tilfeldig variasjon.

---

## Del 2 – Språk, innhold og figurer

### 2.1 Rapporttekst – kapittel 7.4 Validering

**Språk:** Godt norsk fagspråk, klare setninger, passende lengde. Ingen skrivefeil oppdaget.

**Faglig innhold:** Teksten gir først en visuell vurdering av residualene (fra diagnostikkplottet i 3.2), deretter supplerer med formelle tester (fra 3.3). Overgangen er logisk. Avsnittet avslutter med en tydelig oppsummering av hvilke forutsetninger som brytes og peker fremover til diskusjonskapitlet.

En liten uklarhet: teksten sier først «Korrelogrammet viser ingen signifikant autokorrelasjon» (basert på visuell inspeksjon og Ljung-Box lag 1), men deretter viser de formelle testene signifikant autokorrelasjon ved lag 12 og 24. Forskjellen skyldes at kort-lag-autokorrelasjon er ubetydelig mens sesong-kumulativ autokorrelasjon er signifikant. Teksten håndterer overgangen, men en eksplisitt setning om denne distinksjonen ville styrke avsnittet.

### 2.2 Rapporttekst – kapittel 8.1 Resultater fra testsettvalidering

**Språk:** Godt og presist. God balanse mellom nøktern resultatpresentasjon og relevante tolkninger.

**Faglig innhold:** Teksten identifiserer korrekt den systematiske positive biasen (41/42 måneder) og det største enkeltavviket (desember 1979, 1227.42). Avsnittet avsluttes med en passende kobling til diskusjonskapitlet. Teksten kunne med fordel nevne at feilen øker systematisk over tid (se F1).

### 2.3 Figurer – rapportklarhet

| Figur | Tittel i figur | Vurdering |
|:------|:---------------|:----------|
| 7.3 | Residualdiagnostikk for SARIMA(0,1,1)(0,1,1)₁₂ | Fra ACT-3.2, korrekt gjenbrukt i 7.4. Ryddig fire-panels oppsett. OK. |
| 8.1 | Testsettvalidering for SARIMA(0,1,1)(0,1,1)12 | God figur med klar fargekode (grønn=observert, oransje=prognose). Norske akselabeler. Sesongmønster og bias er tydelig synlig. Format i henhold til CLAUDE.md. |

### 2.4 Tabeller – konsistens og lesbarhet

| Tabell | Innhold | Vurdering |
|:-------|:--------|:----------|
| 7.4 | Residualtester | Stemmer med `tab_01_residualtester.csv`. ARCH-LM p-verdi avrundet til «< 0.001» i rapporten, som er riktig presentasjon. |
| 8.1 | Feilmål | Stemmer med `tab_03_feilmaal.csv`. Tre feilmål presentert ryddig. |

Prognosetabellen (`tab_02_testsettprognose`) er ikke gjengitt i rapporten. Dette er et bevisst valg – 42-raders tabell ville vært for detaljert for brødteksten. Tabellen finnes som artefakt for sporbarhet.

---

## Svakheter og forbedringsforslag

### V1. Hardkodede modellparametere i valideringsskriptet

**Alvorlighetsgrad:** Middels
**Kategori:** Metodikk

Skriptet `02_validere_testsett.py` hardkoder `MODEL_PARAMS = [-0.8217, -0.5998, 0.0146]` i stedet for å lese parameterne fra estimeringsartefaktene i ACT-3.2 eller lagre/laste en serialisert modell. Verdiene er verifisert korrekte, men tilnærmingen er sårbar for transcripsjonfeil og krever manuell oppdatering om modellen endres. Anbefalt tiltak: Les parameterne fra `tab_05_modellparametere.csv` eller serialiser den fittede modellen.

### V2. Manglende eksplisitt omtale av økende feiltrend over testperioden

**Alvorlighetsgrad:** Middels
**Kategori:** Språk og innhold

Rapportteksten i kapittel 8.1 dokumenterer den systematiske positive biasen godt, men sier ikke eksplisitt at feilen øker over tid: gjennomsnittlig APE stiger fra 4.6 % (1978) til 7.5 % (1981 H1). Denne trenden er viktig for tolkningen fordi den viser at modellens implisitte trendekstrapolering overstiger faktisk vekst – et forventet resultat for en lang multi-step-prognose. Anbefalt tiltak: Legg til en setning i 8.1 som kvantifiserer denne trenden, eventuelt supplert med en kort kommentar om at dette er forventet oppførsel.

### F1. Nevn log-transformasjon og bias-korreksjon i diskusjonskapitlet

**Alvorlighetsgrad:** Lav
**Kategori:** Metodikk

Punktprognosene bruker $\exp(\hat{z})$ uten bias-korreksjon ($\exp(\mu + \sigma^2/2)$). Forskjellen er liten og modellen overprogniserer uansett, men det er god praksis å nevne dette som en metodisk nyanse i diskusjonskapitlet.

### F2. Prediksjonsintervall i testsettfiguren

**Alvorlighetsgrad:** Lav
**Kategori:** Metodikk

Figur 8.1 viser kun punktprognoser. Å legge til konfidensband (f.eks. 95 %) ville synliggjort usikkerheten i prognosen og vist at observerte verdier i stor grad faller innenfor båndet. Dette er mer relevant for ACT-3.4, men kunne også berike testsettfiguren.

### F3. Tydeliggjør distinksjonen mellom kort-lag- og sesong-lag-autokorrelasjon i 7.4

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Teksten i 7.4 går fra «ingen signifikant autokorrelasjon» (visuelt, lag 1) til «forkast nullhypotesen» (lag 12 og 24) uten å eksplisitt forklare at det er sesong-kumulativ autokorrelasjon som gir utslaget. En tilleggssetning ville gjøre overgangen tydeligere for leseren.

---

## Avhukningsliste – tiltak

| # | Tiltak | Kategori | Status | Kommentar |
|:--|:-------|:---------|:-------|:----------|
| V1 | Les parametere fra CSV i stedet for hardkoding | Metodikk | [x] | Parametere leses nå fra tab_05_modellparametere.csv |
| V2 | Legg til setning om økende feiltrend i kap. 8.1 | Språk og innhold | [x] | APE per år kvantifisert i kap. 8.1 |
| F1 | Nevn bias-korreksjon som nyanse i kap. 9 | Metodikk | [x] | Lagt til i ACT-3.5-sjekklisten i status.md |
| F2 | Vurder prediksjonsintervall i testsettfigur | Metodikk | [x] | 95 % prediksjonsintervall lagt til i figur 8.1 |
| F3 | Tydeliggjør lag-distinksjonen i kap. 7.4 | Språk og innhold | [x] | Overgangssetning lagt til mellom visuell og formell diagnostikk |

---

## Samsvar med prosjektplan og krav

| Sjekkpunkt (fra status.md) | Status | Kommentar |
|:---|:---|:---|
| Bygge videre på residualdiagnostikk og rydde den inn i rapportens kapittel 7.4 | OK | Residualdiagnostikk fra 3.2 er integrert med nye formelle tester i 7.4. |
| Kjøre Ljung-Box på sesongrelevante lags, minst 12 og 24 | OK | Lag 12 og 24 er testet med korrekt model_df=2. |
| Kjøre ARCH-LM for heteroskedastisitet | OK | 12 lag, resultat dokumentert. |
| Generere prognoser mot testdatasettet for perioden 1978-01 til 1981-06 | OK | 42 måneder prognostisert med fast holdout. |
| Beregne MAE, RMSE og MAPE | OK | Alle tre feilmål er beregnet og verifisert. |
| Dokumentere kapittel 7.4 Validering | OK | Komplett med figur, tabell og tekst. |
| Dokumentere kapittel 8.1 Resultater fra testsettvalidering | OK | Komplett med figur, tabell og tekst. Se V2 for forbedring. |
| Forberede grunnlag for diskusjon av modellens egnethet i kapittel 9 | OK | Fremoverreferanser til kap. 9 finnes i både 7.4 og 8.1. |

### REQ-004 – Modellen skal valideres

**Krav:** Prosjektet skal dokumentere modellvalidering gjennom residualanalyse og testsettbasert prognosekvalitet med minst ett feilmål.

**Verifiseringskriterium:** Rapporten inneholder residualdiagnostikk i analysekapitlet, testsettvalidering og feilmål i resultatkapitlet og en faglig vurdering av modellens egnethet i diskusjonskapitlet.

**Status:** Oppfylt for analysekapitlet (7.4) og resultatkapitlet (8.1). Diskusjonskapitlet (9) er forberedt med grunnlag, men skrives som del av ACT-3.5.

---

## Samlet vurdering

### Metodikk

Beregninger og kode er korrekte og reproduserbare. Residualtestene er faglig riktig gjennomført med passende valg av lag og frihetsgrader. Testsettvalideringen bruker en streng fast-holdout-tilnærming som gir et konservativt bilde av modellens prognoseevne. Den eneste metodiske svakheten er hardkodede parametere i valideringsskriptet (V1), som er funksjonelt korrekt men sårbar for vedlikeholdsfeil.

### Språk, innhold og figurer

Rapportteksten i kapittel 7.4 og 8.1 er velskrevet, ryddig og faglig presis. Figurer og tabeller følger prosjektets formatstandard. Funnene er presentert ærlig uten bortforklaringer. Den eneste innholdsmessige svakheten er at den økende feiltrenden over testperioden ikke er eksplisitt kvantifisert (V2).

### Anbefalt prioritering videre

1. **(Bør)** V2: Legg til setning om økende feiltrend i kapittel 8.1 – styrker grunnlaget for diskusjonskapitlet.
2. **(Bør)** V1: Erstatt hardkodede parametere med lesing fra artefakt – forbedrer reproduserbarhet.
3. **(Kan)** F3: Tydeliggjør lag-distinksjonen i kapittel 7.4 – liten innsats, bedre leseflyt.
4. **(Kan)** F1: Nevn bias-korreksjon som nyanse i kapittel 9 – relevant når diskusjonskapitlet skrives.
5. **(Kan)** F2: Vurder prediksjonsintervall i testsettfiguren – kan utsettes til ACT-3.4.
