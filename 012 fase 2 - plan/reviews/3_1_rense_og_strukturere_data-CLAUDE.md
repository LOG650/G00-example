# Review av aktivitet 3.1 – Rense og strukturere data

**Reviewer:** Claude (Opus 4.6)
**Dato:** 2026-03-16 (oppdatert etter tiltak)
**Aktivitetsmappe:** `006 analysis/aktiviteter/3_1_rense_og_strukturere_data`
**Planreferanse:** Aktivitet «Rense og strukturere data», planlagt 2026-03-09 til 2026-03-11

---

## Sammendrag

Den opprinnelige reviewen identifiserte to svakheter (V1, V2), fire forbedringsforslag (F1–F4) og fem styrker. Fire av seks tiltak er nå gjennomført (V1, V2, F1, F4), og rapporten er oppdatert med nye artefakter. I tillegg er funn fra CODEX-reviewen tatt med i vurderingen.

Denne oppdaterte reviewen er delt i to hoveddeler: **1) Metodikk** (beregninger og kode) og **2) Språk, innhold og figurer**.

---

## Avhukningsliste – tiltak fra opprinnelig review

| # | Tiltak | Status | Kommentar |
|:--|:-------|:-------|:----------|
| V1 | Datasplitt reproducerbar fra kode | [x] Gjennomført | Ny funksjon `split_and_save_data()` med `SPLIT_DATE`-konstant og docstring |
| V2 | Glidende gjennomsnitt `min_periods=12` | [x] Gjennomført | Endret fra `min_periods=1` til `min_periods=12` |
| F1 | CV og IQR i dataoversikten | [x] Gjennomført | To nye rader i `build_data_overview_table()` og tabell 5.1 i rapporten |
| F2 | Datoakse i figur 1 | [ ] Ikke gjort | Brukervalg – beholdt observasjonsnummer med sekundær årsakse |
| F3 | Månedsnavn i månedsprofiltabell | [ ] Ikke gjort | Brukervalg – beholdt månedsnummer |
| F4 | Boksplott for sesongvariasjon | [x] Gjennomført | Ny funksjon `save_figure_4()` og figur 4.4 i rapporten |
| — | Rapport oppdatert med artefakter | [x] Gjennomført | Tabell 5.1 med CV/IQR, splitbegrunnelse i 5.2, figur 4.4 i 4.3 |

---

## Styrker (uendret fra opprinnelig review)

- **S1.** Ryddig mappestruktur med `fig_`/`tab_`-prefikser iht. CLAUDE.md.
- **S2.** Komplett tidsserie – 210 observasjoner, 0 manglende måneder, eksplisitt dokumentert.
- **S3.** Grundig sesongprofil med gjennomsnitt, standardavvik og rangering per måned.
- **S4.** God håndtering av delåret 1981 via `get_full_years_only()`.
- **S5.** Datakvalitetsantagelsen er eksplisitt formulert som arbeidsantagelse.

---

## Del 1 – Metodikk (beregninger og kode)

### 1.1 Datasplitt (`split_and_save_data()`) – V1

Funksjonen splitter korrekt ved `SPLIT_DATE = "1978-01-01"` og produserer:
- `sales_train.csv`: 168 observasjoner (1964-01 til 1977-12)
- `sales_test.csv`: 42 observasjoner (1978-01 til 1981-06)

Verifisert: 168 + 42 = 210. Splitten bevarer hele kalenderår i treningsdatasettet. Begrunnelsen er dokumentert i docstringen. Logger antall observasjoner til terminalen som anbefalt.

**Vurdering:** Korrekt og tilstrekkelig. Oppfyller nå REQ-008 for datasplittsteget.

### 1.2 Glidende gjennomsnitt – V2

Endret til `min_periods=12`. De første 11 datapunktene får nå `NaN` i stedet for ustabile gjennomsnitt. Figur 1 viser nå kurven først fra observasjon 12, noe som er faglig riktig.

**Vurdering:** Korrekt endring.

### 1.3 Variasjonskoeffisient og IQR – F1

- CV beregnes som `std / mean * 100` = 57,9 %. Korrekt formel.
- IQR beregnes som `Q3 - Q1` = 2680,75. Korrekt formel.

Begge verdiene er lagt til i `build_data_overview_table()` og gjenspeilt i tabell 5.1 i rapporten.

**Vurdering:** Korrekt og konsistent mellom genererte artefakter og rapport.

### 1.4 Boksplott – F4

