# Review av aktivitet 3.10 – «Sammenstille rapportutkast»

**Reviewer:** Claude (automatisert review, uavhengig subagent)
**Dato:** 2026-04-29
**Aktivitetsmappe:** Ikke en analyseaktivitet — sammenstillingsarbeidet er gjort direkte i `005 report/rapport.md` og planfilene
**Planreferanse:** Aktivitet ACT-3.10, planlagt 2026-04-21 til 2026-04-27, milepæl MS-005 (2026-04-27)

---

## Sammendrag

ACT-3.10 leverer et fullstendig hovedutkast av PowerHorse-rapporten med sammendrag, abstract, oppdatert innholdsfortegnelse, ferdig bibliografi (15 oppføringer i alfabetisk rekkefølge) og tre vedlegg. Alle syv overførte forbedringsforslag fra ACT-3.5, ACT-3.6 og ACT-3.9 er implementert i selve rapportteksten, og nøkkeltall (SARIMA(0,1,1)(0,1,1)_{12}, MAPE 5,4 %, ~100 400 enheter, 7:1 sesongamplitude, 36 kandidater) er konsistente på tvers av sammendrag, abstract, kap. 7–9 og kap. 10. Konklusjonskapitlet er reformulert til å være selvstendig og inneholder en konkret handlingsfølge med tallforankrede terskler. Reviewen identifiserer 6 styrker, 4 svakheter og 5 forbedringsforslag. Hovedfunnet er at selve rapportteksten er klar for peer review, men at planfilene (`status.md`, `schedule.json`) og git-historikken ikke er oppdatert til å reflektere at ACT-3.10 faktisk er gjennomført — alle sjekklistepunkter står fortsatt som ubekreftede `[ ]` og status er `not-started`/`not-passed`.

---

## Styrker

- **S1.** Sammendraget (~197 ord) og abstract (~242 ord) speiler hverandre konsistent og dekker problem, metode, hovedfunn og konklusjon. Nøkkeltall (SARIMA(0,1,1)(0,1,1)_{12}, MAPE 5,4 %, om lag 100 400 enheter, 7:1 sesongamplitude, 36 kandidater, treningsperiode januar 1964 til juni 1981) er gjengitt korrekt og samsvarer med detaljerte tall i kapittel 7–9. Begge er på passende lengde og holder god språklig kvalitet på henholdsvis norsk og engelsk.

- **S2.** Innholdsfortegnelsen (linjene 81–132) er fullstendig oppdatert. Underseksjoner for kap. 4 (4.1–4.4), kap. 6 (6.1–6.3), kap. 7 (7.1–7.4), kap. 8 (8.1–8.2) og kap. 9 (9.1–9.6) er nå listet, kap. 6 er korrekt navngitt «Modell» (ikke «Modellering»), og de tre vedleggene (A, B, C) er inkludert. En manuell sjekk viser at alle ankerlenker matcher de faktiske overskriftene i rapporten.

- **S3.** Bibliografien har 15 oppføringer i alfabetisk rekkefølge B–D–D–E–G–H–J–K–L–M–M–P–P–S–S, og samtlige oppføringer er sitert minst én gang i kroppen (Box et al. 9 forekomster, Ljung 11, Hyndman 12, ned til Silver/Polina/Makoni/Makridakis/Petropoulos/Guimarães/De Gooijer som hver har minst 3 forekomster). APA7-formatet er konsistent med kursiverte tidsskrift- og boktitler, fullstendige DOI-er for tidsskriftartiklene og forlag for bøkene.

- **S4.** Vedleggene er reelt nyttige supplementer, ikke duplikater. Vedlegg A inneholder alle 36 SARIMA-kandidater (mot Tabell 7.2 som viser bare topp 10), Vedlegg B inneholder måned-for-måned testsettprognose for alle 42 testmåneder (mot Tabell 8.1 som viser tre aggregerte feilmål) og Vedlegg C peker til faktiske, eksisterende analyseartefaktmapper (`3_1_rense_og_strukturere_data/`, `3_2_velge_og_estimere_modell/`, `3_3_validere_modell/`, `3_4_lage_prognose_og_anbefalinger/`, `3_7_skrive_teorikapittel/`). En reproducerbarhetssjekk viser at alle fem mappene faktisk eksisterer i `006 analysis/aktiviteter/`.

