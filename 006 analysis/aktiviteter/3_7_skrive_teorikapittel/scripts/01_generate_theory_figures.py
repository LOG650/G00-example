"""Genererer pedagogiske teori-figurer for kapittel 3 i rapporten.

Alle figurer bruker fiktive/syntetiske data for å illustrere
teoretiske konsepter. Ingen prosjektdata brukes her.
"""

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

matplotlib.use("Agg")

BASE_DIR = Path(__file__).resolve().parent
FIGURES_DIR = BASE_DIR.parent / "figurer"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

RNG = np.random.default_rng(42)

# Felles stil
plt.rcParams.update({
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "axes.grid": True,
    "grid.alpha": 0.3,
    "font.size": 10,
})


# ──────────────────────────────────────────────────────────────
# Figur 3.1  Tidsseriedekomponering (additiv)
# ──────────────────────────────────────────────────────────────
def fig_01_dekomponering():
    T = 120  # 10 år med månedlige data
    t = np.arange(T)

    trend = 100 + 0.5 * t
    sesong = 15 * np.sin(2 * np.pi * t / 12)
    stoey = RNG.normal(0, 4, T)
    y = trend + sesong + stoey

    fig, axes = plt.subplots(4, 1, figsize=(10, 8), sharex=True)

    axes[0].plot(t, y, color="#2c3e50", linewidth=0.9)
    axes[0].set_ylabel("$y_t$")
    axes[0].set_title("Observert serie", fontsize=11, fontweight="bold")

    axes[1].plot(t, trend, color="#e74c3c", linewidth=1.2)
    axes[1].set_ylabel("$T_t$")
    axes[1].set_title("Trend", fontsize=11, fontweight="bold")

    axes[2].plot(t, sesong, color="#2980b9", linewidth=1.2)
    axes[2].set_ylabel("$S_t$")
    axes[2].set_title("Sesongkomponent", fontsize=11, fontweight="bold")

    axes[3].plot(t, stoey, color="#7f8c8d", linewidth=0.8)
    axes[3].axhline(0, color="black", linewidth=0.5, linestyle="--")
    axes[3].set_ylabel("$\\varepsilon_t$")
    axes[3].set_title("Restledd (støy)", fontsize=11, fontweight="bold")
    axes[3].set_xlabel("Måned")

    fig.suptitle(
        "Additiv dekomponering:  $y_t = T_t + S_t + \\varepsilon_t$",
        fontsize=13, fontweight="bold", y=0.98,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(FIGURES_DIR / "fig_01_dekomponering.png", dpi=150)
    plt.close(fig)
    print("  -> fig_01_dekomponering.png")


# ──────────────────────────────────────────────────────────────
# Figur 3.2  Stasjonaritet og differensiering
# ──────────────────────────────────────────────────────────────
def fig_02_stasjonaritet():
    T = 144  # 12 år
    t = np.arange(T)

    # Ikke-stasjonaer serie med trend og sesong
    trend = 5 + 0.03 * t
    sesong = 0.4 * np.sin(2 * np.pi * t / 12)
    stoey = RNG.normal(0, 0.12, T)
    z = trend + sesong + stoey  # log-skala

    # Differensierte varianter
    diff_ord = np.diff(z, n=1)  # (1-B)z_t
    diff_sesong = z[12:] - z[:-12]  # (1-B^12)z_t
    diff_komb = np.diff(diff_sesong, n=1)  # (1-B)(1-B^12)z_t

    fig, axes = plt.subplots(2, 2, figsize=(12, 7))

    axes[0, 0].plot(t, z, color="#2c3e50", linewidth=0.9)
    axes[0, 0].set_title("$z_t = \\log(y_t)$\nIkke-stasjonær", fontsize=10, fontweight="bold")
    axes[0, 0].set_ylabel("Nivå")

    axes[0, 1].plot(np.arange(len(diff_ord)), diff_ord, color="#e74c3c", linewidth=0.8)
    axes[0, 1].axhline(0, color="black", linewidth=0.5, linestyle="--")
    axes[0, 1].set_title("$(1-B)z_t$\nOrdinært differensiert", fontsize=10, fontweight="bold")

    axes[1, 0].plot(np.arange(len(diff_sesong)), diff_sesong, color="#2980b9", linewidth=0.8)
    axes[1, 0].axhline(0, color="black", linewidth=0.5, linestyle="--")
    axes[1, 0].set_title("$(1-B^{12})z_t$\nSesongdifferensiert", fontsize=10, fontweight="bold")
    axes[1, 0].set_xlabel("Måned")
    axes[1, 0].set_ylabel("Differanse")

    axes[1, 1].plot(np.arange(len(diff_komb)), diff_komb, color="#27ae60", linewidth=0.8)
    axes[1, 1].axhline(0, color="black", linewidth=0.5, linestyle="--")
    axes[1, 1].set_title(
        "$(1-B)(1-B^{12})z_t$\nKombinert differensiert",
        fontsize=10, fontweight="bold",
    )
    axes[1, 1].set_xlabel("Måned")

    fig.suptitle(
        "Differensiering for å oppnå stasjonaritet",
        fontsize=13, fontweight="bold", y=0.98,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(FIGURES_DIR / "fig_02_stasjonaritet.png", dpi=150)
    plt.close(fig)
    print("  -> fig_02_stasjonaritet.png")


# ──────────────────────────────────────────────────────────────
# Figur 3.3  ACF/PACF-signaturmoenstre
# ──────────────────────────────────────────────────────────────
def _compute_acf(x, nlags):
    """Beregn ACF manuelt for fiktive data."""
    n = len(x)
    xm = x - x.mean()
    c0 = np.sum(xm**2) / n
    acf = np.array([np.sum(xm[: n - k] * xm[k:]) / (n * c0) for k in range(nlags + 1)])
    return acf


def _compute_pacf(acf_vals):
    """Beregn PACF via Durbin-Levinson fra ACF-verdier."""
    n = len(acf_vals) - 1
    pacf = np.zeros(n + 1)
    pacf[0] = 1.0
    if n == 0:
        return pacf
    pacf[1] = acf_vals[1]
    phi_prev = np.array([acf_vals[1]])
    for k in range(2, n + 1):
        num = acf_vals[k] - np.sum(phi_prev * acf_vals[k - 1 : 0 : -1])
        den = 1.0 - np.sum(phi_prev * acf_vals[1:k])
        if abs(den) < 1e-12:
            break
        pacf[k] = num / den
        phi_new = phi_prev - pacf[k] * phi_prev[::-1]
        phi_prev = np.append(phi_new, pacf[k])
    return pacf


def fig_03_acf_pacf():
    N = 500
    nlags = 24

    # AR(1) med phi=0.7
    ar1 = np.zeros(N)
    ar1[0] = RNG.normal()
    for i in range(1, N):
        ar1[i] = 0.7 * ar1[i - 1] + RNG.normal()

    # MA(1) med theta=0.8
    eps = RNG.normal(size=N + 1)
    ma1 = eps[1:] + 0.8 * eps[:-1]

    fig, axes = plt.subplots(2, 2, figsize=(12, 7))

    # AR(1) ACF
    acf_ar = _compute_acf(ar1, nlags)
    axes[0, 0].bar(range(nlags + 1), acf_ar, width=0.4, color="#2980b9", edgecolor="#2980b9")
    ci = 1.96 / np.sqrt(N)
    axes[0, 0].axhline(ci, color="red", linestyle="--", linewidth=0.8)
    axes[0, 0].axhline(-ci, color="red", linestyle="--", linewidth=0.8)
    axes[0, 0].set_title("ACF for AR(1)", fontsize=10, fontweight="bold")
    axes[0, 0].set_ylabel("Autokorrelasjon")
    axes[0, 0].set_ylim(-0.3, 1.05)

    # AR(1) PACF
    pacf_ar = _compute_pacf(acf_ar)
    axes[0, 1].bar(range(nlags + 1), pacf_ar, width=0.4, color="#e74c3c", edgecolor="#e74c3c")
    axes[0, 1].axhline(ci, color="red", linestyle="--", linewidth=0.8)
    axes[0, 1].axhline(-ci, color="red", linestyle="--", linewidth=0.8)
    axes[0, 1].set_title("PACF for AR(1)", fontsize=10, fontweight="bold")
    axes[0, 1].set_ylim(-0.3, 1.05)
    axes[0, 1].annotate(
        "Kutoff etter lag 1",
        xy=(2, pacf_ar[2]), xytext=(8, 0.5),
        arrowprops=dict(arrowstyle="->", color="#555"),
        fontsize=9, color="#555",
    )

    # MA(1) ACF
    acf_ma = _compute_acf(ma1, nlags)
    axes[1, 0].bar(range(nlags + 1), acf_ma, width=0.4, color="#2980b9", edgecolor="#2980b9")
    axes[1, 0].axhline(ci, color="red", linestyle="--", linewidth=0.8)
    axes[1, 0].axhline(-ci, color="red", linestyle="--", linewidth=0.8)
    axes[1, 0].set_title("ACF for MA(1)", fontsize=10, fontweight="bold")
    axes[1, 0].set_ylabel("Autokorrelasjon")
    axes[1, 0].set_xlabel("Lag")
    axes[1, 0].set_ylim(-0.3, 1.05)
    axes[1, 0].annotate(
        "Kutoff etter lag 1",
        xy=(2, acf_ma[2]), xytext=(8, 0.5),
        arrowprops=dict(arrowstyle="->", color="#555"),
        fontsize=9, color="#555",
    )

    # MA(1) PACF
    pacf_ma = _compute_pacf(acf_ma)
    axes[1, 1].bar(range(nlags + 1), pacf_ma, width=0.4, color="#e74c3c", edgecolor="#e74c3c")
    axes[1, 1].axhline(ci, color="red", linestyle="--", linewidth=0.8)
    axes[1, 1].axhline(-ci, color="red", linestyle="--", linewidth=0.8)
    axes[1, 1].set_title("PACF for MA(1)", fontsize=10, fontweight="bold")
    axes[1, 1].set_xlabel("Lag")
    axes[1, 1].set_ylim(-0.5, 1.05)

    fig.suptitle(
        "Signaturmønstre i ACF og PACF for AR- og MA-prosesser",
        fontsize=13, fontweight="bold", y=0.98,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(FIGURES_DIR / "fig_03_acf_pacf_moenstre.png", dpi=150)
    plt.close(fig)
    print("  -> fig_03_acf_pacf_moenstre.png")


# ──────────────────────────────────────────────────────────────
# Figur 3.4  Biaskorreksjon ved log-transformasjon
# ──────────────────────────────────────────────────────────────
def fig_04_biaskorreksjon():
    mu_z = 8.5  # log-skala prognose
    sigma_z = 0.12  # log-skala standardfeil

    median_y = np.exp(mu_z)
    mean_y = np.exp(mu_z + sigma_z**2 / 2)

    # Tetthetsfunksjon for log-normalfordeling
    y_vals = np.linspace(2000, 9000, 1000)
    pdf_vals = stats.lognorm.pdf(y_vals, s=sigma_z, scale=np.exp(mu_z))

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.fill_between(y_vals, pdf_vals, alpha=0.15, color="#2980b9")
    ax.plot(y_vals, pdf_vals, color="#2980b9", linewidth=1.5, label="Log-normalfordeling")

    ax.axvline(
        median_y, color="#e74c3c", linewidth=2, linestyle="--",
        label=f"Median = exp($\\hat{{z}}$) = {median_y:.0f}",
    )
    ax.axvline(
        mean_y, color="#27ae60", linewidth=2, linestyle="-",
        label=f"Gjennomsnitt = exp($\\hat{{z}} + \\sigma^2/2$) = {mean_y:.0f}",
    )

    # Annotasjon for biaskorreksjonen
    mid_y = (median_y + mean_y) / 2
    peak_pdf = max(pdf_vals) * 0.6
    ax.annotate(
        "", xy=(mean_y, peak_pdf), xytext=(median_y, peak_pdf),
        arrowprops=dict(arrowstyle="<->", color="#555", linewidth=1.5),
    )
    ax.text(
        mid_y, peak_pdf * 1.08,
        f"Bias = {mean_y - median_y:.0f}",
        ha="center", fontsize=10, color="#555",
    )

    ax.set_xlabel("Salg (originalskala)", fontsize=11)
    ax.set_ylabel("Tetthet", fontsize=11)
    ax.set_title(
        "Biaskorreksjon ved tilbaketransformering fra log-skala\n"
        "(Jensens ulikhet: $E[\\exp(Z)] > \\exp(E[Z])$)",
        fontsize=12, fontweight="bold",
    )
    ax.legend(fontsize=10, loc="upper right")
    ax.set_ylim(bottom=0)

    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "fig_04_biaskorreksjon.png", dpi=150)
    plt.close(fig)
    print("  -> fig_04_biaskorreksjon.png")


# ──────────────────────────────────────────────────────────────
# Hovedprogram
# ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Genererer teori-figurer for kapittel 3 ...")
    fig_01_dekomponering()
    fig_02_stasjonaritet()
    fig_03_acf_pacf()
    fig_04_biaskorreksjon()
    print("Ferdig.")
