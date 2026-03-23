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
MODEL_PARAMS = [-0.8217, -0.5998, 0.0146]


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


def build_filtered_result(train_sales: pd.Series):
    log_train = np.log(train_sales)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        model = ARIMA(log_train, order=ORDER, seasonal_order=SEASONAL_ORDER)
        result = model.filter(MODEL_PARAMS)
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


def save_test_forecast_figure(test_sales: pd.Series, forecast_sales: pd.Series) -> None:
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
    train_sales = load_series(TRAIN_PATH)
    test_sales = load_series(TEST_PATH)

    result = build_filtered_result(train_sales)
    forecast_log = result.get_forecast(steps=len(test_sales)).predicted_mean
    forecast_sales = pd.Series(np.exp(forecast_log), index=test_sales.index, name="Forecast")

    forecast_df = build_forecast_table(test_sales, forecast_sales)
    metrics_df = build_error_metrics_table(test_sales, forecast_sales)

    save_table_outputs(forecast_df, "tab_02_testsettprognose")
    save_table_outputs(metrics_df, "tab_03_feilmaal")
    save_test_forecast_figure(test_sales, forecast_sales)

    print(f"Kjorte testsettvalidering for {MODEL_LABEL}")
    print(metrics_df.to_markdown(index=False))


if __name__ == "__main__":
    main()
