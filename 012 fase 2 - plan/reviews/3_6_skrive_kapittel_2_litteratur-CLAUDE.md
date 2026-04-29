# Review av aktivitet 3.6 – «Skrive kapittel 2 Litteratur»

**Reviewer:** Claude (automatisert review, uavhengig subagent)
**Dato:** 2026-04-29
**Aktivitetsmappe:** ren skriveaktivitet uten egne analyseartefakter (referansegrunnlag i `003 references/theory/md/`)
**Planreferanse:** Aktivitet ACT-3.6, planlagt 2026-04-10 til 2026-04-15

---

## Sammendrag

Kapittel 2 er en kompakt, ryddig og godt strukturert litteraturgjennomgang som plasserer problemstillingen i en moden faglig sammenheng. Litteraturen er organisert tematisk i seks underseksjoner (2.1–2.6), og hver kilde er knyttet til en konkret metodisk beslutning eller et senere kapittel i rapporten. Kapitlet oppfyller CLAUDE.md sitt sentrale krav om at «litteraturkapitlet skal knytte kilder til problemstillingen, ikke bare oppsummere løsrevne referanser». Reviewen identifiserer 6 styrker, 3 svakheter og 5 forbedringsforslag. Aktiviteten er klar for å lukkes etter at «Må»-tiltakene er gjennomført.

---

## Styrker

- **S1.** Kapitlet starter med et tydelig posisjoneringsavsnitt som forklarer kapittelets rolle, hvordan det skiller seg fra teorikapitlet, og hvilken organiserende logikk som er valgt. Dette gir leseren et godt navigasjonsanker og demonstrerer eksplisitt at forfatterne har tenkt gjennom skillet mot kapittel 3.
- **S2.** Hver kilde knyttes konsekvent til konkrete kapitler eller metodiske valg lenger ut i rapporten («kapittel 7.1», «kapittel 7.2», «kapittel 7.4», «kapittel 8», «kapittel 9.2», «kapittel 9.3»). Dette er et viktig grep som gjør at litteraturen ikke fremstår som løsrevet, men som et bevisst metodisk fundament.
- **S3.** Avsnitt 2.1 forankrer eksplisitt litteraturen i datasituasjonen og prosjektets avgrensninger («jf. avgrensning 1 i kapittel 1.3»). Dette er en sterk og direkte kobling mellom litteratur og problemstilling slik CLAUDE.md krever.
- **S4.** APA7-formatet brukes konsistent gjennom kapitlet: forfatter-årstall i parentes, korrekt bruk av «et al.» for Box et al. (2015) og Kwiatkowski et al. (1992), og korrekt bruk av «&» mellom forfattere innenfor parentes (Dickey & Fuller, 1979) versus «og» i løpende tekst.
- **S5.** Avsnitt 2.6 «Posisjonering av rapporten» er en god syntese som binder kildene sammen og avslutter kapitlet med en eksplisitt formulering av rapportens egen posisjon: «bidrar dermed ikke med ny metodikk, men med en problemforankret bruk av etablert metodikk på et konkret beslutningsproblem». Dette er et modent akademisk grep.
- **S6.** Litteraturkapitlet skiller seg meningsfullt fra teorikapitlet: kapittel 2 forteller hvilken litteratur som motiverer metodevalgene og hvorfor disse kildene er relevante, mens kapittel 3 utleder de matematiske og statistiske detaljene. Det er minimal redundans og klar arbeidsdeling.

---

## Del 1 – Metodikk (konsistens med rapporten, samsvar med problemstilling, korrekthet i siteringer)

### 1.1 Konsistens med problemstillingen

Problemstillingen i kapittel 1.1 har to ledd: (i) «hvordan kan en univariat tidsseriemodell brukes til å predikere månedlig traktorsalg for de neste tolv månedene», og (ii) «i hvilken grad gir en slik modell et tilstrekkelig beslutningsgrunnlag for produksjonsplanlegging og lagerstyring».

Litteraturkapitlet adresserer begge ledd:

