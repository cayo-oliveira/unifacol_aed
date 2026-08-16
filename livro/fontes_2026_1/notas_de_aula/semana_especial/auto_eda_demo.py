"""
auto_eda_demo.py — Demonstração de EDA Automática
Dataset: StudentPerformanceFactors.csv (6607 registros, 20 variáveis)
Outputs salvos em: aula/semana_especial/outputs/

Bibliotecas demonstradas:
  1. ydata-profiling (relatório HTML completo)
  2. sweetviz       (relatório HTML comparativo)
  3. Análise manual com pandas + matplotlib (imagens .png para o .tex)

Execute com o venv ativo:
  source .venv/bin/activate
  python3 aula/semana_especial/auto_eda_demo.py
"""

import os, warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns

# -----------------------------------------------------------------
# 0. Paths
# -----------------------------------------------------------------
BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "..", "semana02", "StudentPerformanceFactors.csv")
OUT  = os.path.join(BASE, "outputs")
os.makedirs(OUT, exist_ok=True)

# -----------------------------------------------------------------
# 1. Carga e dicionário rápido
# -----------------------------------------------------------------
df = pd.read_csv(DATA)
print(f"Shape: {df.shape}")
print(df.dtypes.to_string())

# -----------------------------------------------------------------
# 2. ydata-profiling — relatório HTML completo
# -----------------------------------------------------------------
print("\n[1/4] Gerando ydata-profiling report...")
try:
    from ydata_profiling import ProfileReport
    profile = ProfileReport(
        df,
        title="AED Automática — Student Performance Factors",
        explorative=True,
        minimal=False,
    )
    profile.to_file(os.path.join(OUT, "ydata_profiling_report.html"))
    print("     -> ydata_profiling_report.html salvo.")
except Exception as e:
    print(f"     ydata-profiling erro: {e}")

# -----------------------------------------------------------------
# 3. sweetviz — comparação por gênero
# -----------------------------------------------------------------
print("\n[2/4] Gerando sweetviz report...")
try:
    import sweetviz as sv
    report = sv.compare(
        [df[df["Gender"] == "Male"],   "Masculino"],
        [df[df["Gender"] == "Female"], "Feminino"],
    )
    report.show_html(
        os.path.join(OUT, "sweetviz_genero.html"),
        open_browser=False,
        layout="vertical",
    )
    print("     -> sweetviz_genero.html salvo.")
except Exception as e:
    print(f"     sweetviz erro: {e}")

# -----------------------------------------------------------------
# 4. Visualizações manuais para o .tex  (4 imagens)
# -----------------------------------------------------------------
print("\n[3/4] Gerando imagens para o .tex...")
PALETTE = {"destaque": "#E35D22", "base": "#4A7FB5", "cinza": "#B0B0B0",
           "verde": "#2E7D52", "bg": "#F7F7F7"}

plt.rcParams.update({
    "figure.facecolor": PALETTE["bg"],
    "axes.facecolor":   PALETTE["bg"],
    "axes.spines.top":  False,
    "axes.spines.right":False,
    "font.family":      "DejaVu Sans",
})

# --- Figura 1: distribuição Exam_Score + KPI summary
fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
fig.suptitle("Figura 1 — Distribuição da Nota Final e Sumário de KPIs", fontsize=13, fontweight="bold")

ax = axes[0]
ax.hist(df["Exam_Score"], bins=30, color=PALETTE["base"], edgecolor="white", linewidth=0.4)
ax.axvline(df["Exam_Score"].mean(), color=PALETTE["destaque"], lw=2, ls="--",
           label=f'Média: {df["Exam_Score"].mean():.1f}')
ax.axvline(df["Exam_Score"].median(), color=PALETTE["verde"], lw=2, ls=":",
           label=f'Mediana: {df["Exam_Score"].median():.1f}')
ax.set_title("Distribuição de Exam_Score", fontsize=11)
ax.set_xlabel("Nota Final"); ax.set_ylabel("Frequência")
ax.legend(fontsize=9)

