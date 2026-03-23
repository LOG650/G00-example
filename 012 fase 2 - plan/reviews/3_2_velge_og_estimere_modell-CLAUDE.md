# Review av aktivitet 3.2 – Velge og estimere modell

**Reviewer:** Claude (Opus 4.6)
**Dato:** 2026-03-23
**Aktivitetsmappe:** `006 analysis/aktiviteter/3_2_velge_og_estimere_modell`
**Planreferanse:** Aktivitet «Velge og estimere modell», planlagt 2026-03-11 til 2026-03-20

---

## Sammendrag

Aktiviteten er faglig sterk og godt dokumentert. Fire skript bygger opp modellvalget i en logisk sekvens fra modelltype via stasjonaritetsvurdering og kandidatsøk til endelig estimering. Rapporten dekker materialet i kapittel 6 (modellrammeverk) og 7.1–7.3 (analyse), med tre figurer, tre tabeller og en komplett matematisk framstilling av den estimerte SARIMA$(0,1,1)(0,1,1)_{12}$-modellen. Reviewen identifiserer tre svakheter (V1–V3), to forbedringsforslag (F1–F2) og fem styrker.

---

## Styrker

- **S1.** Systematisk og reproduserbar arbeidsflyt med fire skript i logisk sekvens (modelltype → stasjonaritet → ordensvalg → estimering). Hvert skript produserer etterprøvbare artefakter.
- **S2.** Grundig kandidatsøk: 36 SARIMA-modeller ble estimert og rangert etter AIC/BIC. Alle konvergerte. Resultatene er dokumentert i både CSV og Markdown.
- **S3.** Rapportteksten i kapittel 7.1 kobler statistiske tester (ADF, KPSS) med visuell diagnostikk og gir en samlet faglig vurdering i stedet for å bare rapportere p-verdier. Godt akademisk håndverk.
- **S4.** Kapittel 6.3 gir en tydelig matematisk framstilling av det generelle SARIMA-rammeverket, og kapittel 7.3 viser den estimerte modellen i både kompakt og utvidet form med forklaring av hvert ledd.
- **S5.** Ryddig mappestruktur med konsistente filnavn (`fig_`/`tab_`-prefikser) i henhold til CLAUDE.md. Alle 18 filer i aktivitetsmappen er navngitt og organisert konsistent.

---

## Del 1 – Metodikk (beregninger og kode)

### 1.1 Modelltype og SARIMA-begrunnelse (skript 01)

Skriptet `01_vurdere_modelltype.py` evaluerer åtte egenskaper ved treningsdatasettet og konkluderer med at SARIMA er en passende modellklasse. Komplett tidsserie (168 observasjoner, 0 hull), tydelig trend (glidende gjennomsnitt øker fra 3478 til 7328) og sterk sesong (ratio høyeste/laveste måned = 6.79) underbygger valget. Begrunnelsen er konsistent med kapittel 6.1 i rapporten.

**Vurdering:** Korrekt og tilstrekkelig. Oppfyller REQ-003 for modelltype.

### 1.2 Stasjonaritet og differensiering (skript 02)

Skriptet `02_vurdere_stasjonaritet_og_differensiering.py` tester fire differensieringsvarianter med ADF og KPSS. Log-transformasjon brukes konsekvent. Figur `fig_01_serievarianter.png` viser alle fire varianter i et 2×2-rutenett. Testverdiene i `tab_02_stasjonaritetstester.md` stemmer overens med tabell 7.1 i rapporten.

Differensieringsvurderingen i `tab_03_differensieringsvurdering.md` anbefaler $d=0, D=1$ som «Foretrukket kandidat», mens rapporten (avsnitt 7.1) konkluderer med $d=1, D=1$ som hovedkandidat. Se V1 nedenfor.

**Vurdering:** Beregningene er korrekte. Inkonsistensen mellom artefakt og rapportvalg er det viktigste funnet.

### 1.3 ACF/PACF og kandidatsøk (skript 03)

