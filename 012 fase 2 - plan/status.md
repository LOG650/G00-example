# Status for PowerHorse-prosjektet

Statusdato: 2026-03-18

Denne statusen bygger på arbeidskopien per 2026-03-18, med planbaselinen i `project-plan.md`, `schedule.json` og `wbs.json` som referanse for avvik.

## Kort status

- Prosjektet er operativt på plan i fase 3.
- Aktivitet `3.1 Rense og strukturere data` er fullført per 2026-03-16.
- Aktivitet `3.2 Velge og estimere modell` er faglig fullført per 2026-03-18, to dager før planlagt sluttdato 2026-03-20.
- Neste aktivitet er `3.3 Validere modell`, planlagt 2026-03-20 til 2026-03-25.
- `schedule.json` og `wbs.json` er oppdatert slik at aktivitet 3.1 og 3.2 nå står som fullført.

## Faktisk fremdrift per arbeidskopi

| Aktivitet | Planlagt periode | Faktisk status | Kommentar |
| --- | --- | --- | --- |
| Analysere case og databehov | 2026-01-12 til 2026-01-16 | Ferdig | Fase 1 fullført |
| Utarbeide proposal | 2026-01-16 til 2026-01-21 | Ferdig | Fase 1 fullført |
| Etablere planbaseline | 2026-02-11 til 2026-02-13 | Ferdig | Fase 2 fullført |
| Rense og strukturere data | 2026-03-09 til 2026-03-11 | Ferdig 2026-03-16 | Fem dager sent, men hentet inn før neste kritiske steg |
| Velge og estimere modell | 2026-03-11 til 2026-03-20 | Ferdig 2026-03-18 | Fullført to dager før plan |
| Validere modell | 2026-03-20 til 2026-03-25 | Ikke startet | Neste aktivitet |
| Lage prognose og anbefalinger | 2026-03-25 til 2026-04-10 | Ikke startet | Avhenger av 3.3 |
| Skrive rapportutkast | 2026-04-10 til 2026-04-27 | Ikke startet som egen aktivitet | Rapporten er delvis skrevet underveis |

## Analyseartefakter

| Aktivitet | Skript | Figurer | Resultatfiler | Vurdering |
| --- | ---: | ---: | ---: | --- |
| 3.1 Rense og strukturere data | 1 | 4 | 4 | Fullført med dokumenterte artefakter og reviewspor |
| 3.2 Velge og estimere modell | 4 | 3 | 10 | Faglig fullført i arbeidskopien |
| 3.3 Validere modell | 0 | 0 | 0 | Kun mappestruktur og README |
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
| 7 Analyse | Ferdig så langt | 7.1-7.3 dekker stasjonaritet, ordensvalg og estimering |
| 8 Resultat | Tom | Venter på validering og prognose |
| 9 Diskusjon | Tom | Ikke skrevet |
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

## Viktigste risikoer

1. Residualavvik i modellestimeringen må håndteres i aktivitet 3.3. Diagnostikken viser avvik fra normalfordeling og tegn til heteroskedastisitet.
2. Rapporten har et dokumentasjonsgap: problemstilling, avgrensinger, antagelser, litteratur, teori og sluttkapitler er ikke ferdigstilt.
3. Aktivitet 3.2 mangler fortsatt eget reviewspor, noe som svekker den administrative sporbarheten sammenlignet med aktivitet 3.1.

## Vurdering

Prosjektet er operativt på plan per 2026-03-18. Forsinkelsen i aktivitet 3.1 er hentet inn, og aktivitet 3.2 er ferdigstilt før planlagt sluttdato. Planfilene er nå oppdatert til å reflektere dette. Den viktigste åpne utfordringen er sporbarhet rundt review og videre validering. Neste kritiske aktivitet er modellvalidering fra 2026-03-20.