- **Ledd (i):** Seksjon 2.1 begrunner univariat tilnærming gitt datasituasjonen; seksjon 2.2 forankrer SARIMA-rammeverket; seksjon 2.3 og 2.4 gir grunnlaget for stasjonaritetsvurdering og residualdiagnostikk; seksjon 2.5 kobler prognoseevaluering til hold-out-validering.
- **Ledd (ii):** Seksjon 2.1 trekker eksplisitt frem «kapitalbinding» og «tapte salg» som planleggingskonsekvenser, og seksjon 2.5 trekker frem biaskorreksjon som «praktisk viktig i en planleggingskontekst som krever forventet volum».

**Vurdering:** God dekning av begge problemstillingsledd.

### 1.2 Konsistens med øvrig rapporttekst

Alle henvisninger til kapitler senere i rapporten (7.1, 7.2, 7.4, 8, 9.2, 9.3) er korrekte og dekker faktisk de temaene litteraturkapitlet annonserer. Kapittel 2.4 sier at testene «brukes i kapittel 7.4 og diskuteres i kapittel 9.2» – dette stemmer med innholdet i 7.4 (Ljung-Box, ARCH-LM) og 9.2 (residualdiagnostikk og modellforutsetninger).

### 1.3 Korrekthet i siteringer

Alle åtte siteringer i kapittel 2 er sjekket mot referansesammendragene i `003 references/theory/md/` og mot bibliografien i kapittel 11:

| Sitering | Påstand i kap. 2 | Dekning i referansesammendrag | Vurdering |
|:---|:---|:---|:---|
| Hyndman & Athanasopoulos (2021) | Univariate metoder når kun én tidsserie er tilgjengelig | Refsammendraget bekrefter relevant kapittel 9 (ARIMA) og kapittel 5 (evaluering) | OK |
| Box et al. (2015) | Prediksjonsintervaller som usikkerhetsmål | Refsammendraget dekker kap. 8 (prognosefunksjoner) og kap. 9 (sesongmodeller) | OK, men noe svakt forankret – Hyndman & Athanasopoulos er muligens en mer direkte kilde for nyttebudskapet om prediksjonsintervaller |
| Box et al. (2015) | Box-Jenkins-metodikken som iterativ prosedyre | Refsammendraget dekker dette eksplisitt | OK |
| Shumway & Stoffer (2017) | Formell statistisk behandling av stasjonaritet, autokovarians, MLE | Refsammendraget bekrefter kap. 2 (autokovarians) og kap. 3 (MLE) | OK |
| Box et al. (2015) | Flypassasjermodellen som referansespesifikasjon | Refsammendraget bekrefter kap. 9 (SARIMA, flypassasjermodell) | OK |
| Dickey & Fuller (1979) | ADF-testen | Refsammendraget bekrefter dette | OK |
| Kwiatkowski et al. (1992) | KPSS-testen og komplementær bruk med ADF | Refsammendraget bekrefter dette eksplisitt | OK |
| Ljung & Box (1978) | Endelighetskorrigert portmanteau-test, anbefaling om sesonglag | Refsammendraget bekrefter formel og bruk på sesonglag | OK |
| Engle (1982) | ARCH-rammeverket og ARCH-LM-test for heteroskedastisitet | Refsammendraget bekrefter dette | OK |
| Jarque & Bera (1987) | Skjevhet+kurtose i $\chi^2$-statistikk | Refsammendraget bekrefter dette | OK |
| Hyndman & Athanasopoulos (2021) | Hold-out, MAE/RMSE/MAPE/MASE | Refsammendraget dekker «MAE, RMSE, MAPE» – MASE nevnes ikke i refsammendraget, men er et veletablert mål som dekkes i fpp3 kap. 5.8 | OK, men referansesammendraget kan oppdateres for fullstendighet |
| Hyndman & Athanasopoulos (2021) | Biaskorreksjon $\exp(\hat{z}+\sigma^2/2)$ ved tilbaketransformering | Dette er et velkjent resultat som dekkes i fpp3 kap. 3.2 / 9.1, men er ikke listet eksplisitt i refsammendraget | OK i kapitlet, men sammendragsfilen kan utvides |

**Vurdering:** Alle siteringer i kapittel 2 finnes i bibliografien, og alle påstander er dekket av kildene. Et par av påstandene (særlig MASE og bias-korreksjonen) er ikke eksplisitt nevnt i referansesammendragene, men de er gyldige bruk av kilden.

### 1.4 Sporbarhet til bibliografi

Kapittel 11 inneholder alle åtte referanser i konsistent APA7-format. Alle åtte refereres i kapittel 2. Det er ingen siteringer i kapittel 2 som mangler i bibliografien.

