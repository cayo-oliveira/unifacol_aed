"""
Gera imagens didaticas complementares para semana_especial.tex.

As figuras sao estaticas e pensadas para o PDF: explicam conceitos que
ficariam abstratos se aparecessem apenas em texto ou em HTML interativo.
"""

import os
import textwrap

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches


BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "outputs")
os.makedirs(OUT, exist_ok=True)

COLORS = {
    "brand": "#0B3D2E",
    "blue": "#2563EB",
    "orange": "#E35D22",
    "red": "#DC2626",
    "green": "#16A34A",
    "yellow": "#EAB308",
    "gray": "#64748B",
    "light": "#F8FAFC",
    "line": "#CBD5E1",
    "text": "#0F172A",
}

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
})


def wrap(text, width=32):
    return "\n".join(textwrap.wrap(text, width=width))


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=160, bbox_inches="tight")
    plt.close(fig)
    print(name)


def setup(title, subtitle=None, figsize=(12, 7)):
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")
    ax.text(0.25, 6.65, title, fontsize=18, fontweight="bold", color=COLORS["text"], va="top")
    if subtitle:
        ax.text(0.25, 6.25, subtitle, fontsize=10.5, color=COLORS["gray"], va="top")
    return fig, ax


def card(ax, x, y, w, h, title, body="", color="#2563EB", fill="#FFFFFF", lw=1.2):
    box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                 linewidth=lw, edgecolor=color, facecolor=fill)
    ax.add_patch(box)
    ax.text(x + 0.18, y + h - 0.25, title, fontsize=10.5, fontweight="bold", color=color, va="top")
    if body:
        ax.text(x + 0.18, y + h - 0.65, wrap(body, 38), fontsize=8.8, color=COLORS["text"], va="top")


def arrow(ax, x1, y1, x2, y2, color=None):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", lw=1.8, color=color or COLORS["gray"]))


