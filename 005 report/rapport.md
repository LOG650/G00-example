# Tittel (norsk og/eller engelsk)

**Forfatter(e):**

**Totalt antall sider inkludert forsiden:**

**Molde, Innleveringsdato:**

---

## Obligatorisk egenerklæring/gruppeerklæring

### Personvern

#### Personopplysningsloven

Har oppgaven vært vurdert av NSD? ja / nei

- Hvis ja:

Referansenummer:

- Hvis nei:

Jeg/vi erklærer at oppgaven ikke omfattes av Personopplysningsloven:

#### Helseforskningsloven

Har oppgaven vært til behandling hos REK? ja / nei

- Hvis ja:

Referansenummer:

### Publiseringsavtale

**Studiepoeng:**

**Veileder:**

**Fullmakt til elektronisk publisering av oppgaven**

Jeg/vi gir herved Høgskolen i Molde en vederlagsfri rett til å gjøre oppgaven tilgjengelig for elektronisk publisering: ja / nei

Er oppgaven båndlagt (konfidensiell)? ja / nei

(Båndleggingsavtale må fylles ut)

- Hvis ja:

Kan oppgaven publiseres når båndleggingsperioden er over? ja / nei

**Dato:**

---

---

## Sammendrag

For produksjonsbedrifter med sesongavhengig etterspørsel er pålitelige prognoser en forutsetning for effektiv kapasitets- og lagerplanlegging. Denne rapporten utvikler en univariat tidsseriemodell for å predikere månedlig traktorsalg hos PowerHorse for de neste tolv månedene (juli 1981 til juni 1982) og vurderer i hvilken grad modellen gir tilstrekkelig beslutningsgrunnlag for produksjons- og lagerstyring.

Modellutvelgelsen følger Box-Jenkins-metodikken med ACF/PACF-analyse, AIC- og BIC-rangering av 36 kandidater og residualdiagnostikk på den log-transformerte salgsserien (januar 1964 til juni 1981). Log-transformasjonen er valgt for å stabilisere variansen i sesongutslagene som er proporsjonale med salgsnivået. Den valgte SARIMA$(0,1,1)(0,1,1)_{12}$-modellen oppnår lavest AIC og BIC blant kandidatene og er den enkleste spesifikasjonen i hele kandidatsettet med kun tre parametere. På testsettet (1978–1981) gir den en gjennomsnittlig absolutt prosentfeil (MAPE) på 5,4 %. Den 12-måneders prognosen reproduserer det historiske sesongmønsteret med topp i november–desember og bunn i august, gir et samlet salgsvolum på om lag 100 400 enheter og en sesongamplitude på 7:1 mellom topp- og bunnmåneden.

Modellen identifiserer høysesongen oktober–desember som den kritiske kapasitetsperioden og lavsesongmånedene august, januar og februar som naturlige lageroppbyggingsperioder. Testsettvalideringen avdekker en systematisk positiv bias som tiltar over horisonten, og residualdiagnostikken viser brudd på modellforutsetningene ved sesonglag og gjennom heteroskedastisitet. Modellen gir derfor et nyttig, men ikke uttømmende, beslutningsgrunnlag — sesongstrukturen er det sterkeste signalet, mens de absolutte nivåene bør tolkes med forbehold og suppleres med markedsinnsikt og operative ordredata.

---

## Abstract

Reliable forecasts are a prerequisite for effective capacity and inventory planning in companies with seasonal demand. This report develops a univariate time series model to forecast monthly tractor sales at PowerHorse for the next twelve months (July 1981 to June 1982) and assesses the extent to which such a model provides a sufficient decision basis for production and inventory planning.

Model selection follows the Box-Jenkins methodology with ACF/PACF analysis, AIC and BIC ranking of 36 candidates, and residual diagnostics on the log-transformed sales series (January 1964 to June 1981). The log transformation is applied to stabilise the variance in seasonal swings that scale proportionally with the sales level. The selected SARIMA$(0,1,1)(0,1,1)_{12}$ model achieves the lowest AIC and BIC among the candidates and is the simplest specification in the candidate set with only three parameters. On the test set (1978–1981) it achieves a mean absolute percentage error (MAPE) of 5.4%. The 12-month forecast reproduces the historical seasonal pattern with peaks in November–December and a trough in August, yielding a total sales volume of approximately 100,400 units and a seasonal amplitude of 7:1 between peak and trough months.

The model identifies the high season October–December as the critical capacity period and the low-season months August, January and February as natural inventory build-up periods. Test set validation reveals a systematic positive bias that grows over the forecast horizon, and residual diagnostics show violations of model assumptions at seasonal lags and through heteroscedasticity. The model therefore provides a useful, but not exhaustive, decision basis — the seasonal structure is the strongest signal, while absolute levels should be interpreted with caution and supplemented with market insight and operational order data.

---

## Innhold

