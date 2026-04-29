# Polina et al. (2024)

## Full APA7-referanse

Polina, P., Ganesan, S., Karunarathne, L., & Somasiri, N. (2024). Time series analysis for tractor sales using SARIMAX and deep learning models. *International Journal of Computer Communication and Informatics*, *6*(1), 27–57. https://doi.org/10.34256/ijcci2413

## Beskrivelse

Et anvendt case-studie fra York St John University som modellerer historisk traktorsalg ved hjelp av SARIMAX (Seasonal ARIMA med eksogene variabler) og en rekke dyplæringsmodeller (GRU, RNN, LSTM, Bidirectional LSTM, CNN-LSTM Encoder-Decoder, CNN). Studien dokumenterer en fullstendig Box-Jenkins-arbeidsflyt med stasjonaritetsvurdering, modellestimering og residualdiagnostikk via Q-Q-plot, residualplott og ACF/PACF-grafer. Resultatene sammenlignes med RMSE som hovedmål.

## Relevante funn

- SARIMAX gir lavere RMSE (0,01) enn alle de testede dyplæringsmodellene.
- Studien gir direkte empirisk støtte for at SARIMA-familien er konkurransedyktig på traktorsalg som domene og månedlig oppløsning som frekvens.
- Diagnostiske verktøy (Q-Q, residualplott, ACF/PACF) er sentrale i modellvalideringen.

## Bruk i rapporten

- Kapittel 2.6: Direkte domeneparallell — traktorsalg modellert med SARIMAX og sammenlignet med ML-metoder.