- **S5.** Alle syv overførte forbedringsforslag er implementert: ACT-3.5 F1 (avgrensing 4 fokuserer nå på dataperioden og henviser eksplisitt til antagelse 2 i seksjon 1.4), F2 (tredje avsnittet om rapportens oppbygging er fjernet — innledningen består nå av to avsnitt), F3 (prognoseperioden «juli 1981 til juni 1982» er presisert direkte i problemstillingen). ACT-3.6 F4 (kort begrunnelse for hvorfor normalitet er relevant er lagt til i seksjon 2.4: kobling til MLE-estimering og prediksjonsintervaller). ACT-3.6 F5 (`ref_hyndman_athanasopoulos_2021.md` er utvidet med MASE og biaskorreksjon, jf. linjene 13–14, 19, 21 i den filen). ACT-3.9 F2 (konklusjonen er omformulert til selvstendig prosa med detaljer som ikke gjentar 9.6 ordrett — eksempelvis treningsperiode, testperiode, parsimonipoeng) og F4 (konkret handlingsfølge med terskler: lageroppbygging i august–september, behov på ~34 700 enheter i nov–des med toppmåneden desember på 19 500 enheter, periodisk reestimering hvert kvartal).

- **S6.** Konsistenskontroll av kvantitative tall: Vedlegg B-tabellen reproduserer Tabell 8.1-feilmålene innenfor avrundingsforskjell (uavhengig kontrollberegning ga MAE = 415,18 mot rapportert 415,17, MAPE = 5,40 % mot 5,39 %, RMSE = 494,14 mot 494,13). Refittede parametere i Tabell 9.1 er konsistente med tallene oppgitt i kap. 8.2 (θ₁ = -0,82, Θ₁ = -0,62, σ̂² = 0,012). Sesongkategoriseringen i Tabell 9.2 er konsistent med Tabell 8.2.

---

## Del 1 – Metodikk (konsistens og korrekt implementasjon av overførte forbedringsforslag)

### 1.1 Konsistens i sammendrag og abstract

Sammendraget er på 197 ord og abstract på 242 ord. Begge dekker de fire kjernedelene problem-metode-hovedfunn-konklusjon i samme rekkefølge, og oppgir identiske nøkkeltall: 36 kandidater, MAPE 5,4 %, sesongamplitude 7:1, samlet salgsvolum ~100 400 enheter, treningsperiode 1964–1981, testperiode 1978–1981. Nivåbias og residualbrudd er nevnt i begge. Modellnavnet SARIMA$(0,1,1)(0,1,1)_{12}$ er gjengitt med samme matematiske notasjon. Setningsbygningen i abstract er noe rikere på detaljer enn på norsk (forskjell på 45 ord), noe som henger sammen med litt mer ordrike formuleringer på engelsk og bruk av komma som tusensepartor (100,400) — men det er ingen substansielle innholdsforskjeller.

**Vurdering:** Sammendrag og abstract er innholdsmessig konsistente og lingvistisk velkonstruerte.

### 1.2 Konsistens for nylig endrede deler

**Kapittel 1 Innledning.** ACT-3.5 F1, F2 og F3 er alle implementert. Avgrensing 4 (linje 165) sier nå: «Datasettet dekker perioden januar 1964 til juni 1981, og analysen er begrenset til denne perioden. Forhold som ligger utenfor dataperioden er ikke modellert eksplisitt. Antagelsen om at de historiske mønstrene fortsatt er gyldige i prognoseperioden behandles separat under antagelse 2 i seksjon 1.4.» Dette skiller eksplisitt mellom dataperioden (avgrensing) og relevansantagelsen (antagelse). Innledningen består nå av to avsnitt — avsnittet om rapportens oppbygging er fjernet. Problemstillingen (linje 144) inkluderer nå «(juli 1981 til juni 1982)».

**Seksjon 2.4 Residualdiagnostikk og modellforutsetninger.** ACT-3.6 F4 er implementert. Setningen (linje 205): «Normalitet er relevant fordi maksimum likelihood-estimering av SARIMA-parametere og de tilhørende prediksjonsintervallene baserer seg på en antakelse om tilnærmet normalfordelte residualer; betydelige avvik svekker dermed presisjonen i konfidensintervaller og prognoseusikkerhetsmål.» Begrunnelsen er kort, korrekt og koblet til de senere bruksstedene i kap. 7.4 og 9.2.

**Kapittel 10 Konklusjon.** ACT-3.9 F2 og F4 er implementert. Konklusjonen (linjene 925–935) er fem avsnitt med selvstendig formulering — ingen setninger er ordrett kopi av 9.6. F4 leverer en operativ handlingsfølge med konkrete tall: lageroppbygging i august–september, høysesongbehov ~34 700 enheter med desembertopp på 19 500, og periodisk reestimering hvert kvartal.

