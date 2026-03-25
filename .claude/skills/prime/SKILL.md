---
name: prime
description: >-
  Last inn PowerHorse-prosjektkontekst.
  Bruk ved oppstart av ny samtale eller når du trenger full oversikt.
  Triggeres av «prime», «last inn kontekst» eller «/prime».
allowed-tools: Read, Glob, Grep, Bash
---

# Prime: Last inn PowerHorse-prosjektkontekst

## Mål

Bygg rask, korrekt arbeidskontekst for LOG650-prosjektet før du gjør noe annet. Dette repoet er et studentprosjekt for prognoseanalyse, rapportskriving og prosjektstyring rundt PowerHorse-caset.

`CLAUDE.md` lastes automatisk inn i konteksten. Ikke les den på nytt.

## Arbeidsmåte

### 1. Kartlegg prosjektstrukturen

List toppnivået og analysemappene:

```bash
ls -1 .
ls -1 "006 analysis/aktiviteter/"
```

Kjenn hovedområdene:

| Mappe | Innhold |
| --- | --- |
| `004 data/` | Salgsdata (rådata og bearbeidet) |
| `005 report/` | `rapport.md` — selve rapporten |
| `006 analysis/` | Analysearbeid organisert etter aktiviteter (`aktiviteter/X_Y_…/`) |
| `011 fase 1 - proposal/` | Ferdig proposal |
| `012 fase 2 - plan/` | Prosjektplan, status, WBS, schedule, risiko og reviews |
| `013 fase 3 - gjennomføring/` | Arbeidsfiler for gjennomføringsfasen |
| `014 fase 4 - report/` | Arbeidsfiler for rapportfasen |
| `000 templates/` | Maler (inkl. prosjektmal for LOG650) |
| `003 references/` | Kilder og referanser |
| `.claude/skills/` | Claude-skills (review-mal m.m.) |

### 2. Les prosjektets nåværende status

Les disse filene i fulltekst:

- `012 fase 2 - plan/status.md` — faktisk fremdrift og sjekklister
- `012 fase 2 - plan/project-plan.md` — planbaseline og milepæler
- `006 analysis/README.md` — oversikt over analysemapper

Les deretter innholdsfortegnelse og overskrifter i `005 report/rapport.md` (bare de første ~80 linjene) for å forstå rapportens nåværende omfang. Ikke les hele rapporten med mindre oppgaven krever det.

### 3. Forstå faktisk progresjon

```bash
git status --short
git log -8 --oneline
```

Bruk dette sammen med `status.md` for å forstå hva som er pågående, ferdig og hva som er neste naturlige aktivitet.

### 4. Les bare det som trengs for oppgaven

Velg ut filer avhengig av oppgavetype:

- **Rapportarbeid**: Les relevante seksjoner i `005 report/rapport.md`.
- **Analysearbeid**: Les README, skript, figurer og resultater i riktig aktivitetsmappe under `006 analysis/aktiviteter/`.
- **Plan/status-arbeid**: Les relevante filer i `012 fase 2 - plan/` (`wbs.json`, `schedule.json`, `requirements.json`, `risk.json`, review-filer).
- **Dataspørsmål**: Les filer i `004 data/`.
- **Review**: Bruk `/review-act`-skillen i stedet for manuelt arbeid.

Ikke les alt ukritisk, men sørg for at du forstår sammenhengen mellom analyse, rapport og plan.

## Faglig kontekst

- Caset gjelder PowerHorse og månedlig traktorsalg.
- Prosjektets mål er å utvikle en faglig forsvarlig prognosemodell som støtter produksjons- og lagerplanlegging.
- Modellsporet er SARIMA-baserte tidsseriemodeller.
- Analysearbeidet er strukturert etter prosjektaktiviteter, ikke bare etter kodefiler.
- Rapporten skiller tydelig mellom casebeskrivelse, metode/data, modellering, analyse, resultat, diskusjon og konklusjon.
- Beskrivende historiske figurer hører hjemme i casekapitlet, ikke i analysekapitlet.

## Hva du skal rapportere tilbake etter priming

Gi en kort, skannbar oppsummering på norsk:

### 1. Prosjektoversikt
- Hva prosjektet handler om
- Overordnet struktur

### 2. Nåværende status
- Hva som er fullført
- Hva som er pågående
- Neste kritiske aktivitet

### 3. Arbeidskonsekvenser
- Hvilke filer som mest sannsynlig må berøres for neste oppgave
- Om status/plan må oppdateres
- Eventuelle risikopunkter (encoding, avvik mellom rapport og artefakter, utestående review-tiltak)

## Viktig

- Skriv oppsummeringen på norsk.
- Ikke lat som om noe er verifisert hvis det bare er en antagelse.
- Hvis terminalen viser rare tegn, behandle det som mulig visningsproblem — kontroller filinnholdet direkte før du antar encoding-feil.
- Hvis du endrer prosjektets innhold senere, hold analyse, rapport og plan/status i sync.
