"""
Refaz imagens ruins do refinamento visual da semana especial.

Objetivo: substituir caixas genericas por paineis que parecam dashboards
didaticos, com KPIs, graficos, tabelas e chamada para acao.
"""

import os
import textwrap

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "outputs")
os.makedirs(OUT, exist_ok=True)

TXT = "#0F172A"
MUTED = "#64748B"
LINE = "#CBD5E1"
BG = "#F8FAFC"
RED = "#DC2626"
ORANGE = "#E35D22"
BLUE = "#2563EB"
GREEN = "#16A34A"
YELLOW = "#EAB308"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=170, bbox_inches="tight")
    plt.close(fig)
    print(name)


def wrap(s, n=40):
    return "\n".join(textwrap.wrap(s, width=n))


def title(ax, main, sub):
    ax.text(0.35, 7.55, main, fontsize=18, fontweight="bold", color=TXT, va="top")
    ax.text(0.35, 7.15, sub, fontsize=10, color=MUTED, va="top")


def panel(ax, x, y, w, h, label="", fill="white", edge=LINE):
    ax.add_patch(patches.FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.025,rounding_size=0.06",
        facecolor=fill, edgecolor=edge, linewidth=1.0
    ))
    if label:
        ax.text(x + 0.18, y + h - 0.25, label, fontsize=9.5, fontweight="bold", color=TXT, va="top")


def kpi(ax, x, y, w, value, label, color):
    panel(ax, x, y, w, 0.78, "", "white", LINE)
    ax.text(x + 0.15, y + 0.54, value, fontsize=15, fontweight="bold", color=color, va="center")
    ax.text(x + 0.15, y + 0.2, wrap(label, 18), fontsize=6.8, color=MUTED, va="center")


def bars(ax, x, y, w, h, labels, values, color, highlight=0, title_text=""):
    panel(ax, x, y, w, h, title_text)
    maxv = max(values)
    for i, (lab, val) in enumerate(zip(labels, values)):
        yy = y + h - 0.78 - i * ((h - 1.1) / len(labels))
        ax.text(x + 0.2, yy, lab, fontsize=7, color=TXT, va="center")
        bw = (w - 1.55) * val / maxv
        ax.add_patch(patches.Rectangle((x + 1.25, yy - 0.08), bw, 0.16,
                                       color=color if i == highlight else "#CBD5E1"))
        ax.text(x + 1.32 + bw, yy, str(val), fontsize=7, color=MUTED, va="center")


def scatter(ax, x, y, w, h, color, title_text="", trend=True):
    panel(ax, x, y, w, h, title_text)
    rng = np.random.default_rng(4)
    xs = np.linspace(0.2, 0.9, 14)
    ys = 0.78 - xs * 0.45 + rng.normal(0, 0.04, len(xs))
    for xx, yy in zip(xs, ys):
        ax.scatter(x + 0.35 + xx * (w - 0.75), y + 0.35 + yy * (h - 0.9),
                   s=24, color=color, alpha=0.75)
    if trend:
        ax.plot([x + 0.5, x + w - 0.3], [y + h - 0.85, y + 0.55],
                color=TXT, lw=1.1, ls="--")
    ax.text(x + 0.2, y + 0.12, "eixo X", fontsize=6.3, color=MUTED)
    ax.text(x + 0.1, y + h - 0.72, "eixo Y", fontsize=6.3, color=MUTED, rotation=90)


def line_chart(ax, x, y, w, h, color, title_text=""):
    panel(ax, x, y, w, h, title_text)
    xs = np.linspace(x + 0.25, x + w - 0.2, 8)
    ys = np.array([0.3, 0.35, 0.4, 0.5, 0.48, 0.62, 0.72, 0.78])
    ys = y + 0.35 + ys * (h - 0.9)
    ax.plot(xs, ys, color=color, lw=2.3)
    ax.scatter(xs, ys, color=color, s=18)
    ax.axhline(y + 0.35 + 0.6 * (h - 0.9), x + 0.25, x + w - 0.2, color=LINE, lw=1)


def table(ax, x, y, w, h, rows, color, title_text="Tabela analitica"):
    panel(ax, x, y, w, h, title_text)
    ax.add_patch(patches.Rectangle((x + 0.18, y + h - 0.65), w - 0.36, 0.28, color=color))
    cols = ["Segmento", "Metric", "Risco", "Acao"]
    colx = [x + 0.3, x + 1.9, x + 3.2, x + 4.4]
    for cx, c in zip(colx, cols):
        ax.text(cx, y + h - 0.51, c, fontsize=6.8, color="white", fontweight="bold", va="center")
    for i, row in enumerate(rows):
        yy = y + h - 0.9 - i * 0.28
        ax.plot([x + 0.18, x + w - 0.18], [yy - 0.13, yy - 0.13], color="#E2E8F0", lw=0.8)
        for cx, val in zip(colx, row):
            ax.text(cx, yy, val, fontsize=6.5, color=TXT, va="center")