---

## Del 2 – Språk, innhold og figurer

### 2.1 Innledende avsnitt (før 2.1)

**Språk:** God akademisk norsk. Setningene er presise og logikken i organiseringen formidles klart.

**Faglig innhold:** Avsnittet etablerer eksplisitt skillet mot teorikapitlet («Hensikten er ikke å gjenta teorigjennomgangen i kapittel 3») og forklarer den tematiske organiseringen. Dette er et godt grep.

### 2.2 Seksjon 2.1 Tidsserieprognoser i produksjons- og lagerstyring

**Språk:** Godt fagspråk. Begreper som «bindeledd», «kapasitetsbinding» og «underdekning» brukes presist. Norske bokstaver er konsistent benyttet (æ, ø, å).

**Faglig innhold:** Seksjonen begrunner univariat tilnærming og kobler til avgrensning 1. Den henviser også til at prediksjonsintervaller er vesentlige – en god overgang til diskusjonen om usikkerhet senere. Imidlertid hviler hele seksjonen om planleggingskonsekvenser («kapitalbinding», «tapte salg», «lang ledetid») nesten utelukkende på (Hyndman & Athanasopoulos, 2021), som primært er en prognose-lærebok, ikke en supply chain-kilde. Litteratur fra produksjons- og lagerstyringsfaget (f.eks. Silver, Pyke & Thomas, eller Chopra & Meindl) ville styrket seksjonen og gitt den en mer eksplisitt logistisk forankring – som tross alt er en sentral del av problemstillingens andre ledd og av studiekontekstens (LOG650) fagprofil.

### 2.3 Seksjon 2.2 SARIMA-rammeverket og Box-Jenkins-metodikken

**Språk:** Klart og korrekt fagspråk. Den lange setningen om Box et al. (2015) og Shumway og Stoffer (2017) kunne deles i to for bedre lesbarhet, men er lesbar slik den står.

**Faglig innhold:** Seksjonen forankrer SARIMA-valget i etablert litteratur og forklarer det komplementære forholdet mellom Box et al. og Shumway og Stoffer på en god måte. Henvisningen til at modellen brukes som «sammenligningsgrunnlag i modellutvelgelsen i kapittel 7.2» er konkret og verifiserbar.

### 2.4 Seksjon 2.3 Stasjonaritet og statistiske enhetsrottester

**Språk:** Presist og kompakt.

**Faglig innhold:** Den parvise bruken av ADF og KPSS er godt motivert. Setningen «Forfatterne anbefaler eksplisitt å bruke testene sammen» kan presiseres – det er primært KPSS-artikkelen (Kwiatkowski et al., 1992) som eksplisitt formulerer det komplementære synet, ikke begge artiklene. Dette er en mindre upresishet.

### 2.5 Seksjon 2.4 Residualdiagnostikk og modellforutsetninger

**Språk:** Strukturert og klart.

**Faglig innhold:** Seksjonen presenterer de tre testene (Ljung-Box, ARCH-LM, Jarque-Bera) og kobler dem til kapittel 7.4 og 9.2. Innholdet er presist og dekkende. En liten forbedring: Jarque-Bera nevnes som «mye brukt», men den faglige begrunnelsen for hvorfor normalitet er viktig i SARIMA-sammenheng (MLE-inferens, prediksjonsintervaller) kommer først i kapittel 3.5. Dette er en akseptabel arbeidsdeling, men en setning her om hvorfor normalitet er relevant ville styrke koblingen.

### 2.6 Seksjon 2.5 Prognoseevaluering og hold-out-validering

**Språk:** Godt skrevet. Akronymene MAE, RMSE, MAPE og MASE introduseres uten å forklare dem fullt ut – men ettersom de utdypes i kapittel 3.5, er dette akseptabelt.

**Faglig innhold:** Seksjonen er godt forankret i Hyndman & Athanasopoulos (2021) og dekker både feilmålvalg og biaskorreksjon ved tilbaketransformering. Påpekningen om at «evaluering ikke bør reduseres til ett tall» er en god metodisk refleksjon. Biaskorreksjonen $\exp(\hat{z}_{T+h} + \sigma_h^2/2)$ er korrekt formulert.

### 2.7 Seksjon 2.6 Posisjonering av rapporten