**Vurdering:** Alle tre nylig endrede deler implementerer overførte forbedringsforslag korrekt og er internt konsistente.

### 1.3 Sammendrag og abstract — speilingskontroll

Setning-for-setning-sammenligning gir ingen avvik på substansnivå. Begge tekstene starter med samme grunninnsikt (sesongavhengig etterspørsel og pålitelige prognoser), introduserer caset, beskriver Box-Jenkins-metodikken, navngir modellen, oppgir MAPE, beskriver sesongprofilen, oppgir kvantitative resultater og konkluderer med samme nyanse om at modellen gir et nyttig, men ikke uttømmende, beslutningsgrunnlag.

**Vurdering:** God speiling.

### 1.4 Innholdsfortegnelsen — anker mot faktiske overskrifter

Manuell sammenligning av alle 49 ankerlenker i innholdsfortegnelsen (linjene 81–132) mot de faktiske overskriftene (linjene 136 og utover) gir 100 % treff. Spesielt:
- Kapittel 6 er listet som «Modell» i innholdsfortegnelsen og som «## 6 Modell» i kroppen.
- Underseksjonene for kap. 4 (4.1–4.4), 6 (6.1–6.3), 7 (7.1–7.4), 8 (8.1–8.2) og 9 (9.1–9.6) er listet og samsvarer med kroppen.
- Vedlegg A, B og C er inkludert med korrekte ankerlenker (`#vedlegg-a--fullstendig-oversikt-over-evaluerte-sarima-kandidater`, osv.).
- Ingen «Modellering» eller parentesbemerkning for kap. 5 — de to spesifikke korreksjonsstegene fra ACT-3.10-planen er gjennomført.

**Vurdering:** Innholdsfortegnelsen er korrekt og fullstendig.

### 1.5 Bibliografi — alfabetisk rekkefølge og siteringskontroll

Bibliografien (linjene 939–969) inneholder 15 oppføringer:

1. Box, Jenkins, Reinsel & Ljung (2015) — B
2. De Gooijer & Hyndman (2006) — D
3. Dickey & Fuller (1979) — D
4. Engle (1982) — E
5. Guimarães, Marques & Tortato (2020) — G
6. Hyndman & Athanasopoulos (2021) — H
7. Jarque & Bera (1987) — J
8. Kwiatkowski et al. (1992) — K
9. Ljung & Box (1978) — L
10. Makoni & Chikobvu (2023) — M
11. Makridakis, Spiliotis & Assimakopoulos (2020) — M
12. Petropoulos et al. (2022) — P
13. Polina, Ganesan, Karunarathne & Somasiri (2024) — P
14. Shumway & Stoffer (2017) — S
15. Silver, Pyke & Thomas (2017) — S

Alfabetisk rekkefølge B–D–D–E–G–H–J–K–L–M–M–P–P–S–S er korrekt. APA7-format er konsistent: forfatterliste med komma og ampersand, årstall i parentes, kursivert tittel for bøker / kursivert tidsskrift med volum (utgave) for artikler, sidetall, og DOI/URL der det finnes. En siteringssjekk viser at alle 15 oppføringer brukes minst én gang i kroppen.

**Vurdering:** Bibliografien er fullstendig og veletablert som referanseapparat.

### 1.6 Vedleggene — nytte og reproduserbarhet

**Vedlegg A** (Tabell A.1) lister alle 36 SARIMA-spesifikasjoner sortert etter AIC. Dette er en faglig nyttig utvidelse av Tabell 7.2 (topp 10) som lar leseren etterprøve hele modellrangeringen.

**Vedlegg B** (Tabell B.1) lister 42 testmåneder med observert salg, prognose, feil, absolutt feil og prosentfeil. En uavhengig kontrollberegning på dataene gir MAE = 415,18, MAPE = 5,40 % og RMSE = 494,14, som matcher Tabell 8.1 (415,17 / 5,39 % / 494,13) innenfor avrundingsforskjell.

**Vedlegg C** (Tabell C.1) peker til fem aktivitetsmapper i `006 analysis/aktiviteter/`. Sjekk av filsystemet bekrefter at alle fem mappene eksisterer (`3_1_rense_og_strukturere_data`, `3_2_velge_og_estimere_modell`, `3_3_validere_modell`, `3_4_lage_prognose_og_anbefalinger`, `3_7_skrive_teorikapittel`). Vedlegg C nevner også undermappestrukturen `scripts/`, `figurer/`, `resultat/` og rådata i `004 data/`.

**Vurdering:** Alle tre vedleggene er reelle, nyttige supplementer som unngår duplisering med hovedteksten.

