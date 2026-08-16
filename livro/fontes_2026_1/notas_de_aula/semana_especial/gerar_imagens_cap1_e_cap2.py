#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera imagens para Cap 1 (Fundamentos Avançados) e imagens extras Cap 2.
Execute: python3 gerar_imagens_cap1_e_cap2.py
"""
import os, warnings
warnings.filterwarnings("ignore")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

OUT = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(OUT, exist_ok=True)

DPI = 150
BRAND = "#0B3D2E"
DESTAQUE = "#E35D22"
PRIMARIA = "#2563EB"
POSITIVO = "#16A34A"
ALERTA   = "#DC2626"
ATENCAO  = "#EAB308"
NEUTRA   = "#64748B"
BGCLARO  = "#F1F5F9"
WHITE    = "#FFFFFF"

def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"  ✓ {name}")

# ──────────────────────────────────────────────────────────────────────────────
# CAP 1 — SECTION 2: Caminho do Olhar
# ──────────────────────────────────────────────────────────────────────────────
def cap1_02_caminho_olhar():
    fig, axes = plt.subplots(1, 3, figsize=(15, 6), facecolor=BGCLARO)
    fig.suptitle("Caminho do Olhar: Como Cada Perfil Lê um Dashboard",
                 fontsize=14, fontweight='bold', color=BRAND, y=1.02)

    titles = ["Padrão F\n(Analista)", "Padrão Z\n(Executivo / CEO)", "Diagonal + Tabela\n(Gerente)"]
    colors = [PRIMARIA, DESTAQUE, POSITIVO]

    # ── Padrão F (Analista)
    ax = axes[0]
    ax.set_facecolor(WHITE)
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    ax.set_title(titles[0], fontsize=11, fontweight='bold', color=colors[0], pad=8)

    # Blocos representando conteúdo
    for y, h, alpha in [(8.2, 0.7, 1.0), (6.8, 0.7, 0.8), (5.4, 0.5, 0.4), (4.0, 0.5, 0.3), (2.6, 0.4, 0.2)]:
        ax.add_patch(FancyBboxPatch((0.3, y), 9.4, h, boxstyle="round,pad=0.05",
                                    facecolor="#E8F4FD", edgecolor="#CCDDEE", linewidth=0.5))

    # Seta horizontal topo
    ax.annotate('', xy=(9.5, 8.85), xytext=(0.5, 8.85),
                arrowprops=dict(arrowstyle='->', color=colors[0], lw=2.5))
    ax.text(5, 9.15, "① Lê topo completo", ha='center', fontsize=8, color=colors[0], fontweight='bold')

    # Seta horizontal segunda linha
    ax.annotate('', xy=(9.5, 7.45), xytext=(0.5, 7.45),
                arrowprops=dict(arrowstyle='->', color=colors[0], lw=2.0))
    ax.text(5, 7.75, "② Relê segunda linha", ha='center', fontsize=8, color=colors[0])

    # Seta vertical lado esquerdo
    ax.annotate('', xy=(1.2, 2.0), xytext=(1.2, 6.9),
                arrowprops=dict(arrowstyle='->', color=colors[0], lw=2.0))
    ax.text(2.5, 4.5, "③ Varre\nlado\nesquerdo", ha='center', fontsize=8, color=colors[0])

    ax.text(5, 1.2, "→ Dado mais importante: 1ª linha, esquerda",
            ha='center', fontsize=7.5, style='italic', color=NEUTRA,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF8E7', edgecolor=ATENCAO, linewidth=1))
    ax.set_xticks([]); ax.set_yticks([])
    for spine in ax.spines.values(): spine.set_visible(False)

    # ── Padrão Z (CEO / Executivo)
    ax = axes[1]
    ax.set_facecolor(WHITE)
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    ax.set_title(titles[1], fontsize=11, fontweight='bold', color=colors[1], pad=8)

    # Zonas
    zonas = [
        (0.3, 7.5, 4.0, 1.8, "#FFF3E0", "BIG NUMBER\n+ Big Idea", DESTAQUE),
        (5.5, 7.5, 4.2, 1.8, "#FFF3E0", "KPI 2 | KPI 3", DESTAQUE),
        (0.3, 1.0, 4.0, 5.0, "#E8F5E9", "Gráfico\nDiagnóstico", POSITIVO),
        (5.5, 1.0, 4.2, 5.0, "#FFE8E8", "CALL TO\nACTION", ALERTA),
    ]
    for x, y, w, h, fc, txt, tc in zonas:
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1",
                                    facecolor=fc, edgecolor=tc, linewidth=1.5))
        ax.text(x + w/2, y + h/2, txt, ha='center', va='center',
                fontsize=8.5, fontweight='bold', color=tc)

    # Setas Z
    setas = [(2.3, 9.0, 7.7, 9.0), (7.7, 9.0, 2.3, 3.5), (2.3, 3.5, 7.7, 3.5)]
    for x1, y1, x2, y2 in setas:
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=colors[1], lw=2.5,
                                   connectionstyle='arc3,rad=0'))

    ax.text(5, 9.3, "← Percurso Z: topo → diagonal → rodapé →",
            ha='center', fontsize=8, color=colors[1], fontweight='bold')
    ax.set_xticks([]); ax.set_yticks([])
    for spine in ax.spines.values(): spine.set_visible(False)

    # ── Gerente: diagonal + tabela
    ax = axes[2]
    ax.set_facecolor(WHITE)
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    ax.set_title(titles[2], fontsize=11, fontweight='bold', color=colors[2], pad=8)

    # KPI zona
    ax.add_patch(FancyBboxPatch((0.3, 7.5), 9.4, 1.8, boxstyle="round,pad=0.1",
                                facecolor="#E8F5E9", edgecolor=POSITIVO, linewidth=1.5))
    ax.text(5, 8.4, "KPI Principal (vai direto aqui confirmar hipótese)",
            ha='center', fontsize=8, fontweight='bold', color=POSITIVO)

    # Gráfico zona
    ax.add_patch(FancyBboxPatch((0.3, 4.0), 9.4, 3.0, boxstyle="round,pad=0.1",
                                facecolor="#EEF2FF", edgecolor=PRIMARIA, linewidth=1.5))
    ax.text(5, 5.5, "Gráfico de detalhe\n(confirma ou refuta hipótese)",
            ha='center', fontsize=8.5, color=PRIMARIA)

    # Tabela zona (importante para gerente!)
    ax.add_patch(FancyBboxPatch((0.3, 0.8), 9.4, 2.7, boxstyle="round,pad=0.1",
                                facecolor="#FFF9E7", edgecolor=ATENCAO, linewidth=2))
    ax.text(5, 2.2, "📋 Tabela de Detalhe\n(salva o gerente das exceções)",
            ha='center', fontsize=9, fontweight='bold', color="#8B5E00")

    # Seta do gerente
    ax.annotate('', xy=(5, 4.2), xytext=(5, 7.3),
                arrowprops=dict(arrowstyle='->', color=colors[2], lw=2.5))
    ax.annotate('', xy=(5, 1.1), xytext=(5, 3.8),
                arrowprops=dict(arrowstyle='->', color=ATENCAO, lw=2.5))

    ax.text(5, 0.3, "→ Ofereça SEMPRE tabela de detalhe no rodapé",
            ha='center', fontsize=7.5, style='italic', color=NEUTRA,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF8E7', edgecolor=ATENCAO, linewidth=1))
    ax.set_xticks([]); ax.set_yticks([])
    for spine in ax.spines.values(): spine.set_visible(False)

    fig.tight_layout(pad=1.5)
    save(fig, "cap1_02_caminho_olhar.png")

# ──────────────────────────────────────────────────────────────────────────────
# CAP 1 — SECTION 3: Carga Cognitiva (Dashboard antes/depois)
# ──────────────────────────────────────────────────────────────────────────────
def cap1_03_carga_cognitiva():
    fig, axes = plt.subplots(1, 2, figsize=(15, 7), facecolor=BGCLARO)
    fig.suptitle("Carga Cognitiva: Dashboard com Carga Alta vs Carga Baixa",
                 fontsize=13, fontweight='bold', color=BRAND, y=1.02)

    # ── ESQUERDA: Alta Carga Cognitiva (ruim)
    ax = axes[0]
    ax.set_facecolor("#F5F5F5")
    ax.set_xlim(0, 12); ax.set_ylim(0, 10)
    ax.set_title("❌  Alta Carga Cognitiva\n(Design Ruim — Evitar)", fontsize=11,
                 fontweight='bold', color=ALERTA, pad=8)

    # Cabeçalho pesado
    ax.add_patch(FancyBboxPatch((0, 8.5), 12, 1.3, boxstyle="square",
                                facecolor="#333333", edgecolor="black", linewidth=2))
    ax.text(6, 9.15, "RELATÓRIO DE PERFORMANCE Q1/2026 — v3.2 final-FINAL-revisado",
            ha='center', va='center', fontsize=7, color='white', fontweight='bold')

    # 4 gauges/velocímetros (chartjunk)
    colors_bad = ['#FF0000', '#00AA00', '#0000FF', '#FF8800']
    labels_bad = ['Receita', 'Lucro', 'NPS', 'Churn']
    vals_bad   = [0.72, 0.55, 0.83, 0.48]
    for i, (c, l, v) in enumerate(zip(colors_bad, labels_bad, vals_bad)):
        cx = 1.5 + i * 2.8
        theta = np.linspace(np.pi, 0, 100)
        ax.plot(cx + 0.9*np.cos(theta), 5.5 + 0.9*np.sin(theta), color='#CCCCCC', lw=6)
        ax.plot(cx + 0.9*np.cos(theta[:int(v*100)]),
                5.5 + 0.9*np.sin(theta[:int(v*100)]), color=c, lw=6)
        ax.text(cx, 4.3, f"{int(v*100)}%", ha='center', fontsize=10, fontweight='bold', color=c)
        ax.text(cx, 3.9, l, ha='center', fontsize=7.5, color='gray')
        ax.text(cx, 6.55, f"Meta: {int((v+0.1)*100)}%", ha='center', fontsize=6.5, color='gray')

    # Legendas confusas com muitas cores
    for i, (c, l) in enumerate(zip(['#FF0000','#00AA00','#0000FF','#FF8800','#AA00AA','#008888'],
                                    ['Cat A','Cat B','Cat C','Cat D','Cat E','Cat F'])):
        ax.add_patch(mpatches.Rectangle((0.3 + i*1.8, 2.8), 0.3, 0.3, facecolor=c))
        ax.text(0.65 + i*1.8, 2.95, l, fontsize=7, va='center')

    # Tabela cheia de dados no meio
    for row in range(5):
        for col in range(6):
            ax.add_patch(FancyBboxPatch((0.2 + col*1.9, 0.4 + row*0.38), 1.7, 0.32,
                                        boxstyle="square", facecolor='white', edgecolor='#AAAAAA', linewidth=0.5))
            ax.text(1.05 + col*1.9, 0.56 + row*0.38,
                    f"{np.random.randint(100,9999)}", ha='center', va='center', fontsize=6)

    # Setas de "atenção" espalhadas
    for x, y in [(2,7.5),(7,7),(10,6.5),(4,3.5)]:
        ax.annotate('', xy=(x, y-0.3), xytext=(x, y+0.3),
                    arrowprops=dict(arrowstyle='->', color='red', lw=1.5))

    ax.text(6, -0.3, "Problemas: gauges ilegíveis · legenda separada · tabela desnecessária · 6 cores sem propósito",
            ha='center', fontsize=7, color=ALERTA, style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFEEEE', edgecolor=ALERTA))
    ax.set_xticks([]); ax.set_yticks([])
    for spine in ax.spines.values(): spine.set_visible(False)

    # ── DIREITA: Baixa Carga Cognitiva (bom)
    ax = axes[1]
    ax.set_facecolor(WHITE)
    ax.set_xlim(0, 12); ax.set_ylim(0, 10)
    ax.set_title("✅  Baixa Carga Cognitiva\n(Design Cognitivo — Recomendado)", fontsize=11,
                 fontweight='bold', color=POSITIVO, pad=8)

    # Cabeçalho limpo
    ax.add_patch(FancyBboxPatch((0, 8.5), 12, 1.3, boxstyle="round,pad=0.1",
                                facecolor=BRAND, edgecolor="none"))
    ax.text(6, 9.15, "Churn subiu 3 pp — ação necessária esta semana",
            ha='center', va='center', fontsize=10.5, color='white', fontweight='bold')

    # 4 KPI cards limpos
    kpi_data = [
        (ALERTA, "18%", "Churn", "Meta 15% ▲ +3pp"),
        (POSITIVO, "R$2,4M", "Receita MTD", "Meta atingida ✓"),
        (ATENCAO, "42", "NPS", "Meta 50 — atenção"),
        (PRIMARIA, "73%", "Retenção", "Meta 80% — ok"),
    ]
    for i, (c, v, l, sub) in enumerate(kpi_data):
        x = 0.3 + i*2.9
        ax.add_patch(FancyBboxPatch((x, 6.5), 2.5, 1.7, boxstyle="round,pad=0.15",
                                    facecolor='white', edgecolor=c, linewidth=2.5))
        ax.text(x+1.25, 7.7, v, ha='center', fontsize=13, fontweight='bold', color=c)
        ax.text(x+1.25, 7.25, l, ha='center', fontsize=8, color=NEUTRA)
        ax.text(x+1.25, 6.85, sub, ha='center', fontsize=7, color='gray')

    # Gráfico de barras limpo (apenas 1 cor de destaque)
    categorias = ['Premium', 'Basic', 'Trial', 'Freemium', 'Legacy']
    valores = [18, 9, 23, 7, 12]
    cores_bar = [ALERTA if v > 15 else NEUTRA for v in valores]
    y_pos = np.arange(len(categorias))
    ax.barh([y + 3.7 for y in [0,1,2,3,4]], valores, height=0.55,
            color=cores_bar, left=0.5)
    for i, v in enumerate(valores):
        ax.text(0.5 + v + 0.2, 3.7 + i, f'{v}%', va='center', fontsize=8,
                fontweight='bold' if v > 15 else 'normal',
                color=ALERTA if v > 15 else NEUTRA)
    for i, c in enumerate(categorias):
        ax.text(0.3, 3.7 + i, c, va='center', ha='right', fontsize=8, color=BRAND)

    ax.text(6, 3.3, "Churn por Segmento — destaque apenas onde está acima da meta",
            ha='center', fontsize=8, color=NEUTRA, style='italic')

    # Linha de meta
    ax.axvline(15.5, ymin=0.3, ymax=0.65, color=ALERTA, linestyle='--', linewidth=1.5, alpha=0.7)
    ax.text(15.7, 5.75, "Meta\n15%", fontsize=7, color=ALERTA)

    # Insight e CTA
    ax.add_patch(FancyBboxPatch((0.3, 0.7), 11.4, 2.3, boxstyle="round,pad=0.15",
                                facecolor="#FFF8E7", edgecolor=DESTAQUE, linewidth=2))
    ax.text(6, 2.45, "Insight: Segmento Trial concentra 23% de churn (meta: 15%).",
            ha='center', fontsize=8.5, fontweight='bold', color=BRAND)
    ax.text(6, 2.0, "Ação: Redesenhar onboarding Trial nos próximos 30 dias.",
            ha='center', fontsize=8.5, color=BRAND)
    ax.text(6, 1.55, "Impacto estimado: redução de 23% → 14%. Responsável: PM + CRM.",
            ha='center', fontsize=8, color=NEUTRA)
    ax.text(6, 1.1, "→ Decisão necessária até: 10/maio/2026", ha='center',
            fontsize=8.5, fontweight='bold', color=ALERTA)

    ax.text(6, 0.3, "Carga cognitiva mínima: 1 destaque · título-mensagem · CTA claro · sem decoração",
            ha='center', fontsize=7, color=POSITIVO, style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#EEFFEE', edgecolor=POSITIVO))
    ax.set_xticks([]); ax.set_yticks([])
    for spine in ax.spines.values(): spine.set_visible(False)

    fig.tight_layout(pad=1.5)
    save(fig, "cap1_03_carga_cognitiva.png")

# ──────────────────────────────────────────────────────────────────────────────
# CAP 1 — SECTION 5: Insights Acionáveis (Dashboard sem vs com)
# ──────────────────────────────────────────────────────────────────────────────
def cap1_05_insights_acionaveis():
    fig, axes = plt.subplots(1, 2, figsize=(15, 7.5), facecolor=BGCLARO)
    fig.suptitle("Dashboard sem Insights Acionáveis vs com Insights Acionáveis",
                 fontsize=13, fontweight='bold', color=BRAND, y=1.02)

    # ── ESQUERDA: sem insight acionável
    ax = axes[0]
    ax.set_facecolor(WHITE)
    ax.set_xlim(0, 12); ax.set_ylim(0, 10)
    ax.set_title("❌  Só Insights Informativos\n(Descreve mas não orienta decisão)", fontsize=10,
                 fontweight='bold', color=ALERTA, pad=8)

    ax.add_patch(FancyBboxPatch((0, 8.5), 12, 1.3, boxstyle="round,pad=0.1",
                                facecolor=NEUTRA, edgecolor="none"))
    ax.text(6, 9.15, "Análise de Vendas — Q1/2026", ha='center', va='center',
            fontsize=11, color='white', fontweight='bold')

    kpis_sem = [("12%", "Taxa de Churn"), ("R$2,1M", "Receita"), ("68", "NPS"), ("42%", "Margem")]
    for i, (v, l) in enumerate(kpis_sem):
        x = 0.5 + i * 2.75
        ax.add_patch(FancyBboxPatch((x, 6.6), 2.4, 1.65, boxstyle="round,pad=0.1",
                                    facecolor='#F8F8F8', edgecolor='#CCCCCC', linewidth=1))
        ax.text(x+1.2, 7.55, v, ha='center', fontsize=14, fontweight='bold', color=NEUTRA)
        ax.text(x+1.2, 7.0, l, ha='center', fontsize=8, color='gray')

    # Gráfico de barras sem destaque
    cats = ['SP', 'RJ', 'MG', 'BA', 'RS', 'PR']
    vals = [42, 35, 28, 22, 19, 15]
    for i, (c, v) in enumerate(zip(cats, vals)):
        ax.bar(1 + i*1.75, v/10, width=1.3, color=PRIMARIA, alpha=0.6)
        ax.text(1 + i*1.75, v/10 + 0.1, f'{v}%', ha='center', fontsize=7.5, color=NEUTRA)
        ax.text(1 + i*1.75, 0.1, c, ha='center', fontsize=8)
    ax.text(6, 6.2, "Receita por Estado", ha='center', fontsize=9, color=NEUTRA)

    # Observações descritivas (não acionáveis)
    obs = [
        "SP concentra 42% da receita total.",
        "O churn subiu de 9% para 12% em Q1.",
        "NPS médio é 68, contra 65 no Q4.",
        "Margem caiu 3pp vs ano anterior.",
    ]
    for i, o in enumerate(obs):
        ax.add_patch(FancyBboxPatch((0.3, 0.3 + i*0.75), 11.4, 0.6, boxstyle="round,pad=0.1",
                                    facecolor='#F5F5F5', edgecolor='#DDDDDD', linewidth=1))
        ax.text(0.7, 0.6 + i*0.75, f"• {o}", fontsize=8, color='gray', va='center')

    ax.text(6, -0.25, "→ Reunião termina com perguntas: 'E daí?' 'O que fazemos?' 'Por que isso?'",
            ha='center', fontsize=8, color=ALERTA, style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFEEEE', edgecolor=ALERTA))
    ax.set_xticks([]); ax.set_yticks([])
    for spine in ax.spines.values(): spine.set_visible(False)

    # ── DIREITA: com insight acionável
    ax = axes[1]
    ax.set_facecolor(WHITE)
    ax.set_xlim(0, 12); ax.set_ylim(0, 10)
    ax.set_title("✅  Insights Acionáveis\n(Prescreve ação específica com impacto e prazo)", fontsize=10,
                 fontweight='bold', color=POSITIVO, pad=8)

    ax.add_patch(FancyBboxPatch((0, 8.5), 12, 1.3, boxstyle="round,pad=0.1",
                                facecolor=BRAND, edgecolor="none"))
    ax.text(6, 9.15, "Churn subiu 3pp — Trial sem onboarding é a causa raiz",
            ha='center', va='center', fontsize=10, color='white', fontweight='bold')

    # KPIs com contexto semântico
    kpis_com = [
        (ALERTA, "12%", "Churn MTD", "Meta: 9% ▲ +3pp"),
        (POSITIVO, "R$2,1M", "Receita MTD", "Meta atingida ✓"),
        (ATENCAO, "68", "NPS", "Meta 70 — atenção ⚠"),
        (ALERTA, "42%", "Margem", "Meta 45% ▲ -3pp"),
    ]
    for i, (c, v, l, sub) in enumerate(kpis_com):
        x = 0.5 + i * 2.75
        ax.add_patch(FancyBboxPatch((x, 6.6), 2.4, 1.65, boxstyle="round,pad=0.1",
                                    facecolor='white', edgecolor=c, linewidth=2.5))
        ax.text(x+1.2, 7.55, v, ha='center', fontsize=13, fontweight='bold', color=c)
        ax.text(x+1.2, 7.2, l, ha='center', fontsize=8, color=BRAND)
        ax.text(x+1.2, 6.9, sub, ha='center', fontsize=7, color=c)

    # Gráfico com destaque nos outliers
    cats = ['SP', 'RJ', 'MG', 'BA', 'RS', 'PR']
    vals = [42, 35, 28, 22, 19, 15]
    core_bar = [ALERTA if v >= 35 else NEUTRA for v in vals]
    for i, (c, v, col) in enumerate(zip(cats, vals, core_bar)):
        ax.bar(1 + i*1.75, v/10, width=1.3, color=col, alpha=0.85)
        ax.text(1 + i*1.75, v/10 + 0.1, f'{v}%', ha='center', fontsize=7.5,
                fontweight='bold' if col == ALERTA else 'normal', color=col)
        ax.text(1 + i*1.75, 0.1, c, ha='center', fontsize=8,
                fontweight='bold' if col == ALERTA else 'normal')
    ax.text(6, 6.2, "SP e RJ concentram 77% da receita — prioridade de ação", ha='center',
            fontsize=8.5, color=BRAND, fontweight='bold')

    # 3 insights acionáveis com estrutura completa
    insights = [
        (ALERTA, "AÇÃO URGENTE",
         "Clientes Trial sem 1° acesso em 7 dias têm churn 4× maior (28% vs 7%).",
         "→ Ativar nudge automático no D+3 para 1.200 clientes. Impacto: -14pp. Responsável: PM. Prazo: 1 semana."),
        (ATENCAO, "AÇÃO CURTO PRAZO",
         "Margem caiu 3pp em SP porque desconto >20% em Eletrônicos subiu 18pp.",
         "→ Capar desconto em 12% em SP/Eletrônicos até 30/maio. Impacto: +R$85k margem trimestral."),
        (PRIMARIA, "MONITORAR",
         "NPS caiu de 72 para 68 concentrado no segmento Corporate.",
         "→ Entrevistas com 20 contas Corporate para identificar causa. Prazo: 2 semanas."),
    ]
    for i, (c, tag, obs, acao) in enumerate(insights):
        y = 0.2 + i * 1.85
        ax.add_patch(FancyBboxPatch((0.3, y), 11.4, 1.7, boxstyle="round,pad=0.1",
                                    facecolor='white', edgecolor=c, linewidth=1.5))
        ax.text(0.6, y + 1.45, tag, fontsize=7, fontweight='bold', color='white',
                bbox=dict(boxstyle='round,pad=0.2', facecolor=c, edgecolor='none'))
        ax.text(0.7, y + 1.15, obs, fontsize=7.5, color=BRAND)
        ax.text(0.7, y + 0.6, acao, fontsize=7.5, color=c, fontweight='bold')

    ax.text(6, -0.25, "→ Reunião termina com decisão clara, responsáveis definidos e prazo acordado",
            ha='center', fontsize=8, color=POSITIVO, style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#EEFFEE', edgecolor=POSITIVO))
    ax.set_xticks([]); ax.set_yticks([])
    for spine in ax.spines.values(): spine.set_visible(False)

    fig.tight_layout(pad=1.5)
    save(fig, "cap1_05_insights_acionaveis.png")

# ──────────────────────────────────────────────────────────────────────────────
# CAP 1 — SECTION 6: Dashboard as Code — Fluxo (sem código)
# ──────────────────────────────────────────────────────────────────────────────
def cap1_06_daac_fluxo():
    fig, ax = plt.subplots(figsize=(15, 7), facecolor=BGCLARO)
    ax.set_facecolor(BGCLARO)
    ax.set_xlim(0, 15); ax.set_ylim(0, 8)
    ax.set_title("Dashboard as Code (DaC) — Fluxo de Trabalho Profissional",
                 fontsize=13, fontweight='bold', color=BRAND, pad=12)

    # Etapas do fluxo DaC
    etapas = [
        (1.0,  5.5, PRIMARIA,  "1. Código\nGit",          "Definição em Python/\nJSON versionada"),
        (3.8,  5.5, DESTAQUE,  "2. Pull\nRequest",         "Revisão por par\nantes de publicar"),
        (6.6,  5.5, POSITIVO,  "3. CI/CD\nPipeline",       "GitHub Actions /\nCodePipeline AWS"),
        (9.4,  5.5, ATENCAO,   "4. Deploy\nAutomático",    "boto3 cria/atualiza\nno QuickSight"),
        (12.2, 5.5, "#6F42C1", "5. Dashboard\nPublicado",  "URL compartilhável\npara a equipe"),
    ]

    for x, y, c, titulo, sub in etapas:
        # Círculo principal
        circle = plt.Circle((x + 0.9, y + 0.6), 0.7, color=c, zorder=3)
        ax.add_patch(circle)
        ax.text(x + 0.9, y + 0.6, titulo.split('\n')[0], ha='center', va='center',
                fontsize=8, fontweight='bold', color='white', zorder=4)

        # Caixa abaixo
        ax.add_patch(FancyBboxPatch((x, y - 1.5), 1.8, 1.2,
                                    boxstyle="round,pad=0.12",
                                    facecolor='white', edgecolor=c, linewidth=2, zorder=2))
        ax.text(x + 0.9, y - 0.7, titulo, ha='center', va='center',
                fontsize=8.5, fontweight='bold', color=c, zorder=3)
        ax.text(x + 0.9, y - 1.2, sub, ha='center', va='center',
                fontsize=7, color=NEUTRA, zorder=3)

    # Setas entre etapas
    for xi in [2.0, 4.8, 7.6, 10.4]:
        ax.annotate('', xy=(xi + 0.65, 6.1), xytext=(xi, 6.1),
                    arrowprops=dict(arrowstyle='->', color=BRAND, lw=2.5))

    # Benefícios do DaC
    beneficios_y = 2.5
    ax.add_patch(FancyBboxPatch((0.3, 0.3), 14.4, 2.8, boxstyle="round,pad=0.2",
                                facecolor='white', edgecolor=BRAND, linewidth=2))
    ax.text(7.5, 2.85, "Por que usar Dashboard as Code?", ha='center', fontsize=10,
            fontweight='bold', color=BRAND)

    beneficios = [
        (PRIMARIA,  "📁 Rastreabilidade", "Histórico completo\nde cada mudança no Git"),
        (POSITIVO,  "♻ Reprodutibilidade", "Dev/Homol/Prod\nidênticos e versionados"),
        (DESTAQUE,  "👥 Colaboração", "PR com revisão\nantes de publicar"),
        (ATENCAO,   "⚡ Velocidade", "Deploy de 30 dashboards\nem segundos"),
        ("#6F42C1",  "🔒 Governança", "Permissões como código\nauditáveis e controladas"),
    ]
    for i, (c, titulo, sub) in enumerate(beneficios):
        x = 0.8 + i * 2.8
        ax.add_patch(FancyBboxPatch((x, 0.55), 2.4, 1.9,
                                    boxstyle="round,pad=0.1",
                                    facecolor='#F8FAFF', edgecolor=c, linewidth=1.5))
        ax.text(x+1.2, 2.1, titulo, ha='center', fontsize=8, fontweight='bold', color=c)
        ax.text(x+1.2, 1.5, sub, ha='center', fontsize=7.5, color=NEUTRA)

    ax.set_xticks([]); ax.set_yticks([])
    for spine in ax.spines.values(): spine.set_visible(False)
    save(fig, "cap1_06_daac_fluxo.png")

# ──────────────────────────────────────────────────────────────────────────────
# CAP 1 — SECTION 8: Arquitetura de Agentes (lúdica)
# ──────────────────────────────────────────────────────────────────────────────
def cap1_08_agentes_arquitetura():
    fig, ax = plt.subplots(figsize=(16, 9), facecolor="#0F1724")
    ax.set_facecolor("#0F1724")
    ax.set_xlim(0, 16); ax.set_ylim(0, 9)
    fig.suptitle("Engenheiro de Analytics Virtual — Pipeline Multi-Agente End-to-End",
                 fontsize=13, fontweight='bold', color='#E8EDF5', y=0.98)

    # Agentes
    agentes = [
        (0.5,  6.5, "#2563EB",  "🔍",  "Agente\nDiscovery",         "Lê contrato de negócio\nCalcula estatísticas\nDetecta padrões e outliers"),
        (3.3,  6.5, "#E35D22",  "💡",  "Agente\nInsights",           "Consulta base de insights\nClassifica por impacto\nGera acionáveis com score"),
        (6.1,  6.5, "#16A34A",  "📖",  "Agente\nStoryboard",         "Define Big Idea\nMonta 3 zonas\nEscreve títulos-mensagem"),
        (8.9,  6.5, "#EAB308",  "🎨",  "Agente\nProtótipo",          "Gera HTML + Chart.js\nDashboard autocontido\ncom dados reais"),
        (11.7, 6.5, "#8B5CF6",  "☁",  "Agente\nInfrastrutura",      "DataSet + Analysis\nDashboard via Boto3\nQuickSight AWS"),
        (14.5, 6.5, "#64748B",  "📋",  "Agente\nDocumentação",       "Changelog automático\nDicionário de métricas\nRunbook de suporte"),
    ]

    # Linha de conexão de fundo
    ax.plot([0.5, 15.5], [7.3, 7.3], color='#2A3550', lw=1.5, linestyle='--', zorder=1)

    for x, y, c, emoji, nome, desc in agentes:
        # Caixa principal
        ax.add_patch(FancyBboxPatch((x, y), 2.6, 2.0,
                                    boxstyle="round,pad=0.15",
                                    facecolor='#1A2740', edgecolor=c, linewidth=2, zorder=2))
        # Emoji no topo
        ax.text(x+1.3, y+1.65, emoji, ha='center', va='center', fontsize=16, zorder=3)
        # Nome
        ax.text(x+1.3, y+1.1, nome, ha='center', va='center',
                fontsize=8, fontweight='bold', color='white', zorder=3)

        # Caixa de descrição abaixo
        ax.add_patch(FancyBboxPatch((x, y-2.3), 2.6, 2.1,
                                    boxstyle="round,pad=0.1",
                                    facecolor='#131C2E', edgecolor='#2A3550', linewidth=1, zorder=2))
        ax.text(x+1.3, y-1.25, desc, ha='center', va='center',
                fontsize=7, color='#A0AEC0', zorder=3)

    # Setas entre agentes
    for xi in [3.2, 6.0, 8.8, 11.6, 14.4]:
        ax.annotate('', xy=(xi + 0.2, 7.5), xytext=(xi, 7.5),
                    arrowprops=dict(arrowstyle='->', color='#4A90D9', lw=2.5))

    # Entrada e Saída
    # Entrada
    ax.add_patch(FancyBboxPatch((-0.1, 6.8), 0.55, 1.3,
                                boxstyle="round,pad=0.1",
                                facecolor='#0D1B2A', edgecolor='#2563EB', linewidth=1.5))
    ax.text(0.17, 7.45, "📥\nInput", ha='center', fontsize=6.5, color='#6DB3F2')

    # Saída
    ax.add_patch(FancyBboxPatch((15.5, 6.8), 0.55, 1.3,
                                boxstyle="round,pad=0.1",
                                facecolor='#0D1B2A', edgecolor='#8B5CF6', linewidth=1.5))
    ax.text(15.77, 7.45, "📤\nOutput", ha='center', fontsize=6.5, color='#B39DDB')

    # Orquestrador central
    ax.add_patch(FancyBboxPatch((4.5, 0.3), 7.0, 1.8,
                                boxstyle="round,pad=0.2",
                                facecolor='#1A2740', edgecolor='#E35D22', linewidth=2.5, zorder=2))
    ax.text(8.0, 1.5, "⚙  ORQUESTRADOR", ha='center', fontsize=11,
            fontweight='bold', color='#E35D22', zorder=3)
    ax.text(8.0, 1.0, "LangChain / LangGraph / AWS Step Functions", ha='center',
            fontsize=9, color='#A0AEC0', zorder=3)
    ax.text(8.0, 0.6, "Coordena estado compartilhado · Retry automático · Logging centralizado",
            ha='center', fontsize=7.5, color='#718096', zorder=3)

    # Setas dos agentes para o orquestrador
    for xi in [1.8, 4.6, 7.4, 10.2, 13.0, 15.8]:
        if xi <= 15:
            ax.annotate('', xy=(8.0, 2.1), xytext=(xi, 6.3),
                        arrowprops=dict(arrowstyle='->', color='#2A3550', lw=1,
                                       connectionstyle='arc3,rad=0.1'))

    # Entradas do pipeline
    ax.text(0.5, 3.8, "Entrada\ndo Pipeline:", fontsize=9, fontweight='bold', color='#6DB3F2')
    entradas = [
        "📊 Dataset (CSV/S3/Redshift)",
        "📄 Contrato de Negócio\n    (dores, KPIs, audiência)",
        "🗂 Base de Insights\n    (exemplos validados)",
    ]
    for i, e in enumerate(entradas):
        ax.text(0.5, 3.2 - i*1.1, e, fontsize=8, color='#A0AEC0')

    ax.set_xticks([]); ax.set_yticks([])
    for spine in ax.spines.values(): spine.set_visible(False)
    save(fig, "cap1_08_agentes_arquitetura.png")

# ──────────────────────────────────────────────────────────────────────────────
# CAP 2 — IMAGENS ADICIONAIS (2ª imagem por seção)
# ──────────────────────────────────────────────────────────────────────────────
def cap2_01b_dashboard_sem_vs_com_narrativa():
    """Dashboard sem narrativa vs dashboard com narrativa (AED vs Explanatória)"""
    fig, axes = plt.subplots(1, 2, figsize=(15, 7), facecolor=BGCLARO)
    fig.suptitle("Dashboard sem Narrativa (AED) vs com Narrativa (Explanatório)",
                 fontsize=13, fontweight='bold', color=BRAND, y=1.02)

    # ── SEM narrativa: tudo jogado
    ax = axes[0]
    ax.set_facecolor(WHITE)
    ax.set_xlim(0, 12); ax.set_ylim(0, 10)
    ax.set_title("❌  Sem Narrativa\n(EDA Dump — 10 gráficos, nenhuma decisão)", fontsize=10,
                 fontweight='bold', color=ALERTA, pad=8)

    # Simular 6 mini-gráficos sem conexão
    positions = [(0.3,7.5,5.5,2.0), (6.2,7.5,5.5,2.0),
                 (0.3,5.0,2.5,2.0), (3.3,5.0,2.5,2.0), (6.3,5.0,2.5,2.0), (9.3,5.0,2.5,2.0)]
    titulos_sem = ["Histogram: Exam_Score", "Boxplot por Gender",
                   "Scatter: Hours vs Score", "Correlation Matrix", "Pie: Access to Resources", "Barras: Parental Education"]
    for (x, y, w, h), t in zip(positions, titulos_sem):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1",
                                    facecolor='#F0F0F0', edgecolor='#CCCCCC', linewidth=1))
        ax.text(x + w/2, y + h/2 + 0.2, t, ha='center', fontsize=7.5, color=NEUTRA)
        # Simular um "gráfico" genérico
        for j in range(4):
            h_bar = np.random.uniform(0.2, 0.7)
            ax.bar(x + 0.3 + j*0.55, h_bar, width=0.4, bottom=y + 0.1,
                   color=np.random.choice([PRIMARIA, DESTAQUE, POSITIVO, ATENCAO]), alpha=0.6)

    ax.add_patch(FancyBboxPatch((0.3, 0.4), 11.4, 4.2, boxstyle="round,pad=0.1",
                                facecolor='#FFFDE7', edgecolor=ATENCAO, linewidth=1))
    obs_sem = [
        "• Exam_Score: média=67.2, dp=3.9, mín=55, máx=79",
        "• Gender: M=51%, F=49% — distribuição uniforme",
        "• Hours_Studied correlaciona 0.445 com Exam_Score",
        "• Internet_Access: 78% Sim, 22% Não",
        "• Parental_Education Level varia entre Nenhum e Pós-graduação",
        "• Tutoring_Sessions: 63% tem 0-3 sessões",
    ]
    ax.text(6, 4.3, "Observações (informativas — sem ação):", ha='center', fontsize=8.5,
            fontweight='bold', color=ATENCAO)
    for i, o in enumerate(obs_sem):
        ax.text(0.6, 3.9 - i*0.55, o, fontsize=7.5, color=NEUTRA)

    ax.text(6, 0.1, "→ O aluno vê dados. Não sabe o que fazer com eles.",
            ha='center', fontsize=8, color=ALERTA, style='italic')
    ax.set_xticks([]); ax.set_yticks([])
    for spine in ax.spines.values(): spine.set_visible(False)

    # ── COM narrativa: 1 história, 1 decisão
    ax = axes[1]
    ax.set_facecolor(WHITE)
    ax.set_xlim(0, 12); ax.set_ylim(0, 10)
    ax.set_title("✅  Com Narrativa Explanatória\n(1 história clara → 1 decisão específica)", fontsize=10,
                 fontweight='bold', color=POSITIVO, pad=8)

    ax.add_patch(FancyBboxPatch((0, 8.5), 12, 1.3, boxstyle="round,pad=0.1",
                                facecolor=BRAND, edgecolor="none"))
    ax.text(6, 9.15, "Alunos com baixo envolvimento familiar reprovam 4× mais — é possível reverter",
            ha='center', va='center', fontsize=9, color='white', fontweight='bold')

    # 3 KPIs relevantes para a história
    kpi3 = [(ALERTA, "27%", "Reprovação\n(baixo envolvimento)"),
            (POSITIVO, "7%",  "Reprovação\n(alto envolvimento)"),
            (DESTAQUE, "9pts","Gap de nota\nmédia entre grupos")]
    for i, (c, v, l) in enumerate(kpi3):
        x = 0.8 + i * 3.5
        ax.add_patch(FancyBboxPatch((x, 6.6), 3.0, 1.7, boxstyle="round,pad=0.15",
                                    facecolor='white', edgecolor=c, linewidth=2.5))
        ax.text(x+1.5, 7.55, v, ha='center', fontsize=16, fontweight='bold', color=c)
        ax.text(x+1.5, 7.0, l, ha='center', fontsize=8, color=BRAND)

    # Gráfico relevante para a história (barras: grupos)
    grupos = ['Baixo\n+Poucas horas', 'Baixo\n+Muitas horas', 'Alto\n+Poucas horas', 'Alto\n+Muitas horas']
    notas  = [62.1, 65.8, 68.4, 72.3]
    cores_g = [ALERTA, ATENCAO, ATENCAO, POSITIVO]
    y_pos = [3.2, 3.2 + 1.0, 3.2 + 2.0, 3.2 + 3.0]
    for g, n, c, y in zip(grupos, notas, cores_g, y_pos):
        bar_len = (n - 55) / 25 * 7
        ax.barh(y, bar_len, height=0.7, color=c, alpha=0.85, left=0.3)
        ax.text(0.5 + bar_len, y, f'{n:.1f}', va='center', fontsize=9,
                fontweight='bold', color=c)
        ax.text(0.1, y, g, va='center', ha='right', fontsize=7.5, color=BRAND)

    # Meta line
    ax.axvline(0.3 + (67.2 - 55) / 25 * 7, ymin=0.3, ymax=0.9,
               color=NEUTRA, linestyle='--', linewidth=1.5)
    ax.text(5.0, 6.4, "Média geral: 67.2", fontsize=8, color=NEUTRA, style='italic')

    # Insight acionável final
    ax.add_patch(FancyBboxPatch((0.3, 0.3), 11.4, 2.7, boxstyle="round,pad=0.15",
                                facecolor='#FFF8E7', edgecolor=DESTAQUE, linewidth=2))
    ax.text(6, 2.7, "Insight Acionável:", ha='center', fontsize=9,
            fontweight='bold', color=DESTAQUE)
    ax.text(6, 2.3, "Alunos com baixo envolvimento familiar + <15h estudo representam 34% da turma",
            ha='center', fontsize=8, color=BRAND)
    ax.text(6, 1.9, "e têm taxa de reprovação 4× maior. Programa de mentoria para esse grupo",
            ha='center', fontsize=8, color=BRAND)
    ax.text(6, 1.5, "pode reduzir reprovação de 27% para 12% (+15pp). Responsável: Coordenação.",
            ha='center', fontsize=8, color=BRAND)
    ax.text(6, 1.0, "→ Decisão: implementar programa de mentoria para 1.800 alunos até julho/2026",
            ha='center', fontsize=9, fontweight='bold', color=DESTAQUE)

    ax.set_xticks([]); ax.set_yticks([])
    for spine in ax.spines.values(): spine.set_visible(False)

    fig.tight_layout(pad=1.5)
    save(fig, "cap2_01b_sem_vs_com_narrativa.png")

def cap2_02b_big_idea_comparacao():
    """Exemplos de Big Ideas ruins vs boas"""
    fig, ax = plt.subplots(figsize=(14, 8), facecolor=BGCLARO)
    ax.set_facecolor(BGCLARO)
    ax.set_xlim(0, 14); ax.set_ylim(0, 8)
    ax.set_title("Big Idea: Formulações Ruins vs Formulações Corretas (4 Domínios)",
                 fontsize=13, fontweight='bold', color=BRAND, pad=12)

    pares = [
        (ALERTA, POSITIVO, "E-commerce",
         "❌  'A taxa de devolução é 8%.'\n     (Observação neutra — sem ação)",
         "✅  'Se não reduzirmos devoluções de Eletrônicos em SP\n     de 8% para 4%, perderemos R$95k em GMV anual.\n     Responsável: Logística. Prazo: Q3/2026.'"),
        (ALERTA, POSITIVO, "RH / People Analytics",
         "❌  'O turnover de TI está em 28%.'\n     (Informa mas não orienta nada)",
         "✅  'Engenheiros sem promoção em 3 anos custam R$270k/ano\n     em reposição — implementar plano de carreira acelerado\n     para 23 talentos reduz isso em 60%.'"),
        (ALERTA, POSITIVO, "Saúde",
         "❌  'Pacientes com HbA1c>9 têm readmissão de 34%.'\n     (Dado correto, mas... e daí?)",
         "✅  'Agendar retorno obrigatório na alta para 1.200 pacientes\n     diabéticos evita 312 internações e R$3,7M em custos.\n     Responsável: Assistência. Prazo: próximo semestre.'"),
        (ALERTA, POSITIVO, "Varejo",
         "❌  'Desconto >20% gera margem negativa.'\n     (Observação sem magnitude nem ação)",
         "✅  'Capar desconto em 12% em Tech/Sul preserva R$85k\n     de margem trimestral sem afetar volume de vendas.\n     Implementar na campanha de inverno (julho).'"),
    ]

    for i, (c_ruim, c_bom, dominio, ruim, bom) in enumerate(pares):
        row = i // 2
        col = i % 2
        x = 0.3 + col * 7.0
        y = 0.5 + (1 - row) * 3.8

        # Header do domínio
        ax.add_patch(FancyBboxPatch((x, y + 2.9), 6.5, 0.65, boxstyle="round,pad=0.1",
                                    facecolor=BRAND, edgecolor='none'))
        ax.text(x + 3.25, y + 3.2, f"  {dominio}", ha='center', va='center',
                fontsize=9.5, fontweight='bold', color='white')

        # Box ruim
        ax.add_patch(FancyBboxPatch((x, y + 1.5), 6.5, 1.3, boxstyle="round,pad=0.1",
                                    facecolor='#FFF5F5', edgecolor=c_ruim, linewidth=1.5))
        ax.text(x + 0.15, y + 2.6, ruim, fontsize=7.5, color=ALERTA, va='top')

        # Box bom
        ax.add_patch(FancyBboxPatch((x, y + 0.1), 6.5, 1.3, boxstyle="round,pad=0.1",
                                    facecolor='#F0FFF4', edgecolor=c_bom, linewidth=1.5))
        ax.text(x + 0.15, y + 1.2, bom, fontsize=7.5, color=POSITIVO, va='top')

    ax.text(7, 0.1, "Regra: a Big Idea deve provocar a pergunta 'quando começamos?' — não 'que interessante'",
            ha='center', fontsize=9, color=BRAND, style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=PRIMARIA, linewidth=1.5))

    ax.set_xticks([]); ax.set_yticks([])
    for spine in ax.spines.values(): spine.set_visible(False)
    save(fig, "cap2_02b_big_idea_comparacao.png")

def cap2_05b_titulo_mensagem():
    """Título rótulo vs título mensagem em dashboards reais"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), facecolor=BGCLARO)
    fig.suptitle("Título Rótulo vs Título Mensagem — O Teste do Relance na Prática",
                 fontsize=13, fontweight='bold', color=BRAND, y=1.02)

    cats = ['SP', 'RJ', 'MG', 'RS', 'BA']
    vals = [42, 35, 28, 15, 12]
    cores_bar = [ALERTA, ALERTA, NEUTRA, NEUTRA, NEUTRA]

    for idx, (ax, titulo_tipo, titulo, cor_titulo, nota) in enumerate([
        (axes[0], "Título Rótulo (Ruim):", "Vendas por Estado", ALERTA,
         "Reação do CEO: 'Ok... e daí? Isso é bom ou ruim?'"),
        (axes[1], "Título Mensagem (Bom):", "SP e RJ concentram 77% das vendas — risco de concentração", POSITIVO,
         "Reação do CEO: 'Precisamos diversificar. O que propomos?'"),
    ]):
        ax.set_facecolor(WHITE)
        for spine in ax.spines.values(): spine.set_visible(False)

        # Label tipo de título
        ax.text(0.5, 0.96, titulo_tipo, transform=ax.transAxes,
                fontsize=9, fontweight='bold', color=cor_titulo, ha='center')

        # Título do gráfico
        bg = '#FFF5F5' if idx == 0 else '#F0FFF4'
        bdr = ALERTA if idx == 0 else POSITIVO
        ax.set_title(titulo, fontsize=10, fontweight='bold', color=cor_titulo, pad=6,
                     bbox=dict(boxstyle='round,pad=0.4', facecolor=bg, edgecolor=bdr, linewidth=1.5))

        # Barras
        bars = ax.bar(cats, vals, color=cores_bar if idx == 1 else [PRIMARIA]*5, width=0.6)
        ax.set_ylim(0, 55)
        ax.set_yticks([])
        ax.tick_params(bottom=False)

        # Rótulos diretos nas barras
        for bar, v in zip(bars, vals):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.8,
                    f'{v}%', ha='center', fontsize=9,
                    fontweight='bold' if (v >= 35 and idx == 1) else 'normal',
                    color=ALERTA if (v >= 35 and idx == 1) else NEUTRA)

        # Anotação no idx=1
        if idx == 1:
            ax.annotate('77% aqui', xy=(1, 35), xytext=(2.5, 45),
                        arrowprops=dict(arrowstyle='->', color=ALERTA, lw=1.5),
                        fontsize=8.5, color=ALERTA, fontweight='bold')

        ax.text(0.5, -0.15, nota, transform=ax.transAxes, ha='center',
                fontsize=8.5, style='italic', color=cor_titulo,
                bbox=dict(boxstyle='round,pad=0.3',
                          facecolor='#FFF5F5' if idx == 0 else '#F0FFF4',
                          edgecolor=cor_titulo, linewidth=1))

    fig.tight_layout(pad=2.0)
    save(fig, "cap2_05b_titulo_mensagem.png")

