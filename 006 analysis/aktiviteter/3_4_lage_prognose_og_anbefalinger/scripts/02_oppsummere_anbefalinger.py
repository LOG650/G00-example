from __future__ import annotations

from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
ACTIVITY_DIR = BASE_DIR.parent
ANALYSIS_DIR = BASE_DIR.parents[2]
DATA_DIR = ANALYSIS_DIR.parent / "004 data"
DATA_PATH = DATA_DIR / "sales.csv"
RESULTS_DIR = ACTIVITY_DIR / "resultat"
FORECAST_PATH = RESULTS_DIR / "tab_02_prognose_12_maaneder.csv"
PROFIL_PATH = ANALYSIS_DIR / "aktiviteter" / "3_1_rense_og_strukturere_data" / "resultat" / "tab_02_manedsprofil.csv"


def save_table_outputs(df: pd.DataFrame, stem: str) -> None:
    csv_path = RESULTS_DIR / f"{stem}.csv"
    md_path = RESULTS_DIR / f"{stem}.md"
    df.to_csv(csv_path, index=False, encoding="utf-8")
    md_path.write_text(df.to_markdown(index=False), encoding="utf-8")


def load_forecast() -> pd.DataFrame:
    df = pd.read_csv(FORECAST_PATH)
    df["dato"] = pd.to_datetime(df["maaned"])
    return df


def build_season_map() -> dict[int, str]:
    """Bygg sesongkategori-dict basert på historisk månedsprofil (rang)."""
    profil = pd.read_csv(PROFIL_PATH)
    season_map: dict[int, str] = {}
    for _, row in profil.iterrows():
        rang = int(row["rang"])
        if rang <= 3:
            kategori = "Høysesong"
        elif rang >= 10:
            kategori = "Lavsesong"
        else:
            kategori = "Normalsesong"
        season_map[int(row["måned_nummer"])] = kategori
    return season_map


def build_summary_table(fc: pd.DataFrame) -> pd.DataFrame:
    total = int(fc["punktprognose"].sum())
    mean_monthly = int(round(fc["punktprognose"].mean()))
    top_idx = fc["punktprognose"].idxmax()
    bottom_idx = fc["punktprognose"].idxmin()
    top_month = fc.loc[top_idx, "maaned"]
    top_value = int(fc.loc[top_idx, "punktprognose"])
    bottom_month = fc.loc[bottom_idx, "maaned"]
    bottom_value = int(fc.loc[bottom_idx, "punktprognose"])
    amplitude = top_value - bottom_value

    fc["pi_bredde"] = fc["ki_ovre_95"] - fc["ki_nedre_95"]
    mean_pi = int(round(fc["pi_bredde"].mean()))

    rows = [
        {"noekkeltall": "Totalt prognosesalg (12 mnd)", "verdi": f"{total:,}".replace(",", " ")},
        {"noekkeltall": "Gjennomsnittlig månedssalg", "verdi": f"{mean_monthly:,}".replace(",", " ")},
        {"noekkeltall": "Toppmåned", "verdi": f"{top_month} ({top_value:,})".replace(",", " ")},
        {"noekkeltall": "Bunnmåned", "verdi": f"{bottom_month} ({bottom_value:,})".replace(",", " ")},
        {"noekkeltall": "Sesongamplitude (topp - bunn)", "verdi": f"{amplitude:,}".replace(",", " ")},
        {"noekkeltall": "Gjennomsnittlig PI-bredde (95 %)", "verdi": f"{mean_pi:,}".replace(",", " ")},
    ]
    return pd.DataFrame(rows)


def build_capacity_table(fc: pd.DataFrame) -> pd.DataFrame:
    season_map = build_season_map()
    rows = []
    for _, row in fc.iterrows():
        m = row["dato"].month
        rows.append(
            {
                "maaned": row["maaned"],
                "punktprognose": int(row["punktprognose"]),
                "ki_nedre_95": int(row["ki_nedre_95"]),
                "ki_ovre_95": int(row["ki_ovre_95"]),
                "sesongkategori": season_map[m],
            }
        )
    return pd.DataFrame(rows)


def main() -> None:
    fc = load_forecast()

    summary_df = build_summary_table(fc)
    save_table_outputs(summary_df, "tab_03_prognoseoppsummering")
    print("Lagret prognoseoppsummering:")
    print(summary_df.to_markdown(index=False))

    capacity_df = build_capacity_table(fc)
    save_table_outputs(capacity_df, "tab_04_kapasitetsplanlegging")
    print("\nLagret kapasitetsplanlegging:")
    print(capacity_df.to_markdown(index=False))


if __name__ == "__main__":
    main()
