# Jarque og Bera (1987)

## Full APA7-referanse

Jarque, C. M., & Bera, A. K. (1987). A test for normality of observations and regression residuals. *International Statistical Review*, *55*(2), 163–172. https://doi.org/10.2307/1403192

## Beskrivelse

Artikkelen presenterer en test for normalitet basert på utvalgets skjevhet og kurtose. Jarque-Bera-teststatistikken kombinerer avvik fra forventet skjevhet (0) og forventet kurtose (3) for en normalfordeling i én samlet $\chi^2$-statistikk med 2 frihetsgrader. Testen er enkel å beregne og mye brukt som standarddiagnostikk for residualer i regresjons- og tidsseriemodeller.

## Relevante konsepter

- Teststatistikk: $JB = \frac{n}{6}\left(S^2 + \frac{(K-3)^2}{4}\right)$, der $S$ er skjevhet og $K$ er kurtose.
- Under nullhypotesen (normalitet) følger $JB$ tilnærmet $\chi^2(2)$.
- Relevant fordi MLE-basert inferens i SARIMA (konfidensintervaller, p-verdier) forutsetter tilnærmet normalfordelte feilledd.

## Bruk i rapporten

- Kapittel 3.5: Introduksjon av Jarque-Bera-testen som verktøy for å vurdere normalitet i residualene.