### 1.7 Cross-references — peker referansene til riktig sted?

Stikkprøvekontroll av kapittel-, tabell- og figurreferanser:
- «kapittel 6.2» (linje 175 i seksjon 1.4) → 6.2 Modellantagelser eksisterer (linje 527). OK.
- «kapittel 7.4» (flere steder) → 7.4 Validering eksisterer (linje 719). OK.
- «kapittel 8.1» og «8.2» → 8.1 (linje 750), 8.2 (linje 773). OK.
- «kapittel 9.5» (linje 195) → 9.5 Begrensninger (linje 893). OK.
- «Tabell 7.2» (kap. 7.2 og 9.2) → eksisterer (linje 664–676). OK.
- «Tabell 7.3» (kap. 9.1) og «Tabell 9.1» → begge eksisterer (linje 685–693, 830–836). OK.
- «Tabell 8.1» og «Tabell 8.2» → begge eksisterer. OK.
- «Tabell 9.1» og «Tabell 9.2» → begge eksisterer. OK.
- «Figur 7.1», «Figur 7.2», «Figur 7.3», «Figur 8.1», «Figur 8.2», «Figur 9.1» → alle eksisterer. OK.
- «Figur 4.4 i casebeskrivelsen» (kap. 9.2, linje 846) → 4.4 eksisterer. OK.
- «Figur 9.1» henvises til både i begynnelsen og slutten av kap. 9 — figuren er definert tidlig (linje 818) og refereres til konkret igjen i 9.5 (linje 909). OK.
- Alle Box et al. (2015), Hyndman & Athanasopoulos (2021), Silver et al. (2017) osv.-siteringer matcher bibliografien.

**Vurdering:** Ingen feilreferanser oppdaget i stikkprøvene.

### Gjenstående metodiske observasjoner

To mindre observasjoner notert under svakheter (V3 og F2 nedenfor) — den ene gjelder en intern inkonsistens mellom kap. 8.2 og kap. 9.3 om størrelsen på biaskorreksjonen, og den andre gjelder at kap. 9 har én Box et al. (2015)-sitering med kapittelangivelse mens andre Box-siteringer ikke har det.

---

## Del 2 – Språk, innhold og figurer

### 2.1 Kapitteloverganger

Overgangen fra kap. 9 (Diskusjon) til kap. 10 (Konklusjon) er logisk og bygger på diskusjonens funn uten å være redundant. Konklusjonen åpner med at modellen er nyttig, men ikke uttømmende — dette er en direkte konsekvens av drøftingene i 9.2 (residualbrudd), 9.3 (bias), 9.4 (kapasitetsplanlegging) og 9.5 (begrensninger). Konklusjonen tilfører tallforankrede operative anbefalinger som ikke står som handlingsfølge i 9.4.

Overgangen fra kap. 8 (Resultat) til kap. 9 (Diskusjon) er også god. Avsnittet på linje 807 («En detaljert drøfting av praktiske implikasjoner og modellbegrensninger følger i kapittel 9») fungerer som broavsnitt.

Mindre observasjon: Kap. 5.2 (Data) avsluttes med Tabell 5.1 og går direkte over i «## 6 Modell» uten et overgangsavsnitt som forbereder leseren på modellkapitlet. Dette er ikke en feil, bare en stilmessig observasjon (F1 nedenfor).

### 2.2 Sammendrag — språk og lengde

Sammendraget er ~197 ord (litt på lavsiden av 200–300-rekkevidden, men akseptabelt). Språket er klart og fagteknisk presist. Setningen «gir et samlet salgsvolum på om lag 100 400 enheter og en sesongamplitude på 7:1 mellom topp- og bunnmåneden» er presis og tallforankret. Avslutningssetningen «sesongstrukturen er det sterkeste signalet, mens de absolutte nivåene bør tolkes med forbehold og suppleres med markedsinnsikt og operative ordredata» er en god oppsummerende konklusjon som matcher kap. 10.

### 2.3 Abstract — språk og lengde

Abstract er ~242 ord, et passende toppnivå men 45 ord lengre enn sammendraget. Engelsken er flytende og presis. «Box-Jenkins methodology» (med bindestrek), «AIC and BIC» og bindestrekene rundt «log-transformed» og «test set» er konsistente. Komma som tusensepartor (100,400) er korrekt på engelsk. Talluttrykket «5.4%» (uten mellomrom) på engelsk vs «5,4 %» (med mellomrom) på norsk er begge i samsvar med språkkonvensjonene.

### 2.4 Bibliografi og vedlegg — lesbarhet

