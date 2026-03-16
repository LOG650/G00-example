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

De ukjente størrelsene i modellen er dermed modellordnene $p$, $d$, $q$, $P$, $D$ og $Q$, samt parameterne $\phi_i$, $\Phi_j$, $\theta_k$ og $\Theta_\ell$. I senere aktiviteter skal disse størrelsene bestemmes ved hjelp av analyse av tidsseriens egenskaper og estimering på treningsdata. I dette kapittelet er poenget kun å definere modellformen og å vise hvilke matematiske komponenter som inngår i prognosemodellen.

---

## 7 Analyse

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