def draw_mini_dash(ax, x, y, w, h, title, good=True, accent="#E35D22"):
    ax.add_patch(patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.06",
                                        facecolor="#FFFFFF", edgecolor="#CBD5E1", linewidth=1.0))
    ax.add_patch(patches.Rectangle((x, y + h - 0.42), w, 0.42, color="#E2E8F0" if good else "#94A3B8"))
    ax.text(x + 0.15, y + h - 0.13, title, fontsize=8.2, fontweight="bold", va="top", color=COLORS["text"])
    if good:
        for i, val in enumerate([0.88, 0.66, 0.42]):
            ax.add_patch(patches.Rectangle((x + 0.25, y + h - 0.95 - i * 0.45), val * (w - 0.65), 0.18,
                                           color=accent if i == 0 else "#CBD5E1"))
        ax.add_patch(patches.Rectangle((x + 0.25, y + 0.35), w - 0.5, 0.55, facecolor="#FEF3C7", edgecolor=accent))
        ax.text(x + 0.38, y + 0.73, "acao + responsavel + prazo", fontsize=6.6, color=COLORS["text"])
    else:
        palette = ["#EF4444", "#F59E0B", "#10B981", "#3B82F6", "#8B5CF6", "#EC4899"]
        for i in range(6):
            ax.add_patch(patches.Rectangle((x + 0.22 + (i % 2) * (w / 2 - 0.15),
                                            y + 0.35 + (i // 2) * 0.58),
                                           w / 2 - 0.35, 0.34, color=palette[i]))
        ax.text(x + 0.2, y + h - 0.75, "15 graficos, sem hierarquia", fontsize=6.5, color=COLORS["text"])


def fundamentos():
    fig, ax = setup("Caminho do olhar: F, Z e leitura por perfil",
                    "O layout deve combinar com quem decide: analista, gerente ou CEO.")
    for x, label, color in [(0.7, "Analista: F", COLORS["blue"]), (4.4, "Executivo: Z", COLORS["orange"]), (8.1, "Gerente: KPI + tabela", COLORS["green"])]:
        draw_mini_dash(ax, x, 1.0, 3.0, 4.4, label, True, color)
    ax.plot([1.05, 3.1, 1.05, 2.45, 1.05, 1.05], [4.8, 4.8, 3.9, 3.9, 3.2, 1.5], color=COLORS["blue"], lw=3)
    ax.plot([4.75, 7.0, 4.75, 7.0], [4.8, 4.8, 1.55, 1.55], color=COLORS["orange"], lw=3)
    ax.plot([8.45, 10.7, 10.7], [4.8, 4.8, 1.55], color=COLORS["green"], lw=3)
    save(fig, "cap1_02_caminho_olhar.png")

    fig, ax = setup("Carga cognitiva: dashboard pesado vs dashboard cognitivo",
                    "A carga extrinseca vem do design ruim; ela pode ser removida.")
    draw_mini_dash(ax, 0.8, 1.2, 4.7, 4.5, "Antes: carga extrinseca alta", False)
    draw_mini_dash(ax, 6.5, 1.2, 4.7, 4.5, "Depois: carga util", True)
    arrow(ax, 5.65, 3.5, 6.35, 3.5, COLORS["orange"])
    ax.text(5.35, 3.9, "remover\nruido", fontsize=9, color=COLORS["orange"], ha="center")
    save(fig, "cap1_03_carga_cognitiva.png")

    fig, ax = setup("Insight informativo: aumenta entendimento, mas nao decide",
                    "Bom para EDA e diagnostico tecnico; insuficiente para reuniao executiva.")
    card(ax, 0.9, 3.6, 4.8, 1.7, "Painel informativo", "Churn subiu de 10% para 12%. Clientes Premium tem ticket 3,2x maior.", COLORS["blue"], "#EFF6FF")
    card(ax, 6.4, 3.6, 4.8, 1.7, "Pergunta que ainda fica", "Isso e grave? Quem deve agir? Qual acao reduz o churn? Qual impacto esperado?", COLORS["gray"], "#F8FAFC")
    arrow(ax, 5.8, 4.45, 6.25, 4.45)
    card(ax, 2.7, 1.25, 6.6, 1.2, "Uso correto", "Relatorio exploratorio, discovery com area de negocio e base para formular insights acionaveis.", COLORS["green"], "#F0FDF4")
    save(fig, "cap1_04_insight_informativo.png")

    fig, ax = setup("Insight acionavel: dado + decisao + impacto",
                    "A diferenca e sair de uma observacao para uma recomendacao executavel.")
    draw_mini_dash(ax, 0.75, 1.15, 4.7, 4.55, "Sem acao: so descreve", False)
    draw_mini_dash(ax, 6.55, 1.15, 4.7, 4.55, "Com acao: decide", True, COLORS["red"])
    card(ax, 6.85, 1.6, 4.1, 0.8, "CTA", "Campanha para 285 clientes ate 15/jun. Preserva R$1,2M.", COLORS["red"], "#FEF2F2")
    save(fig, "cap1_05_insight_acionavel.png")

    fig, ax = setup("Dashboard as Code: fluxo conceitual",
                    "O foco aqui e governanca: versionar, revisar, homologar e publicar.")
    steps = [("1. Regra de negocio", "KPI, audiencia, dor"), ("2. Definicao", "dataset, metricas, layout"),
             ("3. Revisao", "PR + validacao"), ("4. Homologacao", "ambiente dev"), ("5. Publicacao", "dashboard prod")]
    x = 0.4
    for i, (t, b) in enumerate(steps):
        card(ax, x + i * 2.25, 2.6, 1.85, 1.55, t, b, COLORS["blue"], "#EFF6FF")
        if i < len(steps) - 1:
            arrow(ax, x + i * 2.25 + 1.9, 3.35, x + (i + 1) * 2.25 - 0.1, 3.35)
    save(fig, "cap1_06_dashboard_as_code_fluxo.png")

    fig, ax = setup("AED automatica: do HTML ao insight",
                    "Os relatorios acham sinais; o professor ensina os alunos a interpretar.")
    card(ax, 0.7, 3.75, 2.6, 1.35, "ydata-profiling", "qualidade, missing, correlacao, outliers", COLORS["blue"], "#EFF6FF")
    card(ax, 3.55, 3.75, 2.6, 1.35, "sweetviz", "comparacao de grupos e variavel alvo", COLORS["orange"], "#FFF7ED")
    card(ax, 6.4, 3.75, 2.6, 1.35, "graficos manuais", "distribuicao, scatter, categorias", COLORS["green"], "#F0FDF4")
    card(ax, 4.0, 1.35, 4.0, 1.25, "Interpretacao em sala", "O que significa? Que decisao ou proxima pergunta nasce daqui?", COLORS["brand"], "#ECFDF5")
    for x in [2.0, 4.85, 7.7]:
        arrow(ax, x, 3.7, 5.8, 2.68)
    save(fig, "cap1_07_autoeda_fluxo.png")

    fig, ax = setup("Engenheiro de Analytics Virtual: agentes end-to-end",
                    "Cada agente tem uma responsabilidade clara e entrega um artefato verificavel.")
    labels = [
        ("Negocio", "dor, KPI, regra"),
        ("Dados", "fonte, schema, qualidade"),
        ("SQL", "tabela, view, metricas"),
        ("EDA", "padroes e anomalias"),
        ("Insight", "acao e impacto"),
        ("Storyboard", "narrativa e layout"),
        ("Prototipo", "HTML validavel"),
        ("Homologacao", "usuario aprova"),
        ("Publicacao", "BI em producao"),
    ]
    positions = [(0.4, 4.65), (3.1, 4.65), (5.8, 4.65), (8.5, 4.65),
                 (8.5, 2.55), (5.8, 2.55), (3.1, 2.55), (0.4, 2.55), (4.45, 0.75)]
    for (t, b), (x, y) in zip(labels, positions):
        card(ax, x, y, 2.25, 1.0, t, b, COLORS["orange"] if t in ["Insight", "Publicacao"] else COLORS["blue"], "#FFFFFF")
    for a, b in zip(positions[:-1], positions[1:]):
        arrow(ax, a[0] + 2.25, a[1] + 0.5, b[0], b[1] + 0.5)
    save(fig, "cap1_08_agentes_analytics_virtual.png")

    fig, ax = setup("Base especializada de insights",
                    "Repositorio de exemplos validados que padroniza a qualidade.")
    card(ax, 0.8, 3.8, 3.2, 1.2, "Exemplos validados", "insights aprovados por gestor, com impacto medido", COLORS["green"], "#F0FDF4")
    card(ax, 4.4, 3.8, 3.2, 1.2, "Busca semantica", "recupera casos parecidos por dominio e padrao", COLORS["blue"], "#EFF6FF")
    card(ax, 8.0, 3.8, 3.2, 1.2, "Novo insight", "gera recomendacao no mesmo padrao de qualidade", COLORS["orange"], "#FFF7ED")
    arrow(ax, 4.05, 4.4, 4.3, 4.4); arrow(ax, 7.65, 4.4, 7.9, 4.4)
    card(ax, 3.2, 1.45, 5.6, 1.15, "Loop de melhoria", "apos 6 meses: comparar impacto estimado vs realizado e atualizar a base.", COLORS["brand"], "#ECFDF5")
    save(fig, "cap1_09_base_insights.png")


def cap2_extra():
    names = [
        ("cap2_01b_dashboard_aed_explanatoria.png", "AED vs Explanatoria em dashboard", "Antes: muitas descobertas soltas. Depois: uma decisao sustentada por poucos visuais."),
        ("cap2_02b_big_idea_dashboard.png", "Dashboard com Big Idea no topo", "A frase principal governa os KPIs, os graficos e o pedido final."),
        ("cap2_03b_com_sem_storyboard.png", "Sem storyboard vs com storyboard", "A narrativa organiza contexto, conflito, resolucao e chamada para acao."),
        ("cap2_04b_preatencao_dashboard.png", "Pre-atencao aplicada ao dashboard", "Cor, tamanho e posicao guiam o olho antes da leitura consciente."),
        ("cap2_05b_relance_dashboard.png", "Teste do relance em dashboard", "Em 3 segundos a audiencia deve captar a mensagem principal."),
        ("cap2_06b_chartjunk_dashboard.png", "Chartjunk removido", "Menos tinta decorativa, mais leitura do dado."),
        ("cap2_07b_interatividade_tableau.png", "Interatividade no Tableau", "Filtro muda linhas; parametro muda calculo; acao conecta views."),
        ("cap2_08b_dashboard_decisorio.png", "Dashboard decisorio completo", "Contexto, diagnostico e recomendacao aparecem como zonas diferentes."),
        ("cap2_09b_kpi_ruim_bom.png", "KPI ruim vs KPI decisorio", "Valor isolado nao decide; meta, gap e tendencia dao contexto."),
        ("cap2_10b_pitch_dashboard.png", "Pitch ancorado no dashboard", "O apresentador percorre situacao, complicacao, resolucao e proximo passo."),
    ]
    for fname, title, subtitle in names:
        fig, ax = setup(title, subtitle)
        draw_mini_dash(ax, 0.8, 1.15, 4.8, 4.6, "Antes / incompleto", False)
        draw_mini_dash(ax, 6.4, 1.15, 4.8, 4.6, "Depois / recomendado", True)
        arrow(ax, 5.75, 3.45, 6.25, 3.45, COLORS["orange"])
        save(fig, fname)


def group_previews():
    data = [
        ("grupo_a_preview.png", "#D62828", "Grupo A - Olist", "Atrasos em Eletronicos/SP reduzem review para 3,2"),
        ("grupo_b_preview.png", "#003DA5", "Grupo B - IBM HR", "Turnover TI 28% vs meta 15%"),
        ("grupo_c_preview.png", "#2E7D52", "Grupo C - Superstore", "Desconto >20% concentra prejuizo"),
        ("grupo_d_preview.png", "#C41E3A", "Grupo D - Saude", "3 sinais clinicos identificam 73% do risco"),
        ("grupo_e_preview.png", "#6F42C1", "Grupo E - FinTech", "Premium baixo uso tem 4x risco de churn"),
    ]
    for fname, color, title, msg in data:
        fig, ax = setup(title, msg)
        draw_mini_dash(ax, 0.7, 0.8, 10.6, 5.1, "Preview do HTML interativo do grupo", True, color)
        ax.text(1.15, 5.35, "Big Number + Insight IA", fontsize=12, fontweight="bold", color=color)
        ax.text(1.15, 4.85, "Diagnostico com dois graficos + tabela analitica + call to action", fontsize=9, color=COLORS["gray"])
        save(fig, fname)


if __name__ == "__main__":
    fundamentos()
    cap2_extra()
    group_previews()
