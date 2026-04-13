# Status for PowerHorse-prosjektet

Statusdato: 2026-04-13

Denne statusen bygger på arbeidskopien per 2026-04-13, med planbaselinen i `project-plan.md`, `schedule.json` og `wbs.json` som referanse for avvik.

## Kort status

- Prosjektet er operativt på plan i fase 3.
- Aktivitet `ACT-3.1 Rense og strukturere data` er fullført per 2026-03-16.
- Aktivitet `ACT-3.2 Velge og estimere modell` er fullført per 2026-03-23. Review gjennomført med fem tiltak (V1–V3, F1–F2) implementert.
- Aktivitet `ACT-3.3 Validere modell` er fullført per 2026-03-23. Review gjennomført med to svakheter (V1–V2) og tre forbedringsforslag (F1–F3) implementert.
- Aktivitet `ACT-3.4 Lage prognose og anbefalinger` er fullført per 2026-03-25. Review gjennomført med tre svakheter (V1–V3) fikset og fire forbedringsforslag (F1–F4) overført til ACT-3.8.
- Aktivitet `ACT-3.5 Skrive kapittel 1 Innledning` er fullført per 2026-03-25. Review gjennomført med to svakheter (V1–V2) fikset og fire forbedringsforslag (F1–F4) notert. F4 overført til ACT-3.10.
- Aktivitet `ACT-3.8 Skrive kapittel 9 Diskusjon` er ferdigskrevet per 2026-04-13. Seks seksjoner (9.1–9.6) med to tabeller og én figur. Alle sjekkliste-punkter unntatt review er fullført. F1–F4 fra ACT-3.4-reviewen er innarbeidet. Venter på review.
- Aktivitet `ACT-3.7 Skrive kapittel 3 Teori` er fullført per 2026-04-13. Review gjennomført med to svakheter (V1–V2) rettet og fem forbedringsforslag (F1–F5) implementert. F5 overført til ACT-3.10.
- Neste steg: Review av ACT-3.8, deretter ACT-3.9 (kap 10 Konklusjon). Parallelt: ACT-3.6 (kap 2) → ACT-3.10.

## Faktisk fremdrift per arbeidskopi

| Aktivitet | Planlagt periode | Faktisk status | Kommentar |
| --- | --- | --- | --- |
| ACT-1.1 Analysere case og databehov | 2026-01-12 til 2026-01-16 | Ferdig | Fase 1 fullført |
| ACT-1.2 Utarbeide proposal | 2026-01-16 til 2026-01-21 | Ferdig | Fase 1 fullført |
| ACT-2.1 Etablere planbaseline | 2026-02-11 til 2026-02-13 | Ferdig | Fase 2 fullført |
| ACT-3.1 Rense og strukturere data | 2026-03-09 til 2026-03-11 | Ferdig 2026-03-16 | Fem dager sent, men hentet inn før neste kritiske steg |
| ACT-3.2 Velge og estimere modell | 2026-03-11 til 2026-03-20 | Ferdig 2026-03-23 | Faglig ferdig 2026-03-18, review gjennomført og lukket 2026-03-23 |
| ACT-3.3 Validere modell | 2026-03-20 til 2026-03-25 | Ferdig 2026-03-23 | Review gjennomført og lukket 2026-03-23 |
| ACT-3.4 Lage prognose og anbefalinger | 2026-03-25 til 2026-04-10 | Ferdig 2026-03-25 | Review gjennomført og lukket 2026-03-25. V1–V3 fikset, F1–F4 overført til ACT-3.8 |
| ACT-3.5 Skrive kapittel 1 Innledning | 2026-04-10 til 2026-04-13 | Ferdig 2026-03-25 | Kapittel 1 med alle underseksjoner ferdigskrevet |
| ACT-3.6 Skrive kapittel 2 Litteratur | 2026-04-10 til 2026-04-15 | Ikke startet | Parallell med 3.5 og 3.7 |
| ACT-3.7 Skrive kapittel 3 Teori | 2026-04-10 til 2026-04-15 | Ferdig 2026-04-13 | Review gjennomført og lukket 2026-04-13. V1–V2 rettet, F1–F4 implementert, F5 overført til ACT-3.10 |
| ACT-3.8 Skrive kapittel 9 Diskusjon | 2026-04-10 til 2026-04-15 | Skrevet 2026-04-13 | Kapittel ferdigskrevet, venter på review |
| ACT-3.9 Skrive kapittel 10 Konklusjon | 2026-04-19 til 2026-04-21 | Ikke startet | Kritisk sti, avhenger av ACT-3.8 |
| ACT-3.10 Sammenstille rapportutkast | 2026-04-21 til 2026-04-27 | Ikke startet | Avhenger av 3.5, 3.6, 3.7 og 3.9. Knyttet til MS-005 |

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

#### ACT-3.3 Validere modell

- [x] Bygge videre på residualdiagnostikk og rydde den inn i rapportens kapittel 7.4
- [x] Kjøre Ljung-Box på sesongrelevante lags, minst 12 og 24
- [x] Kjøre ARCH-LM for heteroskedastisitet
- [x] Generere prognoser mot testdatasettet for perioden 1978-01 til 1981-06
- [x] Beregne MAE, RMSE og MAPE
- [x] Dokumentere kapittel 7.4 Validering
- [x] Dokumentere kapittel 8.1 Resultater fra testsettvalidering
- [x] Forberede grunnlag for diskusjon av modellens egnethet i kapittel 9
- [x] Gjennomføre review og lukke aktiviteten

#### ACT-3.4 Lage prognose og anbefalinger