Bibliografien er innrykket konsistent uten kulepunkter, slik APA7 forutsetter. DOI-er er klikkbare lenker. Ingen blandet typografi.

Vedlegg A (Tabell A.1) er kompakt nok til å passe på én side i de fleste rendringer (36 rader × 9 kolonner). Vedlegg B (Tabell B.1) er på 42 rader × 6 kolonner og strekker seg over ca. én side. Vedlegg C er kort og oversiktlig.

### 2.5 Innholdsfortegnelsen

Som dokumentert i 1.4 over: TOC er korrekt og fullstendig. Den lille observasjonen som verdt å merke er at vedleggene står som underseksjoner under «12 Vedlegg» med to-bindestrek-prefiks (`Vedlegg A —`), noe som er en stilistisk konvensjon som er konsistent gjennom hele rapporten.

### 2.6 Figurer — overordnet sjekk

Alle figurer (3.1–3.4, 4.1–4.4, 7.1–7.3, 8.1–8.2, 9.1) bruker den foreskrevne HTML-strukturen med `width="80%"`, sentrering og kursivert figurtekst. Stiene refererer til faktiske bilder i `006 analysis/aktiviteter/...`. Manuell stikkprøve på fig_01–fig_04 i 3_7_skrive_teorikapittel og fig_01–fig_04 i 3_1_rense_og_strukturere_data viser at filene eksisterer.

### 2.7 Tabeller — konsistens og lesbarhet

Tabellene 4.1, 5.1, 7.1, 7.2, 7.3, 7.4, 8.1, 8.2, 9.1, 9.2, A.1, B.1 og C.1 er alle nummerert, har kursivert tabelltekst og er introdusert med en setning før de presenteres — i samsvar med CLAUDE.md.

Mindre stilobservasjon: Tabell 5.1 mangler en eksplisitt tabelltekst nederst (det er bare en innledningssetning), mens andre tabeller har det. Dette er en pre-eksisterende stilinkonsistens fra ACT-3.1, ikke ACT-3.10s ansvar — men den er passende å notere her som F4 nedenfor siden ACT-3.10 inkluderer «Konsistenssjekk» som sjekkpunkt.

---

## Svakheter og forbedringsforslag

### V1. Endringene er ikke committet til git

**Alvorlighetsgrad:** Høy
**Kategori:** Prosess

`git status` viser `M 003 references/theory/md/ref_hyndman_athanasopoulos_2021.md`, `M 005 report/rapport.md`, `M 012 fase 2 - plan/schedule.json` og `M 012 fase 2 - plan/status.md` som modifisert i arbeidskopien, samt syv nye `??`-referansefiler og to nye review-filer (3.6 og 3.9) som er utracked. ACT-3.10 leverer altså rapportutkastet i arbeidskopien, men ikke i git-historikken. For sporbarhet og som forutsetning for at peer review skal kunne hentes ut fra et stabilt commit-punkt, må endringene committes før aktiviteten lukkes.

### V2. Status.md og schedule.json reflekterer ikke at ACT-3.10 er gjennomført

**Alvorlighetsgrad:** Høy
**Kategori:** Prosess / Sporbarhet

I `status.md` står alle 15 sjekklistepunktene for ACT-3.10 som ubekreftede `[ ]` (linjene 156–179). I fremdriftstabellen (linje 37) står ACT-3.10 som «Ikke startet». I `schedule.json` (linje 758) har ACT-3.10 status `not-started` og `percentComplete: 0`, og alle tre kriteriene (C01–C03) har status `not-passed` med tomme `result`-felt. Likevel er sammendrag, abstract, oppdatert TOC, ferdig bibliografi, alle tre vedlegg og alle syv overførte forbedringsforslag implementert i rapport.md. Planfilene må oppdateres til å reflektere det faktiske arbeidet, ellers er prosjektets sporbarhet brutt mellom innhold og styringsgrunnlag.

I tillegg: Status.md (linje 216) bruker fortsatt «6 Modellering | Ferdig» i rapportstatustabellen, mens TOC og kroppen er rettet til «Modell». Linjen bør oppdateres for konsistens.

### V3. Liten talluinkonsistens om biaskorreksjonens størrelse mellom kap. 8.2 og kap. 9.3

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold (intern konsistens)

Kapittel 8.2 (linje 805) sier: «oppjusteringen er marginal (ca. 0,6 %)». Kapittel 9.3 (linje 860) sier: «For denne modellen er korreksjonsfaktoren liten — fra om lag 0.6 % ved horisont 1 til om lag 0.8 % ved horisont 12». Tallene er teknisk konsistente (8.2 oppgir gjennomsnittsfaktor og 9.3 oppgir endepunktene), men leseren kan oppfatte dem som motstridende på første gjennomlesning. En kort presisering i kap. 8.2 kunne avhjulpet det. Dette er en finpussobservasjon, ikke en faktafeil.

