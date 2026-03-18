from __future__ import annotations

from pathlib import Path
import warnings

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA


BASE_DIR = Path(__file__).resolve().parent
ACTIVITY_DIR = BASE_DIR.parent
ANALYSIS_DIR = BASE_DIR.parents[2]
DATA_DIR = ANALYSIS_DIR.parent / "004 data"
DATA_PATH = DATA_DIR / "sales_train.csv"
FIGURES_DIR = ACTIVITY_DIR / "figurer"
RESULTS_DIR = ACTIVITY_DIR / "resultat"

# Valgt spesifikasjon fra kandidatsøk (script 03)
ORDER = (0, 1, 1)
SEASONAL_ORDER = (0, 1, 1, 12)
MODEL_LABEL = "SARIMA(0,1,1)(0,1,1)_12"


def ensure_output_dirs() -> None:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def load_train_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)
    df["Month"] = pd.to_datetime(df["Month"])
    df = df.sort_values("Month").reset_index(drop=True)
    df = df.set_index("Month")
    return df


def save_table_outputs(df: pd.DataFrame, stem: str) -> None:
    csv_path = RESULTS_DIR / f"{stem}.csv"
    md_path = RESULTS_DIR / f"{stem}.md"
    df.to_csv(csv_path, index=False, encoding="utf-8")
    md_path.write_text(df.to_markdown(index=False), encoding="utf-8")


def fit_model(df: pd.DataFrame):
    sales = df["Sales"].astype(float)
    log_sales = pd.Series(np.log(sales), index=sales.index)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        model = ARIMA(log_sales, order=ORDER, seasonal_order=SEASONAL_ORDER)
        result = model.fit()

    return result


def build_parameter_table(result) -> pd.DataFrame:
    params = result.params
    bse = result.bse
    zvalues = result.zvalues
    pvalues = result.pvalues
    conf_int = result.conf_int()

    rows: list[dict[str, object]] = []
    for name in params.index:
        rows.append(
            {
                "parameter": name,
                "koeffisient": round(params[name], 6),
                "standardfeil": round(bse[name], 6),
                "z_verdi": round(zvalues[name], 4),
                "p_verdi": round(pvalues[name], 6),
                "ki_nedre_95": round(conf_int.loc[name].iloc[0], 6),
                "ki_ovre_95": round(conf_int.loc[name].iloc[1], 6),
            }
        )

    return pd.DataFrame(rows)


def plot_diagnostics(result) -> None:
    fig = result.plot_diagnostics(figsize=(14, 10))
    fig.suptitle(f"Residualdiagnostikk for {MODEL_LABEL}", fontsize=13, y=1.01)
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "fig_03_diagnostikk.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    ensure_output_dirs()
    df = load_train_data()

    print(f"Tilpasser {MODEL_LABEL} på log-transformert treningsserie...")
    result = fit_model(df)

    print("\n--- Modellsammendrag ---")
    print(result.summary())

    param_df = build_parameter_table(result)
    save_table_outputs(param_df, "tab_05_modellparametere")
    print(f"\nLagret parametertabell: {RESULTS_DIR / 'tab_05_modellparametere.csv'}")

    plot_diagnostics(result)
    print(f"Lagret diagnostikkfigur: {FIGURES_DIR / 'fig_03_diagnostikk.png'}")

    print(f"\nAIC: {result.aic:.2f}")
    print(f"BIC: {result.bic:.2f}")
    print(f"Log-likelihood: {result.llf:.2f}")


if __name__ == "__main__":
    main()
