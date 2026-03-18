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

---

## Abstract

---

## Innhold

1. [Innledning](#1-innledning)
   1. [Problemstilling](#11-problemstilling)
   2. [Delproblemer (valgfri)](#12-delproblemer-valgfri)
   3. [Avgrensinger](#13-avgrensinger)
   4. [Antagelser](#14-antagelser)
2. [Litteratur](#2-litteratur)
3. [Teori](#3-teori)
4. [Casebeskrivelse](#4-casebeskrivelse)
5. [Metode og data (kan splittes i to)](#5-metode-og-data-kan-splittes-i-to)
   1. [Metode](#51-metode)
   2. [Data](#52-data)
6. [Modellering](#6-modellering)
7. [Analyse](#7-analyse)
8. [Resultat](#8-resultat)
9. [Diskusjon](#9-diskusjon)
10. [Konklusjon](#10-konklusjon)
11. [Bibliografi](#11-bibliografi)
12. [Vedlegg](#12-vedlegg)

---

## 1 Innledning

PowerHorse brukes i denne oppgaven som casebedrift for å undersøke hvordan historiske salgsdata kan gi bedre beslutningsstøtte i produksjons- og lagerplanlegging. Bedriften opererer i et marked der etterspørselen varierer både over tid og mellom måneder, noe som gjør det krevende å planlegge kapasitet og lager på en presis måte. Når prognosene er svake, øker risikoen for både overproduksjon, unødvendig lagerbinding og for lav tilgjengelighet i perioder med høy etterspørsel. Analysen bygger derfor på historiske månedlige salgsdata for å belyse etterspørselsmønstre og danne grunnlag for videre modellering og prognosearbeid.

### 1.1 Problemstilling

### 1.2 Delproblemer

### 1.3 Avgrensinger

### 1.4 Antagelser

---

## 2 Litteratur

---

## 3 Teori

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

## 5 Metode og data (kan splittes i to)

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

---

## 6 Modell

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

| Serievariant | Kandidat | ADF teststat | ADF p-verdi | KPSS teststat | KPSS p-verdi | Kort vurdering |
| :--- | :--- | ---: | ---: | ---: | ---: | :--- |
| Log-transformert serie $z_t = log(y_t)$ | $d=0, D=0$ | -1.8701 | 0.3463 | 1.5675 | 0.0100 | Testene peker samlet mot fortsatt ikke-stasjonaritet. |
| Ordinært differensiert $(1-B)z_t$ | $d=1, D=0$ | -4.6489 | 0.0001 | 0.1412 | 0.1000 | Testene peker mot stasjonaritet, men figurdiagnostikken viser fortsatt tydelig sesongstruktur. |
| Sesongdifferensiert $(1-B^{12})z_t$ | $d=0, D=1$ | -3.6410 | 0.0050 | 0.1775 | 0.1000 | Testene peker mot stasjonaritet og fjerner sesongmønsteret bedre enn ordinær differensiering alene. |
| Kombinert differensiert $(1-B)(1-B^{12})z_t$ | $d=1, D=1$ | -4.6172 | 0.0001 | 0.0961 | 0.1000 | Testene peker mot stasjonaritet og figuren gir den mest balanserte serien samlet sett. |

<p align="center"><small><i>Tabell 7.1 Testresultater for stasjonaritet og differensiering.</i></small></p>

Resultatene viser først og fremst at den log-transformerte serien ikke bør brukes videre uten differensiering. ADF- og KPSS-testene gir deretter støtte til tre alternative kandidater: ordinær differensiering, sesongdifferensiering og kombinert differensiering. Testene alene peker derfor ikke entydig på én vinner, men de utelukker at serien kan modelleres direkte uten videre transformasjon.

Når testresultatene tolkes sammen med figur 7.1, blir det likevel tydelig at ordinær differensiering alene ikke er tilstrekkelig. Varianten med $d=1$ og $D=0$ får gode testresultater, men figuren viser fortsatt en tydelig gjenværende sesongstruktur. Dette tyder på at sesongmessig ikke-stasjonaritet ikke er fjernet godt nok selv om den ordinære trenden er redusert. Sesongdifferensiering alene med $d=0$ og $D=1$ er også en plausibel kandidat, men den kombinerte varianten gir den mest balanserte serien når både trend og sesong vurderes samlet på log-skala.

På dette grunnlaget vurderes derfor kombinert differensiering med $d=1$ og $D=1$ som hovedkandidat videre i modellarbeidet. Denne konklusjonen bygger ikke bare på p-verdiene, men på en samlet faglig vurdering av teststatistikkene, p-verdiene og den visuelle diagnostikken på log-transformert serie. Sesongdifferensiering alene beholdes som et enklere alternativ dersom senere analyse skulle vise at kombinert differensiering er mer omfattende enn nødvendig.

### 7.2 ACF/PACF-analyse og ordensvalg

Med differensieringsordnene $d=1$ og $D=1$ fastlagt gjenstår det å bestemme de autoregressive og glidende gjennomsnittsordnene $p$, $q$, $P$ og $Q$. Til dette brukes autokorrelasjonsfunksjonen (ACF) og den partielle autokorrelasjonsfunksjonen (PACF) beregnet på den differensierte log-serien $w_t = (1-B)(1-B^{12})\log(y_t)$.

<div align="center">
  <img src="../006%20analysis/aktiviteter/3_2_velge_og_estimere_modell/figurer/fig_02_acf_pacf.png" alt="Figur 7.2 ACF og PACF for den differensierte log-serien" width="80%">
  <p align="center"><small><i>Figur 7.2 ACF og PACF for $(1-B)(1-B^{12})\log(y_t)$.</i></small></p>
</div>

Figur 7.2 viser ACF og PACF med 36 lags. I ACF-plottet er det en tydelig negativ spike ved lag 1 og en negativ spike ved sesonglag 12. Etter disse lagene faller ACF raskt innenfor konfidensintervallet. PACF-plottet viser et avtagende mønster ved de første lagene og ved sesonglagene 12 og 24. Denne kombinasjonen — avkuttende ACF ved lag 1 og lag 12 med avtagende PACF — er et klassisk mønster for en modell med glidende gjennomsnittsledd av første orden både på ikke-sesongmessig og sesongmessig nivå. Mønsteret peker dermed mot en SARIMA$(0,1,1)(0,1,1)_{12}$-spesifikasjon.

For å støtte den visuelle tolkningen ble det gjennomført et systematisk kandidatsøk der alle kombinasjoner av $p \in \{0,1,2\}$, $q \in \{0,1,2\}$, $P \in \{0,1\}$ og $Q \in \{0,1\}$ ble tilpasset med faste differensieringsordner $d=1$ og $D=1$. Dette gir 36 kandidater som alle ble estimert på den log-transformerte treningsserien. Tabell 7.2 viser de ti beste kandidatene rangert etter AIC.

| Modell | Parametere | Log-likelihood | AIC | BIC |
| :--- | ---: | ---: | ---: | ---: |
| SARIMA(0,1,1)(0,1,1)₁₂ | 3 | 104.41 | -202.83 | -193.70 |
| SARIMA(1,1,1)(0,1,1)₁₂ | 4 | 104.88 | -201.76 | -189.59 |
| SARIMA(0,1,1)(1,1,1)₁₂ | 4 | 104.87 | -201.75 | -189.57 |
| SARIMA(0,1,2)(0,1,1)₁₂ | 4 | 104.81 | -201.61 | -189.44 |
| SARIMA(1,1,2)(0,1,1)₁₂ | 5 | 105.68 | -201.37 | -186.15 |
| SARIMA(2,1,1)(0,1,1)₁₂ | 5 | 105.33 | -200.66 | -185.45 |
| SARIMA(1,1,1)(1,1,1)₁₂ | 5 | 105.22 | -200.44 | -185.23 |
| SARIMA(0,1,2)(1,1,1)₁₂ | 5 | 105.16 | -200.32 | -185.10 |
| SARIMA(2,1,1)(1,1,1)₁₂ | 6 | 105.76 | -199.53 | -181.27 |
| SARIMA(1,1,2)(1,1,1)₁₂ | 6 | 105.01 | -198.03 | -179.77 |

<p align="center"><small><i>Tabell 7.2 Topp 10 SARIMA-kandidater rangert etter AIC. Alle 36 kandidater konvergerte.</i></small></p>

Resultatene viser at SARIMA$(0,1,1)(0,1,1)_{12}$ har lavest AIC (-202.83) og lavest BIC (-193.70) blant alle kandidatene. De mer komplekse modellene forbedrer log-likelihood bare marginalt, men straffes av det ekstra antallet parametere i begge informasjonskriteriene. Modellen som velges er dermed SARIMA$(0,1,1)(0,1,1)_{12}$ — den såkalte airline-modellen, som er en velkjent og mye brukt spesifikasjon for månedlige tidsserier med trend og sesong. Valget bygger på at modellen har best AIC og BIC, er konsistent med ACF/PACF-tolkningen, og er den enkleste blant toppkandidatene.

### 7.3 Modellestimering og parameterresultater

Den valgte modellen SARIMA$(0,1,1)(0,1,1)_{12}$ estimeres på den log-transformerte treningsserien $z_t = \log(y_t)$ for perioden 1964-01 til 1977-12. Modellen spesifiseres med ordinær differensiering $d=1$, sesongmessig differensiering $D=1$ og sesonglengde $m=12$. Parameterne estimeres med maksimum likelihood.

Tabell 7.3 viser de estimerte parameterne med tilhørende standardfeil, z-verdier og p-verdier.

| Parameter | Koeffisient | Standardfeil | z-verdi | p-verdi | 95 % KI nedre | 95 % KI øvre |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| $\theta_1$ (ma.L1) | -0.8217 | 0.0303 | -27.15 | < 0.001 | -0.881 | -0.762 |
| $\Theta_1$ (ma.S.L12) | -0.5998 | 0.0570 | -10.53 | < 0.001 | -0.711 | -0.488 |
| $\sigma^2$ | 0.0146 | 0.0009 | 16.25 | < 0.001 | 0.013 | 0.016 |

<p align="center"><small><i>Tabell 7.3 Estimerte parametere for SARIMA$(0,1,1)(0,1,1)_{12}$.</i></small></p>

Begge MA-parameterne er sterkt signifikante med p-verdier under 0.001. Den ikke-sesongmessige glidende gjennomsnittsparameteren $\theta_1 = -0.82$ indikerer at modellen bruker en stor andel av forrige måneds prognosefeil til å korrigere neste periodes prognose. Den sesongmessige glidende gjennomsnittsparameteren $\Theta_1 = -0.60$ viser at modellen også korrigerer basert på prognosefeil fra samme måned ett år tilbake. Den estimerte feilvariansen $\sigma^2 = 0.0146$ gjelder på log-skala.

Figur 7.3 viser residualdiagnostikk for den estimerte modellen.

<div align="center">
  <img src="../006%20analysis/aktiviteter/3_2_velge_og_estimere_modell/figurer/fig_03_diagnostikk.png" alt="Figur 7.3 Residualdiagnostikk for SARIMA(0,1,1)(0,1,1)₁₂" width="80%">
  <p align="center"><small><i>Figur 7.3 Residualdiagnostikk for SARIMA$(0,1,1)(0,1,1)_{12}$.</i></small></p>
</div>

Korrelogrammet viser ingen signifikant autokorrelasjon i residualene, og Ljung-Box-testen ved lag 1 gir p-verdi 0.46, noe som ikke gir grunnlag for å forkaste hypotesen om hvitt støy. Histogrammet og Q-Q-plottet viser at residualene har noe avvik fra normalfordeling i halene, med tyngre venstrehale og kurtose på 7.95. Jarque-Bera-testen gir p-verdi under 0.01. Det observeres også heteroskedastisitet, der tidlige residualer har høyere varians enn senere perioder. Disse avvikene er verdt å undersøke nærmere, og tas opp i en egen valideringsaktivitet senere i dette kapittelet. Samlet sett gir estimeringen en modell med signifikante parametere og akseptable korrelasjonsegenskaper i residualene, som kan brukes videre til prognosearbeid.

---

## 8 Resultat

---

## 9 Diskusjon

---

## 10 Konklusjon

---

## 11 Bibliografi

---

## 12 Vedlegg
