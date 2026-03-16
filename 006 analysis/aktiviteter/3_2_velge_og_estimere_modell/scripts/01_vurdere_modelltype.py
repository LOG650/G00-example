from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
ACTIVITY_DIR = BASE_DIR.parent
ANALYSIS_DIR = BASE_DIR.parents[2]
DATA_DIR = ANALYSIS_DIR.parent / "004 data"
DATA_PATH = DATA_DIR / "sales_train.csv"
RESULTS_DIR = ACTIVITY_DIR / "resultat"


def ensure_output_dirs() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def load_train_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)
    df["Month"] = pd.to_datetime(df["Month"])
    df = df.sort_values("Month").reset_index(drop=True)
    df["year"] = df["Month"].dt.year
    df["month_num"] = df["Month"].dt.month
    df["rolling_12"] = df["Sales"].rolling(window=12, min_periods=12).mean()
    return df


def count_missing_months(df: pd.DataFrame) -> int:
    full_range = pd.period_range(df["Month"].min(), df["Month"].max(), freq="M")
    observed = df["Month"].dt.to_period("M")
    return len(full_range.difference(observed))


def build_month_profile(df: pd.DataFrame) -> pd.DataFrame:
    month_profile = (
        df.groupby("month_num", as_index=False)["Sales"]
        .agg(gjennomsnittlig_salg="mean", standardavvik="std")
        .sort_values("month_num")
    )
    month_profile["gjennomsnittlig_salg"] = month_profile["gjennomsnittlig_salg"].round(2)
    month_profile["standardavvik"] = month_profile["standardavvik"].round(2)
    return month_profile


def build_model_assessment_table(df: pd.DataFrame, month_profile: pd.DataFrame) -> pd.DataFrame:
    missing_months = count_missing_months(df)
    start = df["Month"].min().strftime("%Y-%m")
    end = df["Month"].max().strftime("%Y-%m")
    full_years = int(df["year"].nunique())
    first_roll = float(df["rolling_12"].dropna().iloc[0])
    last_roll = float(df["rolling_12"].dropna().iloc[-1])
    highest_month = int(month_profile.loc[month_profile["gjennomsnittlig_salg"].idxmax(), "month_num"])
    lowest_month = int(month_profile.loc[month_profile["gjennomsnittlig_salg"].idxmin(), "month_num"])
    highest_sales = float(month_profile["gjennomsnittlig_salg"].max())
    lowest_sales = float(month_profile["gjennomsnittlig_salg"].min())
    seasonal_ratio = highest_sales / lowest_sales
    extra_columns = [col for col in df.columns if col not in {"Month", "Sales", "year", "month_num", "rolling_12"}]

    rows = [
        (
            "Tidsoppløsning",
            f"Månedlig serie fra {start} til {end} med {len(df)} observasjoner.",
            "En SARIMA-modell kan eksplisitt håndtere månedlig frekvens med sesonglengde 12.",
        ),
        (
            "Datakompletthet",
            f"{missing_months} manglende måneder i treningsperioden.",
            "Jevne tidsintervaller gjør en klassisk tidsseriemodell egnet uten ekstra imputering.",
        ),
        (
            "Kalenderstruktur",
            f"Treningssettet dekker {full_years} hele kalenderår.",
            "Hele år bevarer sesongmønsteret og gjør sesongmodellering mer robust.",
        ),
        (
            "Trendindikasjon",
            f"12-måneders glidende gjennomsnitt øker fra {first_roll:.1f} til {last_roll:.1f}.",
            "Modellen må kunne håndtere nivåendring og trend gjennom differensiering.",
        ),
        (
            "Sesongmønster",
            f"Høyest månedsgjennomsnitt i måned {highest_month} ({highest_sales:.1f}) og lavest i måned {lowest_month} ({lowest_sales:.1f}); forhold {seasonal_ratio:.2f}.",
            "Serien har tydelig årlig sesong og bør modelleres med sesongledd.",
        ),
        (
            "Variabelsett",
            "Datasettet inneholder bare tid og salg." if not extra_columns else f"Ekstra kolonner: {', '.join(extra_columns)}.",
            "En univariat modell er naturlig fordi prosjektet ikke bruker eksterne forklaringsvariabler.",
        ),
        (
            "Krav til metode",
            "Prosjektplanen krever en modell som håndterer både trend og sesong.",
            "SARIMA oppfyller kravene uten å utvide scope til mer avanserte forklaringsmodeller.",
        ),
        (
            "Konklusjon",
            "Treningsdataene viser en månedlig, komplett og tydelig sesongpreget serie med trend.",
            "SARIMA vurderes som riktig modellklasse for videre arbeid i aktivitet 3.2.",
        ),
    ]
    return pd.DataFrame(rows, columns=["forhold", "observasjon", "implikasjon_for_modellvalg"])


def save_results(table_df: pd.DataFrame) -> None:
    csv_path = RESULTS_DIR / "tab_01_modellvurdering.csv"
    md_path = RESULTS_DIR / "tab_01_modellvurdering.md"
    table_df.to_csv(csv_path, index=False, encoding="utf-8")
    md_path.write_text(table_df.to_markdown(index=False), encoding="utf-8")


def main() -> None:
    ensure_output_dirs()
    df = load_train_data()
    month_profile = build_month_profile(df)
    assessment = build_model_assessment_table(df, month_profile)

    save_results(assessment)
    print(f"Generated results in: {RESULTS_DIR}")


if __name__ == "__main__":
    main()
