# 3.2 Velge og estimere modell

Denne mappen dekker modellvalg og estimering i aktivitet 3.2.

## Arbeidsflyt

1. **01_vurdere_modelltype.py** – Evaluerer åtte egenskaper ved treningsdatasettet og konkluderer med at SARIMA er en passende modellklasse.
2. **02_vurdere_stasjonaritet_og_differensiering.py** – Tester fire differensieringsvarianter med ADF og KPSS på log-transformert serie. Produserer `fig_01_serievarianter.png`.
3. **03_velge_sarima_ordener.py** – Beregner ACF/PACF og gjennomfører grid search over 36 SARIMA-kandidater med faste $d=1, D=1$. Produserer `fig_02_acf_pacf.png`.
4. **04_estimere_modell.py** – Estimerer den valgte modellen med MLE og genererer diagnostikkfigur `fig_03_diagnostikk.png`.

## Nøkkelresultat

Valgt modell: **SARIMA(0,1,1)(0,1,1)₁₂** med AIC = -202.83 og BIC = -193.70.

## Viktige artefakter

- `figurer/fig_01_serievarianter.png` – Log-transformerte serievarianter (tabell 7.1 i rapporten)
- `figurer/fig_02_acf_pacf.png` – ACF og PACF for differensiert log-serie
- `figurer/fig_03_diagnostikk.png` – Residualdiagnostikk
- `resultat/tab_04_modellkandidater.md` – Topp 10 SARIMA-kandidater rangert etter AIC
- `resultat/tab_05_modellparametere.md` – Estimerte parametere for valgt modell

## Mappestruktur

- `scripts/` – Analyseskript i rekkefølge 01–04
- `figurer/` – Modellvalgfigurer og diagnostikk
- `resultat/` – Parameteroversikter og mellomresultater