Skriptet `03_velge_sarima_ordener.py` beregner ACF/PACF for den kombinert differensierte log-serien og gjennomfører et systematisk grid search over $p \in \{0,1,2\}$, $q \in \{0,1,2\}$, $P \in \{0,1\}$, $Q \in \{0,1\}$ med faste $d=1, D=1$. Alle 36 kandidater konvergerte. SARIMA$(0,1,1)(0,1,1)_{12}$ kommer best ut med AIC = -202.83 og BIC = -193.70.

Kandidatsøket bruker kun $d=1, D=1$ som fast differensiering. Ettersom skript 02 anbefalte $d=0, D=1$ som foretrukket, er det en metodisk begrensning at kandidater med den differensieringen ikke ble evaluert. Se V2 nedenfor.

**Vurdering:** Grid search og rangering er korrekte. Begrensningen i differensieringsrommet bør kommenteres.

### 1.4 Modellestimering (skript 04)

Skriptet `04_estimere_modell.py` estimerer den valgte modellen med MLE. Parametertabellen i `tab_05_modellparametere.md` stemmer overens med tabell 7.3 i rapporten. Begge MA-parameterne er sterkt signifikante ($p < 0.001$). Diagnostikkfiguren `fig_03_diagnostikk.png` genereres fra statsmodels' `plot_diagnostics()`.

Interaksjonsleddet $0.4929\varepsilon_{t-13}$ i den utvidede formen er korrekt ($0.8217 \times 0.5998 = 0.4929$). Rapporten forklarer dette korrekt som et samspillsledd mellom de to MA-komponentene.

**Vurdering:** Korrekt estimering og dokumentasjon.

### Gjenstående metodiske observasjoner

- Hard-kodede ordner i skript 04 (`ORDER = (0,1,1)`, `SEASONAL_ORDER = (0,1,1,12)`) i stedet for å lese fra skript 03-output. Fungerer, men er litt skjørt dersom kandidatvurderingen endres.
- Warnings fra matplotlib og statsmodels er undertrykt. Akseptabelt for batchkjøring, men kan skjule relevante meldinger.

---

## Del 2 – Språk, innhold og figurer

### 2.1 Rapporttekst – kapittel 6 (Modellering)

**Språk:** Korrekt norsk, formelt akademisk register. Setninger er presise og konsistente. Antagelseslisten i 6.2 er tydelig formulert med et eksplisitt forbehold om at antagelsene ikke er verifiserte fakta.

**Faglig innhold:** Kapittel 6 gir et selvstendig rammeverk for SARIMA uten å repetere casedata fra kapittel 4 (dette ble ryddet som eget steg i aktiviteten). Den generelle formuleringen med lag-operator, differensiering og polynomdefinisjonene er korrekt og pedagogisk. Kryssreferanser til kapittel 4 (figurer 4.1–4.4, tabell 4.1) og kapittel 5 er på plass.

### 2.2 Rapporttekst – kapittel 7.1–7.3 (Analyse)

**Språk:** Godt norsk. Avsnitt 7.1 har en særlig god formulering der konklusjonen «bygger ikke bare på p-verdiene, men på en samlet faglig vurdering av teststatistikkene, p-verdiene og den visuelle diagnostikken». Noen setninger er lange (35+ ord), men de er fortsatt lesbare.

**Faglig innhold:** Stasjonaritetsvurderingen (7.1) er nyansert og unngår blind avhengighet av p-verdier. ACF/PACF-tolkningen (7.2) er faglig presis og kobler korrekt til airline-modellen. Parameterinterpretasjonen (7.3) forklarer hvert ledd i den utvidede formen, noe som er pedagogisk verdifullt.

### 2.3 Figurer – rapportklarhet

| Figur | Tittel i figur | Vurdering |
|:------|:---------------|:----------|
| 7.1 | «Log-transformerte serievarianter» | OK – tydelig 2×2-rutenett, riktig HTML-format med 80 % bredde |
| 7.2 | «ACF og PACF for $(1-B)(1-B^{12})\log(y_t)$» | OK – LaTeX i figurtekst, konsistent med teksten |
| 7.4 | «Residualdiagnostikk for SARIMA$(0,1,1)(0,1,1)_{12}$» | OK faglig, men figurnummeret hopper fra 7.2 til 7.4 (se V3) |