### V4. Sammendrag (197 ord) er ~45 ord kortere enn abstract (242 ord)

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

CLAUDE.md sier ikke eksplisitt at sammendrag og abstract skal ha lik lengde, men det er en utbredt konvensjon i akademisk skriving. Sammendraget kan utvides med 30–40 ord (for eksempel ved å legge til en setning om treningsperiodens lengde og testperiodens lengde, eller en kort referanse til at modellen er den enkleste blant alle 36 kandidater) for å oppnå bedre symmetri. Alternativt kan abstract forkortes noe.

### F1. Vurder kort overgangsavsnitt fra kap. 5 til kap. 6

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Kapittel 5.2 avsluttes direkte med Tabell 5.1, og kapittel 6 starter uten et tema-introduserende avsnitt. Et kort broavsnitt (én til tre setninger) som forbereder leseren på at metodevalget «en SARIMA-tilnærming» fra 5.1 skal konkretiseres til en formelt definert modell, kunne styrke den narrative flyten. Dette er en finpussobservasjon.

### F2. Vurder å gjøre Box et al. (2015)-siteringene konsistente i kapittelangivelser

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold (sitering)

Linje 824 og 850 har «Box et al., 2015, kap. 9» og linje 850 har «Hyndman & Athanasopoulos, 2021, kap. 9», mens andre Box et al.-siteringer (linjene 187, 191, 193, 195, 311, 319, 325) skriver kun «(Box et al., 2015)» uten kapittelangivelse. APA7 anbefaler kapittel- eller sideangivelser for direkte påstander. En konsistent praksis (enten alle siteringer med kapittelangivelse eller bare de som direkte siterer en spesifikk passasje) er lett oppnåelig.

### F3. Vurder å nevne kort i sammendraget at log-transformasjon er brukt

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Sammendraget nevner «den log-transformerte salgsserien» i parentes, men kan styrkes ved å si eksplisitt «på den log-transformerte salgsserien for å stabilisere variansen» — det er en metodisk nøkkelvalg som er sentralt for tolkningen og som blir drøftet i kap. 9.1. Tilsvarende kan abstract få samme nyanse.

### F4. Tabell 5.1 mangler kursivert tabelltekst nederst

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold (stilkonsistens)

Tabell 5.1 har en innledningssetning («Tabell 5.1 oppsummerer de viktigste egenskapene ved datasettet.») men ingen kursivert tabelltekst nederst, slik alle andre tabeller i rapporten har. ACT-3.10 inkluderer «Konsistenssjekk av hele utkastet» i sjekklisten, og dette er nettopp typen stilinkonsistens som bør fanges opp der. En kort kursivert tekst som «Tabell 5.1 Datasettets nøkkelegenskaper.» under tabellen ville harmonisert stilen.

### F5. Vedlegg C kan oppgi at status.md inneholder fullstendig artefaktoversikt

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Tabell C.1 nevner ACT-3.1, 3.2, 3.3, 3.4 og 3.7, men ikke at det også finnes en mer detaljert oversikt i `012 fase 2 - plan/status.md` (under «Analyseartefakter»). En kort henvisning ville styrke sporbarheten. Dette er en finpussobservasjon.

---

## Avhukingsliste – tiltak

| #   | Tiltak                                                                                                                                                                | Kategori          | Status | Kommentar                                                          |
| :-- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------- | :----- | :----------------------------------------------------------------- |
| V1  | Committe alle endringer til git (rapport.md, schedule.json, status.md og nye referanse-/review-filer)                                                                 | Prosess           | [ ]    |                                                                    |
| V2  | Oppdatere status.md (15 sjekklistepunkter, fremdriftstabellraden og «Modellering»→«Modell» i rapportstatustabellen) og schedule.json (status, percentComplete, kriterier C01–C03 og lastEvent) til å reflektere at ACT-3.10 er gjennomført | Prosess / Sporbarhet | [ ] |                                                                    |
| V3  | Vurder å presisere i kap. 8.2 at biaskorreksjonen «ca. 0,6 %» er gjennomsnittsverdi over horisonten, slik at det stemmer med 0,6–0,8 %-spennet i kap. 9.3            | Språk og innhold  | [ ]    | Pre-eksisterende, fanget under konsistenssjekk                     |
| V4  | Vurder å utvide sammendrag med 30–40 ord (eller forkorte abstract) for bedre symmetri                                                                                 | Språk og innhold  | [ ]    |                                                                    |
| F1  | Vurder kort overgangsavsnitt mellom kap. 5 og kap. 6                                                                                                                  | Språk og innhold  | [ ]    |                                                                    |
| F2  | Gjøre Box et al. (2015)-siteringene konsistente i kapittelangivelser                                                                                                  | Språk og innhold  | [ ]    |                                                                    |
| F3  | Nevn kort i sammendrag/abstract at log-transformasjon er brukt for variansstabilisering                                                                              | Språk og innhold  | [ ]    |                                                                    |
| F4  | Legge til kursivert tabelltekst nederst i Tabell 5.1                                                                                                                  | Språk og innhold  | [ ]    | Pre-eksisterende stilinkonsistens                                  |
| F5  | Henvise til status.md sin Analyseartefakter-tabell i Vedlegg C for fullstendig artefaktoversikt                                                                      | Språk og innhold  | [ ]    |                                                                    |

