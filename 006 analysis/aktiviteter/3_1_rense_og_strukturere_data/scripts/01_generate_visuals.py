from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


matplotlib.use("Agg")

BASE_DIR = Path(__file__).resolve().parent
ACTIVITY_DIR = BASE_DIR.parent
ANALYSIS_DIR = BASE_DIR.parents[2]
DATA_PATH = ANALYSIS_DIR.parent / "004 data" / "sales.csv"
FIGURES_DIR = ACTIVITY_DIR / "figurer"
RESULTS_DIR = ACTIVITY_DIR / "resultat"


def load_sales_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)
    df["Month"] = pd.to_datetime(df["Month"])
    df = df.sort_values("Month").reset_index(drop=True)
    df["obs_id"] = range(1, len(df) + 1)
    df["year"] = df["Month"].dt.year
    df["month_num"] = df["Month"].dt.month
    df["rolling_12"] = df["Sales"].rolling(window=12, min_periods=1).mean()
    return df


def get_full_years_only(df: pd.DataFrame) -> pd.DataFrame:
    last_year = int(df["year"].max())
    return df[df["year"] < last_year].copy()


def ensure_output_dirs() -> None:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def build_data_overview_table(df: pd.DataFrame) -> pd.DataFrame:
    full_range = pd.period_range(df["Month"].min(), df["Month"].max(), freq="M")
    observed = df["Month"].dt.to_period("M")
    missing_months = len(full_range.difference(observed))

    rows = [
        ("Startdato", df["Month"].min().strftime("%Y-%m")),
        ("Sluttdato", df["Month"].max().strftime("%Y-%m")),
        ("Antall observasjoner", len(df)),
        ("Antall manglende måneder", missing_months),
        ("Min salg", int(df["Sales"].min())),
        ("Maks salg", int(df["Sales"].max())),
        ("Gjennomsnittlig salg", round(df["Sales"].mean(), 2)),
        ("Median salg", round(df["Sales"].median(), 2)),
        ("Standardavvik", round(df["Sales"].std(), 2)),
        ("Merknad", "1981 er delår og dekker kun januar-juni"),
    ]
    return pd.DataFrame(rows, columns=["Måltall", "Verdi"])


def build_month_profile_table(full_years_df: pd.DataFrame) -> pd.DataFrame:
    month_profile = (
        full_years_df.groupby("month_num", as_index=False)["Sales"]
        .agg(antall_observasjoner="count", gjennomsnittlig_salg="mean", standardavvik="std")
        .sort_values("month_num")
    )
    month_profile["rang"] = month_profile["gjennomsnittlig_salg"].rank(
        ascending=False, method="dense"
    ).astype(int)
    month_profile["gjennomsnittlig_salg"] = month_profile["gjennomsnittlig_salg"].round(2)
    month_profile["standardavvik"] = month_profile["standardavvik"].round(2)
    return month_profile.rename(columns={"month_num": "måned_nummer"})


def write_table_outputs(table_df: pd.DataFrame, stem: str) -> None:
    csv_path = RESULTS_DIR / f"{stem}.csv"
    md_path = RESULTS_DIR / f"{stem}.md"
    table_df.to_csv(csv_path, index=False, encoding="utf-8")
    md_path.write_text(table_df.to_markdown(index=False), encoding="utf-8")


def save_figure_1(df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(12, 5))
    start_year = int(df["year"].min())
    end_year = int(df["year"].max())
    ax.plot(df["obs_id"], df["Sales"], color="#7a8fa8", linewidth=1.2, label="Månedlig salg")
    ax.plot(
        df["obs_id"],
        df["rolling_12"],
        color="#1f4e79",
        linewidth=2.2,
        label="12-observasjoners glidende gjennomsnitt",
    )
    ax.set_title(f"Månedlig salg per observasjon ({start_year}-{end_year})")
    ax.set_xlabel("Måneder")
    ax.set_ylabel("Salg")
    ax.set_xlim(1, len(df))
    ax.set_xticks(range(1, len(df) + 1, 12))
    ax.grid(axis="y", alpha=0.3)
    ax.legend()

    top_ax = ax.twiny()
    top_ax.set_xlim(ax.get_xlim())
    year_starts = df.groupby("year", as_index=False)["obs_id"].min()
    top_years = year_starts[year_starts["year"] >= 1965]
    top_years = top_years[(top_years["year"] - 1965) % 5 == 0]
    top_ax.set_xticks(top_years["obs_id"])
    top_ax.set_xticklabels(top_years["year"])
    top_ax.set_xlabel("")

    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "fig_01_salgsserie_observasjoner.png", dpi=300)
    plt.close(fig)


def save_figure_2(full_years_df: pd.DataFrame) -> None:
    yearly_totals = full_years_df.groupby("year", as_index=False)["Sales"].sum()

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(yearly_totals["year"], yearly_totals["Sales"], color="#4f81bd", width=0.75)
    ax.set_title("Årlig totalsalg for fullførte år")
    ax.set_xlabel("År")
    ax.set_ylabel("Totalt salg")
    ax.set_xticks(yearly_totals["year"])
    ax.tick_params(axis="x", rotation=45)
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "fig_02_aarstotaler_fullforte_ar.png", dpi=300)
    plt.close(fig)


def save_figure_3(month_profile_df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(
        month_profile_df["måned_nummer"],
        month_profile_df["gjennomsnittlig_salg"],
        color="#9bbb59",
        width=0.75,
    )
    ax.set_title("Gjennomsnittlig salg per måned")
    ax.set_xlabel("Månedsnummer")
    ax.set_ylabel("Gjennomsnittlig salg")
    ax.set_xticks(month_profile_df["måned_nummer"])
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "fig_03_gjennomsnitt_per_maned.png", dpi=300)
    plt.close(fig)


def main() -> None:
    ensure_output_dirs()
    df = load_sales_data()
    full_years_df = get_full_years_only(df)

    data_overview = build_data_overview_table(df)
    month_profile = build_month_profile_table(full_years_df)

    write_table_outputs(data_overview, "tab_01_dataoversikt")
    write_table_outputs(month_profile, "tab_02_manedsprofil")

    save_figure_1(df)
    save_figure_2(full_years_df)
    save_figure_3(month_profile)

    print(f"Generated figures in: {FIGURES_DIR}")
    print(f"Generated tables in: {RESULTS_DIR}")


if __name__ == "__main__":
    main()