Alle figurer bruker korrekt HTML-format per CLAUDE.md: sentrert, `width="80%"`, kursiv figurtekst i liten skrift.

### 2.4 Tabeller – konsistens og lesbarhet

| Tabell | Innhold | Vurdering |
|:-------|:--------|:----------|
| 7.1 | Stasjonaritetstester | Korrekt, men mangler mellomrom mellom serienavn og LaTeX-formel (se F1) |
| 7.2 | Topp 10 SARIMA-kandidater | OK – stemmer med `tab_04_modellkandidater.md` |
| 7.3 | Estimerte parametere | OK – stemmer med `tab_05_modellparametere.md` |

Alle tabeller har sentrert kursiv tabelltekst under, konsistent med CLAUDE.md.

---

## Svakheter og forbedringsforslag

### V1. Artefakt og rapporttekst avviker om differensieringsvalg

**Alvorlighetsgrad:** Middels
**Kategori:** Metodikk

Resultatfilen `tab_03_differensieringsvurdering.md` anbefaler $d=0, D=1$ som «Foretrukket kandidat» med begrunnelsen at det er den enkleste varianten som oppnår stasjonaritet. Rapporten i avsnitt 7.1 velger likevel $d=1, D=1$ som hovedkandidat, med en faglig begrunnelse knyttet til visuell diagnostikk og bedre balanse mellom trend- og sesongfjerning.

Rapportens begrunnelse er forsvarlig, men artefaktet og teksten er inkonsistente. Anbefalt tiltak: Oppdater `tab_03` slik at anbefalingene reflekterer det endelige valget, eller legg til en tydelig note i rapporten som eksplisitt forklarer avviket fra den genererte tabellens anbefaling.

### V2. Kandidatsøket dekker kun én differensieringsvariant

**Alvorlighetsgrad:** Middels
**Kategori:** Metodikk

Alle 36 kandidater i grid search (skript 03) har faste $d=1, D=1$. Dersom $d=0, D=1$ er et gyldig alternativ — som artefaktet fra skript 02 hevder — burde kandidatsøket også ha inkludert modeller med den differensieringen, eller rapporten bør eksplisitt begrunne hvorfor kun $d=1, D=1$ ble søkt. Dette er ikke en feil i beregningene, men en metodisk begrensning som bør kommenteres.

### V3. Figurnummerering hopper fra 7.2 til 7.4

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Figur 7.3 finnes ikke i rapporten. Figurnummereringen går fra 7.2 (ACF/PACF) direkte til 7.4 (residualdiagnostikk). Årsaken er at `fig_03_diagnostikk.png` ble produsert i ACT-3.2 men plassert i seksjon 7.4, som hører til ACT-3.3. Anbefalt tiltak: Omnummerer figuren til 7.3 slik at nummereringen er sammenhengende, eller behold nummereringen men legg inn en figur 7.3 i seksjonen som mangler den.

### F1. Manglende mellomrom i tabell 7.1

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

I «Serievariant»-kolonnen i tabell 7.1 mangler det mellomrom mellom beskrivende tekst og LaTeX-formel: «serie$z_t$» bør være «serie $z_t$», «differensiert$(1-B)z_t$» bør være «differensiert $(1-B)z_t$», osv. Mellomrommet er nødvendig for korrekt rendering og lesbarhet.

### F2. README i aktivitetsmappen er minimal

**Alvorlighetsgrad:** Lav
**Kategori:** Metodikk

`README.md` (291 bytes) inneholder bare en kort beskrivelse og pekere til undermapper. Kan med fordel utvides med en kort beskrivelse av arbeidsflyt (skript 01 → 02 → 03 → 04), nøkkelresultater og den valgte modellen, slik at en leser raskt kan orientere seg uten å åpne hvert skript.

---

## Avhukningsliste – tiltak