def dashboard(ax, x, y, w, h, title_text, subtitle, color, kpis, bar_data, insight, cta, table_rows, show_table=True):
    panel(ax, x, y, w, h, "", "#F8FAFC", LINE)
    ax.add_patch(patches.Rectangle((x, y + h - 0.65), w, 0.65, color=color))
    ax.text(x + 0.25, y + h - 0.23, title_text, fontsize=10.5, fontweight="bold", color="white", va="top")
    ax.text(x + 0.25, y + h - 0.48, subtitle, fontsize=7.2, color="#E2E8F0", va="top")
    gap = 0.12
    kw = (w - 0.5 - 3 * gap) / 4
    for i, item in enumerate(kpis):
        kpi(ax, x + 0.25 + i * (kw + gap), y + h - 1.6, kw, item[0], item[1], item[2])
    chart_y = y + h - 3.75
    chart_h = 1.72
    bars(ax, x + 0.25, chart_y, (w - 0.7) / 2, chart_h, bar_data[0], bar_data[1], color, 0, bar_data[2])
    scatter(ax, x + 0.45 + (w - 0.7) / 2, chart_y, (w - 0.7) / 2, chart_h, color, bar_data[3])

    cta_y = chart_y - 0.62
    panel(ax, x + 0.25, cta_y, w - 0.5, 0.42, "", color, color)
    ax.text(x + 0.42, cta_y + 0.21, cta, fontsize=7.3, color="white", fontweight="bold", va="center")

    insight_y = cta_y - 0.92
    panel(ax, x + 0.25, insight_y, w - 0.5, 0.7, "Insight IA", "#FFF7ED", ORANGE)
    ax.text(x + 0.45, insight_y + 0.28, wrap(insight, 90), fontsize=7.2, color=TXT, va="top")

    if show_table:
        table(ax, x + 0.25, y + 0.18, w - 0.5, max(0.72, insight_y - y - 0.38), table_rows, color)


def group_previews():
    groups = [
        ("grupo_a_preview.png", "#D62828", "Grupo A - Olist: Atrasos Logisticos",
         "Base Olist | foco em atraso, review e vendedor parceiro",
         [("34%", "atraso SP eletronicos", RED), ("3.2", "review com atraso", ORANGE), ("4.1", "review potencial", GREEN), ("R$280k", "GMV protegido", RED)],
         (["Eletronicos", "Moveis", "Livros", "Esportes"], [34, 22, 18, 12], "Top categorias atrasadas", "Dias de atraso x review"),
         "Eletronicos em SP concentram 34% dos atrasos e derrubam review para 3,2. Redesenhar rota pode elevar review para 4,1.",
         "CTA: redesenhar rota de Eletronicos/SP ate Q3/2026",
         [["SP/Eletro", "34%", "Critico", "Rota"], ["RJ/Eletro", "28%", "Alto", "SLA"], ["SP/Moveis", "22%", "Alto", "CD"]]),
        ("grupo_b_preview.png", "#003DA5", "Grupo B - IBM HR: Turnover de TI",
         "People Analytics | retencao de talentos",
         [("28%", "turnover TI", RED), ("15%", "meta", GREEN), ("41", "talentos risco", ORANGE), ("R$270k", "economia anual", BLUE)],
         (["TI", "Vendas", "RH", "Operacoes"], [28, 18, 12, 10], "Turnover por area", "Tempo empresa x risco"),
         "Funcionarios de TI com menos de 2 anos e sem promocao tem 3x mais chance de saida. Mentoria reduz risco.",
         "CTA: mentoria + revisao salarial para 41 talentos",
         [["TI junior", "28%", "Critico", "Mentoria"], ["TI pleno", "19%", "Alto", "Plano"], ["Vendas", "18%", "Medio", "Monitor"]]),
        ("grupo_c_preview.png", "#2E7D52", "Grupo C - Superstore: Margem Negativa",
         "Varejo | desconto, lucro e politica comercial",
         [("-4.2%", "margem Tech/Sul", RED), ("20%", "limite atual", ORANGE), ("12%", "limite proposto", GREEN), ("R$85k", "margem recuperada", GREEN)],
         (["Maquinas", "Copiadoras", "Phones", "Binders"], [73, 55, 31, 18], "Prejuizo por subcategoria", "Desconto x margem"),
         "Descontos acima de 20% concentram 73% do prejuizo. Cap em 12% pode reverter margem sem perder volume relevante.",
         "CTA: aprovar teto de desconto de 12% ate 01/jun",
         [["Maquinas", "-4.2%", "Critico", "Cap 12%"], ["Copiadoras", "-2.8%", "Alto", "Revisar"], ["Phones", "5.1%", "OK", "Manter"]]),
        ("grupo_d_preview.png", "#C41E3A", "Grupo D - Saude: Risco Cardiaco",
         "Saude publica | triagem preventiva",
         [("38%", "internacoes cardiacas", RED), ("73%", "casos com 3 sinais", ORANGE), ("42", "pacientes risco", RED), ("R$2.1M", "economia anual", GREEN)],
         (["Pressao", "Colesterol", "Idade", "Acucar"], [44, 42, 38, 28], "Fatores de risco", "Colesterol x pressao"),
         "Colesterol >240, pressao >140 e idade >55 identificam 73% do alto risco com apenas 3 variaveis simples.",
         "CTA: triagem preventiva mensal para 42 pacientes",
         [[">55 anos", "68%", "Critico", "Triagem"], ["45-54", "45%", "Alto", "Monitor"], ["35-44", "28%", "Medio", "Check-up"]]),
        ("grupo_e_preview.png", "#6F42C1", "Grupo E - FinTech: Churn Premium",
         "Cartao de credito | uso, limite e churn",
         [("18%", "churn Premium", RED), ("8%", "benchmark", GREEN), ("285", "clientes risco", ORANGE), ("R$1.2M", "receita preservada", GREEN)],
         (["<10k", "10-30k", ">30k", "Black"], [18, 12, 7, 5], "Churn por limite", "Transacoes x ticket"),
         "Premium com limite <R$10k e menos de 20 transacoes/ano tem 4x mais risco de churn. Reengajamento e limite temporario reduzem perda.",
         "CTA: campanha de reengajamento ate 15/jun",
         [["Premium baixo", "18%", "Critico", "Cashback"], ["Gold", "12%", "Alto", "Nudge"], ["Black", "5%", "OK", "Manter"]]),
    ]
    for fname, color, t, sub, kpis, bars_data, insight, cta, rows in groups:
        fig, ax = plt.subplots(figsize=(13.5, 7.8))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis("off")
        title(ax, t, sub)
        dashboard(ax, 0.45, 0.35, 11.1, 6.35, t, sub, color, kpis, bars_data, insight, cta, rows)
        save(fig, fname)


