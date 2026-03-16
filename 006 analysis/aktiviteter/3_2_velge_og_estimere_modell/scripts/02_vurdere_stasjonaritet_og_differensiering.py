from __future__ import annotations

from pathlib import Path
import warnings

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller, kpss


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


def build_series_variants(df: pd.DataFrame) -> list[dict[str, object]]:
    sales = df["Sales"].astype(float)
    if (sales <= 0).any():
        raise ValueError("Log-transformasjon krever at alle salgstall er større enn null.")
    log_sales = pd.Series(np.log(sales), index=sales.index)
    return [
        {
            "serievariant": "Log-transformert serie z_t = log(y_t)",
            "kortnavn": "d=0, D=0",
            "series": log_sales,
        },
        {
            "serievariant": "Ordinært differensiert (1-B)z_t",
            "kortnavn": "d=1, D=0",
            "series": log_sales.diff(),
        },
        {
            "serievariant": "Sesongdifferensiert (1-B^12)z_t",
            "kortnavn": "d=0, D=1",
            "series": log_sales.diff(12),
        },
        {
            "serievariant": "Kombinert differensiert (1-B)(1-B^12)z_t",
            "kortnavn": "d=1, D=1",
            "series": log_sales.diff(12).diff(),
        },
    ]


def run_stationarity_tests(series: pd.Series) -> tuple[float, float, float, float]:
    clean = series.dropna()
    adf_stat, adf_pvalue, *_ = adfuller(clean, autolag="AIC")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        kpss_stat, kpss_pvalue, *_ = kpss(clean, regression="c", nlags="auto")
    return adf_stat, adf_pvalue, kpss_stat, kpss_pvalue


def interpret_tests(adf_pvalue: float, kpss_pvalue: float) -> str:
    adf_stationary = adf_pvalue < 0.05
    kpss_stationary = kpss_pvalue > 0.05

    if adf_stationary and kpss_stationary:
        return "Begge testene peker mot stasjonaritet."
    if (not adf_stationary) and (not kpss_stationary):
        return "Begge testene peker mot fortsatt ikke-stasjonaritet."
    if adf_stationary and (not kpss_stationary):
        return "ADF peker mot stasjonaritet, men KPSS antyder at serien fortsatt ikke er stabil nok."
    return "KPSS peker mot stasjonaritet, men ADF gir ikke tydelig støtte for at enhetsrot er fjernet."


def build_stationarity_table(variants: list[dict[str, object]]) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for variant in variants:
        adf_stat, adf_pvalue, kpss_stat, kpss_pvalue = run_stationarity_tests(variant["series"])  # type: ignore[arg-type]
        rows.append(
            {
                "serievariant": variant["serievariant"],
                "kandidat": variant["kortnavn"],
                "adf_teststat": round(adf_stat, 4),
                "adf_pverdi": round(adf_pvalue, 4),
                "kpss_teststat": round(kpss_stat, 4),
                "kpss_pverdi": round(kpss_pvalue, 4),
                "tolkning": interpret_tests(adf_pvalue, kpss_pvalue),
            }
        )
    return pd.DataFrame(rows)


def build_differencing_assessment(test_df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, str]] = []
    for _, row in test_df.iterrows():
        candidate = row["kandidat"]
        adf_pvalue = float(row["adf_pverdi"])
        kpss_pvalue = float(row["kpss_pverdi"])

        if candidate == "d=0, D=0":
            assessment = "Referansepunkt på log-skala uten differensiering."
            recommendation = "Forkast hvis testene ikke støtter stasjonaritet."
        elif candidate == "d=1, D=0":
            assessment = "Fjerner generell trend på log-skala, men beholder eksplisitt sesongstruktur."
            recommendation = "Aktuell bare hvis sesongkomponenten ikke er hovedårsaken til ikke-stasjonaritet."
        elif candidate == "d=0, D=1":
            assessment = "Fjerner årlig sesong på log-skala og bevarer ellers modellen så enkel som mulig."
            recommendation = "Foretrukket kandidat hvis testene peker mot tilstrekkelig stasjonaritet."
        else:
            assessment = "Fjerner både trend og sesong på log-skala, men øker risikoen for overdifferensiering."
            recommendation = "Velges hvis enklere differensiering ikke fjerner gjenværende sesong og trend godt nok."

        if adf_pvalue < 0.05 and kpss_pvalue > 0.05:
            recommendation = f"{recommendation} Testene gir støtte."
        elif adf_pvalue >= 0.05 and kpss_pvalue <= 0.05:
            recommendation = f"{recommendation} Testene gir ikke støtte."
        else:
            recommendation = f"{recommendation} Krever faglig skjønn sammen med figurvurdering."

        rows.append(
            {
                "kandidat": candidate,
                "faglig_vurdering": assessment,
                "anbefaling": recommendation,
            }
        )
    return pd.DataFrame(rows)


def save_table_outputs(df: pd.DataFrame, stem: str) -> None:
    csv_path = RESULTS_DIR / f"{stem}.csv"
    md_path = RESULTS_DIR / f"{stem}.md"
    df.to_csv(csv_path, index=False, encoding="utf-8")
    md_path.write_text(df.to_markdown(index=False), encoding="utf-8")


def save_series_figure(variants: list[dict[str, object]]) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(12, 8), sharex=False)
    colors = ["#1f4e79", "#7a8fa8", "#9bbb59", "#c0504d"]

    for ax, variant, color in zip(axes.flatten(), variants, colors):
        series = variant["series"].dropna()  # type: ignore[union-attr]
        ax.plot(series.index, series.values, color=color, linewidth=1.2)
        ax.set_title(str(variant["kortnavn"]))
        ax.set_xlabel("Tid")
        ax.set_ylabel("Log-salg / differensiert log-salg")
        ax.grid(axis="y", alpha=0.3)

    fig.suptitle("Log-transformerte serievarianter for vurdering av stasjonaritet og differensiering", fontsize=12)
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "fig_01_serievarianter.png", dpi=300)
    plt.close(fig)


def main() -> None:
    ensure_output_dirs()
    df = load_train_data()
    variants = build_series_variants(df)
    test_df = build_stationarity_table(variants)
    assessment_df = build_differencing_assessment(test_df)

    save_table_outputs(test_df, "tab_02_stasjonaritetstester")
    save_table_outputs(assessment_df, "tab_03_differensieringsvurdering")
    save_series_figure(variants)

    print(f"Generated figure in: {FIGURES_DIR}")
    print(f"Generated tables in: {RESULTS_DIR}")


if __name__ == "__main__":
    main()