| # | Tiltak | Kategori | Status | Kommentar |
|:--|:-------|:---------|:-------|:----------|
| V1 | Oppdater `tab_03` eller legg til note i rapporten om differensieringsavvik | Metodikk | [x] Gjennomført | Note lagt til i avsnitt 7.1 |
| V2 | Kommenter i rapporten at kandidatsøket kun dekker $d=1, D=1$ | Metodikk | [x] Gjennomført | Setning lagt til i avsnitt 7.2 |
| V3 | Omnummerer figur 7.4 til 7.3 eller legg inn manglende figur | Språk og innhold | [x] Gjennomført | Figur 7.4 omnummerert til 7.3 |
| F1 | Legg til mellomrom i tabell 7.1 mellom tekst og LaTeX-formel | Språk og innhold | [x] Gjennomført | Mellomrom lagt til i alle fire rader |
| F2 | Utvid README med arbeidsflyt og nøkkelfunn | Metodikk | [x] Gjennomført | Arbeidsflyt, nøkkelresultat og artefaktpekere lagt til |

---

## Samsvar med prosjektplan og krav

| Sjekkpunkt | Status | Kommentar |
|:---|:---|:---|
| Beskrive generell SARIMA-modell matematisk i kapittel 6 | OK | Lag-operator, polynomer og differensiering er dekket i 6.3 |
| Vurdere aktuell modelltype for trend og sesong | OK | Skript 01 + kapittel 6.1 |
| Rydde modellkapitlet (ikke repetere kap. 4) | OK | Kapittel 6 refererer til kapittel 4 uten å kopiere figurer |
| Velge log-transformasjon for stasjonaritetsvurdering | OK | Gjennomgående i skript 02 og rapporten |
| Teste for stasjonaritet og velge differensiering | OK | ADF + KPSS med fire varianter, tabell 7.1, begrunnet valg |
| Analysere ACF og PACF | OK | Figur 7.2 med 36 lags og faglig tolkning |
| Velge SARIMA-spesifikasjon | OK | Grid search, tabell 7.2, konsistent med ACF/PACF |
| Estimere modellparametere | OK | MLE, tabell 7.3, alle parametere signifikante |
| Gjennomføre review og lukke aktiviteten | Denne reviewen | Aktiviteten kan lukkes etter at tiltak er vurdert |
| ACT-3.2-C01: Valgt modell er begrunnet | OK | SARIMA(0,1,1)(0,1,1)₁₂ begrunnet med tester, ACF/PACF og AIC/BIC |
| ACT-3.2-C02: Parametere estimert og dokumentert | OK | Tabell 7.3, kompakt og utvidet form i rapporten |
| REQ-003: Trend og sesong modelleres | OK | Differensiering ($d=1, D=1$) og MA-ledd håndterer begge |
| REQ-008: Analyse kan etterprøves | OK | Skript, artefakter og rapport henger sammen steg for steg |

---

## Samlet vurdering

### Metodikk

Arbeidet er faglig solid. Modellvalget bygger på en ryddig prosess fra datavurdering via stasjonaritetstester og ACF/PACF til systematisk kandidatsøk med informasjonskriterier. De to viktigste metodiske observasjonene (V1 og V2) handler om at det genererte artefaktet for differensieringsvurdering avviker fra rapporten, og at kandidatsøket kun dekker én differensieringsvariant. Ingen av disse undergraver det endelige modellvalget, men de bør kommenteres for sporbarhet og faglig åpenhet.

### Språk, innhold og figurer

Rapportteksten i kapittel 6 og 7.1–7.3 er velskrevet, med tydelige overganger mellom seksjoner og en god balanse mellom formell matematikk og forklarende tekst. Figurer og tabeller følger CLAUDE.md-formatet konsistent. Figurnummereringsgapet (V3) og mellomromsfeilen i tabell 7.1 (F1) er mindre kosmetiske funn.

### Anbefalt prioritering videre

1. ~~**(Bør)** Avstem artefakt og rapporttekst om differensieringsvalg (V1) – enten oppdater tabellen eller legg til en tydelig note i rapporten.~~
2. ~~**(Bør)** Kommenter i rapporten at kandidatsøket kun dekker $d=1, D=1$ og hvorfor dette er forsvarlig (V2).~~
3. ~~**(Kan)** Rett figurnummerering (V3) og mellomrom i tabell 7.1 (F1).~~
4. ~~**(Kan)** Utvid README med arbeidsflyt (F2).~~
