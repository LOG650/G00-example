# Ljung og Box (1978)

## Full APA7-referanse

Ljung, G. M., & Box, G. E. P. (1978). On a measure of lack of fit in time series models. *Biometrika*, *65*(2), 297–303. https://doi.org/10.1093/biomet/65.2.297

## Beskrivelse

Artikkelen presenterer en forbedret portmanteau-test for mangel på tilpasning i tidsseriemodeller, kjent som Ljung-Box-testen. Testen utvider den tidligere Box-Pierce-statistikken med en endelighetskorreksjon som gir bedre tilnærming til $\chi^2$-fordelingen i små og moderate utvalg. Testen brukes som standard diagnostikkverktøy for å avgjøre om residualene fra en estimert ARIMA-modell oppfører seg som hvitt støy.

## Relevante konsepter

- Teststatistikk: $Q = n(n+2)\sum_{k=1}^{m}\frac{\hat{\rho}_k^2}{n-k}$, der $\hat{\rho}_k$ er residualautokorrelasjon ved lag $k$.
- Under nullhypotesen (ingen autokorrelasjon) følger $Q$ tilnærmet $\chi^2(m - p - q)$, der $p$ og $q$ er antall estimerte AR- og MA-parametere.
- For sesongmodeller er det vanlig å teste ved sesonglagene (f.eks. lag 12 og 24).

## Bruk i rapporten

- Kapittel 3.5: Introduksjon av Ljung-Box-testen som verktøy for residualdiagnostikk.
