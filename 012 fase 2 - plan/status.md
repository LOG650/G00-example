# Status for PowerHorse-prosjektet

Statusdato: 2026-03-18

Denne statusen bygger på arbeidskopien per 2026-03-18, med planbaselinen i `project-plan.md`, `schedule.json` og `wbs.json` som referanse for avvik.

## Kort status

- Prosjektet er operativt på plan i fase 3.
- Aktivitet `3.1 Rense og strukturere data` er fullført per 2026-03-16.
- Aktivitet `3.2 Velge og estimere modell` er faglig fullført per 2026-03-18, to dager før planlagt sluttdato 2026-03-20.
- Aktivitet `3.3 Validere modell` er godt i gang. Residualdiagnostikk, Ljung-Box og ARCH-LM er nå dokumentert i rapportens 7.4, mens testsettvalidering og samlet vurdering gjenstår.
- `schedule.json` og `wbs.json` er oppdatert slik at aktivitet 3.1 og 3.2 nå står som fullført.

## Faktisk fremdrift per arbeidskopi

| Aktivitet | Planlagt periode | Faktisk status | Kommentar |
| --- | --- | --- | --- |
| Analysere case og databehov | 2026-01-12 til 2026-01-16 | Ferdig | Fase 1 fullført |
| Utarbeide proposal | 2026-01-16 til 2026-01-21 | Ferdig | Fase 1 fullført |
| Etablere planbaseline | 2026-02-11 til 2026-02-13 | Ferdig | Fase 2 fullført |
| Rense og strukturere data | 2026-03-09 til 2026-03-11 | Ferdig 2026-03-16 | Fem dager sent, men hentet inn før neste kritiske steg |
| Velge og estimere modell | 2026-03-11 til 2026-03-20 | Ferdig 2026-03-18 | Fullført to dager før plan |
| Validere modell | 2026-03-20 til 2026-03-25 | Pågår/delvis startet | Residualdiagnostikk, Ljung-Box og ARCH-LM er dokumentert. Testsettvalidering og egne 3.3-artefakter gjenstår |
| Lage prognose og anbefalinger | 2026-03-25 til 2026-04-10 | Ikke startet | Avhenger av 3.3 |
| Skrive rapportutkast | 2026-04-10 til 2026-04-27 | Ikke startet som egen aktivitet | Rapporten er delvis skrevet underveis |

## Avhukingsliste for aktiviteter

### Fullført

#### Analysere case og databehov

- [x] Gjennomgå casebeskrivelsen
- [x] Avklare problemstilling i proposal
- [x] Identifisere beslutningsbehov
- [x] Avklare forventet datagrunnlag

#### Utarbeide proposal

- [x] Beskrive problem og bakgrunn
- [x] Definere mål og avgrensninger
- [x] Begrunne metodevalg på overordnet nivå
- [x] Levere proposal til fasegodkjenning

#### Etablere planbaseline

- [x] Etablere prosjektplan
- [x] Ferdigstille fremdriftsplan
- [x] Ferdigstille WBS
- [x] Etablere baseline for krav, risiko og milepæler

#### Rense og strukturere data

- [x] Kontrollere observasjoner per måned
- [x] Strukturere tidsserien
- [x] Splitte datasettet i trenings- og testdata
- [x] Lage grunnleggende visualiseringer
- [x] Dokumentere datakvalitet
- [x] Bekrefte at dataserien er komplett og riktig indeksert
- [x] Sette inn tekst og figurer på rett plass i `rapport.md`
- [x] Lukke aktiviteten før modellarbeidet starter

#### Velge og estimere modell

- [x] Beskrive generell SARIMA-modell matematisk i rapportens kapittel 6
- [x] Vurdere aktuell modelltype for trend og sesong
- [x] Rydde modellkapitlet slik at kapittel 6 ikke repeterer figurer og tabeller fra kapittel 4
- [x] Velge log-transformasjon som hovedspor for stasjonaritetsvurdering
- [x] Teste for stasjonaritet og velge differensiering
- [x] Analysere ACF og PACF
- [x] Velge SARIMA-spesifikasjon
- [x] Estimere modellparametere
- [x] Dokumentere modellvalg og begrunnelse

### Pågår

#### Validere modell

- [x] Bygge videre på residualdiagnostikk og rydde den inn i rapportens kapittel 7.4
- [x] Kjøre Ljung-Box på sesongrelevante lags, minst 12 og 24
- [x] Kjøre ARCH-LM for heteroskedastisitet
- [ ] Generere prognoser mot testdatasettet for perioden 1978-01 til 1981-06
- [ ] Beregne MAE, RMSE og MAPE
- [x] Dokumentere kapittel 7.4 Validering
- [ ] Dokumentere kapittel 8.1 Resultater fra testsettvalidering
- [ ] Forberede grunnlag for diskusjon av modellens egnethet i kapittel 9

### Neste aktiviteter

#### Lage prognose og anbefalinger

- [ ] Lage 12-måneders prognose
- [ ] Tolke prognoseresultater
- [ ] Vurdere konsekvenser for produksjon og lager
- [ ] Formulere anbefalinger til PowerHorse-caset

#### Skrive rapportutkast

