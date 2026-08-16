#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gerador_materiais_completos.py

Gera TODAS as imagens para Cap 2 (Semana Especial) e 5 protótipos HTML únicos
para cada grupo + seus respectivos PDFs.

Rodas: python3 gerador_materiais_completos.py

Saída:
  - aula/semana_especial/outputs/cap2_*.png (10+ imagens)
  - aula/semana_especial/grupo_a.html, grupo_b.html, ..., grupo_e.html
  - aula/semana_especial/grupo_a.pdf, grupo_b.pdf, ..., grupo_e.pdf
"""

import os
import json
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import seaborn as sns
from matplotlib.patches import Rectangle

warnings.filterwarnings("ignore")

# ===================================================================
# CONFIG
# ===================================================================

BASE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(BASE, "outputs")
os.makedirs(OUT, exist_ok=True)

PALETTE = {
    "destaque": "#E35D22",
    "primaria": "#2563EB",
    "positivo": "#16A34A",
    "alerta":   "#DC2626",
    "atencao":  "#EAB308",
    "neutra":   "#64748B",
    "marca":    "#0B3D2E",
    "bg":       "#F7F7F7",
}

plt.rcParams.update({
    "figure.facecolor": PALETTE["bg"],
    "axes.facecolor":   PALETTE["bg"],
    "font.family":      "DejaVu Sans",
    "axes.spines.top":  False,
    "axes.spines.right": False,
})

print(f"Gerando materiais em: {OUT}\n")

# ===================================================================
# CAP 2 — IMAGENS EXPLICATIVAS
# ===================================================================

print("[1/16] Gerando: AED vs Explanatória...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle("AED vs Análise Explanatória — Mudança de Perspectiva", fontsize=13, fontweight="bold")

# AED
ax1.text(0.5, 0.95, "EXPLORATÓRIA (AED)", ha="center", fontsize=11, fontweight="bold",
         transform=ax1.transAxes, color=PALETTE["primaria"])
ax1.text(0.5, 0.85, "Pergunta: O que os dados me dizem?", ha="center", fontsize=9,
         transform=ax1.transAxes, style="italic")
items_aed = [
    "Visualizações: centenas",
    "Audiência: você mesmo",
    "Objetivo: entender",
    "Processo: descritivo",
    "Saída: curiosidade satisfeita",
]
y = 0.75
for i, item in enumerate(items_aed):
    ax1.text(0.1, y - i*0.12, f"• {item}", fontsize=9, transform=ax1.transAxes)
ax1.axis("off")

# Explanatória
ax2.text(0.5, 0.95, "EXPLANATÓRIA", ha="center", fontsize=11, fontweight="bold",
         transform=ax2.transAxes, color=PALETTE["destaque"])
ax2.text(0.5, 0.85, "Pergunta: Como eu conto para alguém decidir?", ha="center", fontsize=9,
         transform=ax2.transAxes, style="italic")
items_exp = [
    "Visualizações: ~5 (selecionadas)",
    "Audiência: CEO, gerente, investidor",
    "Objetivo: provocar decisão",
    "Processo: prescritivo",
    "Saída: ação definida",
]
y = 0.75
for i, item in enumerate(items_exp):
    ax2.text(0.1, y - i*0.12, f"• {item}", fontsize=9, transform=ax2.transAxes)
ax2.axis("off")

plt.tight_layout()
plt.savefig(os.path.join(OUT, "cap2_01_aed_vs_explanatoria.png"), dpi=150, bbox_inches="tight")
plt.close()

# ===================================================================
print("[2/16] Gerando: Big Idea Framework...")

fig, ax = plt.subplots(figsize=(11, 6))
ax.axis("off")

# Título
ax.text(0.5, 0.95, "Big Idea — 3 Componentes Obrigatórios", ha="center", fontsize=13, fontweight="bold",
        transform=ax.transAxes)

# Caixa 1: Ponto de Vista
rect1 = FancyBboxPatch((0.05, 0.65), 0.28, 0.22, boxstyle="round,pad=0.01",
                       transform=ax.transAxes, facecolor="#FFE5CC", edgecolor=PALETTE["destaque"], linewidth=2)
ax.add_patch(rect1)
ax.text(0.05+0.14, 0.81, "1. PONTO DE VISTA", ha="center", fontsize=9, fontweight="bold",
        transform=ax.transAxes, color=PALETTE["destaque"])
ax.text(0.05+0.14, 0.73, "Afirmação de ação,\nnão observação passiva", ha="center", fontsize=8,
        transform=ax.transAxes)
ax.text(0.05+0.14, 0.66, '✗ "O dado mostra X"\n✓ "Devemos fazer Y"', ha="center", fontsize=7.5,
        transform=ax.transAxes, family="monospace")

# Caixa 2: Tensão
rect2 = FancyBboxPatch((0.36, 0.65), 0.28, 0.22, boxstyle="round,pad=0.01",
                       transform=ax.transAxes, facecolor="#E3F2FD", edgecolor=PALETTE["primaria"], linewidth=2)
ax.add_patch(rect2)
ax.text(0.36+0.14, 0.81, "2. TENSÃO", ha="center", fontsize=9, fontweight="bold",
        transform=ax.transAxes, color=PALETTE["primaria"])
ax.text(0.36+0.14, 0.73, "O que está em jogo?\nQual o risco de não agir?", ha="center", fontsize=8,
        transform=ax.transAxes)
ax.text(0.36+0.14, 0.66, "Dado que revela\no problema urgente", ha="center", fontsize=7.5,
        transform=ax.transAxes, family="monospace")

# Caixa 3: Stake
rect3 = FancyBboxPatch((0.67, 0.65), 0.28, 0.22, boxstyle="round,pad=0.01",
                       transform=ax.transAxes, facecolor="#F1F8E9", edgecolor=PALETTE["positivo"], linewidth=2)
ax.add_patch(rect3)
ax.text(0.67+0.14, 0.81, "3. STAKE", ha="center", fontsize=9, fontweight="bold",
        transform=ax.transAxes, color=PALETTE["positivo"])
ax.text(0.67+0.14, 0.73, "Por que a audiência\ndeveria se importar?", ha="center", fontsize=8,
        transform=ax.transAxes)
ax.text(0.67+0.14, 0.66, "Impacto financeiro\nconcreto: R$, % ou KPI", ha="center", fontsize=7.5,
        transform=ax.transAxes, family="monospace")

# Fórmula
ax.text(0.5, 0.50, "FÓRMULA:", ha="center", fontsize=9, fontweight="bold",
        transform=ax.transAxes)
ax.text(0.5, 0.43, "[Ação Recomendada] + [Dado que Justifica] + [Impacto Financeiro/Operacional]",
        ha="center", fontsize=9, transform=ax.transAxes,
        bbox=dict(boxstyle="round", facecolor=PALETTE["bg"], edgecolor="black", linewidth=1.5))

# Exemplo
ax.text(0.5, 0.28, "EXEMPLO:", ha="center", fontsize=9, fontweight="bold",
        transform=ax.transAxes)
ax.text(0.5, 0.08, '"Se não corrigirmos o onboarding até setembro, perderemos R$1,2M\nem receita\nrecorrente nos próximos 12 meses — implementar fluxo guiado no app pode reverter 40% desse risco."',
        ha="center", fontsize=8, transform=ax.transAxes,
        bbox=dict(boxstyle="round", facecolor="#FFF8E1", edgecolor=PALETTE["atencao"], linewidth=1.5),
        style="italic")

plt.tight_layout()
plt.savefig(os.path.join(OUT, "cap2_02_big_idea_framework.png"), dpi=150, bbox_inches="tight")
plt.close()

# ===================================================================
print("[3/16] Gerando: Storyboard Estrutura...")

fig, ax = plt.subplots(figsize=(13, 7))
ax.axis("off")
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

title = "Storyboard — Estrutura Narrativa em 4 Atos"
ax.text(5, 9.5, title, ha="center", fontsize=13, fontweight="bold")

# Ato 1
rect1 = Rectangle((0.3, 6), 2, 2.5, facecolor="#E3F2FD", edgecolor=PALETTE["primaria"], linewidth=2)
ax.add_patch(rect1)
ax.text(1.3, 8, "ATO 1\nCONTEXTO", ha="center", va="center", fontsize=9, fontweight="bold",
        color=PALETTE["primaria"])
ax.text(1.3, 7.2, "O que é\nEstado Atual\nKPIs Reais", ha="center", va="center", fontsize=7)

# Seta 1
ax.annotate("", xy=(2.8, 7.2), xytext=(2.3, 7.2),
            arrowprops=dict(arrowstyle="->" , lw=2, color="black"))

# Ato 2
rect2 = Rectangle((2.8, 6), 2, 2.5, facecolor="#FFF3E0", edgecolor=PALETTE["destaque"], linewidth=2)
ax.add_patch(rect2)
ax.text(3.8, 8, "ATO 2\nCONFLITO", ha="center", va="center", fontsize=9, fontweight="bold",
        color=PALETTE["destaque"])
ax.text(3.8, 7.2, "O que poderia ser\nTensão Revelada\nProblema Crítico", ha="center", va="center", fontsize=7)

# Seta 2
ax.annotate("", xy=(5.3, 7.2), xytext=(4.8, 7.2),
            arrowprops=dict(arrowstyle="->" , lw=2, color="black"))

# Ato 3
rect3 = Rectangle((5.3, 6), 2, 2.5, facecolor="#F1F8E9", edgecolor=PALETTE["positivo"], linewidth=2)
ax.add_patch(rect3)
ax.text(6.3, 8, "ATO 3\nRESOLUÇÃO", ha="center", va="center", fontsize=9, fontweight="bold",
        color=PALETTE["positivo"])
ax.text(6.3, 7.2, "O que Proponho\nRecomendação\nEvidência", ha="center", va="center", fontsize=7)

# Seta 3
ax.annotate("", xy=(7.8, 7.2), xytext=(7.3, 7.2),
            arrowprops=dict(arrowstyle="->" , lw=2, color="black"))

# Ato 4
rect4 = Rectangle((7.8, 6), 2, 2.5, facecolor="#FCE4EC", edgecolor=PALETTE["marca"], linewidth=2)
ax.add_patch(rect4)
ax.text(8.8, 8, "ATO 4\nAÇÃO", ha="center", va="center", fontsize=9, fontweight="bold",
        color=PALETTE["marca"])
ax.text(8.8, 7.2, "Call to Action\nDecisão + Prazo\n+ Responsável", ha="center", va="center", fontsize=7)

# Em telas
ax.text(1.3, 5.3, "KPIs Atuais", ha="center", fontsize=7, style="italic", color=PALETTE["neutra"])
ax.text(3.8, 5.3, "Gráfico de Problema", ha="center", fontsize=7, style="italic", color=PALETTE["neutra"])
ax.text(6.3, 5.3, "Análise/Evidências", ha="center", fontsize=7, style="italic", color=PALETTE["neutra"])
ax.text(8.8, 5.3, "Recomendação", ha="center", fontsize=7, style="italic", color=PALETTE["neutra"])

# Exemplo prático
ax.text(5, 4.3, "EXEMPLO PRÁTICO — Estrutura de uma Apresentação", ha="center", fontsize=10, fontweight="bold")
ax.text(5, 3.6, 'Tela 1: "Vendas em RJ cresceram 18% em jan/2026, acima da meta 15%"',
        ha="center", fontsize=8)
ax.text(5, 3.1, 'Tela 2: "Mas 70% desse crescimento vem de descontos acima de 25%", destruindo margem',
        ha="center", fontsize=8)
ax.text(5, 2.6, "Tela 3: Análise de elasticidade preço × volume mostra que reduzindo desconto para 15%",
        ha="center", fontsize=8)
ax.text(5, 2.1, "mantemos 85% do volume com margem positiva",
        ha="center", fontsize=8)
ax.text(5, 1.3, 'Tela 4: "Implementar política de desconto máximo 15% em RJ até 15/fev —',
        ha="center", fontsize=8, fontweight="bold")
ax.text(5, 0.8, 'impacto projetado: +R$45k em margem trimestral — Responsável: Gerência Comercial"',
        ha="center", fontsize=8, fontweight="bold")

plt.tight_layout()
plt.savefig(os.path.join(OUT, "cap2_03_storyboard.png"), dpi=150, bbox_inches="tight")
plt.close()

# ===================================================================
print("[4/16] Gerando: Atributos Pré-atencionais...")

fig, axes = plt.subplots(2, 3, figsize=(14, 8))
fig.suptitle("Atributos Pré-atencionais — Decodificados em <250ms", fontsize=13, fontweight="bold")

# COR
ax = axes[0, 0]
ax.bar([1, 2, 3, 4], [5, 3, 4, 2], color=[PALETTE["destaque"], PALETTE["neutra"], PALETTE["neutra"], PALETTE["neutra"]])
ax.set_title("COR: Destaque", fontsize=10, fontweight="bold")
ax.set_ylabel("Valor")
ax.set_xticks([1, 2, 3, 4])
ax.set_xticklabels(["A", "B", "C", "D"])
ax.text(1, 5.3, "← Olho vai\nauqui primeiro", fontsize=8, ha="center", color=PALETTE["destaque"], fontweight="bold")

# TAMANHO
ax = axes[0, 1]
sizes = [100, 300, 150, 200]
ax.scatter([1, 2, 3, 4], [5, 4, 3, 2], s=sizes, color=PALETTE["primaria"], alpha=0.6)
ax.set_title("TAMANHO: Magnitude", fontsize=10, fontweight="bold")
ax.set_ylabel("Categoria")
ax.set_yticks([2, 3, 4, 5])
ax.set_yticklabels(["D", "C", "B", "A"])
ax.set_xticks([])
ax.text(2, 5.5, "← Maior = mais\nimportante", fontsize=8, ha="center", color=PALETTE["primaria"], fontweight="bold")

# POSIÇÃO
ax = axes[0, 2]
ax.axis("off")
rect_tl = Rectangle((0.05, 0.7), 0.4, 0.25, facecolor=PALETTE["destaque"], alpha=0.8)
ax.add_patch(rect_tl)
ax.text(0.25, 0.825, "CRUCIAL", ha="center", va="center", fontsize=8, fontweight="bold", color="white")
rect_tr = Rectangle((0.55, 0.7), 0.4, 0.25, facecolor=PALETTE["neutra"], alpha=0.3)
ax.add_patch(rect_tr)
ax.text(0.75, 0.825, "Secundário", ha="center", va="center", fontsize=8, color="white")
rect_bl = Rectangle((0.05, 0.25), 0.4, 0.25, facecolor=PALETTE["neutra"], alpha=0.3)
ax.add_patch(rect_bl)
ax.text(0.25, 0.375, "Menos", ha="center", va="center", fontsize=8, color="white")
rect_br = Rectangle((0.55, 0.25), 0.4, 0.25, facecolor=PALETTE["neutra"], alpha=0.3)
ax.add_patch(rect_br)
ax.text(0.75, 0.375, "Menos", ha="center", va="center", fontsize=8, color="white")
ax.set_title("POSIÇÃO: Hierarquia", fontsize=10, fontweight="bold")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# INTENSIDADE
ax = axes[1, 0]
x = np.arange(4)
colors_intensity = [plt.cm.Blues(i) for i in [0.3, 0.6, 0.8, 1.0]]
ax.bar(x, [2, 4, 6, 8], color=colors_intensity)
ax.set_title("INTENSIDADE: Contraste", fontsize=10, fontweight="bold")
ax.set_ylabel("Valor")
ax.set_xticks(x)
ax.set_xticklabels(["Fraco", "Médio", "Forte", "Crítico"])
ax.text(2.5, 8.5, "← Mais escuro =\nMais importante", fontsize=8, ha="center", fontweight="bold")

# ENCLOSURE
ax = axes[1, 1]
ax.scatter([1, 2, 3, 4], [5, 4, 3, 2], s=200, color=PALETTE["primaria"], alpha=0.3)
rect_enc = Rectangle((0.7, 2.5), 1.8, 3, facecolor="none", edgecolor=PALETTE["destaque"], linewidth=3)
ax.add_patch(rect_enc)
ax.set_title("ENCLOSURE: Agrupamento", fontsize=10, fontweight="bold")
ax.set_ylabel("Categoria")
ax.set_yticks([2, 3, 4, 5])
ax.set_yticklabels(["D", "C", "B", "A"])
ax.set_xticks([])
ax.text(2.2, 2, "← Caixa agrupa\nos relacionados", fontsize=8, ha="center", color=PALETTE["destaque"], fontweight="bold")

# REGRA PRÁTICA
ax = axes[1, 2]
ax.axis("off")
ax.text(0.5, 0.9, "REGRA DE OURO", ha="center", fontsize=10, fontweight="bold",
        transform=ax.transAxes)
ax.text(0.5, 0.7, "Use MÁXIMO\n2 atributos pré-atencionais\npor visual", ha="center", fontsize=9,
        transform=ax.transAxes,
        bbox=dict(boxstyle="round", facecolor="#FFE5CC", edgecolor=PALETTE["destaque"], linewidth=2))
ax.text(0.5, 0.3, "Acima disso,\na hierarquia colapsa\ne o olho não sabe\nonde pousar", ha="center", fontsize=8,
        transform=ax.transAxes, style="italic")

plt.tight_layout()
plt.savefig(os.path.join(OUT, "cap2_04_atributos_preatencionais.png"), dpi=150, bbox_inches="tight")
plt.close()

# ===================================================================
print("[5/16] Gerando: Teste do Relance (Antes e Depois)...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("Teste do Relance — Seu Gráfico Passa em 3 Segundos?", fontsize=13, fontweight="bold")

# ANTES (Ruim)
ax1.set_title("❌ ANTES — Falha no Teste", fontsize=11, fontweight="bold", color=PALETTE["alerta"])
x = np.arange(5)
y = [45, 38, 52, 31, 47]
colors_bad = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#FFA07A", "#98D8C8"]
ax1.bar(x, y, color=colors_bad)
ax1.set_ylabel("Vendas (R$ mil)", fontsize=9)
ax1.set_xticks(x)
ax1.set_xticklabels(["Jan", "Fev", "Mar", "Abr", "Mai"], fontsize=9)
ax1.set_title("Gráfico de Barras", fontsize=9)
ax1.text(2, -15, "Problemas:\n• Título rótulo, não-mensagem\n• 5 cores diferentes\n• Qual é a mensagem em 3s?",
         ha="center", fontsize=8, bbox=dict(boxstyle="round", facecolor="#FFE5E5", alpha=0.8))

# DEPOIS (Bom)
ax2.set_title("✓ DEPOIS — Passa no Teste", fontsize=11, fontweight="bold", color=PALETTE["positivo"])
x = np.arange(5)
y = [45, 38, 52, 31, 47]
colors_good = [PALETTE["neutra"], PALETTE["neutra"], PALETTE["destaque"], PALETTE["neutra"], PALETTE["neutra"]]
ax2.bar(x, y, color=colors_good)
ax2.set_ylabel("Vendas (R$ mil)", fontsize=9)
ax2.set_xticks(x)
ax2.set_xticklabels(["Jan", "Fev", "Mar", "Abr", "Mai"], fontsize=9)
ax2.set_title("Março ultrapassa meta em 73% — urgência de investigação", fontsize=10, fontweight="bold")
ax2.text(2, -15, "Melhorias:\n• Título-mensagem\n• 1 cor de destaque\n• Mensagem clara em 3s",
         ha="center", fontsize=8, bbox=dict(boxstyle="round", facecolor="#E8F5E9", alpha=0.8))

plt.tight_layout()
plt.savefig(os.path.join(OUT, "cap2_05_teste_relance.png"), dpi=150, bbox_inches="tight")
plt.close()

# ===================================================================
print("[6/16] Gerando: Data-Ink Ratio e Chartjunk...")

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle("Data-Ink Ratio — Maximizar a Proporção de Tinta que Representa Dados", fontsize=13, fontweight="bold")

# Antes (Chartjunk)
ax = axes[0]
ax.set_title("❌ ANTES: Data-Ink Ratio Baixo (~40%)", fontsize=10, fontweight="bold", color=PALETTE["alerta"])
x = ["A", "B", "C", "D"]
y = [65, 78, 52, 45]
# Gráfico 3D (fake)
for i, (xi, yi) in enumerate(zip(x, y)):
    ax.bar(xi, yi, color=PALETTE["primaria"], alpha=0.7, width=0.6,
           edgecolor="black", linewidth=2)
    ax.plot([i-0.35, i-0.35], [0, yi], "k-", linewidth=2)
ax.set_ylabel("Valor", fontsize=9)
ax.grid(True, alpha=0.3, linestyle="--", linewidth=1)
ax.set_axisbelow(True)
ax.text(1.5, -20, "Problemas:\n• Grades pesadas\n• Bordas escuras\n• 'Profundidade' desnecessária\n• Legendas redundantes",
        ha="center", fontsize=8, bbox=dict(boxstyle="round", facecolor="#FFE5E5", alpha=0.8))

# Depois (Limpo)
ax = axes[1]
ax.set_title("✓ DEPOIS: Data-Ink Ratio Alto (~85%)", fontsize=10, fontweight="bold", color=PALETTE["positivo"])
x = ["A", "B", "C", "D"]
y = [65, 78, 52, 45]
colors_clean = [PALETTE["neutra"] if yi != max(y) else PALETTE["destaque"] for yi in y]
ax.bar(x, y, color=colors_clean, width=0.5, edgecolor="none")
ax.spines["left"].set_visible(True)
ax.spines["left"].set_linewidth(0.5)
ax.spines["bottom"].set_visible(True)
ax.spines["bottom"].set_linewidth(0.5)
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.set_ylabel("Valor", fontsize=9)
ax.set_yticks([0, 20, 40, 60, 80])
ax.grid(True, alpha=0.1, axis="y", linestyle="-", linewidth=0.5)
ax.set_axisbelow(True)
ax.text(1.5, -20, "Melhorias:\n• Sem grades\n• Sem decoração\n• 1 cor de destaque\n• Máxima clareza",
        ha="center", fontsize=8, bbox=dict(boxstyle="round", facecolor="#E8F5E9", alpha=0.8))

plt.tight_layout()
plt.savefig(os.path.join(OUT, "cap2_06_datainkriatio.png"), dpi=150, bbox_inches="tight")
plt.close()

# ===================================================================
print("[7/16] Gerando: Filtros vs Parâmetros...")

fig, ax = plt.subplots(figsize=(13, 6))
ax.axis("off")

title = "Tableau: FILTROS vs PARÂMETROS"
ax.text(0.5, 0.95, title, ha="center", fontsize=13, fontweight="bold",
        transform=ax.transAxes)

# FILTRO (esquerda)
rect_f = FancyBboxPatch((0.05, 0.5), 0.4, 0.35, boxstyle="round,pad=0.02",
                       transform=ax.transAxes, facecolor="#E3F2FD", edgecolor=PALETTE["primaria"], linewidth=2)
ax.add_patch(rect_f)
ax.text(0.25, 0.81, "🔍 FILTRO", ha="center", fontsize=11, fontweight="bold",
        transform=ax.transAxes, color=PALETTE["primaria"])
ax.text(0.25, 0.755, "Inclui / Exclui LINHAS\ndo dataset", ha="center", fontsize=9,
        transform=ax.transAxes, fontweight="bold")
ax.text(0.25, 0.65, "Exemplo: Ver só PE", ha="center", fontsize=9, transform=ax.transAxes, family="monospace")
ax.text(0.25, 0.585, "→ Dados de SP desaparecem\n  da view", ha="center", fontsize=8,
        transform=ax.transAxes, style="italic")

# PARÂMETRO (direita)
rect_p = FancyBboxPatch((0.55, 0.5), 0.4, 0.35, boxstyle="round,pad=0.02",
                       transform=ax.transAxes, facecolor="#FFF3E0", edgecolor=PALETTE["destaque"], linewidth=2)
ax.add_patch(rect_p)
ax.text(0.75, 0.81, "⚙️ PARÂMETRO", ha="center", fontsize=11, fontweight="bold",
        transform=ax.transAxes, color=PALETTE["destaque"])
ax.text(0.75, 0.755, "Muda o CÁLCULO\nnenhuma linha é excluída", ha="center", fontsize=9,
        transform=ax.transAxes, fontweight="bold")
ax.text(0.75, 0.65, "Exemplo: Alternar Receita/Margem", ha="center", fontsize=9, transform=ax.transAxes, family="monospace")
ax.text(0.75, 0.585, "→ Todos dados permanecem\n  mudam apenas os valores", ha="center", fontsize=8,
        transform=ax.transAxes, style="italic")

# QUANDO USAR
ax.text(0.5, 0.42, "QUANDO USAR?", ha="center", fontsize=10, fontweight="bold",
        transform=ax.transAxes)

ax.text(0.25, 0.35, "FILTRO", ha="center", fontsize=9, fontweight="bold",
        transform=ax.transAxes, color=PALETTE["primaria"])
items_f = ["Selecionar região", "Escolher produto", "Ver período X", "Segmentar por categoria"]
for i, item in enumerate(items_f):
    ax.text(0.25, 0.30 - i*0.05, f"• {item}", ha="center", fontsize=8,
            transform=ax.transAxes)

ax.text(0.75, 0.35, "PARÂMETRO", ha="center", fontsize=9, fontweight="bold",
        transform=ax.transAxes, color=PALETTE["destaque"])
items_p = ["Alternar métrica", "Ajustar meta dinâmica", "Top N (5 vs 10 vs 20)", "Mudar granularidade (€ vs milhares)"]
for i, item in enumerate(items_p):
    ax.text(0.75, 0.30 - i*0.05, f"• {item}", ha="center", fontsize=8,
            transform=ax.transAxes)

# PSEUDOCÓDIGO
ax.text(0.5, 0.02, "PSEUDOCÓDIGO TABLEAU: IF [Métrica] = \"Receita\" THEN [Receita] ELSE [Unidades] END",
        ha="center", fontsize=8, transform=ax.transAxes, family="monospace",
        bbox=dict(boxstyle="round", facecolor=PALETTE["bg"], edgecolor="black", linewidth=1))

plt.tight_layout()
plt.savefig(os.path.join(OUT, "cap2_07_filtros_parametros.png"), dpi=150, bbox_inches="tight")
plt.close()

# ===================================================================
print("[8/16] Gerando: 3 Zonas do Dashboard Decisório...")

fig, ax = plt.subplots(figsize=(14, 6))
ax.axis("off")
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

title = "As 3 Zonas do Dashboard Decisório"
ax.text(5, 9.5, title, ha="center", fontsize=13, fontweight="bold")

# ZONA 1
rect1 = FancyBboxPatch((0.2, 6.5), 3, 2.5, boxstyle="round,pad=0.1",
                       facecolor="#E3F2FD", edgecolor=PALETTE["primaria"], linewidth=2.5)
ax.add_patch(rect1)
ax.text(1.7, 8.6, "ZONA 1 — CONTEXTO", ha="center", fontsize=10, fontweight="bold",
        color=PALETTE["primaria"])
ax.text(1.7, 8.0, "O que está acontecendo agora?", ha="center", fontsize=9, style="italic")
ax.text(1.7, 7.4, "✓ KPIs com meta\n✓ Deltas em ▲▼\n✓ Período explícito", ha="center", fontsize=8)
ax.text(1.7, 6.7, "Tempo: <5 seg", ha="center", fontsize=7, style="italic", color=PALETTE["neutra"])

# ZONA 2
rect2 = FancyBboxPatch((3.5, 6.5), 3, 2.5, boxstyle="round,pad=0.1",
                       facecolor="#FFF3E0", edgecolor=PALETTE["destaque"], linewidth=2.5)
ax.add_patch(rect2)
ax.text(5.0, 8.6, "ZONA 2 — DIAGNÓSTICO", ha="center", fontsize=10, fontweight="bold",
        color=PALETTE["destaque"])
ax.text(5.0, 8.0, "Por que está acontecendo?", ha="center", fontsize=9, style="italic")
ax.text(5.0, 7.4, "✓ Drill-down detalhado\n✓ Segmentação clara\n✓ Gráficos estratégicos", ha="center", fontsize=8)
ax.text(5.0, 6.7, "Tempo: 5-15 seg", ha="center", fontsize=7, style="italic", color=PALETTE["neutra"])

# ZONA 3
rect3 = FancyBboxPatch((6.8, 6.5), 3, 2.5, boxstyle="round,pad=0.1",
                       facecolor="#F1F8E9", edgecolor=PALETTE["positivo"], linewidth=2.5)
ax.add_patch(rect3)
ax.text(8.3, 8.6, "ZONA 3 — RECOMENDAÇÃO", ha="center", fontsize=10, fontweight="bold",
        color=PALETTE["positivo"])
ax.text(8.3, 8.0, "O que fazer?", ha="center", fontsize=9, style="italic")
ax.text(8.3, 7.4, "✓ 1-2 recomendações\n✓ Evidência clara\n✓ Call to Action", ha="center", fontsize=8)
ax.text(8.3, 6.7, "Tempo: decisão!", ha="center", fontsize=7, style="italic", color=PALETTE["neutra"])

# Fluxo
ax.annotate("", xy=(3.4, 7.75), xytext=(3.2, 7.75),
            arrowprops=dict(arrowstyle="->", lw=2, color="black"))
ax.annotate("", xy=(6.7, 7.75), xytext=(6.5, 7.75),
            arrowprops=dict(arrowstyle="->", lw=2, color="black"))

# Exemplo
ax.text(5, 5.5, "EXEMPLO PRÁTICO — Dashboard de Vendas", ha="center", fontsize=10, fontweight="bold")
ax.text(1.7, 4.9, "Big Number:\n\"R$ 2,3M\nGap vs Meta: +15%\n↑ verde", ha="center", fontsize=7.5,
        bbox=dict(boxstyle="round", facecolor="#E3F2FD", alpha=0.7))
ax.text(5.0, 4.9, "Scatter:\nReceita × Desconto\nlinha em 20%\n(onde margem cai)", ha="center", fontsize=7.5,
        bbox=dict(boxstyle="round", facecolor="#FFF3E0", alpha=0.7))
ax.text(8.3, 4.9, "Recomendação:\n\"Capear desconto\nem 15%\nImpacto: +R$ 85k\nPrazo: Q3\"", ha="center", fontsize=7.5,
        bbox=dict(boxstyle="round", facecolor="#F1F8E9", alpha=0.7))

# Regra
ax.text(5, 2.5, "REGRA:", ha="center", fontsize=9, fontweight="bold")
ax.text(5, 1.8, "Sem a Zona 3, o leitor sai com dados mas sem CLAREZA DE AÇÃO",
        ha="center", fontsize=9, style="italic",
        bbox=dict(boxstyle="round", facecolor="#FFE5CC", edgecolor=PALETTE["destaque"], linewidth=1.5))

plt.tight_layout()
plt.savefig(os.path.join(OUT, "cap2_08_3zonas_dashboard.png"), dpi=150, bbox_inches="tight")
plt.close()

# ===================================================================
print("[9/16] Gerando: Anatomia de um KPI...")

fig, ax = plt.subplots(figsize=(12, 7))
ax.axis("off")

title = "Anatomia de um KPI Decisório — 5 Componentes"
ax.text(0.5, 0.96, title, ha="center", fontsize=12, fontweight="bold",
        transform=ax.transAxes)

# Exemplo visual
kpi_box = FancyBboxPatch((0.1, 0.6), 0.8, 0.25, boxstyle="round,pad=0.02",
                        transform=ax.transAxes, facecolor="#F5F5F5", edgecolor="black", linewidth=2)
ax.add_patch(kpi_box)

# Rótulo
ax.text(0.15, 0.82, "Taxa de Aprovação", ha="left", fontsize=9, fontweight="bold",
        transform=ax.transAxes)

# Big Number
ax.text(0.5, 0.72, "78%", ha="center", fontsize=32, fontweight="bold",
        transform=ax.transAxes, color=PALETTE["primaria"])

# Meta
ax.text(0.72, 0.75, "Meta: 80%", ha="left", fontsize=8, transform=ax.transAxes)

# Gap
ax.text(0.72, 0.70, "Gap: -2pp", ha="left", fontsize=8, color=PALETTE["alerta"], fontweight="bold",
        transform=ax.transAxes)

# Tendência
ax.text(0.72, 0.65, "Tendência: ▼", ha="left", fontsize=10, color=PALETTE["alerta"], fontweight="bold",
        transform=ax.transAxes)

# Período
ax.text(0.15, 0.62, "Período: YTD 2026", ha="left", fontsize=7, style="italic",
        transform=ax.transAxes, color=PALETTE["neutra"])

# 5 Componentes explicados
components = [
    ("1. Rótulo Descritivo", "Diz o que o número representa", 0.88),
    ("2. Valor Atual", "78% — o número do período", 0.82),
    ("3. Meta (Target)", "80% — o que deveria ser", 0.76),
    ("4. Gap", "-2pp — distância em valor\ne percentual. Cor semântica!", 0.70),
    ("5. Tendência", "▼ — seta indica direção.\n▲ = melhorando, ▼ = piorando", 0.62),
]

for label, desc, y in components:
    ax.text(0.05, y, label, ha="left", fontsize=9, fontweight="bold",
            transform=ax.transAxes)
    ax.text(0.35, y, desc, ha="left", fontsize=8,
            transform=ax.transAxes, style="italic", color=PALETTE["neutra"])

# VARIAÇÃO
ax.text(0.5, 0.45, "VARIAÇÕES DE KPI VISUAL", ha="center", fontsize=10, fontweight="bold",
        transform=ax.transAxes)

# Bullet Chart
ax.text(0.2, 0.36, "Bullet Chart (Stephen Few)", ha="center", fontsize=8, fontweight="bold",
        transform=ax.transAxes)
ax.barh([1], [78], left=0, height=0.3, color=PALETTE["primaria"], transform=ax.transAxes)
ax.barh([1], [80], left=0, height=0.5, color=PALETTE["neutra"], alpha=0.2, transform=ax.transAxes)
ax.plot([0.8, 0.8], [0.8, 1.2], "r-", linewidth=2, transform=ax.transAxes)
ax.text(0.5, 0.15, "Real (78) vs Meta (80)\nem uma linha — eficiente!", ha="center", fontsize=7,
        transform=ax.transAxes, style="italic")

# Sparkline
ax.text(0.75, 0.36, "Sparkline (Mudança)", ha="center", fontsize=8, fontweight="bold",
        transform=ax.transAxes)
spark_x = [0.65, 0.68, 0.70, 0.72, 0.75, 0.78, 0.80]
spark_y = [0.25, 0.27, 0.26, 0.24, 0.23, 0.22, 0.20]
ax.plot(spark_x, spark_y, linewidth=2, color=PALETTE["alerta"], transform=ax.transAxes, marker="o", markersize=3)
ax.text(0.75, 0.15, "Sparkline mostra\ntendência em 1cm", ha="center", fontsize=7,
        transform=ax.transAxes, style="italic")

# ANTI-PADRÕES
ax.text(0.5, 0.05, "❌ ANTI-PADRÕES: Número isolado sem meta | Sem período de referência | " +
        "Sem tendência | Sem definição da métrica",
        ha="center", fontsize=7, transform=ax.transAxes,
        bbox=dict(boxstyle="round", facecolor="#FFE5E5", alpha=0.8))

plt.tight_layout()
plt.savefig(os.path.join(OUT, "cap2_09_anatomia_kpi.png"), dpi=150, bbox_inches="tight")
plt.close()

# ===================================================================
print("[10/16] Gerando: Pitch de 3 Minutos (SCR)...")

fig, ax = plt.subplots(figsize=(14, 7))
ax.axis("off")

title = "Pitch de 3 Minutos — Estrutura SCR (Situação, Complicação, Resolução)"
ax.text(0.5, 0.96, title, ha="center", fontsize=12, fontweight="bold",
        transform=ax.transAxes)

# SITUAÇÃO
rect_s = FancyBboxPatch((0.05, 0.70), 0.27, 0.20, boxstyle="round,pad=0.01",
                       transform=ax.transAxes, facecolor="#E3F2FD", edgecolor=PALETTE["primaria"], linewidth=2)
ax.add_patch(rect_s)
ax.text(0.185, 0.87, "SITUAÇÃO", ha="center", fontsize=9, fontweight="bold",
        transform=ax.transAxes, color=PALETTE["primaria"])
ax.text(0.185, 0.79, "30 segundos", ha="center", fontsize=7, style="italic",
        transform=ax.transAxes, color=PALETTE["neutra"])
ax.text(0.185, 0.74, "Contexto factual.\nDado impactante,\nNÃO intro genérica", ha="center", fontsize=7.5,
        transform=ax.transAxes)

# COMPLICAÇÃO
rect_c = FancyBboxPatch((0.36, 0.70), 0.27, 0.20, boxstyle="round,pad=0.01",
                       transform=ax.transAxes, facecolor="#FFF3E0", edgecolor=PALETTE["destaque"], linewidth=2)
ax.add_patch(rect_c)
ax.text(0.495, 0.87, "COMPLICAÇÃO", ha="center", fontsize=9, fontweight="bold",
        transform=ax.transAxes, color=PALETTE["destaque"])
ax.text(0.495, 0.79, "45 segundos", ha="center", fontsize=7, style="italic",
        transform=ax.transAxes, color=PALETTE["neutra"])
ax.text(0.495, 0.74, "O problema/\noportunidade\nA Big Idea", ha="center", fontsize=7.5,
        transform=ax.transAxes)

# RESOLUÇÃO
rect_r = FancyBboxPatch((0.67, 0.70), 0.27, 0.20, boxstyle="round,pad=0.01",
                       transform=ax.transAxes, facecolor="#F1F8E9", edgecolor=PALETTE["positivo"], linewidth=2)
ax.add_patch(rect_r)
ax.text(0.805, 0.87, "RESOLUÇÃO", ha="center", fontsize=9, fontweight="bold",
        transform=ax.transAxes, color=PALETTE["positivo"])
ax.text(0.805, 0.79, "60 segundos", ha="center", fontsize=7, style="italic",
        transform=ax.transAxes, color=PALETTE["neutra"])
ax.text(0.805, 0.74, "Evidência +\nrecomendação\n% ou R$ concreto", ha="center", fontsize=7.5,
        transform=ax.transAxes)

# Setas
ax.annotate("", xy=(0.35, 0.80), xytext=(0.32, 0.80),
            arrowprops=dict(arrowstyle="->", lw=2, color="black"))
ax.annotate("", xy=(0.66, 0.80), xytext=(0.63, 0.80),
            arrowprops=dict(arrowstyle="->", lw=2, color="black"))

# PRÓXIMO PASSO
rect_p = FancyBboxPatch((0.2, 0.48), 0.6, 0.15, boxstyle="round,pad=0.01",
                       transform=ax.transAxes, facecolor="#FCE4EC", edgecolor=PALETTE["marca"], linewidth=2)
ax.add_patch(rect_p)
ax.text(0.5, 0.59, "PRÓXIMO PASSO (45 segundos)", ha="center", fontsize=9, fontweight="bold",
        transform=ax.transAxes, color=PALETTE["marca"])
ax.text(0.5, 0.52, "Verbo + Quem + Prazo\nEx.: \"Implementar programa X até 30/junho com orçamento Y\"",
        ha="center", fontsize=8, transform=ax.transAxes)

# EXEMPLO PRÁTICO
ax.text(0.5, 0.40, "EXEMPLO PRÁTICO", ha="center", fontsize=9, fontweight="bold",
        transform=ax.transAxes)

y_start = 0.35
ax.text(0.05, y_start, "SIT:", fontsize=8, fontweight="bold", transform=ax.transAxes)
ax.text(0.15, y_start, "\"6.607 alunos; taxa de aprovação 99%; média 67,2 pts. Mas 27% têm nota < 60.\"",
        fontsize=7.5, transform=ax.transAxes)

y_start -= 0.06
ax.text(0.05, y_start, "COM:", fontsize=8, fontweight="bold", transform=ax.transAxes)
ax.text(0.15, y_start, "\"Alunos com envolvimento familiar baixo + <15h estudo têm nota 9 pts abaixo da média.\"",
        fontsize=7.5, transform=ax.transAxes)

y_start -= 0.06
ax.text(0.05, y_start, "RES:", fontsize=8, fontweight="bold", transform=ax.transAxes)
ax.text(0.15, y_start, "\"Programa de mentoria + comunicação familiar pode recuperar 40% desses alunos.\"",
        fontsize=7.5, transform=ax.transAxes)

y_start -= 0.06
ax.text(0.05, y_start, "PRÓX:", fontsize=8, fontweight="bold", transform=ax.transAxes)
ax.text(0.15, y_start, "\"Implantar protocolo de contato familiar para 220 alunos até fim de maio.\"",
        fontsize=7.5, transform=ax.transAxes)

plt.tight_layout()
plt.savefig(os.path.join(OUT, "cap2_10_pitch_3minutos.png"), dpi=150, bbox_inches="tight")
plt.close()

print("\n✓ [10/16] TODAS AS IMAGENS DO CAP 2 CRIADAS!\n")

# ===================================================================
# PROTÓTIPOS HTML PARA OS 5 GRUPOS
# ===================================================================

print("[11/16] Gerando: Protótipo HTML Grupo A (Olist E-commerce)...")

grupo_a_html = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Dashboard Olist — Atrasos Logísticos</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
:root {
  --brand: #D62828;
  --accent: #F77F00;
  --bg: #FCBAD3;
  --text: #2A2A2A;
  --light: #FFFFFF;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Segoe UI', Arial, sans-serif; background: linear-gradient(135deg, #FFFFFF 0%, var(--bg) 100%); }
header { background: linear-gradient(135deg, var(--brand) 0%, #A41E34 100%); color: white; padding: 25px 30px; }
header h1 { font-size: 1.8rem; margin-bottom: 8px; }
.dash { max-width: 1400px; margin: 20px auto; padding: 0 20px; }
.section-title { font-size: 0.85rem; font-weight: 700; color: var(--brand); text-transform: uppercase; margin: 25px 0 12px; letter-spacing: 0.08em; }
.kpi-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 20px; }
.kpi { background: white; padding: 15px; border-radius: 8px; border-left: 4px solid var(--brand); }
.kpi .val { font-size: 1.8rem; font-weight: 700; color: var(--brand); }
.kpi .lbl { font-size: 0.75rem; color: #888; margin-top: 6px; }
.charts { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 20px; }
.chart-card { background: white; padding: 18px; border-radius: 8px; }
.chart-card h3 { font-size: 0.9rem; font-weight: 700; margin-bottom: 10px; color: var(--brand); }
.insight { background: linear-gradient(135deg, #FFF8DC 0%, #FFECCC 100%); border-left: 4px solid var(--accent); padding: 15px; border-radius: 6px; margin: 15px 0; }
.insight .tag { font-size: 0.7rem; font-weight: 700; color: var(--accent); text-transform: uppercase; }
.insight .txt { font-size: 0.85rem; margin-top: 6px; line-height: 1.4; }
table { width: 100%; border-collapse: collapse; margin: 15px 0; font-size: 0.85rem; }
th { background: var(--brand); color: white; padding: 10px; text-align: left; font-weight: 700; }
td { padding: 8px; border-bottom: 1px solid #eee; }
tr:hover { background: #f9f9f9; }
.cta { background: var(--brand); color: white; padding: 20px; border-radius: 8px; margin: 15px 0; text-align: center; }
.cta h3 { font-size: 1rem; margin-bottom: 10px; }
footer { text-align: center; padding: 20px; font-size: 0.75rem; color: #999; }
</style>
</head>
<body>
<header>
  <h1>🚚 Dashboard Olist — Análise de Atrasos Logísticos</h1>
  <p>Impacto de atrasos nas avaliações dos clientes e churn de vendedores | Base: 100k+ pedidos</p>
</header>

<div class="dash">
  <p class="section-title">Contexto — KPIs Críticos</p>
  <div class="kpi-row">
    <div class="kpi">
      <div class="val" style="color:#D62828;">34%</div>
      <div class="lbl">Eletrônicos em SP<br>com atraso</div>
    </div>
    <div class="kpi">
      <div class="val" style="color:#F77F00;">3.2★</div>
      <div class="lbl">Review médio<br>(com atraso)</div>
    </div>
    <div class="kpi">
      <div class="val">4.1★</div>
      <div class="lbl">Review potencial<br>(sem atraso)</div>
    </div>
    <div class="kpi">
      <div class="val" style="color:#D62828;">-15%</div>
      <div class="lbl">Churn de vendedores<br>em risco</div>
    </div>
  </div>

  <p class="section-title">Diagnóstico — Onde Estão os Atrasos?</p>
  <div class="charts">
    <div class="chart-card">
      <h3>Top 5 Categorias com Mais Atrasos</h3>
      <canvas id="chart1" height="200"></canvas>
    </div>
    <div class="chart-card">
      <h3>Dias de Atraso vs Review Score</h3>
      <p style="font-size:0.75rem; color:#999; margin-bottom:8px;">Correlação: -0.62 | Cada dia de atraso = -0.15 ★</p>
      <canvas id="chart2" height="200"></canvas>
    </div>
  </div>

  <div class="insight">
    <div class="tag">[Insight IA] Acionável</div>
    <div class="txt"><strong>Eletrônicos em SP concentram 34% dos atrasos totais e puxam o review médio para 3,2 estrelas — priorizar logística nessa categoria pode elevar o review para 4,1 e reduzir o churn de vendedores em 15%, preservando R$280k em GMV anual.</strong></div>
  </div>

  <div class="cta">
    <h3>📋 CALL TO ACTION</h3>
    <p><strong>Redesenhar a rota logística de Eletrônicos em SP até Q3/2026.</strong><br>
    Responsável: Gerência de Logística | Impacto projetado: +0.9★ no review médio</p>
  </div>

  <p class="section-title">Análise Detalhada</p>
  <table>
    <thead><tr><th>Estado</th><th>Categoria</th><th>% Atraso</th><th>Review Médio</th><th>Prioridade</th></tr></thead>
    <tbody>
      <tr><td>SP</td><td>Eletrônicos</td><td>34%</td><td>3.2</td><td><strong style="color:#D62828;">CRÍTICA</strong></td></tr>
      <tr><td>RJ</td><td>Eletrônicos</td><td>28%</td><td>3.5</td><td style="color:#F77F00;">Alta</td></tr>
      <tr><td>SP</td><td>Móveis</td><td>22%</td><td>3.7</td><td style="color:#F77F00;">Alta</td></tr>
      <tr><td>MG</td><td>Eletrônicos</td><td>18%</td><td>3.8</td><td>Média</td></tr>
      <tr><td>BA</td><td>Eletrônicos</td><td>15%</td><td>3.9</td><td>Média</td></tr>
    </tbody>
  </table>

  <footer>Dashboard gerado via Pipeline Multi-Agente | Dados: Olist Public Dataset | Atualização: mai/2026</footer>
</div>

<script>
new Chart(document.getElementById('chart1'), {
  type: 'bar',
  data: {
    labels: ['Eletrônicos', 'Móveis', 'Livros', 'Esportes', 'Beleza'],
    datasets: [{
      label: '% Atraso',
      data: [34, 22, 18, 12, 9],
      backgroundColor: ['#D62828', '#F77F00', '#F77F00', '#CCCCCC', '#CCCCCC']
    }]
  },
  options: {
    indexAxis: 'y',
    plugins: { legend: { display: false } },
    scales: { x: { min: 0, max: 40 } }
  }
});

new Chart(document.getElementById('chart2'), {
  type: 'scatter',
  data: {
    datasets: [{
      label: 'Atraso vs Review',
      data: [{x:0, y:4.3}, {x:1, y:4.1}, {x:2, y:3.9}, {x:3, y:3.7}, {x:4, y:3.5}, {x:5, y:3.2}, {x:8, y:2.8}],
      backgroundColor: '#D62828',
      borderColor: '#D62828',
      showLine: true,
      fill: false,
      tension: 0.4
    }]
  },
  options: {
    plugins: { legend: { display: false } },
    scales: {
      x: { title: { display: true, text: 'Dias de Atraso' } },
      y: { title: { display: true, text: 'Review Score' }, min: 2.5, max: 4.5 }
    }
  }
});
</script>
</body>
</html>
'''

with open(os.path.join(BASE, "grupo_a.html"), "w", encoding="utf-8") as f:
    f.write(grupo_a_html)

# ===================================================================
print("[12/16] Gerando: Protótipo HTML Grupo B (IBM HR)...")

grupo_b_html = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Dashboard IBM HR — Turnover em TI</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
:root {
  --brand: #003DA5;
  --accent: #FFA500;
  --bg: #F0F7FF;
  --text: #1A1A1A;
  --light: #FFFFFF;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Segoe UI', Arial, sans-serif; background: linear-gradient(135deg, var(--bg) 0%, #E6F2FF 100%); }
header { background: linear-gradient(135deg, var(--brand) 0%, #1E3A5F 100%); color: white; padding: 25px 30px; }
header h1 { font-size: 1.8rem; margin-bottom: 8px; }
.dash { max-width: 1400px; margin: 20px auto; padding: 0 20px; }
.section-title { font-size: 0.85rem; font-weight: 700; color: var(--brand); text-transform: uppercase; margin: 25px 0 12px; letter-spacing: 0.08em; }
.kpi-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 20px; }
.kpi { background: white; padding: 15px; border-radius: 8px; border-top: 4px solid var(--brand); }
.kpi .val { font-size: 1.8rem; font-weight: 700; color: var(--brand); }
.kpi .lbl { font-size: 0.75rem; color: #888; margin-top: 6px; }
.charts { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 20px; }
.chart-card { background: white; padding: 18px; border-radius: 8px; border: 1px solid #E0E0E0; }
.chart-card h3 { font-size: 0.9rem; font-weight: 700; margin-bottom: 10px; color: var(--brand); }
.insight { background: linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%); border-left: 4px solid var(--accent); padding: 15px; border-radius: 6px; margin: 15px 0; }
.insight .tag { font-size: 0.7rem; font-weight: 700; color: var(--accent); text-transform: uppercase; }
.insight .txt { font-size: 0.85rem; margin-top: 6px; line-height: 1.4; color: var(--text); }
table { width: 100%; border-collapse: collapse; margin: 15px 0; font-size: 0.85rem; }
th { background: var(--brand); color: white; padding: 10px; text-align: left; font-weight: 700; }
td { padding: 8px; border-bottom: 1px solid #eee; }
tr:hover { background: #f5f5f5; }
.cta { background: var(--brand); color: white; padding: 20px; border-radius: 8px; margin: 15px 0; }
.cta h3 { font-size: 1rem; margin-bottom: 10px; }
footer { text-align: center; padding: 20px; font-size: 0.75rem; color: #999; }
</style>
</head>
<body>
<header>
  <h1>👥 IBM HR Analytics — Turnover em Tecnologia</h1>
  <p>Análise de saída de talentos em TI | Custo anual: R$ 450k | Base: 1470 colaboradores</p>
</header>

<div class="dash">
  <p class="section-title">Contexto — Emergência</p>
  <div class="kpi-row">
    <div class="kpi">
      <div class="val" style="color:#DC143C;">28%</div>
      <div class="lbl">Turnover TI<br>(Meta: 15%)</div>
    </div>
    <div class="kpi">
      <div class="val">3x</div>
      <div class="lbl">Risco relativo<br>Júnior sem promoção</div>
    </div>
    <div class="kpi">
      <div class="val" style="color:#FF6B6B;">41</div>
      <div class="lbl">Funcionários<br>em perfil alto risco</div>
    </div>
    <div class="kpi">
      <div class="val" style="color:#FF6B6B;">R$ 270k</div>
      <div class="lbl">Economia potencial<br>com mentoria</div>
    </div>
  </div>

  <p class="section-title">Diagnóstico — Quem Sai?</p>
  <div class="charts">
    <div class="chart-card">
      <h3>Turnover por Departamento</h3>
      <p style="font-size:0.75rem; color:#999; margin-bottom:8px;">Linha vermelha = meta 15%</p>
      <canvas id="chart1" height="200"></canvas>
    </div>
    <div class="chart-card">
      <h3>Perfil de Saída: Anos Empresa vs Promoção</h3>
      <p style="font-size:0.75rem; color:#999; margin-bottom:8px;">Cor = probabilidade de saída</p>
      <canvas id="chart2" height="200"></canvas>
    </div>
  </div>

  <div class="insight">
    <div class="tag">[Insight IA] Acionável — Alto Impacto</div>
    <div class="txt"><strong>Funcionários de TI com menos de 2 anos de empresa e sem promoção nos últimos 3 anos têm 3× mais probabilidade de saída (taxa de 28% vs 9% na base). Esse perfil representa 41 colaboradores. Implantar programa de mentoria acelerada + revisão salarial para esse grupo pode reduzir turnover de 28% para 15% e economizar R$ 270k/ano em custos de reposição.</strong></div>
  </div>

  <div class="cta">
    <h3>🎯 CALL TO ACTION</h3>
    <p><strong>Ativar programa de mentoria + revisão salarial para 41 talentos em risco até 30 dias.</strong><br>
    Responsável: HRBP TI + Diretor de Engenharia | Impacto: turnover TI 28% → 15% em 6 meses</p>
  </div>

  <p class="section-title">Análise Detalhada por Departamento</p>
  <table>
    <thead><tr><th>Depto</th><th>Turnover</th><th>Meta</th><th>Gap</th><th>Ação</th></tr></thead>
    <tbody>
      <tr><td><strong>TI</strong></td><td style="color:#DC143C;"><strong>28%</strong></td><td>15%</td><td>+13pp</td><td>MENTORIA URGENTE</td></tr>
      <tr><td>Vendas</td><td>22%</td><td>20%</td><td>+2pp</td><td>Monitorar</td></tr>
      <tr><td>Operações</td><td>12%</td><td>15%</td><td>-3pp</td><td>OK</td></tr>
      <tr><td>RH</td><td>9%</td><td>15%</td><td>-6pp</td><td>OK</td></tr>
    </tbody>
  </table>

  <footer>Dashboard gerado via Pipeline Multi-Agente | Dados: IBM HR Dataset | Atualização: mai/2026</footer>
</div>

<script>
new Chart(document.getElementById('chart1'), {
  type: 'bar',
  data: {
    labels: ['TI', 'Vendas', 'Operações', 'RH', 'Financeiro'],
    datasets: [{
      label: 'Turnover %',
      data: [28, 22, 12, 9, 16],
      backgroundColor: ['#DC143C', '#FF8C00', '#FFD700', '#90EE90', '#FF8C00']
    },
    {
      label: 'Meta 15%',
      data: [15, 15, 15, 15, 15],
      type: 'line',
      borderColor: '#FF0000',
      borderWidth: 2,
      fill: false,
      pointRadius: 0,
      tension: 0
    }]
  },
  options: {
    plugins: { legend: { display: true } },
    scales: { y: { min: 0, max: 35 } }
  }
});

new Chart(document.getElementById('chart2'), {
  type: 'scatter',
  data: {
    datasets: [{
      label: 'Alto Risco (3x)',
      data: [{x:0.5, y:4}, {x:1.2, y:4.5}, {x:1.8, y:3.8}],
      backgroundColor: '#FF0000',
      pointRadius: 8
    },
    {
      label: 'Médio',
      data: [{x:3.0, y:2.5}, {x:3.5, y:3}, {x:4, y:2}],
      backgroundColor: '#FFA500',
      pointRadius: 6
    },
    {
      label: 'Baixo',
      data: [{x:5.5, y:1}, {x:6, y:1.5}, {x:7, y:0.8}],
      backgroundColor: '#00AA00',
      pointRadius: 6
    }]
  },
  options: {
    plugins: { legend: { display: true } },
    scales: {
      x: { title: { display: true, text: 'Anos na Empresa' }, min: 0, max: 8 },
      y: { title: { display: true, text: 'Anos Sem Promoção' }, min: 0, max: 5 }
    }
  }
});
</script>
</body>
</html>
'''

with open(os.path.join(BASE, "grupo_b.html"), "w", encoding="utf-8") as f:
    f.write(grupo_b_html)

# ===================================================================
print("[13/16] Gerando: Protótipo HTML Grupo C (Superstore)...")

grupo_c_html = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Dashboard Superstore — Margens Negativas</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
:root {
  --brand: #2E7D52;
  --accent: #FF6B35;
  --bg: #F0FFF4;
  --text: #1A1A1A;
  --light: #FFFFFF;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Segoe UI', Arial, sans-serif; background: linear-gradient(135deg, var(--bg) 0%, #E6FFED 100%); }
header { background: linear-gradient(135deg, var(--brand) 0%, #1A4D2E 100%); color: white; padding: 25px 30px; }
header h1 { font-size: 1.8rem; margin-bottom: 8px; }
.dash { max-width: 1400px; margin: 20px auto; padding: 0 20px; }
.section-title { font-size: 0.85rem; font-weight: 700; color: var(--brand); text-transform: uppercase; margin: 25px 0 12px; letter-spacing: 0.08em; }
.kpi-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 20px; }
.kpi { background: white; padding: 15px; border-radius: 8px; border-right: 4px solid var(--brand); }
.kpi .val { font-size: 1.8rem; font-weight: 700; color: var(--brand); }
.kpi .lbl { font-size: 0.75rem; color: #888; margin-top: 6px; }
.charts { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 20px; }
.chart-card { background: white; padding: 18px; border-radius: 8px; border: 1px solid #E8F5E9; }
.chart-card h3 { font-size: 0.9rem; font-weight: 700; margin-bottom: 10px; color: var(--brand); }
.insight { background: linear-gradient(135deg, #FFF3E0 0%, #FFE0B2 100%); border-left: 4px solid var(--accent); padding: 15px; border-radius: 6px; margin: 15px 0; }
.insight .tag { font-size: 0.7rem; font-weight: 700; color: var(--accent); text-transform: uppercase; }
.insight .txt { font-size: 0.85rem; margin-top: 6px; line-height: 1.4; color: var(--text); }
table { width: 100%; border-collapse: collapse; margin: 15px 0; font-size: 0.85rem; }
th { background: var(--brand); color: white; padding: 10px; text-align: left; font-weight: 700; }
td { padding: 8px; border-bottom: 1px solid #eee; }
tr:hover { background: #f9f9f9; }
.cta { background: var(--brand); color: white; padding: 20px; border-radius: 8px; margin: 15px 0; }
.cta h3 { font-size: 1rem; margin-bottom: 10px; }
footer { text-align: center; padding: 20px; font-size: 0.75rem; color: #999; }
</style>
</head>
<body>
<header>
  <h1>📊 Superstore — Controle de Margens por Região</h1>
  <p>Tecnologia/Sul drenam R$ 120k/trimestre | Análise de desconto vs margem | Base: 9995 transações</p>
</header>

<div class="dash">
  <p class="section-title">Contexto — Prejuízo Concentrado</p>
  <div class="kpi-row">
    <div class="kpi">
      <div class="val" style="color:#FF4444;">-4.2%</div>
      <div class="lbl">Margem<br>Tech/Sul</div>
    </div>
    <div class="kpi">
      <div class="val" style="color:#FF4444;">R$ 120k</div>
      <div class="lbl">Prejuízo trimestral<br>esta combinação</div>
    </div>
    <div class="kpi">
      <div class="val">73%</div>
      <div class="lbl">do prejuízo vem de<br>descontos > 20%</div>
    </div>
    <div class="kpi">
      <div class="val" style="color:#2E7D52;">+5.8%</div>
      <div class="lbl">Margem potencial<br>com desconto ≤ 12%</div>
    </div>
  </div>

  <p class="section-title">Diagnóstico — Onde Está o Prejuízo?</p>
  <div class="charts">
    <div class="chart-card">
      <h3>Desconto vs Margem Unitária (Tech/Sul)</h3>
      <p style="font-size:0.75rem; color:#999; margin-bottom:8px;">Linha em 20% = limite de risco; Linha Y=0 = breakeven</p>
      <canvas id="chart1" height="200"></canvas>
    </div>
    <div class="chart-card">
      <h3>Distribuição de Descontos em Tech/Sul</h3>
      <p style="font-size:0.75rem; color:#999; margin-bottom:8px;">Foco: reduzir a fatia vermelha</p>
      <canvas id="chart2" height="200"></canvas>
    </div>
  </div>

  <div class="insight">
    <div class="tag">[Insight IA] Acionável</div>
    <div class="txt"><strong>Descontos acima de 20% em Máquinas e Copiadoras na Região Sul concentram 73% do prejuízo total (R$ 87.6k). Capear o desconto máximo em 12% mantém a competitividade de preço percebida e projeta recuperação de R$ 85k de margem trimestral, transformando -4.2% em +5.8%.</strong></div>
  </div>

  <div class="cta">
    <h3>⚙️ CALL TO ACTION</h3>
    <p><strong>Implementar política de desconto máximo 12% em Tecnologia/Sul até 01/junho.</strong><br>
    Responsável: Gerência Comercial | Impacto: +R$ 85k margem trimestral</p>
  </div>

  <p class="section-title">Top Subcategorias com Prejuízo</p>
  <table>
    <thead><tr><th>Subcategoria</th><th>Região</th><th>Desconto Médio</th><th>Margem %</th><th>Prejuízo Trimestral</th></tr></thead>
    <tbody>
      <tr><td><strong>Máquinas</strong></td><td><strong>Sul</strong></td><td><strong>26%</strong></td><td style="color:#FF4444;"><strong>-6.2%</strong></td><td style="color:#FF4444;"><strong>R$ 45k</strong></td></tr>
      <tr><td><strong>Copiadoras</strong></td><td><strong>Sul</strong></td><td><strong>23%</strong></td><td style="color:#FF4444;"><strong>-2.8%</strong></td><td style="color:#FF4444;"><strong>R$ 32k</strong></td></tr>
      <tr><td>Telefone</td><td>Sul</td><td>18%</td><td>1.5%</td><td>R$ 8k</td></tr>
      <tr><td>Máquinas</td><td>Norte</td><td>14%</td><td>4.2%</td><td>OK</td></tr>
    </tbody>
  </table>

  <footer>Dashboard gerado via Pipeline Multi-Agente | Dados: Superstore Public Dataset | Atualização: mai/2026</footer>
</div>

<script>
new Chart(document.getElementById('chart1'), {
  type: 'scatter',
  data: {
    datasets: [{
      label: 'Transações (Tech/Sul)',
      data: [{x:8, y:2.1}, {x:12, y:1.5}, {x:15, y:0.8}, {x:20, y:-0.5}, {x:23, y:-2.8}, {x:26, y:-6.2}, {x:28, y:-8.1}],
      backgroundColor: function(ctx) { return ctx.raw.x > 20 ? '#FF4444' : '#2E7D52'; },
      pointRadius: 6
    }]
  },
  options: {
    plugins: { legend: { display: false } },
    scales: {
      x: { title: { display: true, text: 'Desconto %' } },
      y: { title: { display: true, text: 'Margem Unitária %' } }
    }
  }
});

new Chart(document.getElementById('chart2'), {
  type: 'doughnut',
  data: {
    labels: ['0-10%', '10-20%', '20-30%', '>30%'],
    datasets: [{
      data: [15, 35, 40, 10],
      backgroundColor: ['#90EE90', '#FFD700', '#FF8C00', '#FF4444']
    }]
  },
  options: {
    plugins: { legend: { position: 'bottom' } }
  }
});
</script>
</body>
</html>
'''

with open(os.path.join(BASE, "grupo_c.html"), "w", encoding="utf-8") as f:
    f.write(grupo_c_html)

# ===================================================================
print("[14/16] Gerando: Protótipo HTML Grupo D (Saúde)...")

grupo_d_html = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Dashboard Saúde — Prevenção Doença Cardíaca</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
:root {
  --brand: #C41E3A;
  --accent: #F0E68C;
  --bg: #FFF5F5;
  --text: #1A1A1A;
  --light: #FFFFFF;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Segoe UI', Arial, sans-serif; background: linear-gradient(135deg, var(--bg) 0%, #FFE4E1 100%); }
header { background: linear-gradient(135deg, var(--brand) 0%, #8B1A1A 100%); color: white; padding: 25px 30px; }
header h1 { font-size: 1.8rem; margin-bottom: 8px; }
.dash { max-width: 1400px; margin: 20px auto; padding: 0 20px; }
.section-title { font-size: 0.85rem; font-weight: 700; color: var(--brand); text-transform: uppercase; margin: 25px 0 12px; letter-spacing: 0.08em; }
.kpi-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 20px; }
.kpi { background: white; padding: 15px; border-radius: 8px; border-bottom: 4px solid var(--brand); }
.kpi .val { font-size: 1.8rem; font-weight: 700; color: var(--brand); }
.kpi .lbl { font-size: 0.75rem; color: #888; margin-top: 6px; }
.charts { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 20px; }
.chart-card { background: white; padding: 18px; border-radius: 8px; border: 1px solid #FFE4E1; }
.chart-card h3 { font-size: 0.9rem; font-weight: 700; margin-bottom: 10px; color: var(--brand); }
.insight { background: linear-gradient(135deg, #FFE4E1 0%, #FFD700 100%); border-left: 4px solid var(--brand); padding: 15px; border-radius: 6px; margin: 15px 0; }
.insight .tag { font-size: 0.7rem; font-weight: 700; color: var(--brand); text-transform: uppercase; }
.insight .txt { font-size: 0.85rem; margin-top: 6px; line-height: 1.4; color: var(--text); }
table { width: 100%; border-collapse: collapse; margin: 15px 0; font-size: 0.85rem; }
th { background: var(--brand); color: white; padding: 10px; text-align: left; font-weight: 700; }
td { padding: 8px; border-bottom: 1px solid #eee; }
tr:hover { background: #fff9f9; }
.cta { background: var(--brand); color: white; padding: 20px; border-radius: 8px; margin: 15px 0; }
.cta h3 { font-size: 1rem; margin-bottom: 10px; }
footer { text-align: center; padding: 20px; font-size: 0.75rem; color: #999; }
</style>
</head>
<body>
<header>
  <h1>❤️ Saúde Pública — Prevenção e Triagem de Risco Cardíaco</h1>
  <p>38% das internações são cardíacas | Custo médio: R$ 12k/internação | Base: 303 pacientes</p>
</header>

<div class="dash">
  <p class="section-title">Contexto — Carga de Doença</p>
  <div class="kpi-row">
    <div class="kpi">
      <div class="val" style="color:#C41E3A;">38%</div>
      <div class="lbl">Internações por<br>doença cardíaca</div>
    </div>
    <div class="kpi">
      <div class="val">73%</div>
      <div class="lbl">Casos de alto risco<br>com 3 sinais</div>
    </div>
    <div class="kpi">
      <div class="val" style="color:#C41E3A;">25%</div>
      <div class="lbl">Redução possível<br>internações</div>
    </div>
    <div class="kpi">
      <div class="val" style="color:#C41E3A;">R$ 2.1M</div>
      <div class="lbl">Economia anual<br>se evitar 25%</div>
    </div>
  </div>

  <p class="section-title">Diagnóstico — Quem Está em Risco?</p>
  <div class="charts">
    <div class="chart-card">
      <h3>Fatores de Risco — Correlação com Diagnóstico</h3>
      <p style="font-size:0.75rem; color:#999; margin-bottom:8px;">Quanto mais alto, maior o risco</p>
      <canvas id="chart1" height="200"></canvas>
    </div>
    <div class="chart-card">
      <h3>Colesterol vs Pressão (Cores = Diagnóstico)</h3>
      <p style="font-size:0.75rem; color:#999; margin-bottom:8px;">Zona crítica: >240 e >140 (canto superior)</p>
      <canvas id="chart2" height="200"></canvas>
    </div>
  </div>

  <div class="insight">
    <div class="tag">[Insight IA] Acionável — Prevenção</div>
    <div class="txt"><strong>Colesterol > 240 + pressão arterial > 140 + idade > 55 anos identificam 73% dos casos de alto risco com apenas 3 variáveis simples. Triagem preventiva focada nesse perfil (42 pacientes atualmente não monitorados) pode reduzir internações cardíacas em 25% e gerar R$ 2,1M de economia anual.</strong></div>
  </div>

  <div class="cta">
    <h3>🏥 CALL TO ACTION</h3>
    <p><strong>Implantar protocolo de triagem obrigatória e monitoramento mensal para 42 pacientes em perfil alto risco até 30/junho.</strong><br>
    Responsável: Gerência de Assistência | Impacto: -25% internações cardíacas em 12 meses</p>
  </div>

  <p class="section-title">Perfis de Risco por Faixa Etária</p>
  <table>
    <thead><tr><th>Faixa Etária</th><th>Taxa Doença</th><th>Colesterol Médio</th><th>Pressão Média</th><th>Ação</th></tr></thead>
    <tbody>
      <tr><td><strong>>55 anos</strong></td><td style="color:#C41E3A;"><strong>68%</strong></td><td><strong>258</strong></td><td><strong>152</strong></td><td><strong>TRIAGEM URGENTE</strong></td></tr>
      <tr><td>45-54 anos</td><td>45%</td><td>235</td><td>138</td><td>Monitorar</td></tr>
      <tr><td>35-44 anos</td><td>28%</td><td>210</td><td>125</td><td>Check-up anual</td></tr>
      <tr><td><55 anos</td><td>8%</td><td>185</td><td>115</td><td>OK</td></tr>
    </tbody>
  </table>

  <footer>Dashboard gerado via Pipeline Multi-Agente | Dados: Heart Disease UCI Dataset | Atualização: mai/2026</footer>
</div>

<script>
new Chart(document.getElementById('chart1'), {
  type: 'bar',
  data: {
    labels: ['Pressão Arterial', 'Colesterol', 'Idade', 'Frequência Cardíaca', 'Açúcar'],
    datasets: [{
      label: 'Correlação com Diagnóstico',
      data: [0.44, 0.42, 0.38, 0.32, 0.28],
      backgroundColor: ['#C41E3A', '#FF6B6B', '#FFA07A', '#FFB6C1', '#DDA0DD']
    }]
  },
  options: {
    indexAxis: 'y',
    plugins: { legend: { display: false } },
    scales: { x: { min: 0, max: 0.5 } }
  }
});

new Chart(document.getElementById('chart2'), {
  type: 'scatter',
  data: {
    datasets: [{
      label: 'Com Doença',
      data: [{x:245, y:145}, {x:260, y:155}, {x:248, y:150}, {x:270, y:160}],
      backgroundColor: '#C41E3A',
      pointRadius: 7
    },
    {
      label: 'Sem Doença',
      data: [{x:210, y:125}, {x:220, y:130}, {x:200, y:120}, {x:215, y:128}],
      backgroundColor: '#90EE90',
      pointRadius: 7
    }]
  },
  options: {
    plugins: { legend: { display: true } },
    scales: {
      x: { title: { display: true, text: 'Colesterol' }, min: 180, max: 280 },
      y: { title: { display: true, text: 'Pressão Sistólica' }, min: 110, max: 170 }
    }
  }
});
</script>
</body>
</html>
'''

with open(os.path.join(BASE, "grupo_d.html"), "w", encoding="utf-8") as f:
    f.write(grupo_d_html)

# ===================================================================
print("[15/16] Gerando: Protótipo HTML Grupo E (FinTech)...")

grupo_e_html = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Dashboard FinTech — Churn Cartão Premium</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
:root {
  --brand: #6F42C1;
  --accent: #FFC107;
  --bg: #F8F7FF;
  --text: #1A1A1A;
  --light: #FFFFFF;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Segoe UI', Arial, sans-serif; background: linear-gradient(135deg, var(--bg) 0%, #E9ECEF 100%); }
header { background: linear-gradient(135deg, var(--brand) 0%, #4B2E83 100%); color: white; padding: 25px 30px; }
header h1 { font-size: 1.8rem; margin-bottom: 8px; }
.dash { max-width: 1400px; margin: 20px auto; padding: 0 20px; }
.section-title { font-size: 0.85rem; font-weight: 700; color: var(--brand); text-transform: uppercase; margin: 25px 0 12px; letter-spacing: 0.08em; }
.kpi-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 20px; }
.kpi { background: white; padding: 15px; border-radius: 8px; border: 2px solid var(--brand); }
.kpi .val { font-size: 1.8rem; font-weight: 700; color: var(--brand); }
.kpi .lbl { font-size: 0.75rem; color: #888; margin-top: 6px; }
.charts { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 20px; }
.chart-card { background: white; padding: 18px; border-radius: 8px; border: 1px solid #E9ECEF; }
.chart-card h3 { font-size: 0.9rem; font-weight: 700; margin-bottom: 10px; color: var(--brand); }
.insight { background: linear-gradient(135deg, #FFC107 0%, #FFD54F 100%); border-left: 4px solid var(--brand); padding: 15px; border-radius: 6px; margin: 15px 0; }
.insight .tag { font-size: 0.7rem; font-weight: 700; color: var(--brand); text-transform: uppercase; }
.insight .txt { font-size: 0.85rem; margin-top: 6px; line-height: 1.4; color: var(--text); }
table { width: 100%; border-collapse: collapse; margin: 15px 0; font-size: 0.85rem; }
th { background: var(--brand); color: white; padding: 10px; text-align: left; font-weight: 700; }
td { padding: 8px; border-bottom: 1px solid #eee; }
tr:hover { background: #f9f9f9; }
.cta { background: var(--brand); color: white; padding: 20px; border-radius: 8px; margin: 15px 0; }
.cta h3 { font-size: 1rem; margin-bottom: 10px; }
footer { text-align: center; padding: 20px; font-size: 0.75rem; color: #999; }
</style>
</head>
<body>
<header>
  <h1>💳 FinTech — Churn de Cartão Premium</h1>
  <p>Receita de clientes Premium em risco: R$ 2,1M/ano | Segmentação por uso e limite | Base: 10.127 clientes</p>
</header>

<div class="dash">
  <p class="section-title">Contexto — Emergência Financeira</p>
  <div class="kpi-row">
    <div class="kpi">
      <div class="val" style="color:#6F42C1;">18%</div>
      <div class="lbl">Churn Premium<br>(benchmark: 8%)</div>
    </div>
    <div class="kpi">
      <div class="val">4x</div>
      <div class="lbl">Risco relativo<br>limite <R$10k</div>
    </div>
    <div class="kpi">
      <div class="val" style="color:#6F42C1;">285</div>
      <div class="lbl">Clientes em perfil<br>alto risco</div>
    </div>
    <div class="kpi">
      <div class="val" style="color:#6F42C1;">R$ 1.2M</div>
      <div class="lbl">Receita preservável<br>engajamento proativo</div>
    </div>
  </div>

  <p class="section-title">Diagnóstico — Quem Está Saindo?</p>
  <div class="charts">
    <div class="chart-card">
      <h3>Churn por Faixa de Limite de Crédito</h3>
      <p style="font-size:0.75rem; color:#999; margin-bottom:8px;">Limite baixo = maior risco | Linha em 8% = benchmark</p>
      <canvas id="chart1" height="200"></canvas>
    </div>
    <div class="chart-card">
      <h3>Frequência de Uso vs Ticket Médio (Cores = Churn)</h3>
      <p style="font-size:0.75rem; color:#999; margin-bottom:8px;">Zona vermelha: <20 transações + <R$5k limite</p>
      <canvas id="chart2" height="200"></canvas>
    </div>
  </div>

  <div class="insight">
    <div class="tag">[Insight IA] Acionável — Retenção</div>
    <div class="txt"><strong>Clientes Premium com limite < R$ 10k e menos de 20 transações/ano têm 4× mais chance de cancelamento (taxa 32% vs 8% na base) — equivalente a R$ 420k em receita anual em risco. Engajamento proativo focado nesse perfil (285 clientes) com cashback + limite temporário pode reduzir churn em 50%, preservando R$ 1,2M em receita anual.</strong></div>
  </div>

  <div class="cta">
    <h3>📱 CALL TO ACTION</h3>
    <p><strong>Lançar campanha de reengajamento via app para 285 clientes em risco até 15/junho.</strong><br>
    Responsável: Gerência de CRM | Impacto: reduzir churn Premium de 18% para 9% em 6 meses</p>
  </div>

  <p class="section-title">Matriz de Risco — Limite vs Frequência</p>
  <table>
    <thead><tr><th>Faixa de Limite</th><th>Frequência/Ano</th><th>Churn %</th><th>Clientes</th><th>Receita em Risco</th></tr></thead>
    <tbody>
      <tr><td><strong><R$10k</strong></td><td><strong><20 trans</strong></td><td style="color:#6F42C1;"><strong>32%</strong></td><td style="color:#6F42C1;"><strong>285</strong></td><td style="color:#6F42C1;"><strong>R$ 420k</strong></td></tr>
      <tr><td>R$10-30k</td><td>20-50 trans</td><td>14%</td><td>450</td><td>R$ 180k</td></tr>
      <tr><td>>R$30k</td><td>>50 trans</td><td>6%</td><td>320</td><td>R$ 48k</td></tr>
      <tr><td>Inativo</td><td>0 trans</td><td>72%</td><td>95</td><td>R$ 230k</td></tr>
    </tbody>
  </table>

  <footer>Dashboard gerado via Pipeline Multi-Agente | Dados: Credit Card Customers Dataset | Atualização: mai/2026</footer>
</div>

<script>
new Chart(document.getElementById('chart1'), {
  type: 'bar',
  data: {
    labels: ['<R$5k', 'R$5-10k', 'R$10-30k', '>R$30k'],
    datasets: [{
      label: 'Churn %',
      data: [28, 32, 14, 6],
      backgroundColor: ['#FF4444', '#FF6B6B', '#FFD700', '#90EE90']
    },
    {
      label: 'Benchmark 8%',
      data: [8, 8, 8, 8],
      type: 'line',
      borderColor: '#000000',
      borderWidth: 2,
      fill: false,
      pointRadius: 0
    }]
  },
  options: {
    plugins: { legend: { display: true } },
    scales: { y: { min: 0, max: 40 } }
  }
});

new Chart(document.getElementById('chart2'), {
  type: 'scatter',
  data: {
    datasets: [{
      label: 'Alto Churn (>20%)',
      data: [{x:8, y:2500}, {x:12, y:3000}, {x:15, y:2800}],
      backgroundColor: '#FF4444',
      pointRadius: 8
    },
    {
      label: 'Médio (8-20%)',
      data: [{x:35, y:5000}, {x:42, y:5500}, {x:30, y:4800}],
      backgroundColor: '#FFC107',
      pointRadius: 8
    },
    {
      label: 'Baixo (<8%)',
      data: [{x:65, y:8000}, {x:78, y:9000}, {x:72, y:8500}],
      backgroundColor: '#90EE90',
      pointRadius: 8
    }]
  },
  options: {
    plugins: { legend: { display: true } },
    scales: {
      x: { title: { display: true, text: 'Transações/Ano' }, min: 0, max: 90 },
      y: { title: { display: true, text: 'Ticket Médio (R$)' }, min: 2000, max: 10000 }
    }
  }
});
</script>
</body>
</html>
'''

with open(os.path.join(BASE, "grupo_e.html"), "w", encoding="utf-8") as f:
    f.write(grupo_e_html)

print("\n✓ [15/16] TODOS OS 5 PROTÓTIPOS HTML CRIADOS!\n")

# ===================================================================
# GERAR PDFs (usando wkhtmltopdf ou similar via command line)
# ===================================================================

print("[16/16] Gerando: PDFs para cada grupo...")

# Tentar usar wkhtmltopdf se disponível, senão usar conversão simples via command line
html_files = [
    ("grupo_a.html", "grupo_a.pdf", "E-commerce Olist"),
    ("grupo_b.html", "grupo_b.pdf", "IBM HR Analytics"),
    ("grupo_c.html", "grupo_c.pdf", "Superstore Varejo"),
    ("grupo_d.html", "grupo_d.pdf", "Saúde Pública"),
    ("grupo_e.html", "grupo_e.pdf", "FinTech Premium"),
]

for html_name, pdf_name, desc in html_files:
    html_path = os.path.join(BASE, html_name)
    pdf_path = os.path.join(BASE, pdf_name)
    
    # Tenta usar wkhtmltopdf
    try:
        import subprocess
        subprocess.run(["wkhtmltopdf", html_path, pdf_path], check=True, capture_output=True)
        print(f"  ✓ {pdf_name} (via wkhtmltopdf)")
    except:
        # Se wkhtmltopdf não existir, tenta usar libreoffice ou cria um aviso
        try:
            subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", html_path, "--outdir", BASE], 
                          check=True, capture_output=True)
            print(f"  ✓ {pdf_name} (via LibreOffice)")
        except:
            # Fallback: criar um placeholder com nota
            with open(pdf_path, "w") as f:
                f.write(f"[NOTA] PDF para {desc}\nPara gerar o PDF:\n" +
                       f"1. Abrir {html_name} no navegador\n" +
                       f"2. Pressionar Ctrl+P\n" +
                       f"3. Salvar como PDF\n")
            print(f"  ⚠ {pdf_name} (criado placeholder — use Print to PDF no navegador)")

print("\n" + "="*70)
print("✅ GERAÇÃO COMPLETA!")
print("="*70)
print(f"\nArquivos criados em: {BASE}/\n")
print("IMAGENS (Cap 2):")
for f in sorted([x for x in os.listdir(OUT) if x.startswith("cap2_")]):
    print(f"  ✓ {f}")

print("\nPROTÓTIPOS HTML (Grupos):")
for html_name, pdf_name, desc in html_files:
    print(f"  ✓ {html_name} ({desc})")
    print(f"    → {pdf_name}")

print("\n[PRÓXIMO PASSO] Editar semana_especial.tex para:")
print("  1. Incluir as imagens cap2_*.png em cada seção do Cap 2")
print("  2. Expandir o conteúdo teórico do Cap 2 (pseudocódigo, exemplos)")
print("  3. Substituir os protótipos HTML dos grupos pelos novos (grupo_a.html, etc)")
print("\n")
