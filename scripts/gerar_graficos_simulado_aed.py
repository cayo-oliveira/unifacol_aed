#!/usr/bin/env python3
"""Gera, com Matplotlib, as figuras das questões 9, 10 e 12 do simulado AED."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figuras" / "simulado_enade_aed"
OUT.mkdir(parents=True, exist_ok=True)

NAVY = "#23445D"
TEAL = "#147D83"
ORANGE = "#C86532"
PURPLE = "#69558B"
GRAY = "#65717C"
GRID = "#DCE3E8"
BEFORE = "#23445D"
AFTER = "#C86532"

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.titlesize": 13,
        "axes.labelsize": 10,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "axes.edgecolor": "#AAB5BE",
        "axes.labelcolor": NAVY,
        "text.color": NAVY,
        "xtick.color": GRAY,
        "ytick.color": GRAY,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
    }
)


def polish(ax):
    ax.grid(axis="x", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def q9_distribution():
    values = np.array([4, 5, 6, 7, 8, 8, 10, 15, 27, 50])
    unique, counts = np.unique(values, return_counts=True)
    fig, ax = plt.subplots(figsize=(9.2, 4.2), constrained_layout=True)
    bars = ax.bar(
        unique,
        counts,
        width=0.8,
        color=TEAL,
        edgecolor="white",
        linewidth=1.1,
        zorder=3,
    )
    ax.bar_label(bars, labels=[str(count) for count in counts], padding=4, color=NAVY, fontsize=9, weight="bold")
    ax.set_title("Tempo de resolução dos chamados no turno de teste", loc="left", pad=12, weight="bold")
    ax.set_xlabel("Tempo de resolução (minutos)", labelpad=8)
    ax.set_ylabel("Frequência (nº de chamados)", labelpad=8)
    ax.set_xlim(0, 55)
    ax.set_ylim(0, 2.7)
    ax.set_xticks(np.arange(0, 56, 5))
    ax.set_yticks([0, 1, 2])
    ax.set_yticklabels(["0", "1", "2"])
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.text(
        0.99,
        0.96,
        "A altura de cada barra indica quantos chamados tiveram aquela duração.",
        transform=ax.transAxes,
        ha="right",
        va="top",
        color=GRAY,
        fontsize=8.5,
    )
    fig.savefig(OUT / "aed_q09_frequencia_tempos.png", dpi=240, bbox_inches="tight")
    plt.close(fig)


def q10_weekly_sales():
    weeks = np.arange(1, 7)
    series = {
        "Centro": ([80, 84, 82, 58, 61, 83], NAVY, "o", "-"),
        "Norte": ([62, 65, 67, 68, 66, 69], TEAL, "s", "--"),
        "Sul": ([45, 57, 42, 59, 39, 61], ORANGE, "^", ":"),
    }
    fig, ax = plt.subplots(figsize=(9.2, 4.8), constrained_layout=True)
    for name, (values, color, marker, linestyle) in series.items():
        ax.plot(
            weeks,
            values,
            label=name,
            color=color,
            marker=marker,
            linestyle=linestyle,
            linewidth=2.2,
            markersize=7,
            markeredgecolor="white",
            markeredgewidth=0.8,
        )
    ax.set_title("Índice semanal de vendas por loja", loc="left", pad=12, weight="bold")
    ax.set_xlabel("Semana de acompanhamento", labelpad=8)
    ax.set_ylabel("Índice de vendas (pontos)", labelpad=8)
    ax.set_xticks(weeks, [f"{w}" for w in weeks])
    ax.set_xlim(0.8, 6.2)
    ax.set_ylim(0, 100)
    ax.set_yticks(np.arange(0, 101, 20))
    polish(ax)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.grid(axis="x", visible=False)
    ax.legend(frameon=False, ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.19))
    fig.savefig(OUT / "aed_q10_series_vendas.png", dpi=240, bbox_inches="tight")
    plt.close(fig)


def dumbbell(ax, labels, before, after, xlim, xlabel, fmt):
    y = np.arange(len(labels))[::-1]
    for yi, old, new in zip(y, before, after):
        ax.plot([old, new], [yi, yi], color="#B9C3CA", linewidth=3, zorder=1)
        ax.scatter(old, yi, s=82, color=BEFORE, edgecolor="white", linewidth=1.1, zorder=3)
        ax.scatter(new, yi, s=82, color=AFTER, edgecolor="white", linewidth=1.1, zorder=3)
        ax.annotate(fmt(old), (old, yi), xytext=(0, 12), textcoords="offset points", ha="center", color=BEFORE, weight="bold", fontsize=9)
        ax.annotate(fmt(new), (new, yi), xytext=(0, -17), textcoords="offset points", ha="center", color=AFTER, weight="bold", fontsize=9)
    ax.set_yticks(y, labels)
    ax.set_xlim(*xlim)
    ax.set_xlabel(xlabel, labelpad=8)
    polish(ax)
    ax.grid(axis="y", visible=False)


def q12_before_after():
    fig, (time_ax, quality_ax) = plt.subplots(1, 2, figsize=(10.2, 3.6), constrained_layout=True)
    time_ax.set_title("Tempos de atendimento", loc="left", pad=12, weight="bold")
    dumbbell(
        time_ax,
        ["Tempo médio", "Percentil 90"],
        [18, 34],
        [14, 49],
        (0, 60),
        "Tempo (minutos)",
        lambda x: f"{x} min",
    )
    time_ax.set_xticks(np.arange(0, 61, 15))

    quality_ax.set_title("Indicadores de qualidade", loc="left", pad=12, weight="bold")
    dumbbell(
        quality_ax,
        ["Reabertos", "Resolvidos no\n1º contato"],
        [9, 71],
        [17, 66],
        (0, 100),
        "Chamados (%)",
        lambda x: f"{x}%",
    )
    quality_ax.set_xticks(np.arange(0, 101, 20))
    handles = [
        plt.Line2D([0], [0], marker="o", color="none", markerfacecolor=BEFORE, markeredgecolor="white", markersize=9, label="Antes do chatbot"),
        plt.Line2D([0], [0], marker="o", color="none", markerfacecolor=AFTER, markeredgecolor="white", markersize=9, label="Depois do chatbot"),
    ]
    fig.legend(handles=handles, loc="lower center", ncol=2, frameon=False, bbox_to_anchor=(0.5, -0.05))
    fig.suptitle("Indicadores observados antes e depois do lançamento", x=0.02, ha="left", fontsize=14, weight="bold", color=NAVY)
    fig.savefig(OUT / "aed_q12_comparacao_indicadores.png", dpi=240, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    q9_distribution()
    q10_weekly_sales()
    q12_before_after()
    print(f"Figuras Matplotlib geradas em: {OUT}")