- [x] Lage 12-måneders prognose
- [x] Tolke prognoseresultater
- [x] Vurdere konsekvenser for produksjon og lager
- [x] Formulere anbefalinger til PowerHorse-caset
- [x] Gjennomføre review og lukke aktiviteten

#### ACT-3.5 Skrive kapittel 1 Innledning

- [x] Fylle inn 1.1 Problemstilling
- [x] Vurdere om 1.2 Delproblemer er aktuelt og skrive det
- [x] Skrive 1.3 Avgrensinger
- [x] Skrive 1.4 Antagelser
- [x] Aktualisere tema og koble til caset i innledningen
- [x] Gjennomføre review og lukke aktiviteten

#### ACT-3.7 Skrive kapittel 3 Teori

- [x] Beskrive teoretisk rammeverk (tidsserieanalyse, SARIMA, stasjonaritet)
- [x] Koble teori til metodevalg og diskusjon
- [x] Kontrollere at alle referanser i kap. 3 finnes i kap. 11 og har oppsummeringsfil i `003 references/`
- [x] Gjennomføre review og lukke aktiviteten

### Neste aktiviteter

#### ACT-3.6 Skrive kapittel 2 Litteratur

- [ ] Identifisere relevante kilder
- [ ] Knytte litteratur til problemstilling og metodevalg
- [ ] Gjennomføre review og lukke aktiviteten

#### ACT-3.8 Skrive kapittel 9 Diskusjon

- [x] Drøfte funn opp mot problemstilling og litteratur
- [x] Drøfte log-transformasjon og manglende bias-korreksjon ($\exp(\mu + \sigma^2/2)$ som metodisk nyanse)
- [x] Vurdere begrensninger og praktiske implikasjoner
- [x] Drøft biaskorreksjon med horisontavhengig varians i kap. 9 (ref. ACT-3.4 review F1)
- [x] Vurder refittet parametertabell i rapport eller vedlegg (ref. ACT-3.4 review F2)
- [x] Vurder oppsummeringstabeller (tab_03, tab_04) i kap. 9 eller vedlegg (ref. ACT-3.4 review F3)
- [x] Vurder helhetsfigur med hele tidsserien og prognose i kap. 9 eller vedlegg (ref. ACT-3.4 review F4)
- [ ] Gjennomføre review og lukke aktiviteten

#### ACT-3.9 Skrive kapittel 10 Konklusjon

- [ ] Svare direkte på problemstillingen
- [ ] Løfte fram viktigste funn og implikasjoner
- [ ] Gjennomføre review og lukke aktiviteten

#### ACT-3.10 Sammenstille rapportutkast

- [ ] Skrive sammendrag (norsk)
- [ ] Skrive abstract (engelsk)
- [ ] Oppdatere innholdsfortegnelse (inkl. rette «Modellering» → «Modell» for kap. 6 og fjerne parentesbemerkning for kap. 5)
- [ ] Ferdigstille kapittel 11 Bibliografi
- [ ] Samle vedlegg i kapittel 12
- [ ] Intern kvalitetssjekk av hele utkastet
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
| ACT-3.3 Validere modell | 2 | 1 | 6 | Fullført med dokumenterte artefakter og reviewspor |
| ACT-3.4 Lage prognose og anbefalinger | 2 | 1 | 8 | Fullført med dokumenterte artefakter og reviewspor |
| ACT-3.7 Skrive kapittel 3 Teori | 1 | 4 | 0 | Figurer generert med syntetiske data for teoriillustrasjon |

## Rapportstatus

| Kapittel | Status | Kommentar |
| --- | --- | --- |
| 1 Innledning | Ferdig | Alle underseksjoner (1.1–1.4) ferdigskrevet |
| 2 Litteratur | Tom | Ikke skrevet |
| 3 Teori | Ferdig | Fem seksjoner (3.1–3.5) med APA7-referanser. Review gjennomført og lukket |
| 4 Casebeskrivelse | Ferdig | Fire figurer og én tabell |
| 5 Metode og data | Ferdig | Datasplitt og tabell 5.1 dokumentert |
| 6 Modellering | Ferdig | Modelltype, antagelser og SARIMA-rammeverk |
| 7 Analyse | Ferdig | 7.1–7.4 er skrevet med stasjonaritet, ACF/PACF, estimering og validering |
| 8 Resultat | Ferdig | 8.1 testsettvalidering og 8.2 prognoseresultater er ferdig |
| 9 Diskusjon | Ferdig | Seks seksjoner (9.1–9.6): modellvalg, residualdiagnostikk, bias, kapasitetsplanlegging, begrensninger og samlet vurdering. To tabeller og én figur. Venter på review |
| 10 Konklusjon | Tom | Ikke skrevet |
| 11 Bibliografi | Påbegynt | 8 referanser fra teorikapitlet lagt inn i APA7 |
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

1. Residualavvik er dokumentert og vurdert i kapittel 7.4, og review-tiltak (V1–V2, F1–F3) er implementert. Diagnostikken viser avvik fra normalfordeling, residualautokorrelasjon ved lag 12 og 24 og heteroskedastisitet. Disse funnene skal drøftes i kapittel 9 (Diskusjon) i ACT-3.8.
2. Rapporten har et dokumentasjonsgap: problemstilling, avgrensinger, antagelser, litteratur, teori og sluttkapitler er ikke ferdigstilt.

## Vurdering

Prosjektet er operativt på plan per 2026-03-25. Aktivitetene ACT-3.1, ACT-3.2, ACT-3.3 og ACT-3.4 er fullført. Hovedarbeidet som gjenstår er sluttkapitlene i rapporten (innledning, litteratur, teori, diskusjon, konklusjon) og peer review.
