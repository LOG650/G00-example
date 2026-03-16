# Status for PowerHorse-prosjektet

Statusdato: 2026-03-16

Denne statusen er basert på planbaseline og aktivitetsstatus i `project-plan.md`, `schedule.json` og `wbs.json`.

## Kort status

- Prosjektet er i fase 3 - gjennomføring.
- Fase 1 og fase 2 er ferdigstilt som planlagt.
- Aktiviteten `Rense og strukturere data` er fullført per 2026-03-16.
- Aktiviteten ble ferdigstilt fem dager etter opprinnelig planlagt sluttdato (2026-03-11). Forsinkelsen er tatt igjen ved at artefakter, rapporttekst og review er ferdigstilt samlet.
- Neste aktivitet i kritisk linje er `Velge og estimere modell`, etterfulgt av `Validere modell`.

## Gjennomført

| Aktivitet                   | Periode                   | Status |
| --------------------------- | ------------------------- | ------ |
| Analysere case og databehov | 2026-01-12 til 2026-01-16 | Ferdig |
| Utarbeide proposal          | 2026-01-16 til 2026-01-21 | Ferdig |
| Etablere planbaseline       | 2026-02-11 til 2026-02-13 | Ferdig |
| Rense og strukturere data   | 2026-03-09 til 2026-03-16 | Ferdig |

## Pågående

Ingen pågående aktiviteter.

## Neste aktiviteter

| Prioritet | Aktivitet                            | Planlagt periode          | Avhengighet            |
| --------- | ------------------------------------ | ------------------------- | ---------------------- |
| 1         | Velge og estimere modell             | 2026-03-11 til 2026-03-20 | Etter datarensing      |
| 2         | Validere modell                      | 2026-03-20 til 2026-03-25 | Etter modellvalg       |
| 3         | Lage prognose og anbefalinger        | 2026-03-25 til 2026-04-10 | Etter modellvalidering |
| 4         | Skrive rapportutkast                 | 2026-04-10 til 2026-04-27 | Etter prognosearbeid   |
| 5         | Gjennomføre peer review og revisjon | 2026-04-27 til 2026-04-29 | Etter rapportutkast    |
| 6         | Ferdigstille rapport og presentasjon | 2026-04-30 til 2026-05-15 | Etter peer review      |

## Milepæler

| Milepæl                            | Dato       | Status              |
| ----------------------------------- | ---------- | ------------------- |
| Case og problemstilling avklart     | 2026-01-12 | Oppnådd            |
| Godkjent proposal                   | 2026-01-21 | Oppnådd            |
| Godkjent plan                       | 2026-02-13 | Oppnådd            |
| Første analyseutkast               | 2026-03-16 | Oppnådd (5 dager forsinket) |
| Hovedutkast klart for review        | 2026-04-27 | Planlagt            |
| Peer review gjennomført            | 2026-04-29 | Planlagt            |
| Endelig innlevering og presentasjon | 2026-05-15 | Planlagt            |

## Gantt-status

```mermaid
gantt
    title PowerHorse-prosjektet - status per 2026-03-16
    dateFormat  YYYY-MM-DD
    axisFormat  %d.%m

    section Ferdig
    Analysere case og databehov :done, a1, 2026-01-12, 2026-01-16
    Utarbeide proposal :done, a2, 2026-01-16, 2026-01-21
    Etablere planbaseline :done, a3, 2026-02-11, 2026-02-13

    section Pågår
    Rense og strukturere data :done, a4, 2026-03-09, 2026-03-16

    section Neste
    Velge og estimere modell :crit, a5, 2026-03-11, 2026-03-20
    Validere modell :crit, a6, 2026-03-20, 2026-03-25
    Lage prognose og anbefalinger :crit, a7, 2026-03-25, 2026-04-10
    Skrive rapportutkast :crit, a8, 2026-04-10, 2026-04-27
    Gjennomføre peer review og revisjon :crit, a9, 2026-04-27, 2026-04-29
    Ferdigstille rapport og presentasjon :crit, a10, 2026-04-30, 2026-05-15
```

## Sjekkliste for aktiviteter

### FullfÃ¸rt

#### Analysere case og databehov

- [X] GjennomgÃ¥ casebeskrivelsen
- [X] Avklare problemstilling
- [X] Identifisere beslutningsbehov
- [X] Avklare forventet datagrunnlag

#### Utarbeide proposal

- [X] Beskrive problem og bakgrunn
- [X] Definere mÃ¥l og avgrensning
- [X] Begrunne metodevalg pÃ¥ overordnet nivÃ¥
- [X] Levere proposal til fasegodkjenning

#### Etablere planbaseline

- [X] Etablere prosjektplan
- [X] Ferdigstille fremdriftsplan
- [X] Ferdigstille WBS
- [X] Etablere baseline for krav, risiko og milepÃ¦ler

#### Rense og strukturere data

- [X] Kontrollere observasjoner per måned
- [X] Strukturere tidsserien
- [X] Splitte datasettet i trenings- og testdata
- [X] Lage grunnleggende visualiseringer
- [X] Dokumentere datakvalitet
- [X] Bekrefte at dataserien er komplett og riktig indeksert
- [X] Sette inn tekst og figurer på rett plass i `005 report/rapport.md`
- [X] Lukke aktiviteten før modellarbeidet starter

Datakvalitet er dokumentert med en arbeidsantagelse om at datasettet allerede er kvalitetssjekket av de som leverte det, siden prosjektet ikke har egne kilder for uavhengig verifikasjon av datakvaliteten.

### Neste aktiviteter

#### Velge og estimere modell

- [ ] Vurdere aktuell modelltype for trend og sesong
- [ ] Velge SARIMA-spesifikasjon
- [ ] Estimere modellparametere
- [ ] Dokumentere modellvalg og begrunnelse

#### Validere modell

- [ ] Kontrollere residualer og modellforutsetninger
- [ ] Vurdere prognoseegenskaper mot historiske data
- [ ] Dokumentere styrker, svakheter og usikkerhet
- [ ] Bekrefte at modellen er egnet for prognoseformÃ¥let

#### Lage prognose og anbefalinger

- [ ] Lage 12-måneders prognose
- [ ] Tolke prognoseresultater
- [ ] Vurdere konsekvenser for produksjon og lager
- [ ] Formulere anbefalinger til PowerHorse-caset

#### Skrive rapportutkast

- [ ] Strukturere rapporten
- [ ] Skrive metodekapittel
- [ ] Skrive resultat- og diskusjonskapittel
- [ ] Samle figurer, tabeller og referanser i et komplett utkast

#### GjennomfÃ¸re peer review og revisjon

- [ ] Innhente tilbakemeldinger fra peer review
- [ ] Oppsummere funn og forbedringspunkter
- [ ] Revidere analyse, tekst og presentasjon av resultater
- [ ] Lukke avvik fÃ¸r sluttfÃ¸ring

#### Ferdigstille rapport og presentasjon

- [ ] Ferdigstille endelig rapport
- [ ] Kvalitetssikre sprÃ¥k, sporbarhet og konsistens
- [ ] Ferdigstille presentasjonsmateriell
- [ ] KlargjÃ¸re endelig innlevering og presentasjon

## Vurdering

Prosjektet har fullført initiering, planlegging og datarensing. Aktivitet 3.1 ble lukket 2026-03-16, fem dager etter opprinnelig plan. Forsinkelsen er håndterbar da den ikke har påvirket andre aktiviteter ennå. Det viktigste nå er å starte modellvalg og estimering raskt for å hente inn tid på den kritiske linjen.