---

## Samsvar med prosjektplan og krav

### ACT-3.10 sjekklistepunkter (status.md linjene 156–179)

| Sjekkpunkt                                                                                                                  | Status            | Kommentar                                                                                                           |
| :-------------------------------------------------------------------------------------------------------------------------- | :---------------- | :------------------------------------------------------------------------------------------------------------------ |
| Skrive sammendrag (norsk)                                                                                                   | OK i innhold      | Levert (linjene 59–65). Avhukingen i status.md mangler                                                              |
| Skrive abstract (engelsk)                                                                                                   | OK i innhold      | Levert (linjene 69–75). Avhukingen i status.md mangler                                                              |
| Samle vedlegg i kapittel 12                                                                                                 | OK i innhold      | Tre vedlegg (A, B, C) levert (linjene 977–1087). Avhukingen i status.md mangler                                    |
| Oppdatere innholdsfortegnelse (rette «Modellering» → «Modell» og fjerne parentesbemerkning kap. 5)                          | OK i innhold      | TOC er korrekt (linjene 81–132). Avhukingen i status.md mangler                                                    |
| Ferdigstille kapittel 11 Bibliografi (verifisere alfabetisk rekkefølge og konsistens i 15 oppføringer)                      | OK i innhold      | 15 oppføringer i alfabetisk rekkefølge, APA7-konsistente (linjene 939–969). Avhukingen i status.md mangler         |
| Konsistenssjekk av kapittel 1 Innledning mot fullført rapport (særlig avsnitt om rapportens oppbygging)                     | OK i innhold      | Tredje avsnitt fjernet, problemstilling presisert. Avhukingen i status.md mangler                                  |
| (ACT-3.5 F1) Tydeliggjøre grensen mellom avgrensing 4 og antagelse 2 i kapittel 1                                           | OK i innhold      | Avgrensing 4 fokuserer nå på dataperioden og henviser eksplisitt til antagelse 2. Avhukingen i status.md mangler   |
| (ACT-3.5 F2) Forkorte eller fjerne avsnittet om rapportens oppbygging i kapittel 1                                          | OK i innhold      | Tredje avsnitt fjernet. Avhukingen i status.md mangler                                                              |
| (ACT-3.5 F3) Presisere prognoseperioden (juli 1981 – juni 1982) i problemstillingen i seksjon 1.1                           | OK i innhold      | Prognoseperioden er presisert (linje 144). Avhukingen i status.md mangler                                           |
| (ACT-3.6 F4) Kort forklaring i seksjon 2.4 av hvorfor normalitet er relevant i SARIMA-sammenheng                            | OK i innhold      | Begrunnelse lagt til (linje 205). Avhukingen i status.md mangler                                                    |
| (ACT-3.6 F5) Utvide `ref_hyndman_athanasopoulos_2021.md` med MASE og biaskorreksjon                                         | OK i innhold      | Filen er utvidet (linjene 13–14, 19, 21). Avhukingen i status.md mangler                                            |
| (ACT-3.9 F2) Mer selvstendig formulering av de 9.6-nære setningene i kapittel 10                                            | OK i innhold      | Konklusjonen er omformulert til selvstendig prosa. Avhukingen i status.md mangler                                  |
| (ACT-3.9 F4) Mer konkret PowerHorse-anbefaling med terskelverdier i kapittel 10                                             | OK i innhold      | Konkret handlingsfølge med tall (lager aug–sep, 34 700 enheter nov–des, 19 500 desembertopp, kvartalsvis reestimering) levert. Avhukingen i status.md mangler |
| Intern kvalitetssjekk av hele utkastet                                                                                      | Delvis            | Mindre konsistensobservasjoner gjenstår (V3, F2, F4)                                                               |
| Gjennomføre review og lukke aktiviteten                                                                                     | Pågår             | Denne reviewen                                                                                                       |