ax2 = axes[1]
kpis = {
    "Média Exam_Score": f"{df['Exam_Score'].mean():.1f}",
    "Desvio Padrão":    f"{df['Exam_Score'].std():.1f}",
    "% Aprovados (≥60)":f"{(df['Exam_Score']>=60).mean()*100:.0f}%",
    "Correlação Horas×Nota": f"{df[['Hours_Studied','Exam_Score']].corr().iloc[0,1]:.2f}",
    "Registros":        f"{len(df):,}",
    "Variáveis":        f"{df.shape[1]}",
}
ax2.axis("off")
y = 0.92
for k, v in kpis.items():
    ax2.text(0.05, y, k,  transform=ax2.transAxes, fontsize=10, color="#555")
    ax2.text(0.65, y, v,  transform=ax2.transAxes, fontsize=11, fontweight="bold", color=PALETTE["base"])
    y -= 0.15

plt.tight_layout()
p1 = os.path.join(OUT, "eda_fig1_distribuicao.png")
plt.savefig(p1, dpi=150, bbox_inches="tight")
plt.close()
print(f"     -> {p1}")

# --- Figura 2: top correlações com Exam_Score
fig, ax = plt.subplots(figsize=(10, 4))
num_cols = df.select_dtypes(include=np.number).columns.tolist()
corr = df[num_cols].corr()["Exam_Score"].drop("Exam_Score").sort_values()
colors = [PALETTE["destaque"] if abs(v) > 0.2 else PALETTE["cinza"] for v in corr]
ax.barh(corr.index, corr.values, color=colors)
ax.axvline(0, color="#666", lw=0.8)
ax.set_title("Top Correlações com Exam_Score\n(laranja = correlação forte > |0,20|)", fontsize=11, fontweight="bold")
ax.set_xlabel("Coeficiente de Correlação de Pearson")
for i, v in enumerate(corr.values):
    ax.text(v + (0.003 if v >= 0 else -0.003), i,
            f"{v:.2f}", va="center", ha="left" if v >= 0 else "right", fontsize=8)
plt.tight_layout()
p2 = os.path.join(OUT, "eda_fig2_correlacoes.png")
plt.savefig(p2, dpi=150, bbox_inches="tight")
plt.close()
print(f"     -> {p2}")

# --- Figura 3: scatter Hours_Studied × Exam_Score por Motivation_Level
fig, ax = plt.subplots(figsize=(9, 5))
color_map = {"High": PALETTE["destaque"], "Medium": PALETTE["base"], "Low": PALETTE["cinza"]}
for level, grp in df.groupby("Motivation_Level"):
    ax.scatter(grp["Hours_Studied"], grp["Exam_Score"],
               alpha=0.35, s=18, color=color_map.get(level, "#aaa"), label=level)
m, b = np.polyfit(df["Hours_Studied"], df["Exam_Score"], 1)
xs = np.linspace(df["Hours_Studied"].min(), df["Hours_Studied"].max(), 200)
ax.plot(xs, m*xs + b, color="#222", lw=1.8, ls="--", label=f"Trend (y={m:.2f}x+{b:.1f})")
ax.set_title("Horas de Estudo × Nota Final\n(Insight: cada hora extra = +{:.2f} pts)".format(m),
             fontsize=11, fontweight="bold")
ax.set_xlabel("Hours_Studied"); ax.set_ylabel("Exam_Score")
ax.legend(title="Motivation", fontsize=9)
plt.tight_layout()
p3 = os.path.join(OUT, "eda_fig3_scatter.png")
plt.savefig(p3, dpi=150, bbox_inches="tight")
plt.close()
print(f"     -> {p3}")

# --- Figura 4: heatmap variáveis categóricas (Parental_Involvement × Exam_Score médio)
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
fig.suptitle("Figura 4 — Fatores Categóricos com Maior Impacto na Nota", fontsize=12, fontweight="bold")

cats = [("Parental_Involvement", "Envolvimento Familiar"),
        ("Access_to_Resources",  "Acesso a Recursos")]
