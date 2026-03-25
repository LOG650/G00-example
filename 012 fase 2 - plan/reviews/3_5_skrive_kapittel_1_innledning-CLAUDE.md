# Review av aktivitet 3.5 – «Skrive kapittel 1 Innledning»

**Reviewer:** Claude (automatisert review)
**Dato:** 2026-03-25
**Aktivitetsmappe:** `006 analysis/aktiviteter/3_5_skrive_rapportutkast/` (tom for artefakter; ren skriveaktivitet)
**Planreferanse:** Aktivitet ACT-3.5, planlagt 2026-04-10 til 2026-04-13, faktisk ferdig 2026-03-25

---

## Sammendrag

Kapittel 1 er en solid og velstrukturert innledning som dekker alle kravene i rapportmalen: innledende aktualisering, problemstilling, delproblemer, avgrensinger og antagelser. Teksten er faglig presis, godt skrevet på norsk og viser tydelig kobling mellom casebeskrivelse, metodevalg og rapportens oppbygging. Reviewen identifiserer 5 styrker, 2 svakheter og 4 forbedringsforslag.

---

## Styrker

- **S1.** Innledningen aktualiserer temaet godt ved å starte med det generelle problemet (sesongavhengig etterspørsel og planleggingsutfordringer) før caset introduseres. Dette følger CLAUDE.md sin rapportsjekkliste om at innledningen skal aktualisere temaet og forklare relevansen.
- **S2.** Problemstillingen er formulert som et tydelig «hvordan»-spørsmål med to ledd som dekker både prediksjonsevnen og beslutningsverdien. Dette er i tråd med anbefalingen i CLAUDE.md om å bruke «hvordan»-formulering.
- **S3.** Delspørsmålene er logisk strukturert og korresponderer eksplisitt med kapittelstrukturen (4-5, 6-8, 9-10), noe som gir leseren en klar disposisjon for resten av rapporten.
- **S4.** Avgrensingene er faglig begrunnet (datatilgjengelighet, modellvalg, analyseperiode) i stedet for å skylde på tidsmangel, i samsvar med CLAUDE.md sin sjekkliste.
- **S5.** Antagelsene er tydelig formulert med eksplisitte konsekvenser for hvert punkt, og det skilles klart mellom prosjektantagelser og statistiske modellantagelser (med henvisning til kapittel 6.2).

---

## Del 1 – Metodikk (beregninger og kode)

### 1.1 Artefakter og reproduserbarhet

Aktivitetsmappen `006 analysis/aktiviteter/3_5_skrive_rapportutkast/` inneholder tomme undermapper for figurer, resultat og scripts. Dette er forventet ettersom ACT-3.5 er en ren skriveaktivitet uten analysekode eller genererte artefakter. Det er ingen metodiske beregninger å etterprøve.

**Vurdering:** Ikke relevant for denne aktiviteten.

### 1.2 Konsistens med øvrig rapporttekst

Innledningen refererer til SARIMA-modellering, 12-måneders prognose og univariat tilnærming. Disse referansene er konsistente med det som faktisk er gjennomført i kapittel 5-8. Problemstillingen spør om «månedlig traktorsalg for de neste tolv månedene», og kapittel 8.2 leverer nettopp en 12-måneders punktprognose. Delspørsmål 2 spør om «SARIMA-spesifikasjon», og kapittel 6-7 dokumenterer nettopp dette.

**Vurdering:** God konsistens mellom innledning og eksisterende rapportkapitler.

### 1.3 Samsvar med proposal

Proposalen formulerer problemstillingen som: «Prosjektet skal utvikle en kvantitativ modell for å predikere månedlig salg av traktorer for de neste 12 månedene.» Innledningens problemstilling er en omformulering av dette til et spørsmål, med tillegg om beslutningsgrunnlag. Avgrensingene i innledningen (univariat modellering, én produktkategori, prognosefokus) er konsistente med proposalens avgrensninger. Det er god sporbarhet mellom proposal og rapport.

**Vurdering:** Konsistent og viser faglig modning fra proposal til rapport.

### Gjenstående metodiske observasjoner

Ingen metodiske observasjoner for denne skriveaktiviteten.

---

## Del 2 – Språk, innhold og figurer

### 2.1 Rapporttekst – Kapittel 1 Innledning (brødtekst)

Innledningen består av tre avsnitt: aktualisering av temaet, introduksjon av caset, og rapportens oppbygging. Lengden er omtrent 1 side, i tråd med CLAUDE.md sin anbefaling om 1-2 sider.

**Språk:** Godt norsk fagspråk. Setningene er klare og av varierende lengde. Ingen skrivefeil identifisert. Ord som «produksjonsledetid» og «beslutningsstøtte» brukes korrekt.

**Faglig innhold:** Avsnitt 1 aktualiserer temaet generelt. Avsnitt 2 kobler til caset og nevner SARIMA-modell og 12-måneders prognose. Avsnitt 3 beskriver rapportens oppbygging. Innledningen nevner caset kort uten å gå i detalj, slik CLAUDE.md anbefaler. Det siste avsnittet om rapportens oppbygging er nyttig for leseren, men befinner seg i en gråsone mellom innledning og innholdsfortegnelse.

