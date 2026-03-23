# Status for PowerHorse-prosjektet

Statusdato: 2026-03-23

Denne statusen bygger på arbeidskopien per 2026-03-23, med planbaselinen i `project-plan.md`, `schedule.json` og `wbs.json` som referanse for avvik.

## Kort status

- Prosjektet er operativt på plan i fase 3.
- Aktivitet `ACT-3.1 Rense og strukturere data` er fullført per 2026-03-16.
- Aktivitet `ACT-3.2 Velge og estimere modell` er fullført per 2026-03-23. Review gjennomført med fem tiltak (V1–V3, F1–F2) implementert.
- Aktivitet `ACT-3.3 Validere modell` er faglig fullført per 2026-03-23, men review gjenstår før aktiviteten kan lukkes. Residualdiagnostikk, testsettvalidering og feilmål er dokumentert i rapportens kapittel 7.4 og 8.1.
- Neste steg er review av ACT-3.3, deretter `ACT-3.4 Lage prognose og anbefalinger`.

## Faktisk fremdrift per arbeidskopi

| Aktivitet | Planlagt periode | Faktisk status | Kommentar |
| --- | --- | --- | --- |
| ACT-1.1 Analysere case og databehov | 2026-01-12 til 2026-01-16 | Ferdig | Fase 1 fullført |
| ACT-1.2 Utarbeide proposal | 2026-01-16 til 2026-01-21 | Ferdig | Fase 1 fullført |
| ACT-2.1 Etablere planbaseline | 2026-02-11 til 2026-02-13 | Ferdig | Fase 2 fullført |
| ACT-3.1 Rense og strukturere data | 2026-03-09 til 2026-03-11 | Ferdig 2026-03-16 | Fem dager sent, men hentet inn før neste kritiske steg |
| ACT-3.2 Velge og estimere modell | 2026-03-11 til 2026-03-20 | Ferdig 2026-03-23 | Faglig ferdig 2026-03-18, review gjennomført og lukket 2026-03-23 |
| ACT-3.3 Validere modell | 2026-03-20 til 2026-03-25 | Pågår/faglig ferdig | Faglig arbeid fullført 2026-03-23, review gjenstår |
| ACT-3.4 Lage prognose og anbefalinger | 2026-03-25 til 2026-04-10 | Ikke startet | Avhenger av 3.3 |
| ACT-3.5 Skrive rapportutkast | 2026-04-10 til 2026-04-27 | Ikke startet som egen aktivitet | Rapporten er delvis skrevet underveis |

## Avhukingsliste for aktiviteter

### Fullført

#### ACT-1.1 Analysere case og databehov

- [x] Gjennomgå casebeskrivelsen
- [x] Avklare problemstilling i proposal
- [x] Identifisere beslutningsbehov
- [x] Avklare forventet datagrunnlag
- [x] Gjennomføre review og lukke aktiviteten

#### ACT-1.2 Utarbeide proposal

- [x] Beskrive problem og bakgrunn
- [x] Definere mål og avgrensninger
- [x] Begrunne metodevalg på overordnet nivå
- [x] Levere proposal til fasegodkjenning
- [x] Gjennomføre review og lukke aktiviteten

#### ACT-2.1 Etablere planbaseline

- [x] Etablere prosjektplan
- [x] Ferdigstille fremdriftsplan
- [x] Ferdigstille WBS
- [x] Etablere baseline for krav, risiko og milepæler
- [x] Gjennomføre review og lukke aktiviteten

#### ACT-3.1 Rense og strukturere data

- [x] Kontrollere observasjoner per måned
- [x] Strukturere tidsserien
- [x] Splitte datasettet i trenings- og testdata
- [x] Lage grunnleggende visualiseringer
- [x] Dokumentere datakvalitet
- [x] Bekrefte at dataserien er komplett og riktig indeksert
- [x] Sette inn tekst og figurer på rett plass i `rapport.md`
- [x] Gjennomføre review og lukke aktiviteten

#### ACT-3.2 Velge og estimere modell

- [x] Beskrive generell SARIMA-modell matematisk i rapportens kapittel 6
- [x] Vurdere aktuell modelltype for trend og sesong
- [x] Rydde modellkapitlet slik at kapittel 6 ikke repeterer figurer og tabeller fra kapittel 4
- [x] Velge log-transformasjon som hovedspor for stasjonaritetsvurdering
- [x] Teste for stasjonaritet og velge differensiering
- [x] Analysere ACF og PACF
- [x] Velge SARIMA-spesifikasjon
- [x] Estimere modellparametere
- [x] Dokumentere modellvalg og begrunnelse
- [x] Gjennomføre review og lukke aktiviteten

### Pågår

#### ACT-3.3 Validere modell