1. [Innledning](#1-innledning)
   1. [Problemstilling](#11-problemstilling)
   2. [Delproblemer](#12-delproblemer)
   3. [Avgrensinger](#13-avgrensinger)
   4. [Antagelser](#14-antagelser)
2. [Litteratur](#2-litteratur)
   1. [Tidsserieprognoser i produksjons- og lagerstyring](#21-tidsserieprognoser-i-produksjons--og-lagerstyring)
   2. [SARIMA-rammeverket og Box-Jenkins-metodikken](#22-sarima-rammeverket-og-box-jenkins-metodikken)
   3. [Stasjonaritet og statistiske enhetsrottester](#23-stasjonaritet-og-statistiske-enhetsrottester)
   4. [Residualdiagnostikk og modellforutsetninger](#24-residualdiagnostikk-og-modellforutsetninger)
   5. [Prognoseevaluering og hold-out-validering](#25-prognoseevaluering-og-hold-out-validering)
   6. [SARIMA i tilsvarende anvendelser](#26-sarima-i-tilsvarende-anvendelser)
   7. [Posisjonering av rapporten](#27-posisjonering-av-rapporten)
3. [Teori](#3-teori)
   1. [Tidsserier og dekomponering](#31-tidsserier-og-dekomponering)
   2. [Stasjonaritet og transformasjoner](#32-stasjonaritet-og-transformasjoner)
   3. [ARIMA- og SARIMA-modeller](#33-arima--og-sarima-modeller)
   4. [Modellidentifikasjon og modellvalg](#34-modellidentifikasjon-og-modellvalg)
   5. [Validering og prognoseevaluering](#35-validering-og-prognoseevaluering)
4. [Casebeskrivelse](#4-casebeskrivelse)
   1. [PowerHorse og beslutningssituasjonen](#41-powerhorse-og-beslutningssituasjonen)
   2. [Historisk salgsutvikling](#42-historisk-salgsutvikling)
   3. [Sesongmønster i salget](#43-sesongmønster-i-salget)
   4. [Utfordringer dårlige prognoser medfører i bedriften](#44-utfordringer-dårlige-prognoser-medfører-i-bedriften)
5. [Metode og data](#5-metode-og-data)
   1. [Metode](#51-metode)
   2. [Data](#52-data)
6. [Modell](#6-modell)
   1. [Vurdering av modelltype](#61-vurdering-av-modelltype)
   2. [Modellantagelser](#62-modellantagelser)
   3. [Generell SARIMA-modell](#63-generell-sarima-modell)
7. [Analyse](#7-analyse)
   1. [Stasjonaritet og behov for differensiering](#71-stasjonaritet-og-behov-for-differensiering)
   2. [ACF/PACF-analyse og ordensvalg](#72-acfpacf-analyse-og-ordensvalg)
   3. [Modellestimering og parameterresultater](#73-modellestimering-og-parameterresultater)
   4. [Validering](#74-validering)
8. [Resultat](#8-resultat)
   1. [Resultater fra testsettvalidering](#81-resultater-fra-testsettvalidering)
   2. [Resultater fra prognosearbeidet](#82-resultater-fra-prognosearbeidet)
9. [Diskusjon](#9-diskusjon)
   1. [Modellvalg og parsimoni](#91-modellvalg-og-parsimoni)
   2. [Residualdiagnostikk og modellforutsetninger](#92-residualdiagnostikk-og-modellforutsetninger)
   3. [Prognoseevne og bias i testsettvalideringen](#93-prognoseevne-og-bias-i-testsettvalideringen)
   4. [Prognosen og implikasjoner for kapasitetsplanlegging](#94-prognosen-og-implikasjoner-for-kapasitetsplanlegging)
   5. [Begrensninger](#95-begrensninger)
   6. [Samlet vurdering opp mot problemstillingen](#96-samlet-vurdering-opp-mot-problemstillingen)
10. [Konklusjon](#10-konklusjon)
11. [Bibliografi](#11-bibliografi)
12. [Vedlegg](#12-vedlegg)
    1. [Vedlegg A — Fullstendig oversikt over evaluerte SARIMA-kandidater](#vedlegg-a--fullstendig-oversikt-over-evaluerte-sarima-kandidater)
    2. [Vedlegg B — Månedlig testsettprognose](#vedlegg-b--månedlig-testsettprognose)
    3. [Vedlegg C — Reproduserbarhet og analyseartefakter](#vedlegg-c--reproduserbarhet-og-analyseartefakter)

---

## 1 Innledning

For produksjonsbedrifter med sesongavhengig etterspørsel er pålitelige prognoser en forutsetning for effektiv kapasitets- og lagerplanlegging. Når etterspørselen svinger systematisk gjennom året, fører upresise prognoser til overproduksjon og kapitalbinding i perioder med lav etterspørsel, eller til underdekning og tapte salg når etterspørselen er høy. Konsekvensene forsterkes i bransjer med lang produksjonsledetid, der det er vanskelig å justere volumet på kort varsel.

Denne rapporten bruker PowerHorse som casebedrift for å undersøke hvordan historiske salgsdata kan gi bedre beslutningsstøtte i produksjons- og lagerplanlegging. Bedriften opererer i et marked der etterspørselen varierer både over tid og mellom måneder, noe som gjør det krevende å planlegge kapasitet og lager presist. Med utgangspunkt i et månedlig salgsdatasett utvikles en SARIMA-basert tidsseriemodell som skal fange opp trend- og sesongmønstre og danne grunnlag for en 12-måneders prognose.

### 1.1 Problemstilling

Hvordan kan en univariat tidsseriemodell brukes til å predikere månedlig traktorsalg for de neste tolv månedene (juli 1981 til juni 1982), og i hvilken grad gir en slik modell et tilstrekkelig beslutningsgrunnlag for produksjonsplanlegging og lagerstyring hos PowerHorse?

Spørsmålet er motivert av at bedriften mangler et systematisk grunnlag for å planlegge produksjonsvolum fremover. Kapittel 4 beskriver casesituasjonen nærmere og dokumenterer de historiske salgsmønstrene som danner utgangspunktet for modelleringsarbeidet.

### 1.2 Delproblemer

For å strukturere analyseløpet brytes hovedproblemstillingen ned i tre delspørsmål:

1. Hvilke mønstre i trend og sesong finnes i de historiske salgsdataene?
2. Hvilken SARIMA-spesifikasjon gir best tilpasning, og hvordan presterer modellen på data den ikke er estimert på?
3. Hvilke implikasjoner har prognosen for PowerHorse sin produksjons- og lagerplanlegging?

Delspørsmålene korresponderer med henholdsvis casebeskrivelse og datautforsking (kapittel 4–5), modellering og validering (kapittel 6–8), og diskusjon og konklusjon (kapittel 9–10).

### 1.3 Avgrensinger

Analysen er avgrenset på følgende måter:

1. **Univariat modellering.** Datasettet inneholder kun tid og salgsvolum, uten eksterne forklaringsvariabler som pris, markedsføring eller makroøkonomiske indikatorer. Modelleringen er derfor begrenset til mønstre i selve tidsserien.
2. **Én produktkategori og månedlig oppløsning.** Datagrunnlaget gjelder samlet traktorsalg på månedsnivå. Finere inndeling etter produkttype, region eller uke er ikke mulig med tilgjengelige data.
3. **Prognosefokus, ikke forsyningskjedeoptimalisering.** Rapporten utvikler en etterspørselsprognose, men gjennomfører ikke en helhetlig optimalisering av produksjon og lager. Slik optimalisering ville kreve kostnads- og kapasitetsdata som ikke inngår i datagrunnlaget.
4. **Historisk analyseperiode 1964–1981.** Datasettet dekker perioden januar 1964 til juni 1981, og analysen er begrenset til denne perioden. Forhold som ligger utenfor dataperioden er ikke modellert eksplisitt. Antagelsen om at de historiske mønstrene fortsatt er gyldige i prognoseperioden behandles separat under antagelse 2 i seksjon 1.4.

### 1.4 Antagelser

Analysen bygger på tre overordnede antagelser:

1. **Datakvalitet.** Datasettet antas å være kvalitetssjekket av kilden som leverte det, ettersom prosjektet ikke har tilgang til eksterne kilder for uavhengig verifikasjon. Konsekvensen er at eventuelle feil i kildedata vil forplante seg uoppdaget gjennom analysen.
2. **Relevans av historiske mønstre.** Trend- og sesongmønstrene som er observert i treningsperioden antas å være tilstrekkelig stabile til å danne grunnlag for prognoser i den nærmeste fremtiden. Dersom markedet har gjennomgått strukturelle endringer, kan prognosen bli misvisende.
3. **Mønsterbasert tilnærming.** Analysen bygger på statistiske mønstre i tidsserien, ikke på kausale forklaringer av etterspørselsdrivere. Modellen kan dermed fange regelmessigheter uten å forklare hvorfor de oppstår, noe som begrenser evnen til å vurdere effekten av strukturelle endringer.

Disse antagelsene gjelder på prosjektnivå. For detaljerte statistiske modellantagelser, se kapittel 6.2.

---

## 2 Litteratur

Dette kapitlet plasserer problemstillingen — univariat prognosering av månedlig traktorsalg som beslutningsgrunnlag for produksjons- og lagerplanlegging hos PowerHorse — i en større faglig sammenheng. Hensikten er ikke å gjenta teorigjennomgangen i kapittel 3, men å vise hvilken litteratur som motiverer og begrunner metodevalgene som gjøres senere i rapporten. Litteraturen er organisert tematisk: først prognosemetodikkens rolle i operativ planlegging, deretter SARIMA-rammeverket som etablert tilnærming til sesongtidsserier, og til slutt de statistiske verktøyene som er nødvendige for å vurdere modellens gyldighet og prognoseevne.

### 2.1 Tidsserieprognoser i produksjons- og lagerstyring

For produksjonsbedrifter med sesongavhengig etterspørsel er prognoser et grunnleggende bindeledd mellom etterspørselsdrevne salg og kapasitetsdrevet produksjon. Hyndman og Athanasopoulos (2021) understreker at valg av prognosemetode må tilpasses dataene man faktisk har tilgjengelig: når kun én tidsserie og ingen forklaringsvariabler foreligger, er univariate metoder det naturlige utgangspunktet. Dette korresponderer direkte med datasituasjonen i PowerHorse-caset, der kun månedlig salgsvolum og tidspunkt er tilgjengelig (jf. avgrensning 1 i kapittel 1.3).

I et planleggingsperspektiv brukes etterspørselsprognoser som inngangsdata for produksjonsplanlegging og lagerstyring. Silver, Pyke og Thomas (2017) viser hvordan prognoser kobler seg direkte til operative beslutninger gjennom dimensjonering av sikkerhetslager, aggregert produksjonsplanlegging og oppbygging av lager foran høysesong. Dårlige prognoser fører enten til kapitalbinding gjennom overproduksjon eller til tapte salg ved underdekning, og effekten forsterkes når ledetiden er lang og produksjonen er sesongorientert (Silver et al., 2017; Hyndman & Athanasopoulos, 2021). Litteraturen peker også på at en pålitelig punktprognose alene ikke er tilstrekkelig: usikkerhetsmål i form av prediksjonsintervaller er vesentlige for risikobaserte planleggingsbeslutninger (Box et al., 2015), og prognosevariansen er nettopp den størrelsen som inngår i klassiske formler for sikkerhetslager (Silver et al., 2017). Denne erkjennelsen ligger til grunn for hvordan prognosen i kapittel 8 kobles videre til planleggingsdiskusjonen i kapittel 9.

### 2.2 SARIMA-rammeverket og Box-Jenkins-metodikken

Det metodiske utgangspunktet for rapporten er Box-Jenkins-metodikken slik den er formulert i Box et al. (2015) — en iterativ prosedyre med identifikasjon, estimering og diagnostikk som har vært det dominerende rammeverket for univariat tidsserieprognosering siden 1970-tallet. Metodikken er forankret i ARIMA-familien av modeller, og utvides med sesongmessige polynom for å håndtere periodiske mønstre i en multiplikativ SARIMA$(p,d,q)(P,D,Q)_s$-struktur. Box et al. (2015) og Shumway og Stoffer (2017) gir komplementære framstillinger: førstnevnte legger vekt på det praktiske rammeverket og inneholder den klassiske flypassasjeranalysen, mens sistnevnte gir en formell statistisk behandling av stasjonaritet, autokovarians og estimering med maksimum likelihood.

Den klassiske flypassasjermodellen SARIMA$(0,1,1)(0,1,1)_{12}$ fungerer som referansespesifikasjon for månedlige sesongserier (Box et al., 2015). Dens utbredelse og dokumenterte robusthet gjør den til et naturlig sammenligningsgrunnlag i modellutvelgelsen i kapittel 7.2. At PowerHorse-dataene er månedlige med en tydelig årlig sesong (kapittel 4.3), gir umiddelbar metodisk forankring til denne litteraturen.

Box-Jenkins-metodikken har også vist seg å være levedyktig over tid. De Gooijer og Hyndman (2006) gir en bred oversikt over 25 års utvikling i tidsserieprognosering og dokumenterer at ARIMA-familien har vært et stabilt referansepunkt parallelt med utviklingen av eksponentiell utjevning og statspace-modeller. Empirisk støttes dette av Makridakis, Spiliotis og Assimakopoulos (2020), som i M4-konkurransen testet 61 prognosemetoder mot 100 000 tidsserier og viste at statistiske metoder fra ARIMA- og ETS-familiene fortsatt presterer konkurransedyktig — også sammenlignet med moderne maskinlæringsmetoder. SARIMA er dermed ikke bare et teoretisk veletablert valg, men et empirisk konkurransedyktig valg for det univariate månedlige sesongprognoseproblemet i denne rapporten. Begrensninger ved valget — særlig at alternativer som ETS ikke er sammenlignet eksplisitt — drøftes i kapittel 9.5.

### 2.3 Stasjonaritet og statistiske enhetsrottester

Stasjonaritet er en bærende forutsetning i ARIMA-rammeverket, og litteraturen tilbyr to komplementære tester som i praksis brukes sammen. Dickey og Fuller (1979) utleder fordelingen til estimatoren under nullhypotesen om enhetsrot og legger grunnlaget for Augmented Dickey-Fuller-testen (ADF), som tester om en serie er ikke-stasjonær. Kwiatkowski et al. (1992) snur perspektivet med KPSS-testen, der nullhypotesen er stasjonaritet, og argumenterer eksplisitt for at de to testene brukes sammen: en sammenfallende konklusjon styrker tolkningen, mens uenighet avdekker tvetydige tilfeller som krever supplerende vurdering. Denne anbefalingen er fulgt i kapittel 7.1, der både ADF og KPSS brukes på den log-transformerte salgsserien før differensieringsbehovet avgjøres.

### 2.4 Residualdiagnostikk og modellforutsetninger

En estimert SARIMA-modell er bare gyldig dersom residualene tilfredsstiller forutsetningene om hvit støy: ingen autokorrelasjon, konstant varians og tilnærmet normalitet. Litteraturen tilbyr veletablerte tester for hver av disse egenskapene.

Ljung og Box (1978) utviklet en endelighetskorrigert portmanteau-test (Ljung-Box-testen) som er bedre tilpasset moderate utvalg enn den tidligere Box-Pierce-statistikken. Testen er i dag standard for å vurdere gjenværende autokorrelasjon i residualene, og forfatterne anbefaler at den utføres på flere lag, særlig sesonglag for sesongmodeller. Engle (1982) introduserte ARCH-rammeverket og en tilhørende Lagrange-multiplikatortest (ARCH-LM) som avdekker tidsvarierende varians — heteroskedastisitet — i residualene. Jarque og Bera (1987) presenterte en enkel og mye brukt normalitetstest som kombinerer skjevhet og kurtose i én $\chi^2$-statistikk. Normalitet er relevant fordi maksimum likelihood-estimering av SARIMA-parametere og de tilhørende prediksjonsintervallene baserer seg på en antakelse om tilnærmet normalfordelte residualer; betydelige avvik svekker dermed presisjonen i konfidensintervaller og prognoseusikkerhetsmål. Sammen utgjør disse tre testene det diagnostiske rammeverket som brukes i kapittel 7.4 og diskuteres i kapittel 9.2.

### 2.5 Prognoseevaluering og hold-out-validering

For å vurdere prognoseevne anbefaler litteraturen at modellen evalueres på data den ikke er estimert på (Hyndman & Athanasopoulos, 2021). Hold-out-validering med en disjunkt trenings-/testsplitt gir et realistisk bilde av out-of-sample-ytelse og er standard praksis i moderne prognoselitteratur. Hyndman og Athanasopoulos (2021) gjennomgår de mest brukte feilmålene: MAE som intuitivt absolutt avvik, RMSE som vekter store feil tyngre, MAPE som skalauavhengig prosentvis avvik med kjente svakheter ved nullverdier og skjeve fordelinger, og MASE som et skalauavhengig alternativ basert på en naiv referanseprognose. Petropoulos et al. (2022) bekrefter i sin brede praksisrettede gjennomgang at evaluering ikke bør reduseres til ett tall: ulike feilmål belyser ulike egenskaper ved prognosefeilene, punktprognosenøyaktighet og prediksjonsintervall-dekning er adskilte ytelsesdimensjoner, og en helhetlig vurdering krever at flere mål rapporteres samtidig.

Når en modell er estimert på log-transformerte data, må tilbaketransformeringen behandles eksplisitt. Hyndman og Athanasopoulos (2021) påpeker at $\exp(\hat{z}_{T+h})$ gir medianprognosen, ikke forventningsverdien, og at biaskorreksjonen $\exp(\hat{z}_{T+h} + \sigma_h^2/2)$ gir et bedre estimat av forventet etterspørsel. Dette skillet er praktisk viktig i en planleggingskontekst som krever forventet volum, og er drøftet videre i kapittel 9.3.

### 2.6 SARIMA i tilsvarende anvendelser

Litteraturen rommer flere case-studier som anvender SARIMA og Box-Jenkins-metodikken på problemstillinger som ligner PowerHorse-caset i både domene og formål. Tre arbeider er særlig relevante.

Polina, Ganesan, Karunarathne og Somasiri (2024) modellerer historisk traktorsalg med SARIMAX og sammenligner med flere dyplæringsmodeller (LSTM, GRU, RNN, CNN-LSTM). I deres analyse oppnår SARIMAX bedre treffsikkerhet enn dyplæringsmodellene målt med RMSE. Studien gir direkte empirisk støtte for at SARIMA-familien er et fornuftig metodevalg på samme produktdomene og frekvensnivå som vår analyse, og dokumenterer en fullstendig Box-Jenkins-arbeidsflyt med Q-Q-plott, residualplott og ACF/PACF-grafer som diagnostikkverktøy.

Makoni og Chikobvu (2023) modellerer månedlig nybilsalg i Sør-Afrika i perioden 1998–2017 og identifiserer SARIMA(0,1,1)(0,0,2)$_{12}$ som beste spesifikasjon. Modellutvelgelsen følger Box-Jenkins-metodikken med AIC og BIC som beslutningsverktøy, og prognoseevalueringen bruker RMSE og MAPE — tilsvarende metodikkpakke som i denne rapporten, og med en sluttmodell i samme klasse som vår SARIMA(0,1,1)(0,1,1)$_{12}$. Studien er et eksempel på at samme arbeidsflyt gir robust modellutvelgelse på en sammenlignbar månedlig sesongserie i et beslektet markedssegment.

Guimarães, Marques og Tortato (2020) anvender Box-Jenkins-metodikken på etterspørselen etter høyomløps reservedeler hos en multinasjonal produsent av landbruks- og anleggsmaskiner. Studien sammenligner Box-Jenkins-tilnærmingen med eksponentiell utjevning i bedriftens ERP-system og finner at den statistiske metodikken reduserer gjennomsnittlig prognosefeil fra 26 % til 10 % og bringer andelen usolgte ordrer ned fra 9,6 % til 1,4 %. Forfatterne kvantifiserer deretter de logistiske konsekvensene som potensielle lagerreduksjoner i størrelsesorden 76 % på tvers av alle klasse-A-deler, uten reduksjon i servicegrad. Dette case-eksempelet illustrerer eksplisitt bindeleddet mellom prognoseforbedring og operative lagerbeslutninger som problemstillingens andre ledd handler om, og er metodisk og domenemessig nærmest knyttet til PowerHorse-caset av kildene gjennomgått her.

Samlet styrker disse arbeidene den praktiske forankringen av metodevalget i denne rapporten. SARIMA er ikke bare teoretisk forsvarlig og empirisk konkurransedyktig på generelle benchmarkdata — den er også dokumentert anvendt med gode resultater på sammenlignbare problemer i tilstøtende markeder, med målbare effekter på operative lagerbeslutninger.

### 2.7 Posisjonering av rapporten

Den gjennomgåtte litteraturen utgjør en moden og veletablert verktøykasse for univariat sesongprognosering brukt i en logistikk-kontekst. Silver et al. (2017) gir den logistiske rammen som kobler prognoser til lager- og produksjonsplanlegging, mens Box et al. (2015), Shumway og Stoffer (2017) og Hyndman og Athanasopoulos (2021) gir det overordnede metodiske rammeverket for tidsseriemodellering og prognoseevaluering. De Gooijer og Hyndman (2006), Makridakis et al. (2020) og Petropoulos et al. (2022) gir den empiriske og praksisorienterte forankringen som dokumenterer at SARIMA-rammeverket holder seg godt og fortsatt brukes aktivt i moderne prognosearbeid. Polina et al. (2024), Makoni og Chikobvu (2023) og Guimarães et al. (2020) gir konkrete domenenære case-studier som viser at metodikken fungerer godt på sammenlignbare problemstillinger. Dickey og Fuller (1979) og Kwiatkowski et al. (1992) gir verktøyene for stasjonaritetsvurdering, og Ljung og Box (1978), Engle (1982) og Jarque og Bera (1987) gir det diagnostiske apparatet for å vurdere modellens gyldighet. Rapporten anvender disse bidragene som en samlet metodisk pakke på PowerHorse-caset, og bidrar dermed ikke med ny metodikk, men med en problemforankret bruk av etablert metodikk på et konkret beslutningsproblem i produksjons- og lagerplanlegging.

---

## 3 Teori

Dette kapitlet presenterer det teoretiske rammeverket som ligger til grunn for analysemetodene som brukes i kapittel 6 til 8. Hensikten er å gi et faglig fundament for modellvalg, estimering, diagnostikk og prognoseevaluering, slik at valg og tolkninger senere i rapporten kan forankres i etablert teori. Kapitlet dekker først tidsserier som analyseobjekt, deretter stasjonaritet og transformasjoner, modellrammeverket ARIMA og SARIMA, identifikasjons- og modellvalgverktøy, og til slutt validering og prognoseevaluering.

### 3.1 Tidsserier og dekomponering

En tidsserie er en sekvens av observasjoner $y_1, y_2, \dots, y_T$ registrert i en fast tidsrekkefølge med lik avstand mellom observasjonene. Det som skiller tidsseriedata fra tverrsnittsdata er at rekkefølgen er meningsbærende: observasjoner som ligger nær hverandre i tid, er ofte mer like enn observasjoner som ligger langt fra hverandre. Denne temporale avhengigheten er nettopp det tidsseriemodeller utnytter for å lage prognoser (Hyndman & Athanasopoulos, 2021).

Et nyttig utgangspunkt for å forstå en tidsserie er å tenke på den som sammensatt av tre komponenter: en trendkomponent $T_t$ som fanger opp langsiktig utvikling, en sesongkomponent $S_t$ som fanger opp gjentakende mønstre med fast periode, og en restkomponent $\varepsilon_t$ som representerer uforklart variasjon. Sammenhengen kan uttrykkes enten additivt,

$$
y_t = T_t + S_t + \varepsilon_t,
$$

eller multiplikativt,

$$
y_t = T_t \cdot S_t \cdot \varepsilon_t.
$$

En multiplikativ struktur innebærer at sesongutslaget vokser proporsjonalt med nivået i serien. I mange salgsserier er dette tilfellet: høysesongsvingningene er større i absolutte tall når salget er høyt enn når det er lavt. En log-transformasjon $z_t = \log(y_t)$ konverterer en multiplikativ struktur til en additiv, fordi $\log(T_t \cdot S_t \cdot \varepsilon_t) = \log(T_t) + \log(S_t) + \log(\varepsilon_t)$. Denne egenskapen gjør log-transformasjonen til et naturlig første steg når variansen i serien øker med nivået, noe som leder videre til spørsmålet om stasjonaritet.

Figur 3.1 illustrerer prinsippet med en syntetisk tidsserie som er dekomponert i sine tre additive komponenter.

<div align="center">
  <img src="../006%20analysis/aktiviteter/3_7_skrive_teorikapittel/figurer/fig_01_dekomponering.png" alt="Figur 3.1 Additiv dekomponering av en tidsserie" width="80%">
  <p align="center"><small><i>Figur 3.1 Additiv dekomponering av en syntetisk tidsserie i trend, sesong og restledd.</i></small></p>
</div>

### 3.2 Stasjonaritet og transformasjoner

ARIMA-modeller forutsetter at serien, etter eventuelle transformasjoner og differensieringer, er stasjonær. En tidsserie $\{y_t\}$ kalles svakt stasjonær dersom tre betingelser er oppfylt: forventningen $E[y_t] = \mu$ er konstant over tid, variansen $\text{Var}(y_t) = \sigma^2$ er konstant over tid, og autokovariansen $\gamma(h) = \text{Cov}(y_t, y_{t+h})$ avhenger kun av tidsavstanden $h$ og ikke av tidspunktet $t$ (Shumway & Stoffer, 2017). Stasjonaritet er viktig fordi en modell med faste parametere bare gir mening dersom de statistiske egenskapene til serien ikke endrer seg systematisk over tid.

Mange økonomiske og salgsrelaterte tidsserier er ikke stasjonære i sin opprinnelige form. Nivået kan stige over tid (trend), og variansen kan øke med nivået. For å håndtere dette brukes to typer transformasjoner.

**Log-transformasjon.** Når variansen i serien øker proporsjonalt med nivået, stabiliserer log-transformasjonen $z_t = \log(y_t)$ variansen slik at serien bedre oppfyller kravet om konstant varians. Transformasjonen krever at alle observasjoner er strengt positive.

**Differensiering.** Differensiering fjerner ikke-stasjonær struktur fra serien. Med forsinkelsesoperatoren $B$, definert ved $By_t = y_{t-1}$, kan ordinær differensiering skrives som

$$
(1-B) y_t = y_t - y_{t-1},
$$

som fjerner lineær trend ved å beregne endringen fra én periode til den neste. Sesongmessig differensiering med periode $s$ skrives som

$$
(1-B^s) y_t = y_t - y_{t-s},
$$

som fjerner sesongstruktur ved å sammenligne hver observasjon med observasjonen $s$ perioder tilbake. For månedlige data med årlig sesong er $s = 12$. Ordinær og sesongmessig differensiering kan kombineres: $(1-B)(1-B^{12}) y_t$ fjerner både trend og sesong. Forsinkelsesoperatoren $B$ og differensieringsoperatorene brukes videre i den formelle SARIMA-spesifikasjonen i kapittel 6.3.

Figur 3.2 viser effekten av ulike differensieringsstrategier på en syntetisk ikke-stasjonær serie med trend og sesong. Som figuren illustrerer, fjerner sesongdifferensieringen alene sesongen, men den underliggende trenden er fortsatt tydelig. Først når ordinær og sesongmessig differensiering kombineres, oppnås en tilnærmet stasjonær serie.

<div align="center">
  <img src="../006%20analysis/aktiviteter/3_7_skrive_teorikapittel/figurer/fig_02_stasjonaritet.png" alt="Figur 3.2 Differensiering for å oppnå stasjonaritet" width="80%">
  <p align="center"><small><i>Figur 3.2 Effekten av ordinær, sesongmessig og kombinert differensiering på en syntetisk serie.</i></small></p>
</div>

For å vurdere om en serie er tilstrekkelig stasjonær, brukes statistiske tester. To mye brukte tester har komplementære nullhypoteser og brukes derfor ofte sammen:

- **Augmented Dickey-Fuller-testen (ADF)** tester nullhypotesen om at serien har en enhetsrot, det vil si at den er ikke-stasjonær (Dickey & Fuller, 1979). En lav p-verdi gir grunnlag for å forkaste nullhypotesen og konkludere med stasjonaritet.

- **KPSS-testen** tester nullhypotesen om at serien er stasjonær (Kwiatkowski et al., 1992). Her dekomponeres serien i en deterministisk trend, en tilfeldig vandring og et stasjonært feilledd, og testen undersøker om variansen til den tilfeldige vandringen er null. En høy p-verdi gir støtte til stasjonaritet.

Brukt sammen gir testene et mer robust bilde enn hver for seg: dersom begge peker i samme retning, er konklusjonen klarere. Når testene er uenige, kan det tyde på at serien er nær grensen til stasjonaritet, og visuell vurdering bør supplere de formelle testresultatene. I kapittel 7.1 brukes ADF- og KPSS-testene til å avgjøre differensieringsbehovet for den log-transformerte salgsserien.

### 3.3 ARIMA- og SARIMA-modeller

Med stasjonaritetsbegrepet og differensiering på plass kan selve modellrammeverket beskrives. Utgangspunktet er tre grunnleggende byggesteiner. En autoregressiv modell av orden $p$, skrevet AR($p$), forklarer nåværende verdi som en lineær funksjon av de $p$ foregående verdiene i serien. En glidende gjennomsnittsmodell av orden $q$, skrevet MA($q$), forklarer nåværende verdi som en lineær funksjon av nåværende og de $q$ foregående feilleddene. En ARMA($p,q$)-modell kombinerer begge mekanismene.

Når serien ikke er stasjonær og må differensieres $d$ ganger for å oppnå stasjonaritet, utvides modellen til en ARIMA($p,d,q$)-modell — en autoregressiv integrert glidende gjennomsnittsmodell. Bokstaven I står for «integrert» og reflekterer at den observerte serien er den integrerte (summerte) versjonen av den stasjonære differensserien (Shumway & Stoffer, 2017).

For tidsserier med sesongmønster — som månedlige salgsdata med årlige svingninger — utvides rammeverket ytterligere til en SARIMA-modell. En SARIMA$(p,d,q)(P,D,Q)_s$-modell legger til sesongmessige autoregressive og glidende gjennomsnittsledd, samt sesongmessig differensiering, der $s$ angir sesonglengden. Det karakteristiske ved SARIMA er den multiplikative strukturen: de ikke-sesongmessige og sesongmessige operatorene virker sammen, slik at modellen kan fange opp samspillet mellom kortsiktige og sesongmessige mønstre. Den kompakte formen skrives som

$$
\Phi(B^s) \, \phi(B) \, (1-B)^d (1-B^s)^D y_t = \Theta(B^s) \, \theta(B) \, \varepsilon_t,
$$

der $\phi(B)$ og $\theta(B)$ er de ikke-sesongmessige polynomene, $\Phi(B^s)$ og $\Theta(B^s)$ er de sesongmessige polynomene, og $\varepsilon_t$ er feilleddet. Den fullstendige utledningen med alle polynomdefinisjoner finnes i kapittel 6.3.

**Box-Jenkins-metodikken** gir et systematisk rammeverk for å arbeide med ARIMA- og SARIMA-modeller (Box et al., 2015). Prosedyren er iterativ og består av tre steg som gjentas til en tilfredsstillende modell er funnet:

1. **Identifikasjon:** Vurdere stasjonaritet, bestemme differensieringsordner, og bruke ACF og PACF til å foreslå modellordner.
2. **Estimering:** Estimere modellparameterne, typisk med maksimum likelihood (MLE), som finner parameterverdiene som maksimerer sannsynligheten for de observerte dataene gitt modellen.
3. **Diagnostikk:** Undersøke residualene for å vurdere om modellen er tilstrekkelig spesifisert. Dersom residualene viser systematiske mønstre, revideres modellen.

Etter at en tilfredsstillende modell er funnet, kan den brukes til å generere prognoser med tilhørende usikkerhetsmål.

En klassisk og mye brukt SARIMA-spesifikasjon for månedlige tidsserier med trend og sesong er SARIMA$(0,1,1)(0,1,1)_{12}$. Denne modellen, ofte kalt flypassasjermodellen etter Box og Jenkins' opprinnelige analyse av månedlige passasjertall for internasjonale flyreiser (Box et al., 2015), kombinerer ordinær og sesongmessig differensiering med ett glidende gjennomsnittsledd på hvert nivå. Modellen fungerer som et naturlig referansepunkt når man modellerer månedlige sesongtidsserier, og er kjent for å gi gode resultater med få parametere.

### 3.4 Modellidentifikasjon og modellvalg

Det første steget i Box-Jenkins-metodikken etter differensiering er å bruke autokorrelasjonsfunksjonen (ACF) og den partielle autokorrelasjonsfunksjonen (PACF) til å foreslå modellordner.

ACF ved lag $h$ måler korrelasjonen mellom $y_t$ og $y_{t+h}$, inkludert effekten av alle mellomliggende observasjoner. PACF ved lag $h$ måler korrelasjonen mellom $y_t$ og $y_{t+h}$ etter at effekten av observasjonene $y_{t+1}, \dots, y_{t+h-1}$ er fjernet. Disse to funksjonene har karakteristiske signaturmønstre for ulike modelltyper (Box et al., 2015):

- En ren AR($p$)-prosess viser gradvis avtagende ACF og en PACF som kuttes av etter lag $p$.
- En ren MA($q$)-prosess viser en ACF som kuttes av etter lag $q$ og gradvis avtagende PACF.
- En blandet ARMA-prosess viser gradvis avfall i både ACF og PACF.

For sesongmodeller gjentar de samme mønstrene seg ved sesonglagene $s$, $2s$, $3s$, og så videre. Når ACF kuttes av ved lag 1 og lag $s$ samtidig som PACF avtar gradvis, peker mønsteret mot glidende gjennomsnittsledd av første orden på begge nivåer.

Figur 3.3 illustrerer de karakteristiske mønstrene med syntetiske AR(1)- og MA(1)-prosesser. For AR(1) avtar ACF gradvis mens PACF kuttes av etter lag 1; for MA(1) er mønsteret omvendt.

<div align="center">
  <img src="../006%20analysis/aktiviteter/3_7_skrive_teorikapittel/figurer/fig_03_acf_pacf_moenstre.png" alt="Figur 3.3 Signaturmønstre i ACF og PACF" width="80%">
  <p align="center"><small><i>Figur 3.3 Signaturmønstre i ACF og PACF for simulerte AR(1)- og MA(1)-prosesser.</i></small></p>
</div>

Visuell ACF/PACF-tolkning er et nyttig utgangspunkt, men gir sjelden en entydig konklusjon. I praksis suppleres tolkningen derfor med en systematisk sammenligning av kandidatmodeller ved hjelp av informasjonskriterier. De to mest brukte er Akaikes informasjonskriterium (AIC) og det bayesianske informasjonskriteriet (BIC):

$$
\text{AIC} = -2\log(L) + 2k, \qquad \text{BIC} = -2\log(L) + k \cdot \ln(n),
$$

der $L$ er den maksimerte likelihood-verdien, $k$ er antall estimerte parametere og $n$ er antall observasjoner. Begge kriteriene balanserer modelltilpasning (uttrykt gjennom log-likelihood) mot modellkompleksitet (uttrykt gjennom antall parametere), men BIC straffer kompleksitet hardere i store utvalg. Lavere verdi er bedre for begge kriterier. Når AIC og BIC peker mot samme modell, gir det ekstra trygghet for valget. Parsimonprinsippet tilsier at man foretrekker den enkleste modellen blant kandidater med tilnærmet lik tilpasning, fordi enklere modeller generaliserer bedre til nye data. I kapittel 7.2 brukes ACF/PACF-analyse og systematisk AIC/BIC-rangering til å velge SARIMA-spesifikasjon.

### 3.5 Validering og prognoseevaluering

Etter estimering er det nødvendig å undersøke om modellen er tilstrekkelig spesifisert, og om den gir pålitelige prognoser. Dette gjøres gjennom residualdiagnostikk og evaluering på data modellen ikke er estimert på.

**Residualdiagnostikk.** Dersom modellen er riktig spesifisert, skal residualene $\hat{\varepsilon}_t$ oppføre seg tilnærmet som hvitt støy: ingen gjenværende autokorrelasjon, tilnærmet konstant varians og tilnærmet normalfordeling. Avvik fra disse egenskapene kan indikere at modellen ikke fanger all systematisk struktur i dataene.

*Ljung-Box-testen* (Ljung & Box, 1978) er en portmanteau-test som undersøker om det finnes gjenværende autokorrelasjon i residualene. Teststatistikken er

$$
Q = n(n+2) \sum_{k=1}^{m} \frac{\hat{\rho}_k^2}{n-k},
$$

der $\hat{\rho}_k$ er den estimerte autokorrelasjon i residualene ved lag $k$, $n$ er antall observasjoner og $m$ er antall lag som testes. Under nullhypotesen om ingen autokorrelasjon følger $Q$ tilnærmet en $\chi^2$-fordeling med $m - p - q$ frihetsgrader, der $p$ og $q$ er antall estimerte AR- og MA-parametere i modellen. For SARIMA-modeller bruker noen implementasjoner $m - p - q - P - Q$, der $P$ og $Q$ er de sesongmessige parameterne, men praksis varierer og den opprinnelige formuleringen med $m - p - q$ er den mest siterte. For sesongmodeller er det viktig å teste ved sesonglagene (for eksempel lag 12 og 24 for månedlige data) for å avdekke gjenværende sesongstruktur.

*ARCH-LM-testen* (Engle, 1982) undersøker om residualvariansen er konstant over tid — et av de tre stasjonaritetskravene beskrevet i seksjon 3.2. Testen regresjonerer kvadrerte residualer på sine egne laggede verdier og tester om koeffisientene samlet sett er signifikante. En signifikant test indikerer heteroskedastisitet, det vil si at modellforutsetningen om konstant feilvarians ikke er oppfylt.

*Jarque-Bera-testen* (Jarque & Bera, 1987) tester om residualfordelingen avviker fra normalfordelingen ved å kombinere avvik i skjevhet og kurtose i én teststatistikk. Normalfordelte residualer har skjevhet lik 0 og kurtose lik 3. Det bør bemerkes at MLE-estimering av SARIMA-parametere er rimelig robust mot moderate avvik fra normalitet, men prediksjonsintervaller og p-verdier forutsetter tilnærmet normalitet for å være nøyaktige.

**Prognosefeilmål.** For å vurdere modellens prognoseevne brukes kvantitative feilmål beregnet på data modellen ikke er estimert på. Tre vanlige mål er (Hyndman & Athanasopoulos, 2021):

$$
\text{MAE} = \frac{1}{n}\sum_{t=1}^{n}|y_t - \hat{y}_t|, \qquad \text{RMSE} = \sqrt{\frac{1}{n}\sum_{t=1}^{n}(y_t - \hat{y}_t)^2}, \qquad \text{MAPE} = \frac{100}{n}\sum_{t=1}^{n}\frac{|y_t - \hat{y}_t|}{y_t}.
$$

MAE gir det gjennomsnittlige absolutte avviket og er lett tolkbart i seriens opprinnelige enhet. RMSE vekter store feil tyngre og er nyttig når store prognosebom er spesielt kostbare. MAPE uttrykker feilen som en prosentandel av observert verdi og er dermed skalauavhengig, men er udefinert for nullverdier og asymmetrisk ved skjeve fordelinger. Et alternativ som unngår disse svakhetene er *Mean Absolute Scaled Error* (MASE), der feilen skaleres mot den gjennomsnittlige absolutte feilen til en naiv prognose (Hyndman & Athanasopoulos, 2021). MASE er skalauavhengig og veldefinert for alle verdier, men krever at man velger en referanseprognose å skalere mot.

**Hold-out-validering.** Prinsippet bak hold-out-validering er å dele datasettet i et treningssett og et testsett. Modellen estimeres kun på treningsdataene, og prognoser evalueres mot testdataene som modellen ikke har sett. Dette gir et realistisk bilde av prognoseevnen utover den tilpasningen som oppnås in-sample. I kapittel 8.1 evalueres modellens prognoser mot et holdout-testsett.

**Prediksjonsintervaller og biaskorreksjon.** Når en SARIMA-modell er estimert på log-transformert serie, genereres prognoser og konfidensgrenser først på log-skala:

$$
\hat{z}_{T+h} \pm z_{\alpha/2} \cdot \sigma_h,
$$

der $\hat{z}_{T+h}$ er punktprognosen, $z_{\alpha/2}$ er kvantilet fra standardnormalfordelingen og $\sigma_h$ er prognosens standardfeil ved horisont $h$. Tilbaketransformeringen til originalskala gjennom eksponensialfunksjonen gir asymmetriske prediksjonsintervaller, fordi eksponensialfunksjonen er konveks.

Et viktig poeng ved tilbaketransformering er at $\exp(\hat{z}_{T+h})$ gir medianprognosen, ikke forventningsverdien. Årsaken er Jensens ulikhet: for en konveks funksjon $g$ og en tilfeldig variabel $Z$ gjelder $E[g(Z)] \geq g(E[Z])$. Forventet verdi på originalskala er dermed

$$
E[y_{T+h}] = \exp\!\left(\hat{z}_{T+h} + \frac{\sigma_h^2}{2}\right),
$$

der $\sigma_h^2$ er prognosevariansen på log-skala. Denne biaskorreksjonen gir gjennomsnittsprognosen i stedet for medianprognosen, og kan være relevant når beslutningskonteksten krever forventede verdier. Figur 3.4 illustrerer forskjellen mellom median og gjennomsnitt for en log-normalfordelt prognose. Forskjellen mellom median- og gjennomsnittsprognosen drøftes i kapittel 9.

<div align="center">
  <img src="../006%20analysis/aktiviteter/3_7_skrive_teorikapittel/figurer/fig_04_biaskorreksjon.png" alt="Figur 3.4 Biaskorreksjon ved tilbaketransformering fra log-skala" width="80%">
  <p align="center"><small><i>Figur 3.4 Forskjellen mellom median- og gjennomsnittsprognose ved tilbaketransformering fra log-skala.</i></small></p>
</div>

Samlet sett gir dette kapitlet det teoretiske rammeverket som de påfølgende kapitlene bygger på: dekomponering og stasjonaritet gir grunnlaget for datatransformasjonene i kapittel 7.1, SARIMA-rammeverket og identifikasjonsverktøyene styrer modellvalget i kapittel 6 og 7.2, og valideringsmetodikken med biaskorreksjon danner referansen for resultatvurderingene i kapittel 8 og diskusjonen i kapittel 9.

---

## 4 Casebeskrivelse

PowerHorse er en casebedrift med behov for bedre beslutningsstøtte i produksjons- og lagerplanlegging. Bedriften selger traktorer i et marked der etterspørselen varierer mellom måneder og over tid. Når salget endrer seg uten at bedriften har gode prognoser, blir det vanskeligere å planlegge kapasitet, produksjon og lager på en effektiv måte.

I denne oppgaven brukes historiske månedlige salgsdata som grunnlag for å beskrive utviklingen i etterspørselen og for senere å bygge en prognosemodell. Casebeskrivelsen viser derfor både hvilken situasjon bedriften står i, og hvilke mønstre som finnes i det historiske salget.

### 4.1 PowerHorse og beslutningssituasjonen

PowerHorse trenger bedre grunnlag for å planlegge hvor mye som skal produseres og hvor mye lager som må bygges opp gjennom året. Når etterspørselen varierer mellom sesonger og fra år til år, øker risikoen for at bedriften enten produserer for mye eller for lite. Et mer strukturert analyseopplegg er derfor nødvendig for å kunne støtte framtidige beslutninger med data.

### 4.2 Historisk salgsutvikling

Figurene under viser den historiske utviklingen i salget slik det faktisk har vært i datasettet. Først vises hele tidsserien i observasjonsrekkefølge, og deretter årssummer for fullførte år. Hensikten er å gi et oversiktsbilde av nivå, variasjon og utvikling over tid i caset.

<div align="center">
  <img src="../006%20analysis/aktiviteter/3_1_rense_og_strukturere_data/figurer/fig_01_salgsserie_observasjoner.png" alt="Figur 4.1 Månedlig salg per observasjon" width="80%">

<p align="center"><small><i>Figur 4.1 Historisk månedlig salg.</i></small></p>
</div>

Figur 4.1 viser månedlige salgsobservasjoner i hele perioden. Figuren gir en samlet framstilling av variasjon i salgsnivået og gjør det lettere å se hvordan dataserien utvikler seg over tid.

<div align="center">
  <img src="../006%20analysis/aktiviteter/3_1_rense_og_strukturere_data/figurer/fig_02_aarstotaler_fullforte_ar.png" alt="Figur 4.2 Årlig totalsalg for fullførte år" width="80%">

<p align="center"><small><i>Figur 4.2 Årlige totalsalg.</i></small></p>
</div>

Figur 4.2 viser årlige totalsalg for fullførte år i datasettet. Årssummene brukes her som en forenklet framstilling av den langsiktige utviklingen i etterspørselen.

### 4.3 Sesongmønster i salget

I tillegg til utviklingen over tid er det viktig å beskrive hvordan salget varierer mellom måneder. Dette gir et bilde av sesongmønsteret i bedriften og viser hvilke deler av året som normalt er sterkere eller svakere.

<div align="center">
  <img src="../006%20analysis/aktiviteter/3_1_rense_og_strukturere_data/figurer/fig_03_gjennomsnitt_per_maned.png" alt="Figur 4.3 Gjennomsnittlig salg per måned" width="80%">

<p align="center"><small><i>Figur 4.3 Gjennomsnittlig salg per måned.</i></small></p>
</div>

Figur 4.3 viser gjennomsnittlig salg fordelt på månedsnummer. Figuren brukes for å beskrive den typiske fordelingen av salget gjennom året.

Tabell 4.1 under viser samme sesongmønster i tallform og gjør det lettere å sammenligne nivå, variasjon og rangering mellom månedene.

| måned_nummer | antall_observasjoner | gjennomsnittlig_salg | standardavvik | rang |
| ------------: | -------------------: | -------------------: | ------------: | ---: |
|             1 |                   17 |              4364.35 |       1099.17 |   10 |
|             2 |                   17 |              3778.12 |        765.49 |   11 |
|             3 |                   17 |              4604.53 |       1010.36 |    8 |
|             4 |                   17 |              4678.71 |        975.46 |    7 |
|             5 |                   17 |              5037.88 |       1172.62 |    5 |
|             6 |                   17 |              5031.53 |       1051.71 |    6 |
|             7 |                   17 |              4419.65 |       1032.04 |    9 |
|             8 |                   17 |              2002.76 |        367.21 |   12 |
|             9 |                   17 |              5691.65 |       1412.22 |    4 |
|            10 |                   17 |              7160.47 |       1607.03 |    3 |
|            11 |                   17 |             10826.90 |       2613.08 |    2 |
|            12 |                   17 |             13792.60 |       3480.87 |    1 |

<p align="center"><small><i>Tabell 4.1 Gjennomsnittlig salg per måned.</i></small></p>

Figur 4.4 viser spredningen i salget innad i hver kalendermåned over alle fullførte år. Boksplottet supplerer figur 4.3 ved å synliggjøre variasjonsbredden og eventuelle utliggere for hver måned.

<div align="center">
  <img src="../006%20analysis/aktiviteter/3_1_rense_og_strukturere_data/figurer/fig_04_sesongvariasjon_boksplott.png" alt="Figur 4.4 Sesongvariasjon i salg per kalendermåned" width="80%">

<p align="center"><small><i>Figur 4.4 Sesongvariasjon i salg per kalendermåned.</i></small></p>
</div>

Figuren viser at spredningen øker markant i høsesongmånedene oktober, november og desember, mens august har svært lav variasjon mellom årene.

### 4.4 Utfordringer dårlige prognoser medfører i bedriften

Når prognosene er svake, risikerer PowerHorse å planlegge produksjon og lager på feil grunnlag. Dersom bedriften overvurderer etterspørselen, kan resultatet bli for høy produksjon og unødvendig lagerbinding. Dersom bedriften undervurderer etterspørselen, kan den stå med for lav kapasitet eller utilstrekkelig lager i perioder med høy etterspørsel.

Disse utfordringene blir ekstra viktige når salget varierer gjennom året. Et tydelig sesongmønster gjør at feilvurderinger i etterspørselen kan få større konsekvenser enn i en mer stabil serie. Dette er hovedgrunnen til at PowerHorse trenger en mer systematisk analyse av historiske salgsdata og en prognosemodell som kan støtte framtidige beslutninger.

---

## 5 Metode og data

### 5.1 Metode

Oppgaven bruker en kvantitativ casebasert tilnærming der historiske månedlige salgsdata analyseres som en tidsserie. Arbeidet er lagt opp som en sekvens av dataklargjøring, deskriptiv beskrivelse av datasettet, splitting i trenings- og testdata, modellering, validering og senere prognosearbeid.

Målet med metoden er å bygge en etterprøvbar analyseprosess der de historiske salgsdataene først beskrives og dokumenteres, før de brukes som grunnlag for modellvalg og prognose. Den videre modelleringen skal gjennomføres med en SARIMA-tilnærming som er egnet for tidsserier med både trend og sesong.

### 5.2 Data

Datagrunnlaget består av historiske månedlige salgsobservasjoner for PowerHorse. Datasettet dekker perioden fra 1964-01 til 1981-06 og inneholder totalt 210 observasjoner. Serien er strukturert kronologisk og brukes som grunnlag for videre modellering og prognosearbeid.

Datasettet er dokumentert med en arbeidsantagelse om at datakvaliteten allerede er kvalitetssjekket av de som leverte dataene. Prosjektet har ikke egne eksterne kilder for uavhengig verifikasjon av datakvaliteten, og denne antagelsen må derfor ligge til grunn for analysen.

For å kunne validere modellen på en ryddig måte er datasettet delt i to deler ved nyttår 1977/1978. Treningsdatasettet dekker perioden 1964-01 til 1977-12 (168 observasjoner), mens testdatasettet dekker 1978-01 til 1981-06 (42 observasjoner). Splitdatoen er valgt slik at treningsdatasettet inneholder utelukkende hele kalenderår, noe som bevarer sesongstrukturen for SARIMA-modellering. Forholdet mellom trenings- og testdata blir omtrent 80/20, og gir et tydelig skille mellom datagrunnlaget som brukes til modellestimering og datagrunnlaget som brukes til å vurdere prognoseegenskaper.

Tabell 5.1 oppsummerer de viktigste egenskapene ved datasettet.

| Måltall                   | Verdi                                    |
| :------------------------- | :--------------------------------------- |
| Startdato                  | 1964-01                                  |
| Sluttdato                  | 1981-06                                  |
| Antall observasjoner       | 210                                      |
| Antall manglende måneder  | 0                                        |
| Min salg                   | 1413                                     |
| Maks salg                  | 19164                                    |
| Gjennomsnittlig salg       | 5958.3                                   |
| Median salg                | 5162.5                                   |
| Standardavvik              | 3450.4                                   |
| Variasjonskoeffisient (CV) | 57.9 %                                   |
| Interkvartilbredde (IQR)   | 2680.75                                  |
| Merknad                    | 1981 er delår og dekker kun januar-juni |

<p align="center"><small><i>Tabell 5.1 Nøkkelegenskaper ved det månedlige salgsdatasettet (1964-01 til 1981-06).</i></small></p>

---

## 6 Modell

Med metode og datagrunnlag på plass formaliseres nå modellrammeverket som ligger til grunn for analysen. Kapitlet begrunner først hvorfor SARIMA er en passende modellklasse for det aktuelle datasettet, klargjør deretter de statistiske antagelsene modellen hviler på, og presenterer til slutt den generelle SARIMA-spesifikasjonen som operasjonaliseres i kapittel 7.

### 6.1 Vurdering av modelltype

Før en konkret spesifikasjon kan velges, må det vurderes hvilken modelltype som passer best til dataserien. Denne vurderingen gjøres på treningsdatasettet for perioden 1964-01 til 1977-12, siden det er dette datagrunnlaget som senere skal brukes til modellestimering. Hensikten i dette delavsnittet er derfor ikke å velge ordener eller estimere parametere, men å begrunne hvorfor en SARIMA-modell er en hensiktsmessig modellklasse for videre arbeid.

Som vist i kapittel 4 har serien både tydelig trend og et markert årlig sesongmønster. Figur 4.1 og figur 4.2 viser at salget ikke ligger stabilt rundt ett fast nivå over tid, mens figur 4.3, figur 4.4 og tabell 4.1 viser klare forskjeller mellom månedene i året. Disse mønstrene peker mot en modelltype som kan håndtere både utvikling over tid og gjentakende sesongvariasjon.

Datagrunnlaget som faktisk brukes i modellarbeidet er beskrevet i kapittel 5. Treningssettet dekker 14 hele kalenderår og inneholder ingen manglende måneder, noe som gir et ryddig grunnlag for tidsseriemodellering. Samtidig består datasettet bare av tid og salg, uten eksterne forklaringsvariabler som pris, kampanjer eller markedsforhold. Dette taler for en univariat modelltilnærming framfor en modell som krever forklaringsvariabler som ikke finnes i datagrunnlaget.

Samlet sett tilsier derfor både mønstrene i historisk salg og strukturen i treningsdatasettet at SARIMA er en passende modellklasse for videre analyse. Modellen kan i prinsippet håndtere trend gjennom differensiering og årlig sesong gjennom sesongledd, samtidig som den holder seg innenfor prosjektets avgrensing og tilgjengelige data. På dette stadiet begrunnes altså modellfamilien, mens valg av konkret spesifikasjon gjøres senere.

### 6.2 Modellantagelser

Bruken av en SARIMA-modell bygger på flere antagelser som må gjøres eksplisitte før videre modellarbeid. Disse antagelsene handler både om datagrunnlaget og om de statistiske egenskapene modellen forutsetter.

- Serien behandles som en univariat månedlig tidsserie med fast sesonglengde på 12 måneder.
- Serien analyseres videre på log-skala, det vil si som $z_t = log(y_t)$, for å stabilisere variansen før differensiering og modellspesifikasjon.
- Observasjonene antas å være korrekt datert, kronologisk ordnet og uten manglende måneder i treningsperioden.
- De historiske mønstrene i trend og sesong antas å være relevante nok til å brukes som grunnlag for videre modellering.
- Framtidig utvikling modelleres uten eksterne forklaringsvariabler, fordi datasettet kun inneholder tid og salg.
- Eventuelle trend- og sesongeffekter antas å kunne håndteres innenfor SARIMA-rammeverket gjennom ordinær og sesongmessig differensiering.
- Modellparametrene antas å være tilstrekkelig stabile i analyseperioden til at én samlet modell kan estimeres på treningsdataene.
- Feilleddet antas å ha forventning lik null.
- Feilleddet antas å ha tilnærmet konstant varians over tid.
- Feilleddet antas å være uten systematisk autokorrelasjon når modellen senere er riktig spesifisert.
- Datakvaliteten bygger fortsatt på arbeidsantagelsen om at datasettet er kvalitetssjekket av kilden som leverte det, siden prosjektet ikke har egne eksterne kilder for uavhengig verifikasjon.

Disse antagelsene er ikke det samme som verifiserte fakta. Noen av dem må testes eller vurderes nærmere i senere aktiviteter, særlig når konkret spesifikasjon, residualdiagnostikk og prognoseegenskaper skal undersøkes. Delavsnittet fungerer derfor som en tydelig avgrensing av hva modellen forutsetter før estimering.

### 6.3 Generell SARIMA-modell

Etter at modelltypen er begrunnet og antagelsene er gjort eksplisitte, kan den generelle modellen beskrives matematisk. I denne oppgaven brukes en sesongbasert autoregressiv integrert glidende gjennomsnittsmodell, forkortet SARIMA. Modellen er egnet for tidsserier der observasjonene er ordnet i tid og der serien kan inneholde både langsiktig utvikling og gjentakende sesongmønster.

La $y_t$ betegne observert salg i måned $t$, der $t = 1, 2, \dots, T$. Her er $T$ antall observerte måneder i datasettet. Videre brukes forsinkelsesoperatoren $B$, definert ved

$$
By_t = y_{t-1}.
$$

Forsinkelsesoperatoren gjør det mulig å skrive modellen kompakt ved å uttrykke dagens observasjon som en funksjon av tidligere observasjoner og tidligere tilfeldige sjokk.

Den generelle modellen skrives som en SARIMA$(p,d,q)(P,D,Q)_{12}$-modell, der tallet $12$ angir at sesonglengden er tolv måneder. Modellen kan da skrives som

$$
\Phi(B^{12}) \, \phi(B) \, (1-B)^d (1-B^{12})^D y_t
=
\Theta(B^{12}) \, \theta(B) \, \varepsilon_t.
$$

I denne ligningen er $p$, $d$ og $q$ de ikke-sesongmessige modellordnene, mens $P$, $D$ og $Q$ er de sesongmessige modellordnene. Alle disse størrelsene er ukjente før modellvalget er gjennomført. De bestemmer hvor mange ledd modellen skal bruke for henholdsvis autoregressive effekter, differensiering og glidende gjennomsnitt, både på vanlig og sesongmessig nivå.

De ikke-sesongmessige polynomene defineres som

$$
\phi(B) = 1 - \phi_1 B - \phi_2 B^2 - \cdots - \phi_p B^p
$$

og

$$
\theta(B) = 1 + \theta_1 B + \theta_2 B^2 + \cdots + \theta_q B^q.
$$

De sesongmessige polynomene defineres tilsvarende som

$$
\Phi(B^{12}) = 1 - \Phi_1 B^{12} - \Phi_2 B^{24} - \cdots - \Phi_P B^{12P}
$$

og

$$
\Theta(B^{12}) = 1 + \Theta_1 B^{12} + \Theta_2 B^{24} + \cdots + \Theta_Q B^{12Q}.
$$

Koeffisientene $\phi_1, \dots, \phi_p$ er de ikke-sesongmessige autoregressive parameterne. De beskriver hvordan dagens salg henger sammen med salg i tidligere måneder. Koeffisientene $\Phi_1, \dots, \Phi_P$ er de sesongmessige autoregressive parameterne og beskriver hvordan dagens salg henger sammen med observasjoner én eller flere sesonger tilbake, det vil si 12, 24 eller flere måneder tilbake i tid.

Koeffisientene $\theta_1, \dots, \theta_q$ er de ikke-sesongmessige glidende gjennomsnittsparameterne. De uttrykker hvordan nåværende observasjon påvirkes av tidligere tilfeldige sjokk i serien. Tilsvarende er $\Theta_1, \dots, \Theta_Q$ de sesongmessige glidende gjennomsnittsparameterne, og disse fanger opp hvordan sjokk fra tidligere sesonger påvirker dagens salg.

Leddene $(1-B)^d$ og $(1-B^{12})^D$ brukes for å differensiere serien. Den ordinære differensieringen $(1-B)^d$ brukes for å fjerne trend eller annen ikke-stasjonær utvikling i nivået til serien. Den sesongmessige differensieringen $(1-B^{12})^D$ brukes for å fjerne systematiske mønstre som gjentar seg med tolv måneders mellomrom. Dersom $d=0$, brukes ingen ordinær differensiering, og dersom $D=0$, brukes ingen sesongmessig differensiering.

For å skrive modellen mer intuitivt kan den differensierte serien defineres som

$$
w_t = (1-B)^d (1-B^{12})^D y_t.
$$

Da kan modellen skrives om til

$$
\Phi(B^{12}) \, \phi(B) \, w_t = \Theta(B^{12}) \, \theta(B) \, \varepsilon_t.
$$

Her er $w_t$ den transformerte serien etter at trend og sesong er håndtert gjennom differensiering. Serien $w_t$ er dermed den delen av dataserien som modelleres videre med autoregressive og glidende gjennomsnittsledd.

Størrelsen $\varepsilon_t$ er modellens feilledd, også kalt innovasjonsledd eller tilfeldig sjokk i periode $t$. Dette leddet representerer den delen av salget modellen ikke kan forklare systematisk ut fra tidligere observasjoner og tidligere sjokk. I en velfungerende modell antas $\varepsilon_t$ å ha forventning lik null, konstant varians og ingen systematisk autokorrelasjon over tid.

Med ord betyr dette at SARIMA-modellen forklarer månedlig salg ved å kombinere fire mekanismer. For det første kan modellen fjerne langsiktig utvikling gjennom ordinær differensiering. For det andre kan den fjerne gjentakende årlig sesong gjennom sesongdifferensiering. For det tredje kan den bruke tidligere observerte salgsnivåer til å forklare nåværende salg gjennom autoregressive ledd. For det fjerde kan den bruke tidligere tilfeldige avvik til å beskrive kortsiktige og sesongmessige justeringer gjennom glidende gjennomsnittsledd.

De ukjente størrelsene i modellen er dermed modellordnene $p$, $d$, $q$, $P$, $D$ og $Q$, samt parameterne $\phi_i$, $\Phi_j$, $\theta_k$ og $\Theta_\ell$. I kapittel 7 skal disse størrelsene bestemmes ved hjelp av analyse av tidsseriens egenskaper og estimering på treningsdata. I dette kapittelet er poenget kun å definere modellformen og å vise hvilke matematiske komponenter som inngår i prognosemodellen.

---

## 7 Analyse

I dette kapittelet gjennomføres den konkrete analysen der SARIMA-modellen fra kapittel 6 spesifiseres og estimeres på treningsdata. Arbeidet følger tre steg: først vurderes stasjonaritet og differensieringsbehov, deretter brukes ACF/PACF-analyse til å bestemme modellordner, og til slutt estimeres parameterne og residualene vurderes.

### 7.1 Stasjonaritet og behov for differensiering

Før en SARIMA-modell kan spesifiseres videre, må det vurderes om serien er tilstrekkelig stasjonær, eller om den må differensieres. Grunnen er at modellen forutsetter at serien etter eventuell differensiering har mer stabile egenskaper over tid, slik at mønstrene kan beskrives med faste parametere. I denne oppgaven gjøres vurderingen på den log-transformerte serien $z_t = log(y_t)$, siden salget er strengt positivt og fordi log-transformasjon reduserer problemet med nivåavhengig varians i datasettet.

For å gjøre denne vurderingen brukes to komplementære tester. Augmented Dickey-Fuller-testen (ADF) brukes for å undersøke om serien fortsatt ser ut til å ha en enhetsrot, mens KPSS-testen brukes for å undersøke om serien kan avvises som stasjonær. Testene tolkes samlet og støttes av en visuell sammenligning av serievariantene på log-skala, siden ingen enkelt test alene er tilstrekkelig grunnlag for valg av differensiering.

<div align="center">
  <img src="../006%20analysis/aktiviteter/3_2_velge_og_estimere_modell/figurer/fig_01_serievarianter.png" alt="Figur 7.1 Log-transformerte serievarianter for vurdering av stasjonaritet og differensiering" width="80%">
  <p align="center"><small><i>Figur 7.1 Log-transformerte serievarianter.</i></small></p>
</div>

Tabell 7.1 oppsummerer testresultatene for den log-transformerte serien og de tre aktuelle differensieringsvariantene.

| Serievariant                                  | Kandidat     | ADF teststat | ADF p-verdi | KPSS teststat | KPSS p-verdi | Kort vurdering                                                                                        |
| :-------------------------------------------- | :----------- | -----------: | ----------: | ------------: | -----------: | :---------------------------------------------------------------------------------------------------- |
| Log-transformert serie $z_t = log(y_t)$      | $d=0, D=0$ |      -1.8701 |      0.3463 |        1.5675 |       0.0100 | Testene peker samlet mot fortsatt ikke-stasjonaritet.                                                 |
| Ordinært differensiert $(1-B)z_t$           | $d=1, D=0$ |      -4.6489 |      0.0001 |        0.1412 |       0.1000 | Testene peker mot stasjonaritet, men figurdiagnostikken viser fortsatt tydelig sesongstruktur.        |
| Sesongdifferensiert $(1-B^{12})z_t$          | $d=0, D=1$ |      -3.6410 |      0.0050 |        0.1775 |       0.1000 | Testene peker mot stasjonaritet og fjerner sesongmønsteret bedre enn ordinær differensiering alene. |
| Kombinert differensiert $(1-B)(1-B^{12})z_t$ | $d=1, D=1$ |      -4.6172 |      0.0001 |        0.0961 |       0.1000 | Testene peker mot stasjonaritet og figuren gir den mest balanserte serien samlet sett.                |

<p align="center"><small><i>Tabell 7.1 Testresultater for stasjonaritet og differensiering.</i></small></p>

Resultatene viser først og fremst at den log-transformerte serien ikke bør brukes videre uten differensiering. ADF- og KPSS-testene gir deretter støtte til tre alternative kandidater: ordinær differensiering, sesongdifferensiering og kombinert differensiering. Testene alene peker derfor ikke entydig på én vinner, men de utelukker at serien kan modelleres direkte uten videre transformasjon.

Når testresultatene tolkes sammen med figur 7.1, blir det likevel tydelig at ordinær differensiering alene ikke er tilstrekkelig. Varianten med $d=1$ og $D=0$ får gode testresultater, men figuren viser fortsatt en tydelig gjenværende sesongstruktur. Dette tyder på at sesongmessig ikke-stasjonaritet ikke er fjernet godt nok selv om den ordinære trenden er redusert. Sesongdifferensiering alene med $d=0$ og $D=1$ er også en plausibel kandidat, men den kombinerte varianten gir den mest balanserte serien når både trend og sesong vurderes samlet på log-skala.

På dette grunnlaget vurderes derfor kombinert differensiering med $d=1$ og $D=1$ som hovedkandidat videre i modellarbeidet. Denne konklusjonen bygger ikke bare på p-verdiene, men på en samlet faglig vurdering av teststatistikkene, p-verdiene og den visuelle diagnostikken på log-transformert serie. Sesongdifferensiering alene beholdes som et enklere alternativ dersom senere analyse skulle vise at kombinert differensiering er mer omfattende enn nødvendig. Den automatiserte differensieringsvurderingen i analyseartefaktene anbefalte $d=0, D=1$ som enkleste kandidat, men den samlede vurderingen av testresultater og visuell diagnostikk ledet til at $d=1, D=1$ ble foretrukket som hovedkandidat.

### 7.2 ACF/PACF-analyse og ordensvalg

Med differensieringsordnene $d=1$ og $D=1$ fastlagt gjenstår det å bestemme de autoregressive og glidende gjennomsnittsordnene $p$, $q$, $P$ og $Q$. Til dette brukes autokorrelasjonsfunksjonen (ACF) og den partielle autokorrelasjonsfunksjonen (PACF) beregnet på den differensierte log-serien $w_t = (1-B)(1-B^{12})\log(y_t)$.

<div align="center">
  <img src="../006%20analysis/aktiviteter/3_2_velge_og_estimere_modell/figurer/fig_02_acf_pacf.png" alt="Figur 7.2 ACF og PACF for den differensierte log-serien" width="80%">
  <p align="center"><small><i>Figur 7.2 ACF og PACF for $(1-B)(1-B^{12})\log(y_t)$.</i></small></p>
</div>

Figur 7.2 viser ACF og PACF med 36 lags. I ACF-plottet er det en tydelig negativ spike ved lag 1 og en negativ spike ved sesonglag 12. Etter disse lagene faller ACF raskt innenfor konfidensintervallet. PACF-plottet viser et avtagende mønster ved de første lagene og ved sesonglagene 12 og 24. Denne kombinasjonen — avkuttende ACF ved lag 1 og lag 12 med avtagende PACF — er et klassisk mønster for en modell med glidende gjennomsnittsledd av første orden både på ikke-sesongmessig og sesongmessig nivå. Mønsteret peker dermed mot en SARIMA$(0,1,1)(0,1,1)_{12}$-spesifikasjon.

For å støtte den visuelle tolkningen ble det gjennomført et systematisk kandidatsøk der alle kombinasjoner av $p \in \{0,1,2\}$, $q \in \{0,1,2\}$, $P \in \{0,1\}$ og $Q \in \{0,1\}$ ble tilpasset med faste differensieringsordner $d=1$ og $D=1$. Differensieringsordnene ble holdt faste fordi stasjonaritetsvurderingen i avsnitt 7.1 allerede konkluderte med at kombinert differensiering var hovedkandidaten. Dette gir 36 kandidater som alle ble estimert på den log-transformerte treningsserien. Tabell 7.2 viser de ti beste kandidatene rangert etter AIC.

| Modell                   | Parametere | Log-likelihood |     AIC |     BIC |
| :----------------------- | ---------: | -------------: | ------: | ------: |
| SARIMA(0,1,1)(0,1,1)₁₂ |          3 |         104.41 | -202.83 | -193.70 |
| SARIMA(1,1,1)(0,1,1)₁₂ |          4 |         104.88 | -201.76 | -189.59 |
| SARIMA(0,1,1)(1,1,1)₁₂ |          4 |         104.87 | -201.75 | -189.57 |
| SARIMA(0,1,2)(0,1,1)₁₂ |          4 |         104.81 | -201.61 | -189.44 |
| SARIMA(1,1,2)(0,1,1)₁₂ |          5 |         105.68 | -201.37 | -186.15 |
| SARIMA(2,1,1)(0,1,1)₁₂ |          5 |         105.33 | -200.66 | -185.45 |
| SARIMA(1,1,1)(1,1,1)₁₂ |          5 |         105.22 | -200.44 | -185.23 |
| SARIMA(0,1,2)(1,1,1)₁₂ |          5 |         105.16 | -200.32 | -185.10 |
| SARIMA(2,1,1)(1,1,1)₁₂ |          6 |         105.76 | -199.53 | -181.27 |
| SARIMA(1,1,2)(1,1,1)₁₂ |          6 |         105.01 | -198.03 | -179.77 |

<p align="center"><small><i>Tabell 7.2 Topp 10 SARIMA-kandidater rangert etter AIC. Alle 36 kandidater konvergerte.</i></small></p>

Resultatene viser at SARIMA$(0,1,1)(0,1,1)_{12}$ har lavest AIC (-202.83) og lavest BIC (-193.70) blant alle kandidatene. De mer komplekse modellene forbedrer log-likelihood bare marginalt, men straffes av det ekstra antallet parametere i begge informasjonskriteriene. Modellen som velges er dermed SARIMA$(0,1,1)(0,1,1)_{12}$ — den såkalte airline-modellen, som er en velkjent og mye brukt spesifikasjon for månedlige tidsserier med trend og sesong. Valget bygger på at modellen har best AIC og BIC, er konsistent med ACF/PACF-tolkningen, og er den enkleste blant toppkandidatene.

### 7.3 Modellestimering og parameterresultater

Den valgte modellen SARIMA$(0,1,1)(0,1,1)_{12}$ estimeres på den log-transformerte treningsserien $z_t = \log(y_t)$ for perioden 1964-01 til 1977-12. Modellen spesifiseres med ordinær differensiering $d=1$, sesongmessig differensiering $D=1$ og sesonglengde $m=12$. Parameterne estimeres med maksimum likelihood.

Tabell 7.3 viser de estimerte parameterne med tilhørende standardfeil, z-verdier og p-verdier.

| Parameter               | Koeffisient | Standardfeil | z-verdi | p-verdi | 95 % KI nedre | 95 % KI øvre |
| :---------------------- | ----------: | -----------: | ------: | ------: | ------------: | ------------: |
| $\theta_1$ (ma.L1)    |     -0.8217 |       0.0303 |  -27.15 | < 0.001 |        -0.881 |        -0.762 |
| $\Theta_1$ (ma.S.L12) |     -0.5998 |       0.0570 |  -10.53 | < 0.001 |        -0.711 |        -0.488 |
| $\sigma^2$            |      0.0146 |       0.0009 |   16.25 | < 0.001 |         0.013 |         0.016 |

<p align="center"><small><i>Tabell 7.3 Estimerte parametere for SARIMA$(0,1,1)(0,1,1)_{12}$.</i></small></p>

Begge MA-parameterne er sterkt signifikante med p-verdier under 0.001. Den ikke-sesongmessige glidende gjennomsnittsparameteren $\theta_1 = -0.82$ indikerer at modellen bruker en stor andel av forrige måneds prognosefeil til å korrigere neste periodes prognose. Den sesongmessige glidende gjennomsnittsparameteren $\Theta_1 = -0.60$ viser at modellen også korrigerer basert på prognosefeil fra samme måned ett år tilbake. Den estimerte feilvariansen $\sigma^2 = 0.0146$ gjelder på log-skala.

Med de estimerte parameterverdiene kan modellen skrives eksplisitt som

$$
(1-B)(1-B^{12}) z_t = (1 - 0.8217 B)(1 - 0.5998 B^{12}) \varepsilon_t.
$$

Når B-operatoren skrives helt ut og ligningen omformes slik at $z_t$ står alene på venstresiden, får modellen følgende spesifikke form:

$$
z_t
=
z_{t-1} + z_{t-12} - z_{t-13}
+ \varepsilon_t
- 0.8217 \varepsilon_{t-1}
- 0.5998 \varepsilon_{t-12}
+ 0.4929 \varepsilon_{t-13}.
$$

Den estimerte innovasjonsvariansen er samtidig $\sigma^2 = 0.0146$ på log-skala.

Dagens log-salg $z_t$ forklares ved hjelp av to hovedspor i historikken. Leddet $z_{t-1}$ representerer den løpende ikke-sesongmessige utviklingen fra måned til måned, altså det sporet som henger sammen med ordinær differensiering og håndtering av trend. Leddet $z_{t-12}$ representerer sesongsporet, fordi det kobler dagens nivå til samme måned året før. Samtidig trekkes $z_{t-13}$ fra som et korreksjonsledd fordi ordinær og sesongmessig differensiering virker sammen og skaper et overlapp mellom de to sporene. På støysiden beskriver $\varepsilon_{t-1}$ en kortsiktig ikke-sesongmessig korreksjon, mens $\varepsilon_{t-12}$ beskriver en sesongmessig korreksjon fra samme måned året før. Det positive leddet $\varepsilon_{t-13}$ oppstår fordi disse to glidende gjennomsnittsleddene virker sammen i modellen. De negative MA-koeffisientene viser dermed at modellen gjør tydelige justeringer både for kortsiktige avvik og for sesongmessige avvik.

### 7.4 Validering

I dette delavsnittet vurderes om den estimerte modellen oppfyller sentrale modellforutsetninger godt nok til å kunne brukes videre i prognosearbeidet. Hensikten er å undersøke residualene for tegn til gjenværende autokorrelasjon, avvik fra normalitet og ustabil varians, slik at modellens styrker og svakheter blir tydelige før testsettresultatene presenteres i kapittel 8. Heteroskedastisitet behandles her som et teknisk funn i valideringen, mens betydningen av funnet for modellens brukbarhet drøftes senere i kapittel 9.

Figur 7.3 viser residualdiagnostikk for den estimerte modellen.

<div align="center">
  <img src="../006%20analysis/aktiviteter/3_2_velge_og_estimere_modell/figurer/fig_03_diagnostikk.png" alt="Figur 7.3 Residualdiagnostikk for SARIMA(0,1,1)(0,1,1)₁₂" width="80%">
  <p align="center"><small><i>Figur 7.3 Residualdiagnostikk for SARIMA$(0,1,1)(0,1,1)_{12}$.</i></small></p>
</div>

Ved korte lag viser korrelogrammet ingen signifikant autokorrelasjon i residualene, og Ljung-Box-testen ved lag 1 gir p-verdi 0.46, noe som ikke gir grunnlag for å forkaste hypotesen om hvitt støy. Histogrammet og Q-Q-plottet viser at residualene har noe avvik fra normalfordeling i halene, med tyngre venstrehale og kurtose på 7.95. Jarque-Bera-testen gir p-verdi under 0.01. Det observeres også heteroskedastisitet, der tidlige residualer har høyere varians enn senere perioder. Residualdiagnostikken gir dermed et teknisk bilde av hvilke modellforutsetninger som ser rimelige ut, og hvilke svakheter som må tas med videre i vurderingen av modellen.

Selv om korrelogrammet ved korte lag ikke gir grunn til bekymring, kan kumulativ autokorrelasjon ved sesongrelevante lag likevel være til stede. For å undersøke dette ble det gjennomført Ljung-Box-tester ved lag 12 og 24, samt en ARCH-LM-test med 12 lag. Tabell 7.4 oppsummerer testresultatene.

| Test      | Lag | Teststatistikk |  p-verdi | Kort vurdering                                                    |
| :-------- | --: | -------------: | -------: | :---------------------------------------------------------------- |
| Ljung-Box |  12 |        35.6302 | 0.000097 | Nullhypotesen om ingen residualautokorrelasjon forkastes ved 5 %. |
| Ljung-Box |  24 |        35.9690 | 0.030599 | Nullhypotesen om ingen residualautokorrelasjon forkastes ved 5 %. |
| ARCH-LM   |  12 |       134.2280 |  < 0.001 | Nullhypotesen om homoskedastisitet forkastes klart.               |

<p align="center"><small><i>Tabell 7.4 Supplerende residualtester for SARIMA$(0,1,1)(0,1,1)_{12}$.</i></small></p>

De supplerende testene styrker dermed de visuelle funnene. Ljung-Box-testene ved sesongrelevante lag peker mot gjenværende residualautokorrelasjon, og ARCH-LM-testen gir sterk støtte til heteroskedastisitet i residualene. Dette innebærer at modellforutsetningene ikke er fullt oppfylt, og at disse svakhetene må tas med videre når modellens egnethet skal vurderes i diskusjonskapitlet.

Samlet sett viser analysekapitlet at modellen er estimert med signifikante parametere, men også at residualene har svakheter som må vurderes opp mot modellens praktiske bruk. I neste kapittel presenteres derfor hvordan modellen presterer mot testdatasettet, før egnethet og begrensninger diskuteres samlet senere.

---

## 8 Resultat

### 8.1 Resultater fra testsettvalidering

Testsettvalideringen er gjennomført som en fast holdout-evaluering. Den estimerte SARIMA$(0,1,1)(0,1,1)_{12}$-modellen fra kapittel 7.3 er brukt til å generere prognoser for hele testperioden 1978-01 til 1981-06, uten ny modellseleksjon eller rullerende reestimering. Prognosene er deretter sammenlignet med observerte salgstall på original skala.

Figur 8.1 viser hvordan prognosen følger den observerte utviklingen i testperioden.

<div align="center">
  <img src="../006%20analysis/aktiviteter/3_3_validere_modell/figurer/fig_01_testsettprognose.png" alt="Figur 8.1 Testsettvalidering for SARIMA-modellen" width="80%">
  <p align="center"><small><i>Figur 8.1 Observerte og prognostiserte salgstall med 95 % prediksjonsintervall i testperioden 1978-01 til 1981-06.</i></small></p>
</div>

Tabell 8.1 oppsummerer de tre sentrale feilmålene for testsettet.

| Feilmål |  Verdi |
| :------- | -----: |
| MAE      | 415.17 |
| RMSE     | 494.13 |
| MAPE     | 5.39 % |

<p align="center"><small><i>Tabell 8.1 Feilmål for testsettvalidering av SARIMA$(0,1,1)(0,1,1)_{12}$.</i></small></p>

Resultatene viser at modellen følger sesongmønsteret i testperioden godt og ligger tett på de observerte verdiene gjennom store deler av perioden. Samtidig ligger prognosekurven gjennomgående noe over faktisk salg. I 41 av 42 måneder er prognosen høyere enn observert verdi, og største absolutte avvik oppstår i desember 1979 med en overprognose på 1227.42. Gjennomsnittlig absolutt prosentfeil øker fra 4.6 % i 1978 til 4.7 % i 1979, 5.8 % i 1980 og 7.5 % i første halvår 1981, noe som tyder på at modellens implisitte trendekstrapolering overstiger den faktiske veksten i testperioden. Testsettet tyder dermed på at modellen fanger form og timing i sesongmønsteret godt, men at den har en positiv nivåbias som tiltar over prognoshorisonten. Disse funnene danner sammen med residualdiagnostikken i kapittel 7.4 grunnlag for den videre diskusjonen i kapittel 9.

### 8.2 Resultater fra prognosearbeidet

For å produsere den endelige prognosen er SARIMA$(0,1,1)(0,1,1)_{12}$-modellen refittet på hele datasettet (210 observasjoner, januar 1964 til juni 1981). Modellspesifikasjonen er uendret fra estimeringen i kapittel 7.3; formålet med refittingen er å utnytte all tilgjengelig informasjon slik at prognosen blir så oppdatert som mulig. De refittede parameterne er nær de opprinnelige treningsestimatene ($\theta_1 = -0.82$, $\Theta_1 = -0.62$, $\hat{\sigma}^2 = 0.012$), noe som bekrefter at modellstrukturen er stabil over det utvidede datagrunnlaget.

Figur 8.2 viser historisk salg for de siste 3,5 årene sammen med den 12-måneders prognosen og tilhørende 95 % prediksjonsintervall. Den vertikale stiplede linjen markerer prognoseopprinnelsen (juni 1981).

<div align="center">
  <img src="../006%20analysis/aktiviteter/3_4_lage_prognose_og_anbefalinger/figurer/fig_01_prognose_12_maaneder.png" alt="12-måneders prognose med prediksjonsintervall" width="80%">
  <p align="center"><small><i>Figur 8.2 12-måneders prognose for SARIMA$(0,1,1)(0,1,1)_{12}$ med 95 % prediksjonsintervall (juli 1981 til juni 1982).</i></small></p>
</div>

Tabell 8.2 oppsummerer punktprognosen og 95 % prediksjonsintervall for hver måned i prognoseperioden.

| Måned   | Punktprognose | Nedre 95 % | Øvre 95 % |
| :------ | ------------: | ----------: | --------: |
| 1981-07 |         6 159 |       4 990 |     7 602 |
| 1981-08 |         2 694 |       2 176 |     3 337 |
| 1981-09 |         7 991 |       6 431 |     9 928 |
| 1981-10 |         9 918 |       7 956 |    12 362 |
| 1981-11 |        15 188 |      12 146 |    18 992 |
| 1981-12 |        19 483 |      15 531 |    24 439 |
| 1982-01 |         6 308 |       5 013 |     7 937 |
| 1982-02 |         5 293 |       4 194 |     6 680 |
| 1982-03 |         6 584 |       5 201 |     8 334 |
| 1982-04 |         6 578 |       5 181 |     8 353 |
| 1982-05 |         7 201 |       5 655 |     9 170 |
| 1982-06 |         7 016 |       5 494 |     8 961 |

<p align="center"><small><i>Tabell 8.2 Månedlig punktprognose og 95 % prediksjonsintervall for perioden juli 1981 til juni 1982.</i></small></p>

Prognosen viser et tydelig sesongmønster som samsvarer med den historiske salgsprofilen. Desember 1981 er forventet toppmåned med et punktestimat på 19 483, mens august 1981 er forventet bunnmåned med 2 694. Samlet prognosesalg for 12-månedersperioden er 100 413. Prediksjonsintervallene bredder gradvis utover horisonten, med en gjennomsnittlig bredde på om lag 3 800 enheter, noe som reflekterer at usikkerheten øker med antall steg fremover.

Tilbaketransformeringen fra log-skala bruker standard $\exp(\hat{z})$, som gir medianprognosen på originalskala. En analytisk biaskorreksjon med $\exp(\hat{z} + \hat{\sigma}^2/2)$ ville gitt gjennomsnittsprognosen, men oppjusteringen er marginal — fra om lag 0,6 % ved horisont 1 til om lag 0,8 % ved horisont 12 — og ville forsterket den positive nivåbiasen som ble identifisert i testsettvalideringen. Denne metodiske nyansen drøftes nærmere i kapittel 9.3.

Prognosestrukturen har tydelige implikasjoner for kapasitetsplanlegging hos PowerHorse, med høysesong (november–januar) som krever vesentlig høyere produksjonskapasitet enn lavsesong (juni–august). En detaljert drøfting av praktiske implikasjoner og modellbegrensninger følger i kapittel 9.

---

## 9 Diskusjon

I dette kapittelet drøftes funnene fra modellering, analyse og resultat opp mot problemstillingen fra kapittel 1.1. Hensikten er å vurdere i hvilken grad den valgte modellen gir et tilstrekkelig beslutningsgrunnlag for PowerHorse, og å løfte fram styrker, svakheter, begrensninger og praktiske implikasjoner som ikke kommer fram av resultatkapitlet alene.

Figur 9.1 viser hele den historiske tidsserien sammen med den 12-måneders prognosen og setter kontekst for drøftingene som følger.

<div align="center">
  <img src="../006%20analysis/aktiviteter/3_4_lage_prognose_og_anbefalinger/figurer/fig_02_helhetsfigur.png" alt="Figur 9.1 Historisk salg og 12-måneders prognose" width="80%">
  <p align="center"><small><i>Figur 9.1 Historisk månedlig traktorsalg (1964–1981) og 12-måneders prognose med 95 % prediksjonsintervall.</i></small></p>
</div>

### 9.1 Modellvalg og parsimoni

Den valgte modellen SARIMA$(0,1,1)(0,1,1)_{12}$ — den såkalte airline-modellen (Box et al., 2015, kap. 9) — er en av de mest brukte spesifikasjonene for månedlige tidsserier med trend og sesong. Med bare tre estimerte parametere er den den enkleste blant alle 36 kandidater som ble evaluert i kapittel 7.2, og den oppnådde likevel lavest AIC og BIC. De mer komplekse alternativene forbedret log-likelihood bare marginalt, noe som taler for at ekstra parametere ikke fanger opp vesentlig tilleggsinformasjon i denne serien.

Valget av log-transformasjon er sentralt for modellens egenskaper. Transformasjonen stabiliserer variansen ved at sesongutslagene, som er proporsjonale med salgsnivået, blir tilnærmet additive på log-skala. Samtidig innebærer tilbaketransformeringen at prognosene på originalskala har en multiplikativ struktur, der usikkerheten vokser med forventningsverdien. Denne egenskapen er ønskelig for salgsdata der absolutte svingninger normalt øker i takt med volumet.

Et viktig spørsmål er om modellstrukturen er stabil nok til å gi pålitelige prognoser. Tabell 9.1 viser parameterne fra den refittede modellen på hele datasettet (210 observasjoner), sammenlignet med treningsestimatene i Tabell 7.3.

| Parameter | Koeffisient | Standardfeil | z-verdi | p-verdi | 95 % KI nedre | 95 % KI øvre |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| $\theta_1$ (ma.L1) | -0.8215 | 0.0240 | -34.29 | < 0.001 | -0.869 | -0.775 |
| $\Theta_1$ (ma.S.L12) | -0.6228 | 0.0459 | -13.58 | < 0.001 | -0.713 | -0.533 |
| $\sigma^2$ | 0.0115 | 0.0006 | 20.92 | < 0.001 | 0.010 | 0.013 |

<p align="center"><small><i>Tabell 9.1 Refittede parametere for SARIMA$(0,1,1)(0,1,1)_{12}$ estimert på hele datasettet (1964-01 til 1981-06).</i></small></p>

De refittede verdiene er svært nær treningsestimatene ($\theta_1 = -0.82$ mot $-0.82$, $\Theta_1 = -0.62$ mot $-0.60$), og konfidensintervallene overlapper fullstendig. Den estimerte feilvariansen er noe lavere ($\hat{\sigma}^2 = 0.012$ mot $0.015$), noe som er forventet når modellen har mer data til rådighet. Stabiliteten i parameterne styrker tilliten til at modellstrukturen er robust og ikke er et resultat av overtilpasning til treningsdataene.

### 9.2 Residualdiagnostikk og modellforutsetninger

Residualdiagnostikken i kapittel 7.4 avdekket en spenning mellom modellens praktiske ytelse og de formelle kravene til residualenes egenskaper. Ved korte lag viser residualene ingen signifikant autokorrelasjon (Ljung-Box lag 1: $p = 0.46$), noe som innebærer at modellen fanger de kortsiktige dynamikkene i serien godt. Ved sesongmessige lag er bildet annerledes: Ljung-Box-testene ved lag 12 ($p < 0.001$) og lag 24 ($p = 0.031$) forkaster nullhypotesen om hvitt støy. Modellen etterlater dermed noe sesongmessig struktur i residualene som den ikke fanger opp.

I praktisk forstand betyr dette at det finnes systematiske sesongavvik modellen ikke forklarer fullt ut. En mulig forklaring er at den faste tolv-måneders sesongperioden ikke fanger alle nyanser i salgets sesongvariasjon — for eksempel at høysesongens relative intensitet kan variere noe mellom år. En mer kompleks modell, for eksempel med ekstra sesongmessige autoregressive ledd, kunne potensielt redusert denne gjenværende strukturen, men som Tabell 7.2 viste, ga slike utvidelser bare marginale forbedringer i informasjonskriteriene.

ARCH-LM-testen ($p < 0.001$) dokumenterer at residualvariansen ikke er konstant over tid. Heteroskedastisiteten har en praktisk konsekvens: prediksjonsintervallene, som er beregnet under en antakelse om konstant varians, kan være for smale i perioder med høy volatilitet og for brede i roligere perioder. Siden de største sesongutslagene og de høyeste salgsnivåene samvarierer, er det spesielt i høysesongmånedene at prediksjonsintervallene kan undervurdere den reelle usikkerheten. Figur 4.4 i casebeskrivelsen viste at spredningen mellom år øker markant i høstmånedene, noe som er konsistent med dette funnet.

Avviket fra normalfordeling (Jarque-Bera $p < 0.01$, kurtose $= 7.95$) innebærer at residualene har tyngre haler enn normalfordelingen tilsier. For prognoseformål betyr dette at sjeldne, store avvik er noe mer sannsynlige enn modellen formelt antar. Log-transformasjonen har allerede redusert dette problemet sammenlignet med å modellere på originalskala, men fjerner det ikke fullstendig.

Samlet sett bryter modellen med flere formelle forutsetninger. Slike brudd er godt dokumentert for airline-modellen brukt på reelle økonomiske tidsserier (Box et al., 2015; Hyndman & Athanasopoulos, 2021, kap. 9), og de diskvalifiserer ikke modellen for praktisk bruk. Testsettvalideringen i kapittel 8.1 gir et empirisk supplement til de formelle testene og viser hvordan modellen faktisk presterer på data den ikke er estimert på.

### 9.3 Prognoseevne og bias i testsettvalideringen

Testsettvalideringen viste at modellen oppnådde en gjennomsnittlig absolutt prosentfeil (MAPE) på 5.39 % over 42 måneder. For månedlig etterspørselsprognose er dette et godt resultat som tilsier at modellen i snitt treffer innenfor et relativt smalt feilbånd. Modellen fanger formen og timingen i sesongmønsteret godt, noe som bekrefter at den sesongmessige strukturen i dataene er stabil nok til å gi brukbare prognoser.

Likevel har resultatene en systematisk svakhet. I 41 av 42 testmåneder ligger prognosen over faktisk salg, og gjennomsnittlig absolutt prosentfeil øker fra 4.6 % i 1978 til 7.5 % i første halvår 1981. Denne utviklingen tyder på at modellens implisitte trendekstrapolering — som følger av ordinær differensiering med $d = 1$ — overskreddere den faktiske veksten i testperioden. Modellen forutsetter i praksis at vekstraten fra treningsperioden videreføres, men testperioden viser at veksten flater ut eller avtar. Avviket er størst i desember 1979 (+1 227 enheter), som også er den måneden med høyest absolutt salgsnivå. At de største absolutte feilene oppstår i høysesongen er konsistent med heteroskedastisitetsfunnet fra kapittel 7.4 og bekrefter at modellens feilstruktur er nivåavhengig.

Den økende feilen over prognoshorisonten er en viktig innsikt for bruken av modellen. Den innebærer at modellen er mest pålitelig på kort sikt og at prognosekvaliteten gradvis forringes når horisonten strekkes ut over flere år. For en 12-måneders prognose fra et enkelt opprinnelsespunkt, slik som i denne rapporten, betyr det at de første månedene er mer pålitelige enn de siste.

Et metodisk poeng knyttet til tilbaketransformeringen fortjener omtale. Punktprognosen bruker $\exp(\hat{z})$, som gir medianverdien på originalskala. Strengt tatt er den forventningsrette tilbaketransformeringen $\exp(\hat{z}_{t+h} + \hat{\sigma}_h^2/2)$, der $\hat{\sigma}_h^2$ er den horisontspesifikke prognosevariansen (Hyndman & Athanasopoulos, 2021, seksjon 3.1). For denne modellen er korreksjonsfaktoren liten — fra om lag 0.6 % ved horisont 1 til om lag 0.8 % ved horisont 12 — fordi feilvariansen på log-skala er beskjeden. Korreksjonsfaktoren øker med horisonten fordi prognosevariansen akkumuleres, men selv ved 12 steg er oppjusteringen marginal. Siden modellen allerede viser en systematisk positiv bias i testsettvalideringen, ville en biaskorreksjon forsterke denne tendensen ytterligere. Bruken av medianprognosen kan dermed forsvares som en pragmatisk tilnærming der den statistisk sett konservative tilbaketransformeringen delvis motvirker modellens strukturelle overprognose.

### 9.4 Prognosen og implikasjoner for kapasitetsplanlegging

Det tredje delspørsmålet i problemstillingen handler om hvilke implikasjoner prognosen har for PowerHorses produksjons- og lagerplanlegging. Den 12-måneders prognosen i Tabell 8.2 gir et samlet prognosesalg på 100 413 enheter med en sesongamplitude på 16 789 enheter — fra 2 694 i bunnmåneden august til 19 483 i toppmåneden desember. Forholdet mellom topp og bunn er om lag 7:1, noe som innebærer at bedriften står overfor store variasjoner i kapasitetsbehov gjennom året. Gjennomsnittlig bredde på 95 % prediksjonsintervall er om lag 3 844 enheter, noe som gir en indikasjon på usikkerheten beslutningstakeren må håndtere.

Tabell 9.2 utvider prognosetallene fra Tabell 8.2 med en sesongkategorisering basert på de historiske månedlige salgsnivåene.

| Måned | Sesongkategori | Punktprognose |
| :--- | :--- | ---: |
| 1981-07 | Normalsesong | 6 159 |
| 1981-08 | Lavsesong | 2 694 |
| 1981-09 | Normalsesong | 7 991 |
| 1981-10 | Høysesong | 9 918 |
| 1981-11 | Høysesong | 15 188 |
| 1981-12 | Høysesong | 19 483 |
| 1982-01 | Lavsesong | 6 308 |
| 1982-02 | Lavsesong | 5 293 |
| 1982-03 | Normalsesong | 6 584 |
| 1982-04 | Normalsesong | 6 578 |
| 1982-05 | Normalsesong | 7 201 |
| 1982-06 | Normalsesong | 7 016 |

<p align="center"><small><i>Tabell 9.2 Sesongkategorisering av prognosemånedene. Fullstendige prediksjonsintervaller finnes i Tabell 8.2.</i></small></p>

For produksjonsplanlegging innebærer sesongprofilen at kapasitetsbehovet i høysesongen (oktober–desember) er vesentlig høyere enn i resten av året. Dersom produksjonskapasiteten ikke kan skaleres tilsvarende på kort varsel, må bedriften bygge opp lager i forkant av høysesongen. Konkret tilsier prognosen at lageroppbyggingen bør starte senest i august–september, som er månedene med lavest etterspørsel (2 694–7 991 enheter). Målet bør være å dekke gapet mellom normal produksjonskapasitet og toppetterspørselen i november–desember, der punktprognosen indikerer et samlet behov på om lag 34 700 enheter over to måneder. Lavsesongen (august, januar og februar) gir mulighet for en slik oppbygging, forutsatt at lagerkostnadene veies opp mot risikoen for underdekning.

Prediksjonsintervallene gir bedriften et kvantitativt grunnlag for å dimensjonere sikkerhetslager. Intervallene bredder utover horisonten, noe som reflekterer at usikkerheten øker med antall steg fremover. For de første prognosemånedene er intervallene relativt smale, mens de siste månedene har bredere intervaller. I en planleggingssammenheng kan dette bety at produksjonsbeslutninger for nær horisont kan baseres tettere på punktprognosen, mens beslutninger for fjernere horisont bør ta hensyn til et bredere utfallsrom.

Den positive biasen som ble identifisert i testsettvalideringen tilsier at prognosetallene kan overestimere faktisk etterspørsel noe. For lagerstyring innebærer dette at bedriften bør være oppmerksom på risikoen for å produsere mer enn det som faktisk selges, med tilhørende kapitalbinding. En konservativ tilnærming kan være å bruke den nedre delen av prediksjonsintervallet som utgangspunkt for faste produksjonsforpliktelser, og punktprognosen som planleggingsmål for total kapasitet.

Det er viktig å understreke at modellen gir et utgangspunkt, ikke et ferdig svar. Sesongprofilen er modellens sterkeste bidrag — den viser når etterspørselen er høy og lav, og denne informasjonen er verdifull selv om det absolutte nivået kan være noe overestimert. I praksis bør bedriften supplere modellprognosen med markedsinnsikt, informasjon fra ordrepipeline og faglig skjønn for å korrigere nivået og fange opp endringer som modellen ikke kan forutse.

### 9.5 Begrensninger

Analysen har flere begrensninger som påvirker hvor langt konklusjonene kan strekkes.

For det første er modellen univariat. Den bruker kun historiske salgstall og har ingen informasjon om drivere som pris, markedsføring, konkurransesituasjon eller makroøkonomiske forhold. Dersom noen av disse faktorene endrer seg vesentlig, vil modellen ikke fange det opp. En multivariat tilnærming med eksterne forklaringsvariabler kunne potensielt gitt bedre prognoser, men var utenfor prosjektets omfang på grunn av manglende datatilgang.

For det andre dekker datagrunnlaget perioden 1964 til 1981. Modellen bygger på at de historiske mønstrene er tilstrekkelig representative for framtidig utvikling. Dersom markedet har gjennomgått strukturelle endringer etter dataperiodens slutt, kan modellens antakelser være svekket. Innenfor prosjektets rammer er dette en nødvendig antagelse, men den begrenser generaliserbarheten.

For det tredje impliserer den ordinære differensieringen ($d = 1$) en multiplikativ trendekstrapolering som gradvis kan divergere fra virkeligheten. Testsettvalideringen dokumenterte nettopp dette: den positive biasen øker over horisonten, noe som tyder på at trenden i treningsperioden var sterkere enn i testperioden. For prognoser over lengre horisont enn 12 måneder er denne svakheten spesielt relevant.

For det fjerde begrenser de dokumenterte bruddene i residualdiagnostikken — heteroskedastisitet og gjenværende sesongrelatert autokorrelasjon — den formelle tilliten til prediksjonsintervallene. Intervallene kan være for smale i høysesongmånedene og for brede i lavsesongen, noe som betyr at usikkerhetsestimater bør tolkes med forsiktighet.

For det femte ble det kun evaluert modeller innenfor SARIMA-familien. Ingen sammenligning med eksponentiell utjevning (ETS; Hyndman & Athanasopoulos, 2021, kap. 8), dynamisk harmonisk regresjon eller GARCH-utvidelser for variansmodellering (Engle, 1982) ble gjennomført. Det er mulig at andre modellfamilier kunne adressert noen av svakhetene, særlig heteroskedastisiteten.

Til slutt er prognosen en statisk 12-stegs prognose fra ett enkelt opprinnelsespunkt. I praksis ville PowerHorse ha nytte av å reestimere modellen etter hvert som nye salgsdata kommer inn, slik at prognosen løpende oppdateres. En rullerende reestimeringsstrategi ble ikke testet i dette prosjektet, men ville sannsynligvis redusert den økende biasen som ble observert i testsettvalideringen.

Figuren i innledningen av dette kapitlet (Figur 9.1) setter prognosen i perspektiv ved å vise at den bygger på en serie med klar oppadgående trend og tiltagende sesongutslag. Den gjør det visuelt tydelig at prognosen er en kort videreføring av en lang historikk, og at trendens videre utvikling er usikker.

### 9.6 Samlet vurdering opp mot problemstillingen

Problemstillingen i kapittel 1.1 stilte ett sammensatt spørsmål som i kapittel 1.2 ble brutt ned i tre delproblemer: (1) hvilke mønstre i trend og sesong som finnes i de historiske salgsdataene, (2) hvilken SARIMA-spesifikasjon som gir best tilpasning og hvordan modellen presterer på data den ikke er estimert på, og (3) hvilke implikasjoner prognosen har for PowerHorse sin produksjons- og lagerplanlegging.

Til det første delspørsmålet viser casebeskrivelsen og datautforskingen i kapittel 4–5 at serien har en tydelig oppadgående trend og et stabilt sesongmønster med topp i november–desember og bunn i august. Log-transformasjonen stabiliserer variansen og gjør sesongutslagene tilnærmet additive, noe som legger grunnlaget for SARIMA-modelleringen.

Til det andre delspørsmålet viser analysen at SARIMA$(0,1,1)(0,1,1)_{12}$ er en velegnet modell for å fange sesongprofilen i det historiske salget. Modellen oppnår en gjennomsnittlig absolutt prosentfeil på 5.4 % i testsettvalideringen, noe som tilsier at den treffer rimelig godt på månedsnivå. Den 12-måneders prognosen reproduserer det historiske sesongmønsteret og gir kvantitative prediksjonsintervaller som uttrykker usikkerhet for hvert prognosesteg.

Til det tredje delspørsmålet viser seksjon 9.4 at prognosen har direkte implikasjoner for kapasitetsplanlegging. Sesongprofilen identifiserer variasjoner med et forhold på 7:1 mellom topp og bunn, noe som er verdifull informasjon for å planlegge produksjonskapasitet og lageroppbygging gjennom året. Samtidig begrenser den systematiske positive biasen, den økende feilen over horisonten, de diagnostiske svakhetene og den univariate tilnærmingen modellens egnethet som eneste beslutningsgrunnlag.

Modellen bør derfor brukes som ett element i et bredere beslutningsgrunnlag. Sesongprofilen og prediksjonsintervallene gir et kvantitativt rammeverk, men de absolutte nivåene bør suppleres med markedsinnsikt, ordredata og faglig skjønn. I tillegg bør modellen reestimeres periodisk etter hvert som nye salgsdata blir tilgjengelige, slik at prognosen holder seg oppdatert og den økende biasen over tid reduseres.

---

## 10 Konklusjon

Rapporten har vist at en univariat SARIMA-modell kan brukes til å predikere månedlig traktorsalg hos PowerHorse for de neste tolv månedene, og at modellen gir et nyttig — men ikke uttømmende — beslutningsgrunnlag for produksjons- og lagerplanlegging.

Den valgte SARIMA$(0,1,1)(0,1,1)_{12}$-modellen ble estimert på treningsperioden januar 1964 til desember 1977 og evaluert på testsettet januar 1978 til juni 1981, der den oppnådde en gjennomsnittlig absolutt prosentfeil på 5,4 %. Salgsserien har en tydelig oppadgående trend og en stabil tolv-måneders sesongprofil med topp i november–desember og bunn i august, og modellen fanger denne strukturen godt. Med bare tre parametere er den den enkleste blant alle 36 evaluerte kandidater, men oppnår likevel lavest AIC og BIC — et tydelig parsimonisignal.

For PowerHorses planleggingsbehov gir den 12-måneders prognosen for juli 1981 til juni 1982 et kvantitativt utgangspunkt på om lag 100 400 enheter samlet, med en sesongamplitude på 7:1 mellom topp- og bunnmåneden. Dette gir en konkret operasjonell handlingsfølge: lageroppbygging bør starte i august–september, høysesongkapasiteten må dimensjoneres for et samlet behov på om lag 34 700 enheter i november–desember (med toppmåneden desember på 19 500 enheter), og lavsesongen januar–februar gir rom for å nedjustere produksjonsvolumet. Prediksjonsintervallene gjør usikkerheten kvantitativt synlig og gir grunnlag for å dimensjonere sikkerhetslager, og periodisk reestimering — for eksempel etter hvert kvartal — anbefales for å holde prognosen oppdatert og motvirke bias-akkumulering over tid.

Modellen har samtidig klare begrensninger. Testsettvalideringen avdekket en systematisk positiv bias som tiltar over horisonten, og residualdiagnostikken viser brudd på modellforutsetningene ved sesonglag og gjennom heteroskedastisitet. Den univariate tilnærmingen utelukker eksterne drivere som pris, markedsføring og makroøkonomi. Sesongstrukturen treffer derfor bedre enn nivået, og modellen leverer mest verdi som beslutningsstøtte sammen med markedsinnsikt og operative ordredata, ikke alene.

Det viktigste praktiske bidraget er dermed et reproduserbart, statistisk forankret rammeverk for sesongbasert kapasitetsplanlegging hos PowerHorse. Rammeverket gjør usikkerhet kvantitativt synlig og gir bedriften en transparent struktur for å forene tallbaserte prognoser med kvalitativ markedsinnsikt og operativ erfaring i den videre planleggingen.

---

## 11 Bibliografi

Box, G. E. P., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). *Time series analysis: Forecasting and control* (5th ed.). Wiley.

De Gooijer, J. G., & Hyndman, R. J. (2006). 25 years of time series forecasting. *International Journal of Forecasting*, *22*(3), 443–473. https://doi.org/10.1016/j.ijforecast.2006.01.001

Dickey, D. A., & Fuller, W. A. (1979). Distribution of the estimators for autoregressive time series with a unit root. *Journal of the American Statistical Association*, *74*(366), 427–431. https://doi.org/10.2307/2286348

Engle, R. F. (1982). Autoregressive conditional heteroscedasticity with estimates of the variance of United Kingdom inflation. *Econometrica*, *50*(4), 987–1007. https://doi.org/10.2307/1912773

Guimarães, C. B., Marques, J. M., & Tortato, U. (2020). Demand forecasting for high-turnover spare parts in agricultural and construction machines: A case study. *South African Journal of Industrial Engineering*, *31*(2), 116–128. https://doi.org/10.7166/31-2-2084

Hyndman, R. J., & Athanasopoulos, G. (2021). *Forecasting: Principles and practice* (3rd ed.). OTexts. https://otexts.com/fpp3/

Jarque, C. M., & Bera, A. K. (1987). A test for normality of observations and regression residuals. *International Statistical Review*, *55*(2), 163–172. https://doi.org/10.2307/1403192

Kwiatkowski, D., Phillips, P. C. B., Schmidt, P., & Shin, Y. (1992). Testing the null hypothesis of stationarity against the alternative of a unit root. *Journal of Econometrics*, *54*(1–3), 159–178. https://doi.org/10.1016/0304-4076(92)90104-Y

Ljung, G. M., & Box, G. E. P. (1978). On a measure of lack of fit in time series models. *Biometrika*, *65*(2), 297–303. https://doi.org/10.1093/biomet/65.2.297

Makoni, T., & Chikobvu, D. (2023). Assessing and forecasting the long-term impact of the global financial crisis on new car sales in South Africa. *Data*, *8*(5), 78. https://doi.org/10.3390/data8050078

Makridakis, S., Spiliotis, E., & Assimakopoulos, V. (2020). The M4 Competition: 100,000 time series and 61 forecasting methods. *International Journal of Forecasting*, *36*(1), 54–74. https://doi.org/10.1016/j.ijforecast.2019.04.014

Petropoulos, F., Apiletti, D., Assimakopoulos, V., Babai, M. Z., Barrow, D. K., Ben Taieb, S., Bergmeir, C., Bessa, R. J., Bijak, J., Boylan, J. E., Browell, J., Carnevale, C., Castle, J. L., Cirillo, P., Clements, M. P., Cordeiro, C., Cyrino Oliveira, F. L., De Baets, S., Dokumentov, A., ... Ziel, F. (2022). Forecasting: Theory and practice. *International Journal of Forecasting*, *38*(3), 705–871. https://doi.org/10.1016/j.ijforecast.2021.11.001

Polina, P., Ganesan, S., Karunarathne, L., & Somasiri, N. (2024). Time series analysis for tractor sales using SARIMAX and deep learning models. *International Journal of Computer Communication and Informatics*, *6*(1), 27–57. https://doi.org/10.34256/ijcci2413

Shumway, R. H., & Stoffer, D. S. (2017). *Time series analysis and its applications: With R examples* (4th ed.). Springer.

Silver, E. A., Pyke, D. F., & Thomas, D. J. (2017). *Inventory and production management in supply chains* (4th ed.). CRC Press.

---

## 12 Vedlegg

Vedleggene gir utfyllende dokumentasjon som supplerer hovedteksten. Vedlegg A viser den fullstendige modellutvelgelsen som ligger til grunn for valget i kapittel 7.2. Vedlegg B viser den månedlige testsettprognosen som oppsummeres i kapittel 8.1. Vedlegg C peker til de tilhørende analyseartefaktene for reproduserbarhet.

### Vedlegg A — Fullstendig oversikt over evaluerte SARIMA-kandidater

Tabell A.1 viser alle 36 SARIMA-spesifikasjoner som ble estimert og rangert i kapittel 7.2. Modellene er sortert stigende etter AIC, og den valgte modellen står øverst. Alle modeller konvergerte ved estimering.

| Modell | $p$ | $q$ | $P$ | $Q$ | Parametere | Log-lik | AIC | BIC |
|:--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| SARIMA(0,1,1)(0,1,1)$_{12}$ | 0 | 1 | 0 | 1 | 3 | 104,41 | -202,83 | -193,70 |
| SARIMA(1,1,1)(0,1,1)$_{12}$ | 1 | 1 | 0 | 1 | 4 | 104,88 | -201,76 | -189,59 |
| SARIMA(0,1,1)(1,1,1)$_{12}$ | 0 | 1 | 1 | 1 | 4 | 104,87 | -201,75 | -189,57 |
| SARIMA(0,1,2)(0,1,1)$_{12}$ | 0 | 2 | 0 | 1 | 4 | 104,81 | -201,61 | -189,44 |
| SARIMA(1,1,2)(0,1,1)$_{12}$ | 1 | 2 | 0 | 1 | 5 | 105,68 | -201,37 | -186,15 |
| SARIMA(2,1,1)(0,1,1)$_{12}$ | 2 | 1 | 0 | 1 | 5 | 105,33 | -200,66 | -185,45 |
| SARIMA(1,1,1)(1,1,1)$_{12}$ | 1 | 1 | 1 | 1 | 5 | 105,22 | -200,44 | -185,23 |
| SARIMA(0,1,2)(1,1,1)$_{12}$ | 0 | 2 | 1 | 1 | 5 | 105,16 | -200,32 | -185,10 |
| SARIMA(2,1,1)(1,1,1)$_{12}$ | 2 | 1 | 1 | 1 | 6 | 105,76 | -199,53 | -181,27 |
| SARIMA(1,1,2)(1,1,1)$_{12}$ | 1 | 2 | 1 | 1 | 6 | 105,01 | -198,03 | -179,77 |
| SARIMA(2,1,2)(0,1,1)$_{12}$ | 2 | 2 | 0 | 1 | 6 | 104,98 | -197,96 | -179,70 |
| SARIMA(2,1,2)(1,1,1)$_{12}$ | 2 | 2 | 1 | 1 | 7 | 105,31 | -196,62 | -175,31 |
| SARIMA(1,1,2)(1,1,0)$_{12}$ | 1 | 2 | 1 | 0 | 5 | 102,01 | -194,02 | -178,80 |
| SARIMA(1,1,1)(1,1,0)$_{12}$ | 1 | 1 | 1 | 0 | 4 | 100,52 | -193,05 | -180,87 |
| SARIMA(0,1,1)(1,1,0)$_{12}$ | 0 | 1 | 1 | 0 | 3 | 99,41 | -192,82 | -183,69 |
| SARIMA(0,1,2)(1,1,0)$_{12}$ | 0 | 2 | 1 | 0 | 4 | 100,34 | -192,68 | -180,51 |
| SARIMA(2,1,1)(1,1,0)$_{12}$ | 2 | 1 | 1 | 0 | 5 | 101,00 | -192,00 | -176,79 |
| SARIMA(2,1,2)(1,1,0)$_{12}$ | 2 | 2 | 1 | 0 | 6 | 100,87 | -189,74 | -171,47 |
| SARIMA(2,1,0)(0,1,1)$_{12}$ | 2 | 0 | 0 | 1 | 4 | 97,70 | -187,40 | -175,23 |
| SARIMA(2,1,0)(1,1,1)$_{12}$ | 2 | 0 | 1 | 1 | 5 | 98,39 | -186,79 | -171,57 |
| SARIMA(2,1,0)(1,1,0)$_{12}$ | 2 | 0 | 1 | 0 | 4 | 93,04 | -178,07 | -165,90 |
| SARIMA(1,1,2)(0,1,0)$_{12}$ | 1 | 2 | 0 | 0 | 4 | 91,05 | -174,10 | -161,93 |
| SARIMA(1,1,0)(0,1,1)$_{12}$ | 1 | 0 | 0 | 1 | 3 | 89,42 | -172,84 | -163,71 |
| SARIMA(2,1,2)(0,1,0)$_{12}$ | 2 | 2 | 0 | 0 | 5 | 91,20 | -172,39 | -157,18 |
| SARIMA(1,1,0)(1,1,1)$_{12}$ | 1 | 0 | 1 | 1 | 4 | 89,81 | -171,63 | -159,46 |
| SARIMA(2,1,1)(0,1,0)$_{12}$ | 2 | 1 | 0 | 0 | 4 | 89,65 | -171,31 | -159,13 |
| SARIMA(0,1,1)(0,1,0)$_{12}$ | 0 | 1 | 0 | 0 | 2 | 86,89 | -169,77 | -163,69 |
| SARIMA(1,1,1)(0,1,0)$_{12}$ | 1 | 1 | 0 | 0 | 3 | 87,88 | -169,75 | -160,62 |
| SARIMA(0,1,2)(0,1,0)$_{12}$ | 0 | 2 | 0 | 0 | 3 | 87,17 | -168,33 | -159,20 |
| SARIMA(1,1,0)(1,1,0)$_{12}$ | 1 | 0 | 1 | 0 | 3 | 85,19 | -164,37 | -155,24 |
| SARIMA(2,1,0)(0,1,0)$_{12}$ | 2 | 0 | 0 | 0 | 3 | 82,56 | -159,11 | -149,98 |
| SARIMA(1,1,0)(0,1,0)$_{12}$ | 1 | 0 | 0 | 0 | 2 | 72,87 | -141,73 | -135,64 |
| SARIMA(0,1,0)(0,1,1)$_{12}$ | 0 | 0 | 0 | 1 | 2 | 69,59 | -135,18 | -129,09 |
| SARIMA(0,1,0)(1,1,1)$_{12}$ | 0 | 0 | 1 | 1 | 3 | 69,59 | -133,18 | -124,05 |
| SARIMA(0,1,0)(1,1,0)$_{12}$ | 0 | 0 | 1 | 0 | 2 | 67,81 | -131,62 | -125,53 |
| SARIMA(0,1,0)(0,1,0)$_{12}$ | 0 | 0 | 0 | 0 | 1 | 53,53 | -105,07 | -102,02 |

<p align="center"><small><i>Tabell A.1 Fullstendig kandidatoversikt over 36 evaluerte SARIMA-spesifikasjoner sortert stigende etter AIC.</i></small></p>

### Vedlegg B — Månedlig testsettprognose

Tabell B.1 viser observert salg, prognosert salg, prognosefeil, absolutt feil og absolutt prosentfeil for hver av de 42 månedene i testsettet (januar 1978 til juni 1981). Aggregerte feilmål er rapportert i Tabell 8.1.

| Måned | Observert | Prognose | Feil | Absolutt feil | Absolutt prosentfeil |
|:--- | ---: | ---: | ---: | ---: | ---: |
| 1978-01 | 5 649 | 5 586,58 | -62,42 | 62,42 | 1,10 % |
| 1978-02 | 4 713 | 4 716,58 | 3,58 | 3,58 | 0,08 % |
| 1978-03 | 5 816 | 5 901,35 | 85,35 | 85,35 | 1,47 % |
| 1978-04 | 5 764 | 5 951,17 | 187,17 | 187,17 | 3,25 % |
| 1978-05 | 6 275 | 6 510,38 | 235,38 | 235,38 | 3,75 % |
| 1978-06 | 6 066 | 6 427,96 | 361,96 | 361,96 | 5,97 % |
| 1978-07 | 5 408 | 5 761,69 | 353,69 | 353,69 | 6,54 % |
| 1978-08 | 2 353 | 2 500,37 | 147,37 | 147,37 | 6,26 % |
| 1978-09 | 6 964 | 7 482,16 | 518,16 | 518,16 | 7,44 % |
| 1978-10 | 8 655 | 9 283,11 | 628,11 | 628,11 | 7,26 % |
| 1978-11 | 13 337 | 14 193,90 | 856,90 | 856,90 | 6,42 % |
| 1978-12 | 17 235 | 18 202,07 | 967,07 | 967,07 | 5,61 % |
| 1979-01 | 5 627 | 5 859,24 | 232,24 | 232,24 | 4,13 % |
| 1979-02 | 4 758 | 4 946,78 | 188,78 | 188,78 | 3,97 % |
| 1979-03 | 5 973 | 6 189,38 | 216,38 | 216,38 | 3,62 % |
| 1979-04 | 6 011 | 6 241,62 | 230,62 | 230,62 | 3,84 % |
| 1979-05 | 6 623 | 6 828,13 | 205,13 | 205,13 | 3,10 % |
| 1979-06 | 6 469 | 6 741,68 | 272,68 | 272,68 | 4,22 % |
| 1979-07 | 5 786 | 6 042,90 | 256,90 | 256,90 | 4,44 % |
| 1979-08 | 2 526 | 2 622,40 | 96,40 | 96,40 | 3,82 % |
| 1979-09 | 7 420 | 7 847,33 | 427,33 | 427,33 | 5,76 % |
| 1979-10 | 9 155 | 9 736,18 | 581,18 | 581,18 | 6,35 % |
| 1979-11 | 13 964 | 14 886,65 | 922,65 | 922,65 | 6,61 % |
| 1979-12 | 17 863 | 19 090,44 | 1 227,44 | 1 227,44 | 6,87 % |
| 1980-01 | 5 778 | 6 145,21 | 367,21 | 367,21 | 6,36 % |
| 1980-02 | 4 846 | 5 188,21 | 342,21 | 342,21 | 7,06 % |
| 1980-03 | 6 061 | 6 491,46 | 430,46 | 430,46 | 7,10 % |
| 1980-04 | 6 092 | 6 546,25 | 454,25 | 454,25 | 7,46 % |
| 1980-05 | 6 738 | 7 161,38 | 423,38 | 423,38 | 6,28 % |
| 1980-06 | 6 622 | 7 070,72 | 448,72 | 448,72 | 6,78 % |
| 1980-07 | 5 979 | 6 337,83 | 358,83 | 358,83 | 6,00 % |
| 1980-08 | 2 640 | 2 750,39 | 110,39 | 110,39 | 4,18 % |
| 1980-09 | 7 831 | 8 230,33 | 399,33 | 399,33 | 5,10 % |
| 1980-10 | 9 752 | 10 211,37 | 459,37 | 459,37 | 4,71 % |
| 1980-11 | 14 954 | 15 613,21 | 659,21 | 659,21 | 4,41 % |
| 1980-12 | 19 164 | 20 022,18 | 858,18 | 858,18 | 4,48 % |
| 1981-01 | 6 195 | 6 445,13 | 250,13 | 250,13 | 4,04 % |
| 1981-02 | 5 176 | 5 441,43 | 265,43 | 265,43 | 5,13 % |
| 1981-03 | 6 392 | 6 808,28 | 416,28 | 416,28 | 6,51 % |
| 1981-04 | 6 334 | 6 865,75 | 531,75 | 531,75 | 8,40 % |
| 1981-05 | 6 887 | 7 510,90 | 623,90 | 623,90 | 9,06 % |
| 1981-06 | 6 642 | 7 415,81 | 773,81 | 773,81 | 11,65 % |

<p align="center"><small><i>Tabell B.1 Måned-for-måned testsettprognose for SARIMA$(0,1,1)(0,1,1)_{12}$ med observert salg, prognose, prognosefeil og prosentfeil for testperioden januar 1978 til juni 1981.</i></small></p>

### Vedlegg C — Reproduserbarhet og analyseartefakter

All analysekode, datafiler, figurer og resultatfiler ligger samlet i prosjektmappen `006 analysis/aktiviteter/`, organisert etter aktivitetene i prosjektplanen. Tabell C.1 oppsummerer hvor de viktigste artefaktene finnes.

| Aktivitet | Mappe | Innhold |
|:--- | :--- | :--- |
| Datarensing og strukturering | `3_1_rense_og_strukturere_data/` | Datasplitt, månedsprofil, dataoversikt |
| Modellutvelgelse og estimering | `3_2_velge_og_estimere_modell/` | Stasjonaritetstester, kandidatoversikt, parameterestimat, residualdiagnostikk |
| Validering | `3_3_validere_modell/` | Supplerende residualtester, testsettprognose, feilmål |
| 12-måneders prognose og kapasitetsplanlegging | `3_4_lage_prognose_og_anbefalinger/` | Refittede parametere, månedlig prognose, kapasitetstabell, helhetsfigur |
| Teorikapittelets illustrasjoner | `3_7_skrive_teorikapittel/` | Syntetiske figurer for dekomponering, stasjonaritet, ACF/PACF og biaskorreksjon |

<p align="center"><small><i>Tabell C.1 Oversikt over analyseartefakter knyttet til hver aktivitet i fase 3.</i></small></p>

Hver aktivitetsmappe inneholder undermappene `scripts/`, `figurer/` og `resultat/` der det er relevant. Råtidsserien som ligger til grunn for analysen finnes i `004 data/` (`sales.csv` med tilhørende treningssett `sales_train.csv` og testsett `sales_test.csv`).