### 2.2 Rapporttekst – Seksjon 1.1 Problemstilling

**Språk:** Klar formulering. Problemstillingen er én lang setning med to ledd koblet med «og i hvilken grad», noe som gir en naturlig todeling.

**Faglig innhold:** Problemstillingen dekker både prediksjon og beslutningsstøtte. Utdypningsteksten gir kontekst og henviser til kapittel 4. Det er presist nok til at rapporten verken svarer på mer eller mindre enn det som spørres om.

### 2.3 Rapporttekst – Seksjon 1.2 Delproblemer

**Språk:** Ryddig med tydelig nummerering. Koblingssetningen til kapitler er informativ.

**Faglig innhold:** De tre delspørsmålene dekker analyse, modellering og praktiske implikasjoner. Delspørsmål 2 spør «hvilken SARIMA-spesifikasjon gir best tilpasning», noe som forutsetter at SARIMA allerede er valgt. Det kan argumenteres for at modellvalget burde ha vært et åpent spørsmål i delproblematiseringen (f.eks. «hvilken modellspesifikasjon»), men ettersom proposalen allerede har forankret SARIMA-valget og kapittel 6.1 begrunner modelltypen, er dette akseptabelt.

### 2.4 Rapporttekst – Seksjon 1.3 Avgrensinger

**Språk:** Godt strukturert med nummererte punkter og uthevede overskrifter for hvert punkt.

**Faglig innhold:** Fire avgrensinger dekker datatilgjengelighet, oppløsning, analyseomfang og tidsperiode. Alle er faglig begrunnet. Punkt 4 («Historisk analyseperiode 1964-1981») sier at «analysens gyldighet forutsetter at de identifiserte mønstrene er relevante for prognoseperioden». Dette overlapper delvis med antagelse 2 i seksjon 1.4 om «relevans av historiske mønstre». Overlappet er ikke alvorlig, men kan skape en uklar grensegang mellom hva som er en avgrensing og hva som er en antagelse.

### 2.5 Rapporttekst – Seksjon 1.4 Antagelser

**Språk:** Klart formulert med uthevede overskrifter og eksplisitte konsekvenser per antagelse.

**Faglig innhold:** Tre antagelser dekker datakvalitet, stabilitet og mønsterbasert tilnærming. Henvisningen til kapittel 6.2 for modellantagelser er et godt grep. Antagelse 3 om «mønsterbasert tilnærming» ligger tett opp mot en avgrensing (at analysen er univariat), og grensen mellom antagelse og avgrensing er noe uklar. Dette er imidlertid en vanlig utfordring i akademiske rapporter og ikke en alvorlig svakhet.

### 2.6 Figurer – rapportklarhet

Kapittel 1 inneholder ingen figurer. Dette er forventet.

### 2.7 Tabeller – konsistens og lesbarhet

Kapittel 1 inneholder ingen tabeller. Dette er forventet.

### 2.8 Innholdsfortegnelse – konsistens

Innholdsfortegnelsen er oppdatert med riktige underseksjoner for kapittel 1 (1.1-1.4). Referanselinken for delproblemer er oppdatert fra «Delproblemer (valgfri)» til «Delproblemer», noe som er riktig.

**Observasjon:** Innholdsfortegnelsen bruker «Modellering» for kapittel 6, mens den faktiske overskriften er «Modell». Dette er en eksisterende inkonsistens som ikke hører til ACT-3.5, men bør noteres for ACT-3.10 (sammenstilling).

---

## Svakheter og forbedringsforslag

### V1. Endringene er ikke committet til git

**Alvorlighetsgrad:** Høy
**Kategori:** Prosess

Kapittel 1 og planfiloppdateringer (schedule.json, status.md) ligger kun som ucommittede endringer i arbeidskopien. For sporbarhet og sikkerhet bør disse committes før aktiviteten lukkes, slik det er gjort for alle tidligere aktiviteter.

### V2. Fremdriftstabell i status.md refererer fortsatt til ACT-3.5 i ACT-3.4

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

I fremdriftstabellen i status.md står det «V1-V3 fikset, F1-F4 overført til ACT-3.5» for ACT-3.4-raden. Ifølge den oppdaterte kortstatusen ble F1-F4 overført til ACT-3.8 (Diskusjon), ikke ACT-3.5 (Innledning). Denne inkonsistensen bør rettes for å unngå forvirring i planfilene.

### F1. Tydeliggjør grensen mellom avgrensing 4 og antagelse 2

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Avgrensing 4 («Historisk analyseperiode 1964-1981 ... forutsetter at de identifiserte mønstrene er relevante for prognoseperioden») og antagelse 2 («Relevans av historiske mønstre ... antas å være tilstrekkelig stabile») overlapper tematisk. En enkel justering kan skjerpe grensen: avgrensing 4 kan fokusere på den faktiske tidsperioden og dens begrensning, mens relevans-antakelsen flyttes helt til seksjon 1.4.

