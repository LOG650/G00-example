# Repo-verifisert avviksanalyse per 2026-03-23

## Formål

Dette notatet dokumenterer forskjellen mellom faktisk utført arbeid i arbeidskopien og det som fortsatt gjenstår i prosjektet etter at planmappen er synkronisert mot git-historikken per 2026-03-23. Notatet skiller mellom baseline i planfilene og faktisk fremdrift i repoet.

## Hovedkonklusjon

Prosjektet er fortsatt operativt på plan i fase 3. Dokumentasjonsfeilen om at `ACT-3.3` manglet egne artefakter er nå lukket, mens de reelle gjenværende avvikene gjelder testsettvalidering, dokumentasjonsgap i rapporten og manglende review for `ACT-3.2`.

## Hva som er verifisert som utført

### ACT-3.1 Rense og strukturere data

- Én scriptfil, fire figurer og fire resultatfiler finnes i aktivitetsmappen.
- Eget reviewspor finnes i `reviews/3_1_rense_og_strukturere_data-CLAUDE.md`.
- Rapporten dokumenterer casefigurer, sesongtabell, datagrunnlag og datasplitt.

### ACT-3.2 Velge og estimere modell

- Fire scripts, tre figurer og ti resultatfiler finnes i aktivitetsmappen.
- Rapporten har utfylt analysekapittel for stasjonaritet, ACF/PACF, modellvalg og parameterestimering.
- Valgt modell er SARIMA$(0,1,1)(0,1,1)_{12}$, og parameterne er dokumentert som signifikante.

### ACT-3.3 Validere modell

- Én scriptfil og to resultatfiler finnes i aktivitetsmappen.
- Rapportens kapittel 7.4 dokumenterer residualdiagnostikk, Ljung-Box ved lag 12 og 24, samt ARCH-LM.
- Aktiviteten er derfor faglig startet og har egne artefakter, men testsettvalidering og feilmål er ikke gjennomført ennå.

## Gjenværende avvik mot styringsgrunnlaget

### Plan og milepæler

- `MS-004` står fortsatt med baseline-dato `2026-03-11` i planfilene, mens arbeidskopien viser faktisk oppnåelse `2026-03-16`.
- `ACT-3.2` er faglig fullført, men mangler fortsatt gjennomført review og kan derfor ikke lukkes formelt.

### Rapport

- Seksjon 1.1 `Problemstilling` er fortsatt tom i `rapport.md`.
- Seksjon 1.3 `Avgrensinger` og 1.4 `Antagelser` er fortsatt tomme i `rapport.md`.
- Kapittel 2, 3 og 9-12 er fortsatt tomme.
- Kapittel 8 er bare strukturert og mangler testsettresultater og prognosearbeid.

### Modellvalidering

- `ACT-3.3` mangler fortsatt prognoser mot testdatasettet for perioden 1978-01 til 1981-06.
- Feilmålene MAE, RMSE og MAPE er ikke dokumentert.
- Det finnes foreløpig ingen egne figurer for testsettvalidering i aktivitetsmappen.

## Risikovurdering

1. Residualdiagnostikken viser avvik fra normalfordeling, residualautokorrelasjon ved lag 12 og 24 og tydelig heteroskedastisitet. Dette er fortsatt den viktigste faglige risikoen inn i resten av `ACT-3.3`.
2. Dokumentasjonsgap i rapporten gir risiko for svak sporbarhet mellom problemstilling, teori, metode, resultat og diskusjon.
3. Manglende review for `ACT-3.2` gir svakere administrativ sporbarhet enn for `ACT-3.1`.

## Kildegrunnlag

- `005 report/rapport.md`
- `011 fase 1 - proposal/proposal.md`
- `012 fase 2 - plan/project-plan.md`
- `012 fase 2 - plan/status.md`
- `012 fase 2 - plan/core.json`
- `012 fase 2 - plan/requirements.json`
- `012 fase 2 - plan/risk.json`
- `012 fase 2 - plan/schedule.json`
- `012 fase 2 - plan/wbs.json`
- `012 fase 2 - plan/reviews/3_1_rense_og_strukturere_data-CLAUDE.md`
- `006 analysis/aktiviteter/3_1_rense_og_strukturere_data/`
- `006 analysis/aktiviteter/3_2_velge_og_estimere_modell/`
- `006 analysis/aktiviteter/3_3_validere_modell/`
- `006 analysis/aktiviteter/3_4_lage_prognose_og_anbefalinger/`

## Merknad om tegnsett

PowerShell-visning kan fortsatt vise enkelte norske tegn feil. Innholdskontroll i arbeidskopien og git-historikken viser likevel at de oppdaterte Markdown-filene er konsistente og ikke fremstår som filkorrupte.
