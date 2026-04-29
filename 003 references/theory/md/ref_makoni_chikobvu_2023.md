# Makoni og Chikobvu (2023)

## Full APA7-referanse

Makoni, T., & Chikobvu, D. (2023). Assessing and forecasting the long-term impact of the global financial crisis on new car sales in South Africa. *Data*, *8*(5), 78. https://doi.org/10.3390/data8050078

## Beskrivelse

Et anvendt case-studie som modellerer månedlig nybilsalg i Sør-Afrika med Box-Jenkins-metodikken. Forfatterne bruker historiske månedlige salgsdata fra 1998 til 2017 og følger en fullstendig modellutvelgelsesprosedyre med differensiering, ACF/PACF-analyse, AIC- og BIC-rangering, og prognoseevaluering med RMSE og MAPE. Sluttspesifikasjonen er SARIMA(0,1,1)(0,0,2)$_{12}$, som er nær beslektet med flypassasjermodellen og strukturell sammenlignbar med modeller for andre månedlige sesongserier.

## Relevante funn

- Best modell: SARIMA(0,1,1)(0,0,2)$_{12}$, valgt med AIC og BIC.
- Evaluering: RMSE og MAPE på out-of-sample-prognoser.
- Studien er metodisk svært nær arbeidsflyten i denne rapporten: månedlig sesongserie, Box-Jenkins-prosedyre, samme klasse modellspesifikasjon og samme sett feilmål.
- Trendprognose viser oppadgående utvikling for nybilsalg etter finanskrisen, men under nivåene før krisen.

## Bruk i rapporten

- Kapittel 2.6: Direkte metodisk parallell — månedlig sesongserie modellert med Box-Jenkins-rammeverket og en SARIMA-spesifikasjon i samme klasse som vår.