Funksjonen `save_figure_4()` bruker `full_years_df` (ekskluderer 1981), noe som er korrekt for å unngå skjevhet fra delåret. Én boks per kalendermåned (1–12) med `patch_artist=True` for fargelagt visning.

**Vurdering:** Korrekt datagrunnlag og fremstilling. Figuren viser tydelig at august har svært lav variasjon, mens november og desember har størst spredning – begge deler konsistent med månedsprofiltabellen.

### 1.5 Gjenstående metodiske observasjoner

- **Utgangsfiler mangler anførselstegn rundt Sales:** De opprinnelige filene (`sales.csv`) har `Sales` som heltall uten anførselstegn, mens `sales_train.csv` og `sales_test.csv` skrives med anførselstegn rundt `Sales`-verdiene (f.eks. `"2815"` i stedet for `2815`). Dette er en formatforskjell som ikke påvirker funksjonaliteten, men som gjør at de genererte filene ikke er byte-identiske med originalene. For konsistens kan `quoting=csv.QUOTE_MINIMAL` legges til i `to_csv()`-kallet.

---

## Del 2 – Språk, innhold og figurer

### 2.1 Ny tekst i avsnitt 5.2 – datasplittbegrunnelse

**Rapport.md linje 203:**

> «For å kunne validere modellen på en ryddig måte er datasettet delt i to deler ved nyttår 1977/1978. Treningsdatasettet dekker perioden 1964-01 til 1977-12 (168 observasjoner), mens testdatasettet dekker 1978-01 til 1981-06 (42 observasjoner). Splitdatoen er valgt slik at treningsdatasettet inneholder utelukkende hele kalenderår, noe som bevarer sesongstrukturen for SARIMA-modellering. Forholdet mellom trenings- og testdata blir omtrent 80/20, og gir et tydelig skille mellom datagrunnlaget som brukes til modellestimering og datagrunnlaget som brukes til å vurdere prognoseegenskaper.»

**Språk:** Korrekt norsk, ingen skrivefeil. Setningen som begynner med «Splitdatoen er valgt slik at…» er lang (35 ord) og dekker tre poeng (hele kalenderår, sesongstruktur, SARIMA). Vurder å dele den for bedre lesbarhet.

**Faglig innhold:** Begrunnelsen er presis og relevant. Kobler splitvalget til sesongbevaring for SARIMA, noe som er faglig forsvarlig.

### 2.2 Ny tekst i avsnitt 4.3 – boksplottfigur

**Rapport.md linje 173:**

> «Figur 4.4 viser spredningen i salget innad i hver kalendermåned over alle fullførte år. Boksplottet supplerer gjennomsnittsfiguren ved å synliggjøre variasjonsbredden og eventuelle utliggere for hver måned.»

**Funn:**
- ~~«gjennomsnittsfiguren» bør referere eksplisitt til «figur 4.3» for tydelighet.~~ Rettet – teksten refererer nå til «figur 4.3».
- ~~Figur 4.4 mangler forklarende tekst *etter* figuren.~~ Rettet – forklarende setning lagt til etter figuren, konsistent med figur 4.1–4.3.

### 2.3 Tabell 5.1 – konsistens

Tabellen i rapporten (linje 207–220) stemmer nå overens med den genererte `tab_01_dataoversikt.md`. Alle 12 rader er korrekte. Tabellformatet følger Markdown-standarden.

### 2.4 Figurer – rapportklarhet

| Figur | Tittel i figur | Rapportklarhet |
|:------|:---------------|:---------------|
| 4.1 | «Månedlig salg per observasjon (1964-1981)» | OK – tydelig og beskrivende |
| 4.2 | «Årlig totalsalg for fullførte år» | OK |
| 4.3 | «Gjennomsnittlig salg per måned» | OK |
| 4.4 | «Sesongvariasjon i salg per kalendermåned» | OK – god tittel, fargekonsistent med figur 4.3 |

Alle figurer bruker norske titler og akselabeler. Oppløsningen (300 dpi) er tilstrekkelig for rapport.

### 2.5 Funn fra CODEX-reviewen – status og vurdering

CODEX-reviewen (`3_1_..._CODEX.md`) identifiserte fem funn i rapportteksten. Disse gjelder delvis aktivitet 3.1 og delvis senere aktiviteter. Under følger status og vurdering for hvert funn.