**Språk:** Godt skrevet syntese.

**Faglig innhold:** Seksjonen oppsummerer litteraturen i tre grupper (rammeverk, stasjonaritet, diagnostikk) og uttaler eksplisitt rapportens bidrag som en problemforankret anvendelse av etablert metodikk. Dette er ærlig og presist – rapporten gjør ikke krav på metodisk nyhet, men på relevant anvendelse.

### 2.8 Figurer og tabeller

Kapittel 2 inneholder ingen figurer eller tabeller. Dette er forventet og passende for et litteraturkapittel.

### 2.9 Innholdsfortegnelse

Innholdsfortegnelsen i rapporten dekker alle seks underseksjoner (2.1–2.6) med riktige ankerlenker. Konsistent med kapittelets faktiske overskrifter.

### 2.10 Overlapp med kapittel 3 Teori

Det er minimalt overlapp mellom kapittel 2 og kapittel 3:

- Kapittel 2.2 nevner Box-Jenkins-metodikken konseptuelt; kapittel 3.3 utleder den i tre formelle steg.
- Kapittel 2.3 nevner ADF og KPSS som komplementære tester; kapittel 3.2 utleder hva de tester og hva p-verdiene betyr.
- Kapittel 2.4 nevner de tre diagnostiske testene; kapittel 3.5 gir formler og frihetsgrader.
- Kapittel 2.5 nevner feilmål og biaskorreksjon; kapittel 3.5 gir formler.

**Vurdering:** Arbeidsdelingen er bevisst og fungerer godt. Kapittel 2 forteller hva og hvorfor; kapittel 3 forteller hvordan. Dette er nettopp den distinksjonen CLAUDE.md ber om.

### 2.11 Manglende relevant litteratur

For en LOG650-oppgave med eksplisitt produksjons- og lagerstyringsfokus er det noen kilder som mangler:

- **Supply chain forecasting / S&OP-litteratur:** Kilder som Silver, Pyke & Thomas (2017) *Inventory and Production Management in Supply Chains* eller Chopra & Meindl *Supply Chain Management* ville gitt en bredere logistisk forankring.
- **Bullwhip-effekten:** Lee, Padmanabhan & Whang (1997) er en klassiker som viser hvorfor pålitelige prognoser er kritisk i forsyningskjeder. Selv om bullwhip ikke står sentralt i denne univariate analysen, er det en åpenbar referanse for å begrunne hvorfor prognoser er viktig i logistikkfagets sammenheng.
- **Sammenligning av prognosefamilier:** Gardner (2006) eller en oversiktsartikkel om M-konkurransene ville gitt empirisk støtte for at SARIMA-typen er konkurransedyktig på sesongdata.

Dette er ikke kritisk, men kan styrke kapitlet og gjøre det mer balansert mot logistikk-faget. Denne svakheten er allerede til en viss grad anerkjent i kapittel 9.5 («Ingen sammenligning med eksponentiell utjevning (ETS) … ble gjennomført»), men kunne ha vært varslet allerede i litteraturkapitlet.

---

## Svakheter

### V1. Endringene er ikke committet til git, og status.md/schedule.json er ikke oppdatert

**Alvorlighetsgrad:** Høy
**Kategori:** Prosess

Kapittel 2 er skrevet inn i `rapport.md`, men status.md viser fortsatt «ACT-3.6: Ikke startet» og «2 Litteratur: Tom», og schedule.json viser fortsatt status «not-started» og kriteriene C01 og C02 som «not-passed». For sporbarhet og konsistens med tidligere aktiviteter må status.md og schedule.json oppdateres, og endringene committes til git før aktiviteten kan lukkes.

### V2. Litteraturen er svakt forankret i logistikk-/SCM-faget

**Alvorlighetsgrad:** Middels
**Kategori:** Faglig innhold

Seksjon 2.1 hviler nesten utelukkende på Hyndman & Athanasopoulos (2021) for sine planleggingsbetraktninger. For en LOG650-rapport vil det styrke kapitlet å referere til minst én SCM- eller produksjonsstyringskilde (Silver/Pyke/Thomas, Chopra/Meindl, Lee et al. om bullwhip, eller tilsvarende). Dette knytter problemstillingens andre ledd – beslutningsstøtte for produksjons- og lagerplanlegging – til etablert logistikk-litteratur, ikke bare til prognoselitteraturen. CLAUDE.md sin sjekkliste sier eksplisitt at litteraturkapitlet skal knytte kilder til problemstillingen; her er produksjons-/lagersiden av problemstillingen underrepresentert.