- [x] Bygge videre på residualdiagnostikk og rydde den inn i rapportens kapittel 7.4
- [x] Kjøre Ljung-Box på sesongrelevante lags, minst 12 og 24
- [x] Kjøre ARCH-LM for heteroskedastisitet
- [x] Generere prognoser mot testdatasettet for perioden 1978-01 til 1981-06
- [x] Beregne MAE, RMSE og MAPE
- [x] Dokumentere kapittel 7.4 Validering
- [x] Dokumentere kapittel 8.1 Resultater fra testsettvalidering
- [x] Forberede grunnlag for diskusjon av modellens egnethet i kapittel 9
- [ ] Gjennomføre review og lukke aktiviteten

### Neste aktiviteter

#### ACT-3.4 Lage prognose og anbefalinger

- [ ] Lage 12-måneders prognose
- [ ] Tolke prognoseresultater
- [ ] Vurdere konsekvenser for produksjon og lager
- [ ] Formulere anbefalinger til PowerHorse-caset
- [ ] Gjennomføre review og lukke aktiviteten

#### ACT-3.5 Skrive rapportutkast

- [ ] Fylle inn problemstilling, avgrensinger og antagelser i kapittel 1
- [ ] Skrive kapittel 2 Litteratur
- [ ] Skrive kapittel 3 Teori
- [ ] Fylle kapittel 8 Resultat med komprimerte sluttresultater
- [ ] Skrive kapittel 9 Diskusjon
- [ ] Skrive kapittel 10 Konklusjon
- [ ] Samle figurer, tabeller og referanser i et komplett utkast
- [ ] Gjennomføre review og lukke aktiviteten

#### ACT-4.1 Gjennomføre peer review og revisjon

- [ ] Innhente tilbakemeldinger fra peer review
- [ ] Oppsummere funn og forbedringspunkter
- [ ] Revidere analyse, tekst og presentasjon av resultater
- [ ] Lukke avvik før sluttføring
- [ ] Gjennomføre review og lukke aktiviteten

#### ACT-4.2 Ferdigstille rapport og presentasjon

- [ ] Ferdigstille endelig rapport
- [ ] Kvalitetssikre språk, sporbarhet og konsistens
- [ ] Ferdigstille presentasjonsmateriell
- [ ] Klargjøre endelig innlevering og presentasjon
- [ ] Gjennomføre review og lukke aktiviteten

## Analyseartefakter

| Aktivitet | Skript | Figurer | Resultatfiler | Vurdering |
| --- | ---: | ---: | ---: | --- |
| ACT-3.1 Rense og strukturere data | 1 | 4 | 4 | Fullført med dokumenterte artefakter og reviewspor |
| ACT-3.2 Velge og estimere modell | 4 | 3 | 10 | Fullført med dokumenterte artefakter og reviewspor |
| ACT-3.3 Validere modell | 2 | 1 | 6 | Faglig fullført, review gjenstår |
| ACT-3.4 Lage prognose og anbefalinger | 0 | 0 | 0 | Kun mappestruktur og README |

## Rapportstatus

| Kapittel | Status | Kommentar |
| --- | --- | --- |
| 1 Innledning | Delvis | Innledning er skrevet, men 1.1, 1.3 og 1.4 er fortsatt tomme |
| 2 Litteratur | Tom | Ikke skrevet |
| 3 Teori | Tom | Ikke skrevet |
| 4 Casebeskrivelse | Ferdig | Fire figurer og én tabell |
| 5 Metode og data | Ferdig | Datasplitt og tabell 5.1 dokumentert |
| 6 Modellering | Ferdig | Modelltype, antagelser og SARIMA-rammeverk |
| 7 Analyse | Ferdig | 7.1–7.4 er skrevet med stasjonaritet, ACF/PACF, estimering og validering |
| 8 Resultat | Delvis | 8.1 testsettvalidering er ferdig, 8.2 venter på ACT-3.4 prognosearbeid |
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

## Viktigste risikoer

1. Residualavvik er dokumentert og vurdert i kapittel 7.4. Diagnostikken viser avvik fra normalfordeling, residualautokorrelasjon ved lag 12 og 24 og heteroskedastisitet. Disse funnene må drøftes i kapittel 9 (Diskusjon).
2. Rapporten har et dokumentasjonsgap: problemstilling, avgrensinger, antagelser, litteratur, teori og sluttkapitler er ikke ferdigstilt.

## Vurdering

Prosjektet er operativt på plan per 2026-03-23. Aktivitetene ACT-3.1 og ACT-3.2 er fullført og lukket. ACT-3.3 er faglig ferdig med all validering dokumentert, men review gjenstår. Neste steg er review av ACT-3.3, deretter ACT-3.4 (prognose og anbefalinger). Hovedarbeidet som gjenstår er prognosearbeidet, sluttkapitlene i rapporten (innledning, litteratur, teori, diskusjon, konklusjon) og peer review.