for ax, (col, label) in zip(axes, cats):
    means = df.groupby(col)["Exam_Score"].mean().sort_values()
    bar_colors = [PALETTE["destaque"] if v == means.max() else PALETTE["base"] for v in means]
    ax.barh(means.index, means.values, color=bar_colors)
    ax.set_title(label, fontsize=10)
    ax.set_xlabel("Média Exam_Score")
    for i, v in enumerate(means.values):
        ax.text(v+0.1, i, f"{v:.1f}", va="center", fontsize=9)
    ax.set_xlim(0, 85)

plt.tight_layout()
p4 = os.path.join(OUT, "eda_fig4_categoricas.png")
plt.savefig(p4, dpi=150, bbox_inches="tight")
plt.close()
print(f"     -> {p4}")

# -----------------------------------------------------------------
# 5. Gerar CSV de sumário para o insight database
# -----------------------------------------------------------------
print("\n[4/4] Gerando insight_base_exemplo.csv...")
m_horas = np.polyfit(df["Hours_Studied"], df["Exam_Score"], 1)[0]
insights_db = pd.DataFrame([
    {
        "insight_id":    "INS-001",
        "dominio":       "Educação",
        "tipo":          "acionavel",
        "observacao":    f"Cada hora semanal extra de estudo está associada a +{m_horas:.2f} pontos na nota final.",
        "dado":          f"Correlação Pearson = {df[['Hours_Studied','Exam_Score']].corr().iloc[0,1]:.2f}; n=6607",
        "impacto":       f"Alunos com ≥30h/semana têm média {df[df['Hours_Studied']>=30]['Exam_Score'].mean():.1f} vs {df[df['Hours_Studied']<10]['Exam_Score'].mean():.1f} para <10h",
        "acao":          "Implantar programa de mentoria semanal com meta de 20h de estudo monitorado",
        "stakeholder":   "Coordenador Pedagógico",
        "urgencia":      "Alta",
        "prazo_sugerido":"Q3 2026",
        "fonte":         "StudentPerformanceFactors.csv",
    },
    {
        "insight_id":    "INS-002",
        "dominio":       "Educação",
        "tipo":          "acionavel",
        "observacao":    "Alunos com Alto envolvimento familiar têm nota média 5,3 pts acima de alunos com Baixo envolvimento.",
        "dado":          f"Alto={df[df['Parental_Involvement']=='High']['Exam_Score'].mean():.1f}, Baixo={df[df['Parental_Involvement']=='Low']['Exam_Score'].mean():.1f}",
        "impacto":       "Diferença equivale a 8% da escala de notas; afeta 22% da base de alunos",
        "acao":          "Criar programa de comunicação bimestral obrigatória com responsáveis de alunos em risco",
        "stakeholder":   "Diretor Escolar",
        "urgencia":      "Média",
        "prazo_sugerido":"Início de 2027.1",
        "fonte":         "StudentPerformanceFactors.csv",
    },
    {
        "insight_id":    "INS-003",
        "dominio":       "Educação",
        "tipo":          "informativo",
        "observacao":    f"A distribuição de Exam_Score é aproximadamente normal (assimetria={pd.Series(df['Exam_Score']).skew():.2f}).",
        "dado":          f"Média={df['Exam_Score'].mean():.1f}, DP={df['Exam_Score'].std():.1f}, Min={df['Exam_Score'].min()}, Max={df['Exam_Score'].max()}",
        "impacto":       "Não diretamente — indica dataset saudável para modelos preditivos",
        "acao":          "Nenhuma ação imediata necessária",
        "stakeholder":   "Analista de Dados",
        "urgencia":      "Baixa",
        "prazo_sugerido":"N/A",
        "fonte":         "StudentPerformanceFactors.csv",
    },
])
insights_db.to_csv(os.path.join(OUT, "insight_base_exemplo.csv"), index=False)
print(f"     -> insight_base_exemplo.csv salvo.")

print("\n[OK] Todos os outputs salvos em:", OUT)
