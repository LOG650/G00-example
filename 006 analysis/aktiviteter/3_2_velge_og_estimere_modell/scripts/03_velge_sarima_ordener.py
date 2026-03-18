from __future__ import annotations

from pathlib import Path
import warnings

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA


BASE_DIR = Path(__file__).resolve().parent
ACTIVITY_DIR = BASE_DIR.parent
ANALYSIS_DIR = BASE_DIR.parents[2]
DATA_DIR = ANALYSIS_DIR.parent / "004 data"
DATA_PATH = DATA_DIR / "sales_train.csv"
FIGURES_DIR = ACTIVITY_DIR / "figurer"
RESULTS_DIR = ACTIVITY_DIR / "resultat"


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


def compute_differenced_log_series(df: pd.DataFrame) -> pd.Series:
    sales = df["Sales"].astype(float)
    log_sales = pd.Series(np.log(sales), index=sales.index)
    w_t = log_sales.diff(12).diff().dropna()
    return w_t


def plot_acf_pacf(w_t: pd.Series) -> None:
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))

    plot_acf(w_t, lags=36, ax=axes[0], alpha=0.05)
    axes[0].set_title("ACF for $(1-B)(1-B^{12})\\log(y_t)$")
    axes[0].set_xlabel("Lag")
    axes[0].set_ylabel("Autokorrelasjon")

    plot_pacf(w_t, lags=36, ax=axes[1], alpha=0.05, method="ywm")
    axes[1].set_title("PACF for $(1-B)(1-B^{12})\\log(y_t)$")
    axes[1].set_xlabel("Lag")
    axes[1].set_ylabel("Partiell autokorrelasjon")

    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "fig_02_acf_pacf.png", dpi=300)
    plt.close(fig)


def run_candidate_search(df: pd.DataFrame) -> pd.DataFrame:
    sales = df["Sales"].astype(float)
    log_sales = pd.Series(np.log(sales), index=sales.index)

    p_range = [0, 1, 2]
    q_range = [0, 1, 2]
    P_range = [0, 1]
    Q_range = [0, 1]

    rows: list[dict[str, object]] = []

    for p in p_range:
        for q in q_range:
            for P in P_range:
                for Q in Q_range:
                    order = (p, 1, q)
                    seasonal_order = (P, 1, Q, 12)
                    label = f"SARIMA({p},1,{q})({P},1,{Q})_12"

                    try:
                        with warnings.catch_warnings():
                            warnings.simplefilter("ignore")
                            model = ARIMA(
                                log_sales,
                                order=order,
                                seasonal_order=seasonal_order,
                            )
                            result = model.fit()

                        n_params = len(result.params)
                        rows.append(
                            {
                                "modell": label,
                                "p": p,
                                "q": q,
                                "P": P,
                                "Q": Q,
                                "parametere": n_params,
                                "loglik": round(result.llf, 2),
                                "aic": round(result.aic, 2),
                                "bic": round(result.bic, 2),
                                "konvergert": True,
                            }
                        )
                        print(f"  OK  {label:40s} AIC={result.aic:.2f}  BIC={result.bic:.2f}")

                    except Exception as e:
                        rows.append(
                            {
                                "modell": label,
                                "p": p,
                                "q": q,
                                "P": P,
                                "Q": Q,
                                "parametere": None,
                                "loglik": None,
                                "aic": None,
                                "bic": None,
                                "konvergert": False,
                            }
                        )
                        print(f"  FEIL {label:40s} {e}")

    result_df = pd.DataFrame(rows)
    result_df = result_df.sort_values("aic", ascending=True, na_position="last").reset_index(drop=True)
    return result_df


def main() -> None:
    ensure_output_dirs()
    df = load_train_data()

    print("Beregner differensiert log-serie og plotter ACF/PACF...")
    w_t = compute_differenced_log_series(df)
    plot_acf_pacf(w_t)
    print(f"  Lagret figur: {FIGURES_DIR / 'fig_02_acf_pacf.png'}")

    print("\nKjører systematisk kandidatsøk (36 kandidater)...")
    candidates_df = run_candidate_search(df)
    save_table_outputs(candidates_df, "tab_04_modellkandidater")

    n_converged = candidates_df["konvergert"].sum()
    print(f"\n{n_converged} av {len(candidates_df)} kandidater konvergerte.")
    print(f"Lagret tabell: {RESULTS_DIR / 'tab_04_modellkandidater.csv'}")

    print("\nTopp 5 kandidater (lavest AIC):")
    top5 = candidates_df[candidates_df["konvergert"]].head(5)
    print(top5[["modell", "aic", "bic"]].to_string(index=False))


if __name__ == "__main__":
    main()