### V3. «Forfatterne anbefaler eksplisitt» er en upresis tilskrivelse

**Alvorlighetsgrad:** Lav
**Kategori:** Korrekthet i siteringer

I seksjon 2.3 står det «Forfatterne anbefaler eksplisitt å bruke testene sammen». Slik formuleringen står, er det uklart om det er Dickey og Fuller, Kwiatkowski et al., eller begge sett samlet som anbefaler dette. Den eksplisitte komplementære logikken – ADF tester ikke-stasjonaritet som null, KPSS tester stasjonaritet som null – kommer fra KPSS-artikkelen (Kwiatkowski et al., 1992), som eksplisitt argumenterer for dette. Setningen bør presiseres, f.eks. «Kwiatkowski et al. (1992) argumenterer eksplisitt for at testene brukes sammen, fordi …».

---

## Forbedringsforslag

### F1. Legg til en SCM-/logistikk-kilde i seksjon 2.1

**Alvorlighetsgrad:** Middels (henger sammen med V2)
**Kategori:** Faglig innhold

Inkluder minst én etablert SCM-kilde – f.eks. Silver, Pyke & Thomas (2017) for koblingen mellom prognoser og lagerstyring, eller Lee, Padmanabhan & Whang (1997) for bullwhip-effekten. Dette balanserer kapitlet faglig og gir en mer overbevisende kobling til problemstillingens beslutningsstøttedel.

### F2. Vurder å nevne kort at andre prognosefamilier finnes

**Alvorlighetsgrad:** Lav
**Kategori:** Faglig innhold

Litteraturkapitlet kunne kort anerkjenne at SARIMA er én av flere veletablerte univariate prognosefamilier (f.eks. eksponentiell utjevning / ETS-rammeverket; Hyndman & Athanasopoulos, 2021, kap. 8). Dette ville rettferdiggjøre valget bedre og foregripe den begrensningen som identifiseres i kapittel 9.5. En setning eller to i seksjon 2.2 eller 2.6 holder.

### F3. Presiser formuleringen «Forfatterne anbefaler eksplisitt …»

**Alvorlighetsgrad:** Lav
**Kategori:** Korrekthet i siteringer

Som beskrevet i V3, omformuler setningen i seksjon 2.3 slik at det går klart fram hvilken artikkel som argumenterer for komplementær bruk.

### F4. Vurder en kort metodisk refleksjon over normalitetsantakelsens rolle

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

I seksjon 2.4 kan setningen om Jarque-Bera utvides med én bisetning som forklarer hvorfor normalitet er relevant i SARIMA-sammenheng (MLE-inferens, prediksjonsintervaller). Dette gjør koblingen til prognoseevalueringsdelen og diskusjonen i 9.2 enda klarere.

### F5. Oppdater referansesammendragene for Hyndman & Athanasopoulos (2021)

**Alvorlighetsgrad:** Lav
**Kategori:** Sporbarhet

Sammendraget i `ref_hyndman_athanasopoulos_2021.md` nevner MAE, RMSE og MAPE eksplisitt, men kapittel 2.5 trekker også inn MASE og biaskorreksjonen $\exp(\hat{z}+\sigma_h^2/2)$. Disse to elementene kan med fordel legges til i sammendragsfilen for fullstendig sporbarhet. (Påstandene i kapitlet er korrekte – dette er en ren sporbarhetsforbedring.)

---

## Avhukningsliste – tiltak

