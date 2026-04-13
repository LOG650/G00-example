from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
ACTIVITY_DIR = BASE_DIR.parent
ANALYSIS_DIR = BASE_DIR.parents[2]
DATA_DIR = ANALYSIS_DIR.parent / "004 data"
DATA_PATH = DATA_DIR / "sales.csv"
FIGURES_DIR = ACTIVITY_DIR / "figurer"
RESULTS_DIR = ACTIVITY_DIR / "resultat"
FORECAST_PATH = RESULTS_DIR / "tab_02_prognose_12_maaneder.csv"


def load_historical() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)
    df["Month"] = pd.to_datetime(df["Month"])
    df = df.sort_values("Month").reset_index(drop=True)
    df = df.set_index("Month")
    return df


def load_forecast() -> pd.DataFrame:
    df = pd.read_csv(FORECAST_PATH)
    df["maaned"] = pd.to_datetime(df["maaned"])
    df = df.set_index("maaned")
    return df


def main() -> None:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    hist = load_historical()
    fc = load_forecast()

    origin = hist.index[-1]
    fc_index = fc.index

    fig, ax = plt.subplots(figsize=(14, 6))

    ax.plot(
        hist.index, hist["Sales"].values,
        color="#0b6e4f", linewidth=1.2, label="Historisk salg",
    )
    ax.plot(
        fc_index, fc["punktprognose"].values,
        color="#c75100", linewidth=2.0, linestyle="--", label="Prognose",
    )
    ax.fill_between(
        fc_index,
        fc["ki_nedre_95"].values,
        fc["ki_ovre_95"].values,
        color="#c75100", alpha=0.15, label="95 % prediksjonsintervall",
    )
    ax.axvline(origin, color="gray", linewidth=1.0, linestyle="--", alpha=0.6)

    ax.set_title("Historisk salg og 12-måneders prognose for SARIMA(0,1,1)(0,1,1)₁₂")
    ax.set_xlabel("Måned")
    ax.set_ylabel("Salg (antall traktorer)")
    ax.legend(loc="upper left")
    ax.grid(alpha=0.25)

    ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    fig.autofmt_xdate()
    fig.tight_layout()

    out_path = FIGURES_DIR / "fig_02_helhetsfigur.png"
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Lagret helhetsfigur: {out_path}")


if __name__ == "__main__":
    main()
