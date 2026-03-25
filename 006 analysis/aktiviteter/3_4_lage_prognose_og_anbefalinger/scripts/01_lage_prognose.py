from __future__ import annotations

from pathlib import Path
import warnings

import matplotlib

matplotlib.use("Agg")

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA


BASE_DIR = Path(__file__).resolve().parent
ACTIVITY_DIR = BASE_DIR.parent
ANALYSIS_DIR = BASE_DIR.parents[2]
DATA_DIR = ANALYSIS_DIR.parent / "004 data"
DATA_PATH = DATA_DIR / "sales.csv"
FIGURES_DIR = ACTIVITY_DIR / "figurer"
RESULTS_DIR = ACTIVITY_DIR / "resultat"

ORDER = (0, 1, 1)
SEASONAL_ORDER = (0, 1, 1, 12)
MODEL_LABEL = "SARIMA(0,1,1)(0,1,1)_12"
FORECAST_STEPS = 12
FORECAST_START = "1981-07"


def ensure_output_dirs() -> None:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def load_full_data() -> pd.DataFrame:
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


def build_forecast_table(
    forecast_log: pd.Series,
    ci_log: pd.DataFrame,
    sigma2: float,
    forecast_index: pd.DatetimeIndex,
) -> pd.DataFrame:
    punkt = np.exp(forecast_log.to_numpy())
    ki_nedre = np.exp(ci_log.iloc[:, 0].to_numpy())
    ki_ovre = np.exp(ci_log.iloc[:, 1].to_numpy())
    biaskorrigert = np.exp(forecast_log.to_numpy() + sigma2 / 2)

    return pd.DataFrame(
        {
            "maaned": forecast_index.strftime("%Y-%m"),
            "punktprognose": np.round(punkt, 0).astype(int),
            "ki_nedre_95": np.round(ki_nedre, 0).astype(int),
            "ki_ovre_95": np.round(ki_ovre, 0).astype(int),
            "prognose_biaskorrigert": np.round(biaskorrigert, 0).astype(int),
        }
    )


def save_forecast_figure(
    df: pd.DataFrame,
    forecast_index: pd.DatetimeIndex,
    punkt: np.ndarray,
    ki_nedre: np.ndarray,
    ki_ovre: np.ndarray,
) -> None:
    hist_start = pd.Timestamp("1978-01-01")
    hist = df.loc[hist_start:]
    origin = df.index[-1]

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(
        hist.index, hist["Sales"].values,
        color="#0b6e4f", linewidth=2.0, label="Historisk salg",
    )
    ax.plot(
        forecast_index, punkt,
        color="#c75100", linewidth=2.0, linestyle="--", label="Prognose",
    )
    ax.fill_between(
        forecast_index, ki_nedre, ki_ovre,
        color="#c75100", alpha=0.15, label="95 % prediksjonsintervall",
    )
    ax.axvline(origin, color="gray", linewidth=1.0, linestyle="--", alpha=0.6)

    ax.set_title("12-måneders prognose for SARIMA(0,1,1)(0,1,1)₁₂")
    ax.set_xlabel("Måned")
    ax.set_ylabel("Salg")
    ax.legend()
    ax.grid(alpha=0.25)

    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    fig.autofmt_xdate()
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "fig_01_prognose_12_maaneder.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    ensure_output_dirs()
    df = load_full_data()
    print(f"Lastet {len(df)} observasjoner ({df.index[0].strftime('%Y-%m')} til {df.index[-1].strftime('%Y-%m')})")

    print(f"\nRefitter {MODEL_LABEL} på hele datasettet...")
    result = fit_model(df)

    print("\n--- Modellsammendrag ---")
    print(result.summary())

    param_df = build_parameter_table(result)
    save_table_outputs(param_df, "tab_01_modellparametere_refittet")
    print(f"\nLagret parametertabell: {RESULTS_DIR / 'tab_01_modellparametere_refittet.csv'}")

    forecast_obj = result.get_forecast(steps=FORECAST_STEPS)
    forecast_log = forecast_obj.predicted_mean
    ci_log = forecast_obj.conf_int(alpha=0.05)
    sigma2 = float(result.params["sigma2"])

    forecast_index = pd.date_range(start=FORECAST_START, periods=FORECAST_STEPS, freq="MS")

    forecast_df = build_forecast_table(forecast_log, ci_log, sigma2, forecast_index)
    save_table_outputs(forecast_df, "tab_02_prognose_12_maaneder")
    print(f"Lagret prognosetabell: {RESULTS_DIR / 'tab_02_prognose_12_maaneder.csv'}")

    punkt = forecast_df["punktprognose"].to_numpy().astype(float)
    ki_nedre = forecast_df["ki_nedre_95"].to_numpy().astype(float)
    ki_ovre = forecast_df["ki_ovre_95"].to_numpy().astype(float)
    save_forecast_figure(df, forecast_index, punkt, ki_nedre, ki_ovre)
    print(f"Lagret prognosefigur: {FIGURES_DIR / 'fig_01_prognose_12_maaneder.png'}")

    print(f"\nAIC: {result.aic:.2f}")
    print(f"BIC: {result.bic:.2f}")
    print(f"Sigma2: {sigma2:.6f}")
    print(f"Biaskorreksjonsfaktor exp(sigma2/2): {np.exp(sigma2/2):.4f}")


if __name__ == "__main__":
    main()