def cap2_08b_dashboard_sem_vs_com_zonas():
    """Dashboard sem estrutura de zonas vs com 3 zonas"""
    fig, axes = plt.subplots(1, 2, figsize=(15, 8), facecolor=BGCLARO)
    fig.suptitle("Dashboard sem Zonas vs com Estrutura de 3 Zonas Decisórias",
                 fontsize=13, fontweight='bold', color=BRAND, y=1.02)

    # ── SEM zonas
    ax = axes[0]
    ax.set_facecolor('#F5F5F5')
    ax.set_xlim(0, 12); ax.set_ylim(0, 10)
    ax.set_title("❌  Sem Zonas — Tudo no Mesmo Nível\n(Usuário não sabe onde começar)", fontsize=10,
                 fontweight='bold', color=ALERTA, pad=8)

    # 12 KPIs jogados sem hierarquia
    kpi_vals = ['R$2,1M', '42%', 'R$89k', '18%', '68', '12%', '4.3★', 'R$124', '99%', '7,2d', '85%', 'R$340']
    kpi_labs = ['Receita', 'Margem', 'Custo Ops', 'Churn', 'NPS', 'Devolução', 'Review', 'Ticket', 'SLA', 'Ciclo', 'Retenção', 'LTV']
    for i, (v, l) in enumerate(zip(kpi_vals, kpi_labs)):
        x = 0.3 + (i % 4) * 2.9
        y = 7.3 - (i // 4) * 1.2
        ax.add_patch(FancyBboxPatch((x, y), 2.5, 1.0, boxstyle="round,pad=0.1",
                                    facecolor='white', edgecolor='#CCCCCC', linewidth=0.8))
        ax.text(x+1.25, y+0.65, v, ha='center', fontsize=9, fontweight='bold', color=NEUTRA)
        ax.text(x+1.25, y+0.25, l, ha='center', fontsize=7, color='gray')

    ax.add_patch(FancyBboxPatch((0.3, 3.5), 11.4, 2.5, boxstyle="round,pad=0.1",
                                facecolor='white', edgecolor='#CCCCCC', linewidth=0.8))
    ax.text(6, 4.75, "Gráfico de Barras — Receita por Região", ha='center', fontsize=9, color=NEUTRA)
    for i, (reg, val) in enumerate([('SP', 42), ('RJ', 28), ('MG', 18), ('RS', 8), ('BA', 4)]):
        ax.bar(1.5 + i*2.1, val/50 * 1.8, width=1.6, bottom=3.7, color=PRIMARIA, alpha=0.5)
        ax.text(2.3 + i*2.1, 3.7 + val/50 * 1.8 + 0.05, f'{val}%', ha='center', fontsize=7, color=NEUTRA)
        ax.text(2.3 + i*2.1, 3.6, reg, ha='center', fontsize=7)

    ax.add_patch(FancyBboxPatch((0.3, 0.3), 11.4, 2.9, boxstyle="round,pad=0.1",
                                facecolor='white', edgecolor='#CCCCCC', linewidth=0.8))
    ax.text(6, 2.6, "Notas gerenciais diversas:", ha='center', fontsize=8.5, color=NEUTRA)
    for i, note in enumerate(["- Reunião de vendas: quarta 15h", "- Atualização de dados: 06h",
                                "- Última revisão: João Silva (03/05)", "- Filtros: últimos 30 dias"]):
        ax.text(0.8, 2.1 - i*0.45, note, fontsize=7.5, color='gray')

    ax.text(6, -0.2, "→ CEO passa 3 min tentando entender onde está o problema",
            ha='center', fontsize=8, color=ALERTA, style='italic')
    ax.set_xticks([]); ax.set_yticks([])
    for spine in ax.spines.values(): spine.set_visible(False)

    # ── COM 3 zonas
    ax = axes[1]
    ax.set_facecolor(WHITE)
    ax.set_xlim(0, 12); ax.set_ylim(0, 10)
    ax.set_title("✅  Com 3 Zonas — Hierarquia Clara\n(CEO encontra resposta em 5 segundos)", fontsize=10,
                 fontweight='bold', color=POSITIVO, pad=8)

    # ZONA 1 — Contexto
    ax.add_patch(FancyBboxPatch((0.1, 7.5), 11.8, 2.3, boxstyle="round,pad=0.15",
                                facecolor='#EFF6FF', edgecolor=PRIMARIA, linewidth=2.5))
    ax.text(0.4, 9.55, "ZONA 1 — CONTEXTO (<5 segundos)", fontsize=8, fontweight='bold',
            color=PRIMARIA, style='italic')
    kpi_z1 = [(ALERTA, "18%", "Churn", "Meta 15% ▲"), (POSITIVO, "R$2,1M", "Receita", "✓ Meta"),
              (ATENCAO, "68", "NPS", "Meta 70 ⚠"), (NEUTRA, "42%", "Margem", "Meta 45%")]
    for i, (c, v, l, s) in enumerate(kpi_z1):
        x = 0.4 + i*2.85
        ax.add_patch(FancyBboxPatch((x, 7.7), 2.6, 1.7, boxstyle="round,pad=0.1",
                                    facecolor='white', edgecolor=c, linewidth=2))
        ax.text(x+1.3, 8.7, v, ha='center', fontsize=12, fontweight='bold', color=c)
        ax.text(x+1.3, 8.3, l, ha='center', fontsize=8, color=BRAND)
        ax.text(x+1.3, 8.0, s, ha='center', fontsize=7, color=c)

    # ZONA 2 — Diagnóstico
    ax.add_patch(FancyBboxPatch((0.1, 4.3), 11.8, 2.9, boxstyle="round,pad=0.15",
                                facecolor='#FAFAFA', edgecolor=NEUTRA, linewidth=1.5))
    ax.text(0.4, 7.0, "ZONA 2 — DIAGNÓSTICO (5-15 segundos)", fontsize=8, fontweight='bold',
            color=NEUTRA, style='italic')
    segs = ['Premium', 'Basic', 'Trial', 'Legacy']
    churn_s = [12, 8, 23, 15]
    for i, (s, c_val) in enumerate(zip(segs, churn_s)):
        col = ALERTA if c_val > 15 else NEUTRA
        ax.barh(4.7 + i*0.55, c_val/30 * 7, height=0.4, color=col, left=0.5)
        ax.text(0.5 + c_val/30 * 7 + 0.15, 4.7 + i*0.55, f'{c_val}%',
                va='center', fontsize=8, color=col, fontweight='bold' if c_val > 15 else 'normal')
        ax.text(0.3, 4.7 + i*0.55, s, va='center', ha='right', fontsize=8)
    ax.axvline(0.5 + 15/30*7, ymin=0.42, ymax=0.68, color=ATENCAO, linestyle='--', lw=1.5)
    ax.text(4.0, 6.85, "Churn por Segmento — Trial está fora da meta", ha='center',
            fontsize=8, color=NEUTRA, style='italic')

    # ZONA 3 — Recomendação
    ax.add_patch(FancyBboxPatch((0.1, 0.5), 11.8, 3.5, boxstyle="round,pad=0.15",
                                facecolor='#FFFBEB', edgecolor=DESTAQUE, linewidth=2.5))
    ax.text(0.4, 3.8, "ZONA 3 — RECOMENDAÇÃO E DECISÃO", fontsize=8, fontweight='bold',
            color=DESTAQUE, style='italic')
    ax.text(6, 3.3, "Churn no segmento Trial (23%) está 8pp acima da meta por falha no onboarding.",
            ha='center', fontsize=9, color=BRAND, fontweight='bold')
    ax.text(6, 2.85, "→ Ativar nudge no D+3 (15% mais baratos que reposição)",
            ha='center', fontsize=8.5, color=BRAND)
    ax.text(6, 2.4, "Impacto esperado: Trial cai de 23% para 12%. Preserva R$180k em ARR.",
            ha='center', fontsize=8.5, color=BRAND)
    ax.add_patch(FancyBboxPatch((1.5, 0.7), 9.0, 1.4, boxstyle="round,pad=0.1",
                                facecolor=DESTAQUE, edgecolor='none'))
    ax.text(6, 1.45, "Decisão: PM aprova nudge + CRM executa até 10/maio", ha='center',
            fontsize=9.5, fontweight='bold', color='white')
    ax.text(6, 1.0, "Responsável: Product Manager | Prazo: 1 semana", ha='center',
            fontsize=8.5, color='white')

    ax.text(6, -0.2, "→ CEO lê em 5 segundos: 'Trial com problema, ação definida, responsável claro'",
            ha='center', fontsize=8, color=POSITIVO, style='italic')
    ax.set_xticks([]); ax.set_yticks([])
    for spine in ax.spines.values(): spine.set_visible(False)

    fig.tight_layout(pad=1.5)
    save(fig, "cap2_08b_dashboard_sem_vs_com_zonas.png")

def cap2_09b_kpi_anatomia_exemplos():
    """KPI incompleto vs KPI completo (com todos os componentes)"""
    fig, ax = plt.subplots(figsize=(14, 6), facecolor=BGCLARO)
    ax.set_facecolor(BGCLARO)
    ax.set_xlim(0, 14); ax.set_ylim(0, 6)
    ax.set_title("KPI Incompleto vs KPI Completo — Os 5 Componentes que Forçam Decisão",
                 fontsize=13, fontweight='bold', color=BRAND, pad=12)

    # Coluna: KPI incompleto
    ax.add_patch(FancyBboxPatch((0.3, 0.5), 5.8, 5.1, boxstyle="round,pad=0.2",
                                facecolor=WHITE, edgecolor=ALERTA, linewidth=2))
    ax.text(3.2, 5.3, "❌  KPI Incompleto", ha='center', fontsize=11, fontweight='bold', color=ALERTA)

    # Big number sem contexto
    ax.text(3.2, 4.2, "18%", ha='center', fontsize=36, fontweight='bold', color=NEUTRA)
    ax.text(3.2, 3.5, "Churn", ha='center', fontsize=12, color=NEUTRA)

    ax.text(3.2, 2.7, "❓ 18% de quê?", ha='center', fontsize=9, color=ALERTA)
    ax.text(3.2, 2.3, "❓ É bom ou ruim?", ha='center', fontsize=9, color=ALERTA)
    ax.text(3.2, 1.9, "❓ Está melhorando ou piorando?", ha='center', fontsize=9, color=ALERTA)
    ax.text(3.2, 1.5, "❓ De que período?", ha='center', fontsize=9, color=ALERTA)
    ax.text(3.2, 1.1, "❓ Quem é responsável?", ha='center', fontsize=9, color=ALERTA)

    ax.text(3.2, 0.6, "→ Número que não informa nada", ha='center',
            fontsize=8, color=ALERTA, style='italic')

    # Seta central
    ax.annotate('', xy=(8.2, 3.0), xytext=(6.3, 3.0),
                arrowprops=dict(arrowstyle='->', color=PRIMARIA, lw=3))
    ax.text(7.25, 3.4, "Adiciona\ncontexto", ha='center', fontsize=8,
            color=PRIMARIA, fontweight='bold')

    # Coluna: KPI completo
    ax.add_patch(FancyBboxPatch((8.2, 0.5), 5.5, 5.1, boxstyle="round,pad=0.2",
                                facecolor=WHITE, edgecolor=POSITIVO, linewidth=2.5))
    ax.text(10.95, 5.3, "✅  KPI Completo (5 componentes)", ha='center',
            fontsize=11, fontweight='bold', color=POSITIVO)

    # Valor + badge
    ax.text(9.5, 4.4, "18%", ha='center', fontsize=32, fontweight='bold', color=ALERTA)
    ax.add_patch(FancyBboxPatch((12.0, 3.95), 1.5, 0.7, boxstyle="round,pad=0.1",
                                facecolor=ALERTA, edgecolor='none'))
    ax.text(12.75, 4.3, "▲ +3pp", ha='center', fontsize=10, fontweight='bold', color='white')

    componentes = [
        (ALERTA,   "1. Valor atual:",   "18% (MTD maio/2026)"),
        (NEUTRA,   "2. Meta (target):", "15% — benchmark do setor"),
        (ALERTA,   "3. Gap:",           "+3pp acima da meta → ação urgente"),
        (ATENCAO,  "4. Tendência:",     "▲ subindo há 3 meses — piorando"),
        (PRIMARIA, "5. Período:",       "MTD Mai/2026 | vs Abr/2026: +1pp"),
    ]
    for i, (c, label, valor) in enumerate(componentes):
        y_pos = 3.5 - i * 0.55
        ax.text(8.4, y_pos, label, fontsize=8, fontweight='bold', color=c, va='center')
        ax.text(10.0, y_pos, valor, fontsize=8, color=BRAND, va='center')

    ax.text(10.95, 0.6, "→ Decisão: ativar retenção para 1.200 clientes até 10/maio",
            ha='center', fontsize=8, color=POSITIVO, fontweight='bold', style='italic')

    ax.set_xticks([]); ax.set_yticks([])
    for spine in ax.spines.values(): spine.set_visible(False)
    save(fig, "cap2_09b_kpi_completo_vs_incompleto.png")

def cap2_10b_pitch_erros_comuns():
    """Pitch com erros vs pitch correto estrutura SCR"""
    fig, ax = plt.subplots(figsize=(14, 7), facecolor=BGCLARO)
    ax.set_facecolor(BGCLARO)
    ax.set_xlim(0, 14); ax.set_ylim(0, 7)
    ax.set_title("Pitch de 3 Minutos: Erros Comuns vs Estrutura SCR Correta",
                 fontsize=13, fontweight='bold', color=BRAND, pad=12)

    # ESQUERDA: Pitch com erros
    ax.add_patch(FancyBboxPatch((0.2, 0.3), 6.0, 6.3, boxstyle="round,pad=0.15",
                                facecolor=WHITE, edgecolor=ALERTA, linewidth=2))
    ax.text(3.2, 6.35, "❌  Pitch com Erros", ha='center', fontsize=11, fontweight='bold', color=ALERTA)

    erros = [
        (ATENCAO, "0:00–0:30  INTRODUÇÃO GENÉRICA",
         '"Vivemos em uma era de dados onde\nas empresas precisam de analytics..."'),
        (ATENCAO, "0:30–1:30  PROCESSO EXPLORATÓRIO",
         '"Primeiro calculei a média, depois fiz\num boxplot, encontrei correlações..."'),
        (ALERTA,  "1:30–2:30  GRÁFICOS SEM CONTEXTO",
         '"Este gráfico mostra Receita por Estado.\nEste outro mostra Churn por Segmento."'),
        (ALERTA,  "2:30–3:00  FIM ABRUPTO",
         '"Bom... é isso. Alguma pergunta?"\n→ Ninguém sabe o que decidir'),
    ]
    for i, (c, label, texto) in enumerate(erros):
        y = 5.5 - i * 1.3
        ax.add_patch(FancyBboxPatch((0.4, y - 0.9), 5.6, 1.2, boxstyle="round,pad=0.1",
                                    facecolor='#FFF5F5' if c == ALERTA else '#FFFDE7',
                                    edgecolor=c, linewidth=1.5))
        ax.text(0.6, y - 0.0, label, fontsize=8, fontweight='bold', color=c)
        ax.text(0.6, y - 0.5, texto, fontsize=7.5, color=NEUTRA)

    # DIREITA: Pitch SCR correto
    ax.add_patch(FancyBboxPatch((7.8, 0.3), 6.0, 6.3, boxstyle="round,pad=0.15",
                                facecolor=WHITE, edgecolor=POSITIVO, linewidth=2.5))
    ax.text(10.8, 6.35, "✅  Pitch SCR (30-45-60-45s)", ha='center',
            fontsize=11, fontweight='bold', color=POSITIVO)

    blocos_scr = [
        (PRIMARIA, "0:00–0:30  SITUAÇÃO (30s)",
         '"6.600 alunos. 1.800 em risco de\nreprovação. Custando R$45k/semestre."'),
        (DESTAQUE, "0:30–1:15  COMPLICAÇÃO (45s)",
         '"Esses alunos têm envolvimento familiar\nbaixo + <15h estudo. Gap = 9 pontos."'),
        (POSITIVO, "1:15–2:15  RESOLUÇÃO (60s)",
         '"Piloto com 220 alunos reduziu reprovação\nde 27% para 12%. Custo: R$18k/semestre."'),
        (ATENCAO,  "2:15–3:00  PRÓXIMO PASSO (45s)",
         '"Expandir para 1.800 alunos até julho.\nCoord. Pedagógica + TI. Impacto: +8pp."'),
    ]
    for i, (c, label, texto) in enumerate(blocos_scr):
        y = 5.5 - i * 1.3
        ax.add_patch(FancyBboxPatch((8.0, y - 0.9), 5.6, 1.2, boxstyle="round,pad=0.1",
                                    facecolor='white', edgecolor=c, linewidth=2))
        ax.text(8.2, y - 0.0, label, fontsize=8, fontweight='bold', color=c)
        ax.text(8.2, y - 0.5, texto, fontsize=7.5, color=BRAND)

    # Seta central
    ax.annotate('', xy=(7.7, 3.5), xytext=(6.3, 3.5),
                arrowprops=dict(arrowstyle='->', color=PRIMARIA, lw=3))

    ax.set_xticks([]); ax.set_yticks([])
    for spine in ax.spines.values(): spine.set_visible(False)
    save(fig, "cap2_10b_pitch_erros_vs_scr.png")

# ──────────────────────────────────────────────────────────────────────────────
# EXECUÇÃO
# ──────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("\n" + "="*65)
    print("  Gerando imagens — Cap 1 (Fundamentos Avançados)")
    print("="*65)
    cap1_02_caminho_olhar()
    cap1_03_carga_cognitiva()
    cap1_05_insights_acionaveis()
    cap1_06_daac_fluxo()
    cap1_08_agentes_arquitetura()

    print("\n" + "="*65)
    print("  Gerando imagens extras — Cap 2 (2ª imagem por seção)")
    print("="*65)
    cap2_01b_dashboard_sem_vs_com_narrativa()
    cap2_02b_big_idea_comparacao()
    cap2_05b_titulo_mensagem()
    cap2_08b_dashboard_sem_vs_com_zonas()
    cap2_09b_kpi_anatomia_exemplos()
    cap2_10b_pitch_erros_comuns()

    print("\n✅ Todas as imagens geradas com sucesso!")