def cap2_better():
    defs = [
        ("cap2_01b_dashboard_aed_explanatoria.png", "AED vs Explanatoria", "Exploratorio descobre; explanatorio escolhe evidencias para decisao.", ORANGE),
        ("cap2_02b_big_idea_dashboard.png", "Big Idea no dashboard", "A frase principal governa KPIs, visual principal e CTA.", BLUE),
        ("cap2_03b_com_sem_storyboard.png", "Storyboard transforma graficos em historia", "Contexto -> conflito -> evidencia -> recomendacao.", ORANGE),
        ("cap2_04b_preatencao_dashboard.png", "Pre-atencao aplicada", "Cor, tamanho e posicao indicam o que olhar primeiro.", GREEN),
        ("cap2_05b_relance_dashboard.png", "Teste do relance", "Em 3 segundos, a mensagem precisa aparecer.", RED),
        ("cap2_06b_chartjunk_dashboard.png", "Chartjunk removido", "Menos decoracao, mais comparacao.", BLUE),
        ("cap2_07b_interatividade_tableau.png", "Filtros, parametros e acoes", "Interatividade deve responder uma pergunta de negocio.", ORANGE),
        ("cap2_08b_dashboard_decisorio.png", "Dashboard decisorio", "Contexto, diagnostico e recomendacao em zonas separadas.", GREEN),
        ("cap2_09b_kpi_ruim_bom.png", "KPI decisorio", "Valor + meta + gap + tendencia + periodo.", RED),
        ("cap2_10b_pitch_dashboard.png", "Pitch guiado pelo dashboard", "Situacao, complicacao, resolucao e proximo passo.", BLUE),
    ]
    for fname, main, sub, color in defs:
        fig, ax = plt.subplots(figsize=(12.5, 6.2))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 7)
        ax.axis("off")
        title(ax, main, sub)
        dashboard(
            ax, 0.6, 0.45, 10.8, 5.7, main, sub, color,
            [("18%", "KPI principal", color), ("+5pp", "gap vs meta", RED), ("3x", "segmento critico", ORANGE), ("30d", "prazo acao", GREEN)],
            (["Segmento A", "Segmento B", "Segmento C", "Outros"], [58, 31, 22, 12], "Diagnostico principal", "Evidencia x impacto"),
            "A leitura correta conecta padrao, impacto e recomendacao. O dashboard deixa de ser relatorio e vira apoio a decisao.",
            "CTA: decisao clara, responsavel definido e prazo explicito",
            [["A", "58%", "Critico", "Agir"], ["B", "31%", "Alto", "Priorizar"], ["C", "22%", "Medio", "Monitor"]],
            show_table=False
        )
        save(fig, fname)


if __name__ == "__main__":
    cap2_better()
    group_previews()