| # | Tiltak | Kategori | Status | Kommentar |
|:--|:-------|:---------|:-------|:----------|
| V1 | Oppdater status.md (ACT-3.6 → ferdig, kapittel 2 → ferdig) og schedule.json (status → completed, C01/C02 → passed), og committe alle endringer | Prosess | [ ] | Må |
| V2 | Forankre seksjon 2.1 sterkere i SCM-/logistikklitteratur (Silver/Pyke/Thomas, Lee et al. om bullwhip, eller tilsvarende) | Faglig innhold | [ ] | Må |
| V3 | Presiser «forfatterne anbefaler eksplisitt …» i seksjon 2.3 til Kwiatkowski et al. (1992) | Korrekthet i siteringer | [ ] | Bør |
| F1 | Legg til SCM-kilde og oppdater bibliografi tilsvarende | Faglig innhold | [ ] | Inngår delvis i V2 |
| F2 | Nevn kort alternative prognosefamilier (ETS) i seksjon 2.2 eller 2.6 | Faglig innhold | [ ] | Kan |
| F3 | Presiser tilskrivelsen av komplementær ADF/KPSS-bruk | Korrekthet i siteringer | [ ] | Inngår i V3 |
| F4 | Forklar kort hvorfor normalitet er relevant i seksjon 2.4 | Språk og innhold | [ ] | Kan |
| F5 | Utvid `ref_hyndman_athanasopoulos_2021.md` med MASE og biaskorreksjon | Sporbarhet | [ ] | Kan |

---

## Samsvar med prosjektplan og krav

| Sjekkpunkt | Status | Kommentar |
|:---|:---|:---|
| Identifisere relevante kilder | OK | Åtte kilder dekkende for SARIMA-rammeverket, men SCM-/logistikkilder mangler |
| Knytte litteratur til problemstilling og metodevalg | OK | Hver kilde er knyttet til konkrete kapitler/metodevalg |
| Gjennomføre intern review og lukke aktiviteten | Pågår | Denne reviewen |
| ACT-3.6-C01: Kapittel 2 Litteratur ferdigskrevet med relevante kilder koblet til problemstillingen | OK med forbehold | Underrepresentasjon av logistikk-/SCM-litteratur (V2/F1) |
| ACT-3.6-C02: Review er gjennomført og aktiviteten er lukket | Pågår | Denne reviewen |
| CLAUDE.md: Litteraturen knyttes til problemstillingen, ikke ramses opp | OK | Tydelig kobling i hver seksjon |
| CLAUDE.md: Norsk fagspråk med æ, ø, å | OK | Konsistent gjennom hele kapitlet |
| CLAUDE.md: Skille mot teorikapitlet | OK | Bevisst arbeidsdeling, minimalt overlapp |
| APA7-format konsistent | OK | «&» i parentes, «og» i tekst, korrekt «et al.»-bruk |
| Alle siteringer finnes i bibliografien | OK | Åtte siteringer, åtte oppføringer i kap. 11 |

---

## Samlet vurdering

### Metodikk

Aktiviteten er en ren skriveaktivitet uten analyseartefakter. Innholdet i kapittel 2 er konsistent med problemstillingen i kapittel 1, med metodevalgene i kapittel 5–8 og med diskusjonen i kapittel 9. Alle siteringer er korrekte og dekker det som faktisk hevdes. Skillet mot teorikapitlet (kapittel 3) er tydelig og fungerer godt.

### Språk, innhold og figurer

Teksten holder jevnt høy kvalitet med godt akademisk norsk og presise formuleringer. APA7-formatet er konsistent. De seks underseksjonene har en logisk progresjon, og posisjoneringsavsnittet (2.6) gir en moden avslutning. Hovedsvakheten i innholdet er en underrepresentasjon av logistikk-/SCM-litteratur, som er mer påfallende fordi rapporten skrives i et logistikkemne (LOG650) og fordi problemstillingens andre ledd handler om beslutningsstøtte for produksjons- og lagerplanlegging.

### Anbefalt prioritering videre

1. **(Må)** V1 – Oppdater status.md og schedule.json, og committe endringene
2. **(Må)** V2/F1 – Forankre seksjon 2.1 i SCM-/logistikklitteratur ved å legge til minst én relevant kilde (oppdater også bibliografien)
3. **(Bør)** V3/F3 – Presiser tilskrivelsen av ADF/KPSS-anbefalingen
4. **(Kan)** F2 – Nevn kort alternative prognosefamilier
5. **(Kan)** F4 – Kort metodisk refleksjon om normalitetsantakelsen i 2.4
6. **(Kan)** F5 – Utvid referansesammendraget for Hyndman & Athanasopoulos

Med V1 og V2/F1 implementert er kapitlet ferdig og aktiviteten klar for å lukkes. V3, F2, F4 og F5 er finpuss som kan tas inn i ACT-3.10 (sammenstilling) hvis ikke gjennomført her.
