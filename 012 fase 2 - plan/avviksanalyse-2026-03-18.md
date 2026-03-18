# Repo-verifisert avviksanalyse per 2026-03-18

## Formål

Dette notatet dokumenterer forskjellen mellom faktisk utført arbeid i arbeidskopien og status slik den fortsatt fremstår i deler av styringsgrunnlaget. Analysen er skrevet for å gjøre statusvurderingen beslutningsklar uten å blande sammen baseline og faktisk fremdrift.

## Hovedkonklusjon

Prosjektet er operativt på plan. Aktivitet 3.2 er faglig ferdig i arbeidskopien, og planfilene er nå oppdatert slik at 3.1 og 3.2 står som fullført. Det viktigste gjenværende avviket gjelder sporbarhet rundt faktisk milepælsoppnåelse og review.

## Hva som er verifisert som utført

### Aktivitet 3.1 Rense og strukturere data

- Én scriptfil, fire figurer og fire resultatfiler finnes i aktivitetsmappen.
- Eget reviewspor finnes i `reviews/3_1_rense_og_strukturere_data-CLAUDE.md`.
- Rapporten dokumenterer casefigurer, sesongtabell, datagrunnlag og datasplitt.

### Aktivitet 3.2 Velge og estimere modell

- Fire scripts finnes i aktivitetsmappen.
- Tre figurer finnes i aktivitetsmappen.
- Ti resultatfiler finnes i aktivitetsmappen.
- Rapporten har utfylt analysekapittel for stasjonaritet, ACF/PACF, modellvalg og parameterestimering.
- Valgt modell er SARIMA$(0,1,1)(0,1,1)_{12}$, og parameterne er dokumentert som signifikante.

### Aktivitet 3.3 og 3.4

- Begge aktivitetene har opprettet mapper og README-filer.
- Det finnes ingen scripts, figurer eller resultatfiler i disse aktivitetene per 2026-03-18.

## Avvik mot styringsgrunnlaget

### Planfiler

- `schedule.json` og `wbs.json` er oppdatert slik at aktivitet 3.1 og 3.2 står som fullført.
- MS-004 ligger fortsatt med baseline-dato 2026-03-11 i planfilene, selv om faktisk oppnåelse i arbeidskopien vurderes til 2026-03-16.

### Rapport

- Seksjon 1.1 `Problemstilling` er tom i `rapport.md`.
- Seksjon 1.3 `Avgrensinger` og 1.4 `Antagelser` er tomme i `rapport.md`.
- Kapittel 2, 3 og 8-12 er fortsatt tomme.
- Dette er et dokumentasjonsgap, ikke et fullstendig styringsgap: problemstillingen finnes formulert i proposalen.

### Review og administrativ lukking

- Aktivitet 3.1 har dokumentert reviewspor.
- Aktivitet 3.2 har ikke tilsvarende reviewdokument i `012 fase 2 - plan/reviews/`.
- 3.2 kan derfor vurderes som faglig fullført, men ikke fullt administrativt lukket i samme grad som 3.1.

## Risikovurdering

1. Residualdiagnostikken i rapportens analysekapittel viser avvik fra normalfordeling og tegn til heteroskedastisitet. Dette er den viktigste faglige risikoen inn i aktivitet 3.3.
2. Tomme rapportseksjoner gir risiko for svak sporbarhet mellom problemstilling, teori, metode og resultater hvis de fylles sent.
3. Fravær av eget reviewspor for 3.2 gir svakere administrativ sporbarhet enn for 3.1.

## Kildegrunnlag

- `005 report/rapport.md`
- `011 fase 1 - proposal/proposal.md`
- `012 fase 2 - plan/project-plan.md`
- `012 fase 2 - plan/status.md`
- `012 fase 2 - plan/schedule.json`
- `012 fase 2 - plan/wbs.json`
- `012 fase 2 - plan/reviews/3_1_rense_og_strukturere_data-CLAUDE.md`
- `006 analysis/aktiviteter/3_1_rense_og_strukturere_data/`
- `006 analysis/aktiviteter/3_2_velge_og_estimere_modell/`
- `006 analysis/aktiviteter/3_3_validere_modell/`
- `006 analysis/aktiviteter/3_4_lage_prognose_og_anbefalinger/`

## Merknad om tegnsett

PowerShell-visning har enkelte steder vist mojibake for norske tegn. Innholdskontroll i arbeidskopien og git diff viser likevel at de oppdaterte Markdown-filene inneholder korrekt norsk tekst og ikke fremstår som filkorrupte.