### F2. Vurder å fjerne eller forkorte avsnittet om rapportens oppbygging

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Det tredje avsnittet i innledningen («Rapporten er bygd opp slik at casebeskrivelse og datagrunnlag presenteres først ...») overlapper med innholdsfortegnelsen. I en relativt kort rapport med tydelig innholdsfortegnelse kan dette avsnittet oppleves som redundant. Det kan vurderes å enten fjerne det helt eller integrere det som en kort setning i slutten av avsnitt 2.

### F3. Presiser «de neste tolv månedene» i problemstillingen

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Problemstillingen sier «de neste tolv månedene» uten å presisere at dette er juli 1981 til juni 1982. For en caserapport der analyseperioden er historisk, kan det styrke presisjonen å spesifisere perioden eksplisitt, enten i problemstillingen eller i det utdypende avsnittet under. Dette er imidlertid smak og behov; formuleringen fungerer godt som den er.

### F4. Innholdsfortegnelsen bør oppdateres for kapittel 6

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Innholdsfortegnelsen sier «Modellering» for punkt 6, mens den faktiske overskriften er «Modell». Dette er en pre-eksisterende inkonsistens som ikke er skapt av ACT-3.5, men som bør rettes i ACT-3.10 (Sammenstille rapportutkast). Noteres her for sporbarhet.

---

## Avhukningsliste – tiltak

| # | Tiltak | Kategori | Status | Kommentar |
|:--|:-------|:---------|:-------|:----------|
| V1 | Committe alle endringer til git (rapport.md, schedule.json, status.md) | Prosess | [ ] | |
| V2 | Rett «F1-F4 overført til ACT-3.5» til «ACT-3.8» i fremdriftstabellen i status.md | Språk og innhold | [ ] | |
| F1 | Vurder å skjerpe grensen mellom avgrensing 4 og antagelse 2 | Språk og innhold | [ ] | |
| F2 | Vurder å forkorte eller fjerne avsnittet om rapportens oppbygging | Språk og innhold | [ ] | |
| F3 | Vurder å presisere prognoseperioden i problemstillingen | Språk og innhold | [ ] | |
| F4 | Overføres til ACT-3.10: Rett innholdsfortegnelsen for kapittel 6 | Språk og innhold | [ ] | Pre-eksisterende, ikke skapt av ACT-3.5 |

---

## Samsvar med prosjektplan og krav

| Sjekkpunkt | Status | Kommentar |
|:---|:---|:---|
| Fylle inn 1.1 Problemstilling | OK | Presist «hvordan»-spørsmål med to ledd |
| Vurdere om 1.2 Delproblemer er aktuelt og skrive det | OK | Tre delspørsmål koblet til kapittelstruktur |
| Skrive 1.3 Avgrensinger | OK | Fire faglig begrunnede avgrensinger |
| Skrive 1.4 Antagelser | OK | Tre antagelser med eksplisitte konsekvenser |
| Aktualisere tema og koble til caset i innledningen | OK | Generell aktualisering etterfulgt av casekobling |
| Gjennomføre review og lukke aktiviteten | Pågår | Denne reviewen |
| ACT-3.5-C01: Kapittel 1 med alle underseksjoner er ferdigskrevet | OK | Alle seksjoner (1.1-1.4) er skrevet |
| ACT-3.5-C02: Review er gjennomført og aktiviteten er lukket | Pågår | Denne reviewen |
| REQ-006: Norsk fagspråk og sporbarhet | OK | Konsistent norsk fagspråk, god kobling til proposal |
| REQ-007: Leveranser i henhold til kursfaser | OK | Levert 16 dager foran plan |
| REQ-008: Analyse skal kunne etterprøves | Ikke relevant | Ren skriveaktivitet uten analysekode |

---

## Samlet vurdering

### Metodikk

Aktiviteten er en ren skriveaktivitet uten analysekode. Innholdet i kapittel 1 er konsistent med de faktiske resultatene i kapittel 4-8 og med proposalen. Problemstillingen, delspørsmålene og avgrensingene gir et ryddig rammeverk for resten av rapporten.

### Språk, innhold og figurer

Teksten holder jevnt høy kvalitet med godt norsk fagspråk, klar struktur og presis formulering. Innledningen er av passende lengde (ca. 1 side) og følger CLAUDE.md sin rapportsjekkliste på alle vesentlige punkter. De identifiserte svakhetene er begrenset til prosessmessig etterarbeid (commit og planfil-retting), mens forbedringsforsllagene handler om finpuss.

### Anbefalt prioritering videre

1. **(Må)** V1 – Committe endringene til git for sporbarhet
2. **(Må)** V2 – Rette planfilreferansen i fremdriftstabellen (ACT-3.5 -> ACT-3.8)
3. **(Kan)** F1 – Tydeliggjøre grensen mellom avgrensing 4 og antagelse 2
4. **(Kan)** F2 – Vurdere avsnittet om rapportens oppbygging
5. **(Kan)** F3 – Presisere prognoseperioden
6. **(Kan)** F4 – Overføres til ACT-3.10: Rett innholdsfortegnelsen for kapittel 6
