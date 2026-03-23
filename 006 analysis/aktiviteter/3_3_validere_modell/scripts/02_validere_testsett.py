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
TRAIN_PATH = DATA_DIR / "sales_train.csv"
TEST_PATH = DATA_DIR / "sales_test.csv"
FIGURES_DIR = ACTIVITY_DIR / "figurer"
RESULTS_DIR = ACTIVITY_DIR / "resultat"

ORDER = (0, 1, 1)
SEASONAL_ORDER = (0, 1, 1, 12)
MODEL_LABEL = "SARIMA(0,1,1)(0,1,1)_12"
PARAMS_PATH = (
    ACTIVITY_DIR.parent
    / "3_2_velge_og_estimere_modell"
    / "resultat"
    / "tab_05_modellparametere.csv"
)


def load_model_params() -> list[float]:
    df = pd.read_csv(PARAMS_PATH)
    params = df.set_index("parameter")["koeffisient"]
    return [float(params["ma.L1"]), float(params["ma.S.L12"]), float(params["sigma2"])]


def ensure_output_dirs() -> None:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def load_series(path: Path) -> pd.Series:
    df = pd.read_csv(path)
    df["Month"] = pd.to_datetime(df["Month"])
    df = df.sort_values("Month").reset_index(drop=True)
    return pd.Series(df["Sales"].astype(float).to_numpy(), index=df["Month"], name="Sales")


def save_table_outputs(df: pd.DataFrame, stem: str) -> None:
    csv_path = RESULTS_DIR / f"{stem}.csv"
    md_path = RESULTS_DIR / f"{stem}.md"
    df.to_csv(csv_path, index=False, encoding="utf-8")
    md_path.write_text(df.to_markdown(index=False), encoding="utf-8")


def build_filtered_result(train_sales: pd.Series, model_params: list[float]):
    log_train = np.log(train_sales)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        model = ARIMA(log_train, order=ORDER, seasonal_order=SEASONAL_ORDER)
        result = model.filter(model_params)
    return result


def build_forecast_table(test_sales: pd.Series, forecast_sales: pd.Series) -> pd.DataFrame:
    errors = forecast_sales - test_sales
    abs_errors = errors.abs()
    abs_pct_errors = abs_errors / test_sales * 100

    return pd.DataFrame(
        {
            "maaned": test_sales.index.strftime("%Y-%m"),
            "observert_salg": np.round(test_sales.to_numpy(), 2),
            "prognose_salg": np.round(forecast_sales.to_numpy(), 2),
            "prognosefeil": np.round(errors.to_numpy(), 2),
            "absolutt_feil": np.round(abs_errors.to_numpy(), 2),
            "absolutt_prosentfeil": np.round(abs_pct_errors.to_numpy(), 2),
        }
    )


def build_error_metrics_table(test_sales: pd.Series, forecast_sales: pd.Series) -> pd.DataFrame:
    errors = forecast_sales - test_sales
    abs_errors = errors.abs()
    squared_errors = errors.pow(2)
    abs_pct_errors = abs_errors / test_sales * 100

    rows = [
        {
            "modell": MODEL_LABEL,
            "testperiode": "1978-01 til 1981-06",
            "antall_observasjoner": int(len(test_sales)),
            "mae": round(float(abs_errors.mean()), 2),
            "rmse": round(float(np.sqrt(squared_errors.mean())), 2),
            "mape_prosent": round(float(abs_pct_errors.mean()), 2),
        }
    ]
    return pd.DataFrame(rows)


def save_test_forecast_figure(
    test_sales: pd.Series,
    forecast_sales: pd.Series,
    ci_lower: pd.Series,
    ci_upper: pd.Series,
) -> None:
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(test_sales.index, test_sales.values, color="#0b6e4f", linewidth=2.0, label="Observert testdata")
    ax.plot(
        forecast_sales.index,
        forecast_sales.values,
        color="#c75100",
        linewidth=2.0,
        linestyle="--",
        label="Prognose for testperiode",
    )
    ax.fill_between(
        forecast_sales.index,
        ci_lower.values,
        ci_upper.values,
        color="#c75100",
        alpha=0.15,
        label="95 % prediksjonsintervall",
    )

    ax.set_title("Testsettvalidering for SARIMA(0,1,1)(0,1,1)12")
    ax.set_xlabel("Måned")
    ax.set_ylabel("Salg")
    ax.legend()
    ax.grid(alpha=0.25)

    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    fig.autofmt_xdate()
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "fig_01_testsettprognose.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    ensure_output_dirs()
    model_params = load_model_params()
    train_sales = load_series(TRAIN_PATH)
    test_sales = load_series(TEST_PATH)

    result = build_filtered_result(train_sales, model_params)
    forecast_obj = result.get_forecast(steps=len(test_sales))
    forecast_log = forecast_obj.predicted_mean
    forecast_sales = pd.Series(np.exp(forecast_log), index=test_sales.index, name="Forecast")

    ci_log = forecast_obj.conf_int(alpha=0.05)
    ci_lower = pd.Series(np.exp(ci_log.iloc[:, 0]), index=test_sales.index)
    ci_upper = pd.Series(np.exp(ci_log.iloc[:, 1]), index=test_sales.index)

    forecast_df = build_forecast_table(test_sales, forecast_sales)
    metrics_df = build_error_metrics_table(test_sales, forecast_sales)

    save_table_outputs(forecast_df, "tab_02_testsettprognose")
    save_table_outputs(metrics_df, "tab_03_feilmaal")
    save_test_forecast_figure(test_sales, forecast_sales, ci_lower, ci_upper)

    print(f"Kjorte testsettvalidering for {MODEL_LABEL}")
    print(metrics_df.to_markdown(index=False))


if __name__ == "__main__":
    main()