- [ ] Fylle inn problemstilling, avgrensinger og antagelser i kapittel 1
- [ ] Skrive kapittel 2 Litteratur
- [ ] Skrive kapittel 3 Teori
- [ ] Fylle kapittel 8 Resultat med komprimerte sluttresultater
- [ ] Skrive kapittel 9 Diskusjon
- [ ] Skrive kapittel 10 Konklusjon
- [ ] Samle figurer, tabeller og referanser i et komplett utkast

#### Gjennomføre peer review og revisjon

- [ ] Innhente tilbakemeldinger fra peer review
- [ ] Oppsummere funn og forbedringspunkter
- [ ] Revidere analyse, tekst og presentasjon av resultater
- [ ] Lukke avvik før sluttføring

#### Ferdigstille rapport og presentasjon

- [ ] Ferdigstille endelig rapport
- [ ] Kvalitetssikre språk, sporbarhet og konsistens
- [ ] Ferdigstille presentasjonsmateriell
- [ ] Klargjøre endelig innlevering og presentasjon

## Analyseartefakter

| Aktivitet | Skript | Figurer | Resultatfiler | Vurdering |
| --- | ---: | ---: | ---: | --- |
| 3.1 Rense og strukturere data | 1 | 4 | 4 | Fullført med dokumenterte artefakter og reviewspor |
| 3.2 Velge og estimere modell | 4 | 3 | 10 | Faglig fullført i arbeidskopien |
| 3.3 Validere modell | 1 | 0 | 2 | Residualtester er kjørt og dokumentert, men testsettvalidering gjenstår |
| 3.4 Lage prognose og anbefalinger | 0 | 0 | 0 | Kun mappestruktur og README |

## Rapportstatus

| Kapittel | Status | Kommentar |
| --- | --- | --- |
| 1 Innledning | Delvis | Innledning er skrevet, men 1.1, 1.3 og 1.4 er fortsatt tomme |
| 2 Litteratur | Tom | Ikke skrevet |
| 3 Teori | Tom | Ikke skrevet |
| 4 Casebeskrivelse | Ferdig | Fire figurer og én tabell |
| 5 Metode og data | Ferdig | Datasplitt og tabell 5.1 dokumentert |
| 6 Modellering | Ferdig | Modelltype, antagelser og SARIMA-rammeverk |
| 7 Analyse | Pågår videre | 7.1-7.3 er skrevet, og 7.4 Validering dokumenterer residualdiagnostikk, Ljung-Box og ARCH-LM |
| 8 Resultat | Delvis strukturert | 8.1 skal dekke testsettvalidering, og 8.2 skal dekke endelig prognosearbeid |
| 9 Diskusjon | Tom | Skal romme vurdering av modellens egnethet, begrensninger og praktiske implikasjoner |
| 10 Konklusjon | Tom | Ikke skrevet |
| 11 Bibliografi | Tom | Ikke skrevet |
| 12 Vedlegg | Tom | Ikke skrevet |

## Milepæler

| Milepæl | Baseline | Arbeidskopi-status | Vurdering |
| --- | --- | --- | --- |
| MS-001 Case og problemstilling avklart | 2026-01-12 | Oppnådd | Problemstillingen finnes i proposalen, men ikke i rapportens seksjon 1.1 |
| MS-002 Godkjent proposal | 2026-01-21 | Oppnådd | Ingen avvik |
| MS-003 Godkjent plan | 2026-02-13 | Oppnådd | Ingen avvik |
| MS-004 Første analyseutkast | 2026-03-11 | Oppnådd 2026-03-16 | Fem dager forsinket mot baseline |
| MS-005 Hovedutkast klart for review | 2026-04-27 | Planlagt | Ingen endring |
| MS-006 Peer review gjennomført | 2026-04-29 | Planlagt | Ingen endring |
| MS-007 Endelig innlevering og presentasjon | 2026-05-15 | Planlagt | Ingen endring |

## Avvik mellom arbeidskopi og styringsgrunnlag

1. MS-004 står fortsatt med baseline-dato 2026-03-11 i planfilene, mens arbeidskopien viser faktisk oppnåelse 2026-03-16.
2. Aktivitet 3.2 er faglig ferdig, men ikke fullt administrativt lukket med eget reviewspor tilsvarende aktivitet 3.1.
3. Aktivitet 3.3 er startet faglig, men mangler fortsatt egne artefakter i aktivitetsmappen.

## Viktigste risikoer

1. Residualavvik i modellestimeringen må håndteres ferdig i aktivitet 3.3. Diagnostikken viser avvik fra normalfordeling, residualautokorrelasjon ved lag 12 og 24 og tydelig heteroskedastisitet.
2. Rapporten har et dokumentasjonsgap: problemstilling, avgrensinger, antagelser, litteratur, teori og sluttkapitler er ikke ferdigstilt.
3. Aktivitet 3.2 mangler fortsatt eget reviewspor, noe som svekker den administrative sporbarheten sammenlignet med aktivitet 3.1.

## Vurdering

Prosjektet er operativt på plan per 2026-03-18. Forsinkelsen i aktivitet 3.1 er hentet inn, og aktivitet 3.2 er ferdigstilt før planlagt sluttdato. Aktivitet 3.3 er nå formelt godt i gang, og residualdiagnostikken er utvidet med Ljung-Box og ARCH-LM i kapittel 7.4. Hovedarbeidet som gjenstår er testsettvalidering og den samlede vurderingen av modellens egnethet.
