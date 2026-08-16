#!/usr/bin/env python3
"""
wireframe_grupos.py
===================
Gera protótipos visuais de dashboard Tableau para cada grupo da Semana 12.

Execução (a partir do diretório raiz do projeto):
    python tableau/python/wireframe_grupos.py

Saída:
    aula/semana12/wireframes/wireframe_grupo{N}_{slug}.png  (5 PNGs, 150 dpi)

Boas práticas de storytelling aplicadas:
  - Paleta navy + laranja-âncora + cinza-neutro (máx 3 cores/tela)
  - Big Number destacado em laranja (atributo pré-atencional de cor)
  - Insight IA em azul-informação, separado visualmente do big number
  - Hierarquia: Pergunta > Big Number / Insight > Gráficos > Tabela
  - Data-Ink ratio alto: sem grades desnecessárias, sem sombras
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ── Diretório de saída ──────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "..", "..", "aula", "semana12", "wireframes")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Paleta de cores (storytelling-first) ────────────────────────────────────
C = {
    "bg"         : "#F5F7FA",
    "navy"       : "#1B2B4B",
    "navy_mid"   : "#2C4270",
    "orange"     : "#E87722",
    "orange_bg"  : "#FFF3E8",
    "white"      : "#FFFFFF",
    "gray_100"   : "#F8F9FA",
    "gray_200"   : "#E9ECEF",
    "gray_400"   : "#CED4DA",
    "gray_600"   : "#6C757D",
    "gray_800"   : "#343A40",
    "green"      : "#2E8B57",
    "red"        : "#C0392B",
    "blue_chart" : "#5B8EC5",
    "ai_bg"      : "#EDF5FF",
    "ai_border"  : "#3A7EC5",
    "divider"    : "#DEE2E6",
}

# ── Dados de cada grupo ──────────────────────────────────────────────────────
GROUPS = [
    dict(
        id=1, slug="olist",
        name="Grupo 1 — E-commerce (Olist)",
        dataset="Brazilian E-Commerce Public Dataset",
        kaggle="kaggle.com/olistbr/brazilian-ecommerce",
        dor="Atrasos na entrega derrubam avaliações e aumentam o churn de vendedores parceiros",
        q1="Q1: Em quais estados e categorias os atrasos são mais críticos\ne qual o impacto nas avaliações (review_score)?",
        q2="Q2: Como o tempo de entrega (dias) se correlaciona\ncom o review_score do cliente?",
        big_num="34,3%", big_label="pedidos entregues com atraso em SP\nmeta: ≤ 26%",
        delta="▲ +8pp acima da meta", delta_ok=False,
        insight='Eletrônicos têm 2,4× mais atrasos\nque a média. Priorizar logística\nnessa categoria pode aumentar o\nreview: 3,2 → 4,1 estrelas.',
        chart1=("Mapa Coroplético",      "Estado × % Atraso"),
        chart2=("Barras Horizontais",    "Top 10 Categorias × % Atraso"),
        chart3=("Scatter Plot",          "Tempo Entrega (dias) × Review Score"),
        chart4=("Linha Temporal",        "Volume de Atrasos/Mês — 12 meses"),
        cta="Redesenhar rota logística de Eletrônicos em SP até Q3 2026",
        table_cols=["Estado",  "Pedidos",  "% Atraso", "Review Médio", "Impacto Receita"],
        table_rows=[
            ["SP",  "41.746", "34,3%", "3,8 ★",  "R$ 2,1M"],
            ["RJ",  "12.852", "28,1%", "4,0 ★",  "R$ 890k"],
            ["MG",  "11.635", "24,7%", "4,1 ★",  "R$ 720k"],
            ["RS",   "8.970", "31,2%", "3,7 ★",  "R$ 540k"],
            ["PR",   "7.218", "22,5%", "4,2 ★",  "R$ 380k"],
        ],
    ),
    dict(
        id=2, slug="rh_ibm",
        name="Grupo 2 — People Analytics (IBM HR)",
        dataset="IBM HR Analytics Employee Attrition",
        kaggle="kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset",
        dor="Turnover de 28% em TI custa R$ 450k/ano em recrutamento e perda de conhecimento",
        q1="Q1: Qual perfil de funcionário tem maior risco\nde saída e em qual departamento?",
        q2="Q2: Satisfação no trabalho e faixa salarial\ninfluenciam significativamente o turnover?",
        big_num="28%", big_label="turnover em TI\nmédia geral: 11%",
        delta="▲ 2,5× acima da média", delta_ok=False,
        insight='Funcionários com < 2 anos + sem\npromoção nos últimos 3 anos têm\n3× mais risco de saída. Programa\nde retenção pode economizar R$ 270k/ano.',
        chart1=("Barras Horizontais",    "Departamento × Turnover (%)"),
        chart2=("Heatmap",               "Satisfação × Faixa Salarial × Turnover"),
        chart3=("Scatter Plot",          "Anos na Empresa × P(Saída)"),
        chart4=("Bullet Chart",          "Turnover Atual vs Meta — por Depto."),
        cta="Implantar mentoria para funcionários < 2 anos em TI e Vendas até junho/2026",
        table_cols=["Depto.",      "Funcionários", "Turnover", "Custo Est.", "Score Sat."],
        table_rows=[
            ["TI",         "127", "28%",  "R$ 213k", "3,1 / 5"],
            ["Vendas",     "152", "21%",  "R$ 190k", "3,4 / 5"],
            ["RH",          "63", "14%",  "R$  52k", "3,9 / 5"],
            ["Financeiro",  "82", "10%",  "R$  49k", "4,1 / 5"],
            ["Operações",   "94",  "8%",  "R$  45k", "4,3 / 5"],
        ],
    ),
    dict(
        id=3, slug="superstore",
        name="Grupo 3 — Varejo (Superstore)",
        dataset="Sample Superstore Dataset",
        kaggle="kaggle.com/vivek468/superstore-dataset-final",
        dor="Margens negativas em Tecnologia/Sul drenam R$ 120k/trimestre do lucro operacional",
        q1="Q1: Quais combinações de produto × região\ngeram prejuízo consistente?",
        q2="Q2: Existe correlação entre nível de desconto\ne margem negativa?",
        big_num="−4,2%", big_label="margem em Tecnologia/Sul\nmeta: +8%",
        delta="▼ 12,2pp abaixo da meta", delta_ok=False,
        insight='Descontos > 20% em Hardware\nconcentram 73% do prejuízo.\nCapear em 12% pode reverter\nmargem para +5,8% (+R$ 85k/trim).',
        chart1=("Mapa de Calor",         "Subcategoria × Região × Margem (%)"),
        chart2=("Scatter Plot",          "Desconto (%) × Lucro (R$)"),
        chart3=("Barras Agrupadas",      "Subcategoria × Margem por Região"),
        chart4=("Linha Temporal",        "Margem Trimestral — Tecnologia/Sul"),
        cta="Implementar desconto máximo 12% em Tecnologia/Sul no próximo trimestre",
        table_cols=["Subcategoria",   "Região", "Receita",  "Desc. Médio", "Margem"],
        table_rows=[
            ["Máquinas",    "Sul",    "R$ 480k", "24%", "−8,1%"],
            ["Copiadoras",  "Sul",    "R$ 310k", "22%", "−5,4%"],
            ["Acessórios",  "Sul",    "R$ 190k", "18%", "−2,3%"],
            ["Máquinas",    "Centro", "R$ 550k", "11%", "+3,2%"],
            ["Copiadoras",  "Norte",  "R$ 280k",  "8%", "+9,1%"],
        ],
    ),
    dict(
        id=4, slug="saude",
        name="Grupo 4 — Saúde Pública (Heart Disease)",
        dataset="Heart Disease UCI Dataset",
        kaggle="kaggle.com/johnsmith88/heart-disease-dataset",
        dor="Doenças cardíacas = 38% das internações municipais (custo médio R$ 12k/internação)",
        q1="Q1: Quais fatores de risco têm maior\ncorrelação com diagnóstico de doença cardíaca?",
        q2="Q2: Qual faixa etária e perfil clínico\npriorizar em campanhas preventivas?",
        big_num="68%", big_label="prob. de doença em\nhomens > 55 anos",
        delta="▲ 4,5× acima da média geral (15%)", delta_ok=False,
        insight='Colesterol > 240 + pressão > 140\n+ idade > 55 identificam 73%\ndos casos de alto risco com apenas\n3 variáveis — triagem pode reduzir\ninternações em 25%.',
        chart1=("Barras Horizontais",    "Fator de Risco × Correlação com Doença"),
        chart2=("Heatmap",               "Faixa Etária × Combinação de Fatores"),
        chart3=("Scatter Plot",          "Colesterol × Pressão (cor = diagnóstico)"),
        chart4=("Boxplot",               "Distribuição de Idade por Grupo Diagnóstico"),
        cta="Implantar triagem preventiva gratuita para homens > 55 com colesterol > 240",
        table_cols=["Perfil",         "Faixa Etária", "Colesterol", "Pressão",  "% Doença"],
        table_rows=[
            ["Alto Risco M",  "> 55",  "> 240",    "> 140",    "68%"],
            ["Alto Risco F",  "> 60",  "> 250",    "> 145",    "41%"],
            ["Médio Risco M", "45–55", "200–240",  "130–140",  "34%"],
            ["Médio Risco F", "50–60", "210–250",  "130–145",  "22%"],
            ["Baixo Risco",   "< 45",  "< 200",    "< 130",     "8%"],
        ],
    ),
    dict(
        id=5, slug="fintech",
        name="Grupo 5 — Fintech (Credit Card Churn)",
        dataset="Credit Card Customers Dataset",
        kaggle="kaggle.com/sakshigoyal7/credit-card-customers",
        dor="Churn de cartão Premium custa R$ 2,1M/ano em receita perdida de juros e anuidade",
        q1="Q1: Qual perfil de cliente Premium tem\nmaior propensão ao cancelamento?",
        q2="Q2: Frequência de uso e limite de crédito\ninfluenciam significativamente o churn?",
        big_num="26,4%", big_label="churn em Premium\ncom limite < R$ 10k",
        delta="▲ 3,2× acima do benchmark (8%)", delta_ok=False,
        insight='Clientes com < 20 transações/ano\n+ saldo decrescente há 3 meses\ntêm 4× mais chance de churn.\nContato proativo preserva R$ 1,2M/ano.',
        chart1=("Barras Horizontais",    "Faixa de Limite × Churn (%)"),
        chart2=("Scatter Plot",          "Freq. de Uso × Valor Médio (cor=churn)"),
        chart3=("Linha Temporal",        "Churn Mensal por Segmento — 12 meses"),
        chart4=("Heatmap",               "Atividade × Limite × Taxa de Churn"),
        cta="Contato proativo para Premium < R$10k com < 20 trans/ano — início imediato",
        table_cols=["Segmento",         "Clientes", "Churn",  "Receita em Risco", "Economia Est."],
        table_rows=[
            ["Premium < R$10k",  "1.240", "26,4%", "R$ 820k", "R$ 492k"],
            ["Premium R$10–30k", "2.150", "14,2%", "R$ 730k", "R$ 438k"],
            ["Premium > R$30k",    "890",  "8,1%", "R$ 520k", "R$ 312k"],
            ["Standard < R$10k", "3.800", "18,3%", "R$ 390k", "R$ 234k"],
            ["Standard R$10k+",  "2.900", "11,5%", "R$ 290k", "R$ 174k"],
        ],
    ),
]


# ── Funções auxiliares de desenho ────────────────────────────────────────────

def rbox(ax, x, y, w, h, fc, ec="none", lw=0.8, zorder=2, radius=0.008):
    """Desenha um retângulo arredondado (coordenadas de axes 0-1)."""
    from matplotlib.patches import FancyBboxPatch
    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad={radius}",
        facecolor=fc, edgecolor=ec, linewidth=lw,
        transform=ax.transAxes, clip_on=False, zorder=zorder,
    )
    ax.add_patch(box)


def txt(ax, x, y, s, fs=9, color=C["gray_800"], ha="center", va="center",
        weight="normal", style="normal", ls=1.35, zorder=3):
    """Adiciona texto com coordenadas de axes."""
    ax.text(
        x, y, s, transform=ax.transAxes,
        fontsize=fs, color=color, ha=ha, va=va,
        fontweight=weight, fontstyle=style, linespacing=ls,
        clip_on=False, zorder=zorder,
    )


def mini_bars_v(ax, x, y, w, h, n=5, highlight_idx=0):
    """Mini gráfico de barras verticais decorativo."""
    rng = np.random.RandomState(42)
    vals = rng.uniform(0.25, 1.0, n)
    vals[highlight_idx] = max(vals)
    bw = w / (n * 1.6)
    gap = (w - bw * n) / (n - 1) if n > 1 else 0
    for i, v in enumerate(vals):
        bx = x + i * (bw + gap)
        col = C["orange"] if i == highlight_idx else C["blue_chart"]
        rect = mpatches.Rectangle(
            (bx, y), bw, h * v,
            facecolor=col, edgecolor="none",
            transform=ax.transAxes, clip_on=False, zorder=4,
        )
        ax.add_patch(rect)


def mini_bars_h(ax, x, y, w, h, n=5):
    """Mini gráfico de barras horizontais."""
    rng = np.random.RandomState(7)
    vals = rng.uniform(0.2, 1.0, n)
    vals[0] = 1.0
    bh = h / (n * 1.6)
    gap = (h - bh * n) / (n - 1) if n > 1 else 0
    for i, v in enumerate(vals):
        by = y + h - i * (bh + gap) - bh
        col = C["orange"] if i == 0 else C["blue_chart"]
        rect = mpatches.Rectangle(
            (x, by), w * v, bh,
            facecolor=col, edgecolor="none",
            transform=ax.transAxes, clip_on=False, zorder=4,
        )
        ax.add_patch(rect)


def mini_scatter(ax, x, y, w, h):
    """Mini scatter plot."""
    rng = np.random.RandomState(13)
    xs = x + rng.uniform(0.05, 0.95, 18) * w
    ys = y + rng.uniform(0.05, 0.95, 18) * h
    classes = rng.randint(0, 2, 18)
    for sx, sy, cls in zip(xs, ys, classes):
        col = C["orange"] if cls else C["blue_chart"]
        dot = mpatches.Circle(
            (sx, sy), 0.006,
            facecolor=col, edgecolor="none", alpha=0.8,
            transform=ax.transAxes, clip_on=False, zorder=4,
        )
        ax.add_patch(dot)


def mini_line(ax, x, y, w, h):
    """Mini gráfico de linha com tendência."""
    rng = np.random.RandomState(21)
    n = 12
    xs = np.linspace(x + 0.01, x + w - 0.01, n)
    base = np.linspace(0.25, 0.75, n)
    noise = rng.uniform(-0.08, 0.08, n)
    ys = y + h * np.clip(base + noise, 0.05, 0.95)
    for i in range(n - 1):
        ax.plot(
            [xs[i], xs[i + 1]], [ys[i], ys[i + 1]],
            color=C["navy"], linewidth=2.0,
            transform=ax.transAxes, clip_on=False, zorder=4,
        )


def mini_heatmap(ax, x, y, w, h):
    """Mini heatmap (grade colorida)."""
    rng = np.random.RandomState(99)
    rows, cols = 4, 5
    cw = w / cols
    ch = h / rows
    for r in range(rows):
        for c in range(cols):
            v = rng.uniform(0, 1)
            col = plt.cm.RdYlGn(v)
            rect = mpatches.Rectangle(
                (x + c * cw, y + r * ch), cw * 0.92, ch * 0.85,
                facecolor=col, edgecolor="white", linewidth=0.5,
                transform=ax.transAxes, clip_on=False, zorder=4,
            )
            ax.add_patch(rect)


CHART_DRAWERS = [mini_bars_v, mini_bars_h, mini_scatter, mini_line, mini_heatmap]


def draw_chart_box(ax, x, y, w, h, title, subtitle, chart_type):
    """Desenha um card de gráfico com placeholder visual."""
    rbox(ax, x, y, w, h, fc=C["gray_100"], ec=C["gray_400"], lw=0.7)
    # Rótulo do tipo de gráfico
    txt(ax, x + w / 2, y + h - 0.015, title.upper(),
        fs=6.5, color=C["gray_600"], weight="bold")
    # Subtítulo com a métrica
    txt(ax, x + w / 2, y + h - 0.032, subtitle,
        fs=8.0, color=C["navy"], weight="bold")
    # Mini visual decorativo
    pad = 0.035
    inner_x = x + pad
    inner_y = y + pad * 0.6
    inner_w = w - 2 * pad
    inner_h = h - 0.060
    drawer = CHART_DRAWERS[chart_type % len(CHART_DRAWERS)]
    if drawer == mini_bars_v:
        drawer(ax, inner_x, inner_y, inner_w, inner_h, highlight_idx=0)
    else:
        drawer(ax, inner_x, inner_y, inner_w, inner_h)


# ── Função principal de geração ──────────────────────────────────────────────

def generate_wireframe(g):
    fig = plt.figure(figsize=(14, 20))
    fig.patch.set_facecolor(C["bg"])
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    PAD = 0.030          # margem horizontal
    W = 1 - 2 * PAD     # largura do conteúdo
    GAP = 0.012          # gap entre colunas
    HALF = (W - GAP) / 2
    y = 0.980            # cursor vertical (de cima para baixo)

    # ── CABEÇALHO ────────────────────────────────────────────────────────────
    H = 0.058
    rbox(ax, PAD, y - H, W, H, fc=C["navy"])
    txt(ax, 0.5, y - H / 2, g["name"], fs=15, color="white", weight="bold")
    y -= H + 0.006

    H = 0.026
    rbox(ax, PAD, y - H, W, H, fc=C["gray_200"])
    txt(ax, 0.5, y - H / 2,
        f"Dataset: {g['dataset']}   •   {g['kaggle']}",
        fs=8.5, color=C["gray_600"])
    y -= H + 0.006

    H = 0.024
    rbox(ax, PAD, y - H, W, H, fc=C["orange_bg"], ec=C["orange"], lw=1.2)
    txt(ax, 0.5, y - H / 2, f"DOR:  {g['dor']}",
        fs=8.0, color=C["navy"])
    y -= H + 0.016

    # ── PERGUNTA 1 ───────────────────────────────────────────────────────────
    H = 0.034
    rbox(ax, PAD, y - H, W, H, fc=C["navy_mid"])
    txt(ax, PAD + 0.014, y - H / 2, g["q1"].replace("\n", "  "),
        fs=9.5, color="white", ha="left", weight="bold")
    y -= H + 0.010

    # ── BIG NUMBER + INSIGHT IA ───────────────────────────────────────────────
    CARD_H = 0.120
    # Big Number
    rbox(ax, PAD, y - CARD_H, HALF, CARD_H, fc=C["white"], ec=C["gray_400"], lw=1.5)
    txt(ax, PAD + HALF / 2, y - 0.022, "BIG NUMBER",
        fs=7.5, color=C["gray_600"], weight="bold")
    txt(ax, PAD + HALF / 2, y - 0.065, g["big_num"],
        fs=36, color=C["orange"], weight="bold")
    txt(ax, PAD + HALF / 2, y - 0.092, g["big_label"],
        fs=9, color=C["gray_600"], ls=1.4)
    delta_color = C["red"] if not g["delta_ok"] else C["green"]
    txt(ax, PAD + HALF / 2, y - 0.112, g["delta"],
        fs=8.5, color=delta_color, weight="bold")

    # Insight IA
    ix = PAD + HALF + GAP
    rbox(ax, ix, y - CARD_H, HALF, CARD_H, fc=C["ai_bg"], ec=C["ai_border"], lw=2.0)
    txt(ax, ix + HALF / 2, y - 0.020, "[IA]  INSIGHT GERADO POR IA",
        fs=8.0, color=C["ai_border"], weight="bold")
    txt(ax, ix + HALF / 2, y - 0.068,
        f'"{g["insight"]}"',
        fs=8.5, color=C["gray_800"], style="italic", ls=1.45)
    y -= CARD_H + 0.012

    # ── GRÁFICOS 1 e 2 ───────────────────────────────────────────────────────
    CH = 0.145
    draw_chart_box(ax, PAD, y - CH, HALF, CH, *g["chart1"], chart_type=1)
    draw_chart_box(ax, PAD + HALF + GAP, y - CH, HALF, CH, *g["chart2"], chart_type=0)
    y -= CH + 0.014

    # ── PERGUNTA 2 ───────────────────────────────────────────────────────────
    H = 0.034
    rbox(ax, PAD, y - H, W, H, fc=C["navy"])
    txt(ax, PAD + 0.014, y - H / 2, g["q2"].replace("\n", "  "),
        fs=9.5, color="white", ha="left", weight="bold")
    y -= H + 0.010

    # ── GRÁFICOS 3 e 4 ───────────────────────────────────────────────────────
    draw_chart_box(ax, PAD, y - CH, HALF, CH, *g["chart3"], chart_type=2)
    draw_chart_box(ax, PAD + HALF + GAP, y - CH, HALF, CH, *g["chart4"], chart_type=3)
    y -= CH + 0.014

    # ── TABELA ANALÍTICA FINAL ────────────────────────────────────────────────
    H_THDR = 0.030
    rbox(ax, PAD, y - H_THDR, W, H_THDR, fc=C["navy"])
    txt(ax, PAD + 0.014, y - H_THDR / 2, "TABELA ANALÍTICA FINAL",
        fs=8.5, color="white", ha="left", weight="bold")
    y -= H_THDR

    ncols = len(g["table_cols"])
    col_w = W / ncols
    ROW_H = 0.028

    # Cabeçalho
    rbox(ax, PAD, y - ROW_H, W, ROW_H, fc=C["gray_200"], ec=C["gray_400"], lw=0.5)
    for ci, col in enumerate(g["table_cols"]):
        txt(ax, PAD + col_w * ci + col_w / 2, y - ROW_H / 2, col,
            fs=8.0, color=C["gray_800"], weight="bold")
    y -= ROW_H

    # Linhas de dados
    for ri, row in enumerate(g["table_rows"]):
        fc = C["white"] if ri % 2 == 0 else C["gray_100"]
        rbox(ax, PAD, y - ROW_H, W, ROW_H, fc=fc, ec=C["gray_200"], lw=0.3)
        for ci, val in enumerate(row):
            col_color = C["gray_800"]
            if ci == 2:  # coluna de % ou margem
                s = str(val).replace("%", "").replace(",", ".").replace("−", "-")
                try:
                    if float(s) < 0 or float(s) > 22:
                        col_color = C["red"]
                    elif float(s) < 10:
                        col_color = C["green"]
                except ValueError:
                    pass
            txt(ax, PAD + col_w * ci + col_w / 2, y - ROW_H / 2, str(val),
                fs=7.5, color=col_color)
        y -= ROW_H

    y -= 0.012

    # ── CALL TO ACTION ────────────────────────────────────────────────────────
    H = 0.032
    rbox(ax, PAD, y - H, W, H, fc=C["orange"])
    txt(ax, 0.5, y - H / 2, f"CALL TO ACTION:   {g['cta']}",
        fs=9.0, color="white", weight="bold")

    # ── SALVAR ────────────────────────────────────────────────────────────────
    fname = f"wireframe_grupo{g['id']}_{g['slug']}.png"
    fpath = os.path.join(OUTPUT_DIR, fname)
    plt.savefig(fpath, dpi=150, bbox_inches="tight", facecolor=C["bg"])
    plt.close(fig)
    print(f"  ✓  {fname}")


# ── Execução ─────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"\nGerando {len(GROUPS)} wireframes em:\n  {os.path.abspath(OUTPUT_DIR)}\n")
    for group in GROUPS:
        generate_wireframe(group)
    print("\nConcluído!\n")