| # | CODEX-funn | Alvorlighetsgrad | Status | Tilhører akt. 3.1? |
|:--|:-----------|:-----------------|:-------|:--------------------|
| C1 | Problemstilling (1.1), avgrensinger (1.3) og antagelser (1.4) er tomme | Høy | Åpen | Delvis – antagelser er nevnt i 5.2, men formelt kapittel mangler |
| C2 | Ingen kildehenvisninger for metodiske påstander; litteratur/teori tomme | Høy | Åpen | Nei – tilhører rapportskrivingsaktiviteten |
| C3 | Repetisjon mellom innledning, caseintroen, 4.1 og 4.4 | Middels | Åpen | Delvis – caseteksten ble skrevet i akt. 3.1 |
| C4 | Tabellkolonnenavn er rå feltnavn (`måned_nummer` osv.) | Middels | Åpen | Ja – overlapper F3 som ble avslått av bruker |
| C5 | Flere kapitler helt tomme | Lav | Åpen | Nei – naturlig på dette stadiet |

**Vurdering av CODEX-funn mot aktivitet 3.1:**

- **C1** er delvis relevant. Antagelsen om datakvalitet er allerede dokumentert i avsnitt 5.2, men formelt bør den også stå i 1.4. Problemstillingen (1.1) er strengt tatt ikke en del av aktivitet 3.1, men bør fylles ut snart fordi metode- og datakapitlet allerede gjør faglige valg som forutsetter en definert problemstilling.
- **C3** er et reelt funn. Innledningen (linje 92), caseintroduksjonen (linje 114), beslutningssituasjonen (linje 120) og avsnitt 4.4 (linje 183) sier fire varianter av at PowerHorse trenger bedre prognoser fordi etterspørselen varierer. Anbefaling: Stram inn slik at innledningen kort motiverer og casen beskriver – la ikke begge gjøre begge deler.
- **C4** overlapper med F3 (månedsnavn i tabell) som brukeren valgte å ikke gjennomføre. Vurder likevel å forbedre kolonneoverskriftene i tabellen som allerede står i rapporten, uavhengig av om den genererte tabellen endres.

---

## Samsvar med prosjektplan og krav (oppdatert)

| Sjekkpunkt | Status | Kommentar |
|:---|:---|:---|
| Kontrollere observasjoner per måned | OK | 210 obs., ingen hull, dokumentert i tabell |
| Strukturere tidsserien | OK | Datetime-indeksering, sortering, tilleggskolonner |
| Splitte datasettet i trenings- og testdata | OK | Reproducerbar kode med `split_and_save_data()` |
| Lage grunnleggende visualiseringer | OK | Fire figurer med relevante perspektiver |
| Dokumentere datakvalitet | OK | Nøkkeltabell med CV og IQR, eksplisitt antagelse |
| Bekrefte komplett og riktig indeksert dataserie | OK | Sjekket via `period_range` med 0 manglende måneder |
| Sette inn tekst og figurer i rapport.md | OK | Figurer 4.1–4.4, tabell 4.1, tabell 5.1 og splitbegrunnelse |
| Lukke aktiviteten | Kan lukkes | Alle tekniske krav oppfylt |
| REQ-008 Etterprøvbar analyse | OK | Datasplitt, figurer og tabeller er nå alle etterprøvbare |

---

## Samlet vurdering

### Metodikk
Alle implementerte tiltak (V1, V2, F1, F4) er faglig korrekte. Beregninger, splittlogikk og figurgenering er verifisert. Den eneste gjenstående observasjonen er en liten formatforskjell i CSV-anførselstegn (avsnitt 1.5), som er kosmetisk.

### Språk, innhold og figurer
Rapportteksten er språklig god. To konkrete forbedringspunkter er nå rettet:
1. ~~Figur 4.4 mangler forklarende tekst etter figuren.~~ Rettet.
2. ~~Introduksjonssetningen til figur 4.4 bør referere eksplisitt til «figur 4.3».~~ Rettet.

Fra CODEX-reviewen er det mest presserende funnet repetisjon mellom innledning og casekapittel (C3), og at problemstillingen (1.1) bør formuleres snart fordi metode- og datakapitlet allerede bygger på faglige valg (C1). Disse funnene blokkerer ikke lukking av aktivitet 3.1, men bør adresseres før rapportutkastet.

### Anbefalt prioritering videre

1. ~~**(Bør, raskt)** Legg til forklarende tekst etter figur 4.4 og referer til figur 4.3 eksplisitt.~~ Gjort.
2. **(Bør, snart)** Formuler problemstilling (1.1) og antagelser (1.4) slik at rapporten har faglig styring.
3. **(Bør, snart)** Stram inn repetisjon mellom innledning og casekapittel (C3).
4. **(Kan)** Språkvask tabellkolonner i rapporten til leservennlige overskrifter (C4).