### ACT-3.10 kriterier (schedule.json)

| Kriterium      | Beskrivelse                                                                                          | Status        | Kommentar                                                                                  |
| :------------- | :--------------------------------------------------------------------------------------------------- | :------------ | :----------------------------------------------------------------------------------------- |
| ACT-3.10-C01   | Fullstendig hovedutkast foreligger med alle kapitler, sammendrag, abstract, bibliografi og vedlegg   | OK i innhold  | Innholdsmessig levert. Schedule.json viser fortsatt `not-passed` og må oppdateres          |
| ACT-3.10-C02   | Utkastet er klart for peer review                                                                    | OK i innhold (med små forbehold) | Klart etter at V1, V2 (og helst V3, V4) er gjennomført                                    |
| ACT-3.10-C03   | Review er gjennomført og aktiviteten er lukket                                                       | Pågår         | Denne reviewen er gjennomført; lukking forutsetter V1 og V2                                |

### Generelle prosjektkrav

| Krav    | Status        | Kommentar                                                                                                |
| :------ | :------------ | :------------------------------------------------------------------------------------------------------- |
| REQ-006 | OK            | Norsk fagspråk i sammendrag og kropp; engelsk i abstract. Norske bokstaver bevart                       |
| REQ-007 | OK            | Levert til milepæl MS-005 (2026-04-27) per innhold. Planfilene må oppdateres for å bekrefte det        |
| REQ-008 | OK            | Vedlegg C peker til faktiske, etterprøvbare analysemapper                                               |

---

## Samlet vurdering

### Metodikk

Selve sammenstillingsarbeidet er gjennomført med høy kvalitet. Alle syv overførte forbedringsforslag er korrekt implementert og verifisert mot kilden. Sammendrag og abstract er innholdsmessig konsistente og dekker alle fire kjernepunkter i CLAUDE.md sin rapportstrukturanbefaling. Innholdsfortegnelsen, bibliografien og vedleggene er fullstendige, og en uavhengig kontrollberegning på Vedlegg B reproduserer feilmålene i Tabell 8.1 innenfor avrundingsforskjell.

Konsistenskontroller (kvantitative tall, krysshenvisninger, bibliografi-sitering) gir ingen vesentlige avvik. Den eneste tallinkonsistensen er den lille språklige avstanden mellom kap. 8.2 og kap. 9.3 om biaskorreksjonens størrelse (V3), som er teknisk korrekt men kan presiseres.

### Språk, innhold og figurer

Begge språkversjonene (sammendrag på norsk, abstract på engelsk) holder god kvalitet. Alle figurer og tabeller har konsistent stil i samsvar med CLAUDE.md. Konklusjonskapitlet er nå reformulert til å være selvstendig og inneholder en operativ handlingsfølge med tallforankrede terskler.

De identifiserte forbedringsforslagene (F1–F5) er alle finpussbidrag som ikke blokkerer peer review.

### Anbefalt prioritering videre

1. **(Må)** V1 – Committe alle endringer til git for sporbarhet før peer review starter
2. **(Må)** V2 – Oppdatere status.md (alle 15 sjekklistepunkter, fremdriftstabellraden, «Modellering»→«Modell»-rettelsen i rapportstatustabellen) og schedule.json (status, percentComplete, alle tre kriterier, lastEvent) til å reflektere at ACT-3.10 er gjennomført
3. **(Bør)** V3 – Presisere biaskorreksjonsformuleringen i kap. 8.2 for konsistens med kap. 9.3
4. **(Bør)** V4 – Justere lengden på sammendrag/abstract slik at de blir mer symmetriske
5. **(Kan)** F1 – Legge til kort overgangsavsnitt mellom kap. 5 og kap. 6
6. **(Kan)** F2 – Gjøre Box et al. (2015)-siteringene konsistente i kapittelangivelser
7. **(Kan)** F3 – Nevn log-transformasjon eksplisitt i sammendrag/abstract
8. **(Kan)** F4 – Legge til tabelltekst nederst i Tabell 5.1
9. **(Kan)** F5 – Henvise til status.md sin Analyseartefakter-tabell i Vedlegg C

### Klar for peer review?

Etter at V1 og V2 er gjennomført, er rapportutkastet klart for peer review. V3 og V4 er anbefalte, men ikke blokkerende. F1–F5 kan adresseres parallelt med eller etter peer review.
