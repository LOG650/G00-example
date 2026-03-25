# 3.4 Lage prognose og anbefalinger

Denne mappen dekker prognosearbeid og beslutningsstøtte i aktivitet 3.4.

## Arbeidsflyt

1. **01_lage_prognose.py** — Refitter SARIMA(0,1,1)(0,1,1)_12 på hele datasettet (210 obs, 1964-01 til 1981-06) og genererer 12-måneders prognose (1981-07 til 1982-06) med 95 % prediksjonsintervall og biaskorrigert kolonne.
2. **02_oppsummere_anbefalinger.py** — Bygger prognoseoppsummering og kapasitetsplanleggingstabell med sesongkategorisering.

## Nøkkelfunn

- Refittede parametere er stabile: $\theta_1 = -0.82$, $\Theta_1 = -0.62$, $\hat{\sigma}^2 = 0.012$.
- Toppmåned: desember 1981 (19 483), bunnmåned: august 1981 (2 694).
- Totalt prognosesalg 12 mnd: 100 413.
- Gjennomsnittlig PI-bredde (95 %): ca. 3 800.
- Biaskorreksjon marginal (~0,6 %), ikke brukt som hovedprognose.

## Artefakter

| # | Fil | Type |
|---|-----|------|
| 1 | `scripts/01_lage_prognose.py` | Skript |
| 2 | `scripts/02_oppsummere_anbefalinger.py` | Skript |
| 3 | `figurer/fig_01_prognose_12_maaneder.png` | Figur |
| 4 | `resultat/tab_01_modellparametere_refittet.csv` + `.md` | Tabell |
| 5 | `resultat/tab_02_prognose_12_maaneder.csv` + `.md` | Tabell |
| 6 | `resultat/tab_03_prognoseoppsummering.csv` + `.md` | Tabell |
| 7 | `resultat/tab_04_kapasitetsplanlegging.csv` + `.md` | Tabell |

- `scripts/`: generering av prognoser og usikkerhetsvurderinger
- `figurer/`: prognosefigurer og beslutningsstøtte
- `resultat/`: punktprognoser, intervaller og anbefalingstabeller
