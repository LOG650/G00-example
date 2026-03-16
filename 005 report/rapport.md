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

| Måltall                  | Verdi                                    |
| :------------------------ | :--------------------------------------- |
| Startdato                 | 1964-01                                  |
| Sluttdato                 | 1981-06                                  |
| Antall observasjoner      | 210                                      |
| Antall manglende måneder | 0                                        |
| Min salg                  | 1413                                     |
| Maks salg                 | 19164                                    |
| Gjennomsnittlig salg      | 5958.3                                   |
| Median salg               | 5162.5                                   |
| Standardavvik             | 3450.4                                   |
| Variasjonskoeffisient (CV) | 57.9 %                                  |
| Interkvartilbredde (IQR)  | 2680.75                                  |
| Merknad                   | 1981 er delår og dekker kun januar-juni |

---

## 6 Modellering

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
