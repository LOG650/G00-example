from __future__ import annotations

from pathlib import Path
import warnings

import numpy as np
import pandas as pd
from statsmodels.stats.diagnostic import acorr_ljungbox, het_arch
from statsmodels.tsa.arima.model import ARIMA


BASE_DIR = Path(__file__).resolve().parent
ACTIVITY_DIR = BASE_DIR.parent
ANALYSIS_DIR = BASE_DIR.parents[2]
DATA_DIR = ANALYSIS_DIR.parent / "004 data"
DATA_PATH = DATA_DIR / "sales_train.csv"
RESULTS_DIR = ACTIVITY_DIR / "resultat"

ORDER = (0, 1, 1)
SEASONAL_ORDER = (0, 1, 1, 12)
MODEL_LABEL = "SARIMA(0,1,1)(0,1,1)_12"
LJUNG_BOX_LAGS = [12, 24]
ARCH_LAGS = 12
SIGNIFICANCE_LEVEL = 0.05


def ensure_output_dirs() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def load_train_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)
    df["Month"] = pd.to_datetime(df["Month"])
    df = df.sort_values("Month").reset_index(drop=True)
    df = df.set_index("Month")
    return df


def fit_model(df: pd.DataFrame):
    sales = df["Sales"].astype(float)
    log_sales = pd.Series(np.log(sales), index=sales.index)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        model = ARIMA(log_sales, order=ORDER, seasonal_order=SEASONAL_ORDER)
        result = model.fit()

    return result


def classify_p_value(p_value: float, null_hypothesis: str) -> str:
    if p_value < SIGNIFICANCE_LEVEL:
        return f"Forkast nullhypotesen ({null_hypothesis}) ved 5 % nivaa."
    return f"Kan ikke forkaste nullhypotesen ({null_hypothesis}) ved 5 % nivaa."


def run_residual_tests(result) -> pd.DataFrame:
    residuals = pd.Series(result.resid).dropna()

    ljung_box = acorr_ljungbox(
        residuals,
        lags=LJUNG_BOX_LAGS,
        model_df=2,
        return_df=True,
    )

    rows: list[dict[str, object]] = []
    for lag in LJUNG_BOX_LAGS:
        lb_row = ljung_box.loc[lag]
        rows.append(
            {
                "test": "Ljung-Box",
                "lag": lag,
                "statistikk": round(float(lb_row["lb_stat"]), 4),
                "p_verdi": round(float(lb_row["lb_pvalue"]), 6),
                "sekundaer_statistikk": "",
                "sekundaer_p_verdi": "",
                "tolkning": classify_p_value(
                    float(lb_row["lb_pvalue"]),
                    "ingen residualautokorrelasjon ved valgt lag",
                ),
            }
        )

    lm_stat, lm_pvalue, f_stat, f_pvalue = het_arch(residuals, nlags=ARCH_LAGS)
    rows.append(
        {
            "test": "ARCH-LM",
            "lag": ARCH_LAGS,
            "statistikk": round(float(lm_stat), 4),
            "p_verdi": round(float(lm_pvalue), 6),
            "sekundaer_statistikk": round(float(f_stat), 4),
            "sekundaer_p_verdi": round(float(f_pvalue), 6),
            "tolkning": classify_p_value(
                float(lm_pvalue),
                "homoskedastisitet / ingen ARCH-effekt",
            ),
        }
    )

    return pd.DataFrame(rows)


def save_table_outputs(df: pd.DataFrame, stem: str) -> None:
    csv_path = RESULTS_DIR / f"{stem}.csv"
    md_path = RESULTS_DIR / f"{stem}.md"
    df.to_csv(csv_path, index=False, encoding="utf-8")
    md_path.write_text(df.to_markdown(index=False), encoding="utf-8")


def main() -> None:
    ensure_output_dirs()
    df = load_train_data()
    result = fit_model(df)

    tests_df = run_residual_tests(result)
    save_table_outputs(tests_df, "tab_01_residualtester")

    print(f"Kjorte residualtester for {MODEL_LABEL}")
    print(tests_df.to_markdown(index=False))


if __name__ == "__main__":
    main()
