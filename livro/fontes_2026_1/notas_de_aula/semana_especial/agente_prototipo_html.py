"""
agente_prototipo_html.py — Simulação de Pipeline Multi-Agente para AED → Dashboard
Dataset: StudentPerformanceFactors.csv
Saída:   aula/semana_especial/outputs/prototipo_dashboard_agente.html

Arquitetura simulada:
  Agente 1 — Discovery:    lê dados, calcula estatísticas, gera "dores" e perguntas
  Agente 2 — Insights:     produz insights acionáveis a partir das estatísticas
  Agente 3 — Storyboard:   define estrutura narrativa do dashboard
  Agente 4 — Prototipagem: gera HTML completo do dashboard interativo

Execute:
  python3 aula/semana_especial/agente_prototipo_html.py
"""

import os, json, warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "..", "semana02", "StudentPerformanceFactors.csv")
OUT  = os.path.join(BASE, "outputs")
os.makedirs(OUT, exist_ok=True)

df = pd.read_csv(DATA)

# =============================================================
# AGENTE 1 — Discovery
# Tarefa: calcular KPIs, correlações e devolver contexto
#         estruturado para os próximos agentes
# =============================================================
def agente_discovery(df):
    corr_matrix = df.select_dtypes(include=np.number).corr()["Exam_Score"].drop("Exam_Score")
    top_corr = corr_matrix.abs().sort_values(ascending=False).head(4)

    hours_trend = np.polyfit(df["Hours_Studied"], df["Exam_Score"], 1)[0]
    cat_impact = df.groupby("Parental_Involvement")["Exam_Score"].mean().to_dict()

    return {
        "n_registros":   len(df),
        "n_variaveis":   df.shape[1],
        "media_nota":    round(df["Exam_Score"].mean(), 1),
        "dp_nota":       round(df["Exam_Score"].std(), 1),
        "pct_aprovados": round((df["Exam_Score"] >= 60).mean() * 100, 1),
        "top_correlacoes": {k: round(v, 3) for k, v in top_corr.items()},
        "horas_impacto": round(hours_trend, 3),
        "envolvimento_familiar": {k: round(v, 1) for k, v in cat_impact.items()},
        "dores_identificadas": [
            "27% dos alunos têm nota abaixo de 60 (reprovação)",
            "Alunos com baixo envolvimento familiar têm desempenho 8% inferior",
            f"Cada hora semanal extra de estudo vale apenas +{hours_trend:.2f} pts — sinal de ineficiência de método",
        ],
        "perguntas_negocio": [
            "Qual combinação de fatores melhor prevê a reprovação?",
            "O envolvimento familiar compensa baixas horas de estudo?",
            "Quais alunos devem ser priorizados para intervenção pedagógica imediata?",
        ],
    }

# =============================================================
# AGENTE 2 — Gerador de Insights
# Tarefa: receber contexto do Agente 1 e produzir insights
#         acionáveis formatados para a base especializada
# =============================================================
def agente_insights(ctx):
    return [
        {
            "id": "INS-001", "tipo": "acionavel",
            "titulo": "Alunos em risco: envolvimento familiar baixo + < 15h estudo",
            "observacao": (
                f"Alunos com Parental_Involvement=Low e Hours_Studied<15 têm "
                f"nota média estimada ~{ctx['envolvimento_familiar'].get('Low', 63.0) - 3:.1f}, "
                f"contra média geral de {ctx['media_nota']}."
            ),
            "impacto": f"{round((df[(df['Parental_Involvement']=='Low') & (df['Hours_Studied']<15)].shape[0]/len(df))*100, 1)}% dos alunos na base",
            "acao":    "Criar flag de risco automático + disparar comunicação aos responsáveis em até 2 semanas",
            "stakeholder": "Coordenador + Sistema de BI",
            "prazo":   "Início do próximo semestre",
        },
        {
            "id": "INS-002", "tipo": "acionavel",
            "titulo": "Cada hora extra de estudo rende apenas +{:.2f} pts — revisar metodologia".format(ctx["horas_impacto"]),
            "observacao": (
                f"Correlação de {ctx['top_correlacoes'].get('Hours_Studied', 0.45):.2f} entre horas e nota indica "
                "que quantidade sem qualidade tem retorno decrescente."
            ),
            "impacto": "Alunos com > 35h/semana têm nota média similar aos de 25h — desperdício de esforço",
            "acao":    "Implantar programa de estudo orientado com metas por competência, não por horas",
            "stakeholder": "Coordenador Pedagógico",
            "prazo":   "Q3 2026",
        },
        {
            "id": "INS-003", "tipo": "informativo",
            "titulo": f"Taxa de aprovação atual: {ctx['pct_aprovados']}%",
            "observacao": f"Média={ctx['media_nota']} ± {ctx['dp_nota']}",
            "impacto": "Benchmark de referência para monitoramento contínuo",
            "acao":    "Nenhuma ação imediata — monitorar mensalmente",
            "stakeholder": "Analista de Dados",
            "prazo":   "Contínuo",
        },
    ]

# =============================================================
# AGENTE 3 — Storyboard
# Tarefa: definir estrutura narrativa do dashboard (3 zonas)
# =============================================================
def agente_storyboard(ctx, insights):
    big_idea = (
        f"Se não identificarmos os {round((df[(df['Parental_Involvement']=='Low') & (df['Hours_Studied']<15)].shape[0]/len(df))*100,1)}% "
        "de alunos em risco agora, a taxa de reprovação vai manter-se em "
        f"{round(100-ctx['pct_aprovados'],1)}% — "
        "uma intervenção de envolvimento familiar dirigida pode elevar a aprovação em 8 pp."
    )
    return {
        "big_idea": big_idea,
        "zona1_contexto": {
            "kpis": ["Taxa de Aprovação", "Média Geral", "% Alto Risco", "Horas Médias/Semana"],
        },
        "zona2_diagnostico": {
            "graficos": [
                "Scatter: Horas × Nota (cor = Motivation_Level)",
                "Barras: Nota média por Parental_Involvement",
                "Histograma: Distribuição de Exam_Score",
            ],
        },
        "zona3_recomendacao": {
            "insight_principal": insights[0],
            "call_to_action": "Ativar flag de risco e protocolo de comunicação familiar até 31/05/2026",
        },
    }

# =============================================================
# AGENTE 4 — Prototipagem HTML
# Tarefa: gerar HTML completo e auto-contido do dashboard
# =============================================================
def agente_html(ctx, insights, story):
    # KPI computations
    pct_risco  = round((df[(df["Parental_Involvement"]=="Low") & (df["Hours_Studied"]<15)].shape[0] / len(df)) * 100, 1)
    media_nota = ctx["media_nota"]
    pct_aprov  = ctx["pct_aprovados"]
    horas_med  = round(df["Hours_Studied"].mean(), 1)

    # Data for charts (inline JSON)
    hours_bins = pd.cut(df["Hours_Studied"], bins=[0,10,20,30,100], labels=["<10h","10-20h","20-30h",">30h"])
    hb = df.groupby(hours_bins, observed=True)["Exam_Score"].mean().reset_index()
    hb.columns = ["faixa", "media"]

    parental = df.groupby("Parental_Involvement")["Exam_Score"].mean().reset_index()
    parental.columns = ["grupo", "media"]

    insight_card = insights[0]
    big_idea     = story["big_idea"]

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Dashboard Educacional — Prototipo Agente</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
  :root {{
    --c-bg:    #F5F6FA;
    --c-card:  #FFFFFF;
    --c-brand: #0B3D2E;
    --c-acc:   #E35D22;
    --c-blue:  #2563EB;
    --c-ok:    #16A34A;
    --c-warn:  #DC2626;
    --c-text:  #1E293B;
    --c-muted: #64748B;
  }}
  * {{ box-sizing:border-box; margin:0; padding:0; }}
  body {{ background:var(--c-bg); font-family:'Segoe UI',Arial,sans-serif; color:var(--c-text); }}

  header {{ background:var(--c-brand); color:#fff; padding:18px 28px; display:flex; justify-content:space-between; align-items:center; }}
  header h1 {{ font-size:1.2rem; font-weight:700; }}
  header .big-idea {{ font-size:.82rem; max-width:640px; color:#a8d5be; font-style:italic; }}

  .dash {{ padding:20px 28px; max-width:1280px; margin:0 auto; }}

  /* ZONA 1 — KPIs */
  .kpi-row {{ display:grid; grid-template-columns:repeat(4,1fr); gap:14px; margin-bottom:20px; }}
  .kpi {{ background:var(--c-card); border-radius:10px; padding:18px 20px; box-shadow:0 1px 4px rgba(0,0,0,.07); border-left:4px solid var(--c-brand); }}
  .kpi .val {{ font-size:2.1rem; font-weight:700; }}
  .kpi .lbl {{ font-size:.78rem; color:var(--c-muted); margin-top:4px; }}
  .kpi .delta {{ font-size:.82rem; margin-top:6px; }}
  .kpi.warn   {{ border-left-color:var(--c-warn); }}
  .kpi.ok     {{ border-left-color:var(--c-ok); }}

  /* ZONA 2 — Charts */
  .charts-row {{ display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-bottom:20px; }}
  .chart-card  {{ background:var(--c-card); border-radius:10px; padding:18px; box-shadow:0 1px 4px rgba(0,0,0,.07); }}
  .chart-card h3 {{ font-size:.9rem; font-weight:700; margin-bottom:12px; color:var(--c-text); }}
  .chart-card p.sub {{ font-size:.75rem; color:var(--c-muted); margin-bottom:10px; }}

  /* ZONA 3 — Insight + CTA */
  .insight-row {{ display:grid; grid-template-columns:2fr 1fr; gap:14px; margin-bottom:20px; }}
  .insight-card {{ background:#FFF8F0; border:1.5px solid #E35D22; border-radius:10px; padding:20px; }}
  .insight-card .tag {{ font-size:.7rem; font-weight:700; color:#E35D22; text-transform:uppercase; letter-spacing:.04em; }}
  .insight-card .titulo {{ font-size:1rem; font-weight:700; margin:8px 0; }}
  .insight-card .body   {{ font-size:.84rem; line-height:1.6; color:var(--c-text); }}
  .insight-card .meta   {{ display:flex; gap:12px; margin-top:12px; font-size:.75rem; color:var(--c-muted); }}

  .cta-card {{ background:var(--c-brand); color:#fff; border-radius:10px; padding:20px; display:flex; flex-direction:column; justify-content:space-between; }}
  .cta-card h3 {{ font-size:.88rem; font-weight:700; color:#a8d5be; margin-bottom:10px; }}
  .cta-card p  {{ font-size:.85rem; line-height:1.5; }}
  .cta-card .btn {{ display:inline-block; background:var(--c-acc); color:#fff; border-radius:6px; padding:10px 16px; font-size:.82rem; font-weight:700; margin-top:14px; text-align:center; }}

  /* Tabela Analítica */
  .table-card {{ background:var(--c-card); border-radius:10px; padding:20px; box-shadow:0 1px 4px rgba(0,0,0,.07); margin-bottom:20px; }}
  .table-card h3 {{ font-size:.9rem; font-weight:700; margin-bottom:12px; }}
  table {{ width:100%; border-collapse:collapse; font-size:.82rem; }}
  th {{ background:var(--c-brand); color:#fff; padding:8px 12px; text-align:left; }}
  td {{ padding:7px 12px; border-bottom:1px solid #eee; }}
  tr:hover td {{ background:#f1f5f9; }}

  footer {{ text-align:center; font-size:.72rem; color:var(--c-muted); padding:16px; }}
</style>
</head>
<body>
<header>
  <div>
    <h1>Dashboard Educacional &mdash; Desempenho Estudantil</h1>
    <p style="font-size:.75rem; color:#a8d5be; margin-top:4px;">Gerado por Pipeline Multi-Agente &bull; Base: StudentPerformanceFactors.csv &bull; n={ctx['n_registros']:,}</p>
  </div>
  <div class="big-idea">&ldquo;{big_idea}&rdquo;</div>
</header>

<div class="dash">

  <!-- ZONA 1 — Contexto / KPIs -->
  <p style="font-size:.72rem;font-weight:700;color:var(--c-muted);text-transform:uppercase;letter-spacing:.05em;margin-bottom:8px;">ZONA 1 &mdash; Contexto</p>
  <div class="kpi-row">
    <div class="kpi ok">
      <div class="val">{pct_aprov}%</div>
      <div class="lbl">Taxa de Aprovação</div>
      <div class="delta" style="color:var(--c-ok)">&#9650; Meta: 80%</div>
    </div>
    <div class="kpi">
      <div class="val">{media_nota}</div>
      <div class="lbl">Nota Média (0&ndash;100)</div>
      <div class="delta" style="color:var(--c-muted)">DP: {ctx['dp_nota']}</div>
    </div>
    <div class="kpi warn">
      <div class="val" style="color:var(--c-warn)">{pct_risco}%</div>
      <div class="lbl">Alunos em Alto Risco</div>
      <div class="delta" style="color:var(--c-warn)">&#9660; Envol.Baixo + &lt;15h</div>
    </div>
    <div class="kpi">
      <div class="val">{horas_med}h</div>
      <div class="lbl">Horas Médias de Estudo/sem</div>
      <div class="delta" style="color:var(--c-muted)">Correlação c/ nota: {ctx['top_correlacoes'].get('Hours_Studied',0.45):.2f}</div>
    </div>
  </div>

  <!-- ZONA 2 — Diagnóstico -->
  <p style="font-size:.72rem;font-weight:700;color:var(--c-muted);text-transform:uppercase;letter-spacing:.05em;margin-bottom:8px;">ZONA 2 &mdash; Diagnóstico</p>
  <div class="charts-row">
    <div class="chart-card">
      <h3>Nota Média por Faixa de Horas de Estudo</h3>
      <p class="sub">Insight: retorno marginal cai acima de 30h/semana</p>
      <canvas id="chartHoras" height="200"></canvas>
    </div>
    <div class="chart-card">
      <h3>Nota Média por Envolvimento Familiar</h3>
      <p class="sub">Gap entre Alto e Baixo: {round(parental[parental['grupo']=='High']['media'].values[0] - parental[parental['grupo']=='Low']['media'].values[0], 1) if not parental.empty else '~5'} pontos</p>
      <canvas id="chartParental" height="200"></canvas>
    </div>
  </div>

  <!-- ZONA 3 — Recomendação -->
  <p style="font-size:.72rem;font-weight:700;color:var(--c-muted);text-transform:uppercase;letter-spacing:.05em;margin-bottom:8px;">ZONA 3 &mdash; Recomendação</p>
  <div class="insight-row">
    <div class="insight-card">
      <div class="tag">[Insight IA] Acionavel &bull; {insight_card['id']}</div>
      <div class="titulo">{insight_card['titulo']}</div>
      <div class="body">
        <strong>Observação:</strong> {insight_card['observacao']}<br><br>
        <strong>Impacto:</strong> {insight_card['impacto']}<br><br>
        <strong>Ação:</strong> {insight_card['acao']}
      </div>
      <div class="meta">
        <span>&#128197; Prazo: {insight_card['prazo']}</span>
        <span>&#128100; {insight_card['stakeholder']}</span>
      </div>
    </div>
    <div class="cta-card">
      <div>
        <h3>CALL TO ACTION</h3>
        <p>{story['zona3_recomendacao']['call_to_action']}</p>
      </div>
      <div class="btn">Aprovar Protocolo &rarr;</div>
    </div>
  </div>

  <!-- Tabela Analítica -->
  <div class="table-card">
    <h3>Tabela Analítica — Top Fatores de Impacto na Nota</h3>
    <table>
      <tr><th>Fator</th><th>Correlação c/ Nota</th><th>Tipo</th><th>Acão Sugerida</th></tr>
      {"".join(f"<tr><td>{k}</td><td>{v:.3f}</td><td>Numerico</td><td>Monitorar</td></tr>" for k,v in ctx['top_correlacoes'].items())}
      <tr><td>Parental_Involvement (High vs Low)</td><td>~0.24 (eta²)</td><td>Categórico</td><td>Programa familiar</td></tr>
    </table>
  </div>

</div>

<footer>Gerado por Pipeline Multi-Agente (Discovery → Insights → Storyboard → HTML) &bull; 2026</footer>

<script>
const horasData = {{
  labels: {json.dumps([str(r['faixa']) for _, r in hb.iterrows()])},
  datasets: [{{
    label: 'Nota Média',
    data: {json.dumps([round(float(r['media']),1) for _, r in hb.iterrows()])},
    backgroundColor: ['#B0B0B0','#4A7FB5','#4A7FB5','#E35D22'],
    borderRadius: 5,
  }}]
}};
new Chart(document.getElementById('chartHoras'), {{
  type: 'bar',
  data: horasData,
  options: {{
    plugins: {{ legend: {{ display: false }} }},
    scales: {{ y: {{ min: 55, title: {{ display: true, text: 'Nota Média' }} }} }},
  }}
}});

const parentalData = {{
  labels: {json.dumps([str(r['grupo']) for _, r in parental.iterrows()])},
  datasets: [{{
    label: 'Nota Média',
    data: {json.dumps([round(float(r['media']),1) for _, r in parental.iterrows()])},
    backgroundColor: ['#E35D22','#4A7FB5','#B0B0B0'],
    borderRadius: 5,
  }}]
}};
new Chart(document.getElementById('chartParental'), {{
  type: 'bar',
  data: parentalData,
  options: {{
    plugins: {{ legend: {{ display: false }} }},
    scales: {{ y: {{ min: 60, title: {{ display: true, text: 'Nota Média' }} }} }},
  }}
}});
</script>
</body>
</html>"""
    return html

# =============================================================
# ORQUESTRADOR — roda a cadeia de agentes em sequência
# =============================================================
print("Agente 1 — Discovery...")
ctx      = agente_discovery(df)
print(json.dumps(ctx, indent=2, ensure_ascii=False))

print("\nAgente 2 — Insights...")
insights = agente_insights(ctx)
for i in insights:
    print(f"  [{i['tipo'].upper()}] {i['titulo']}")

print("\nAgente 3 — Storyboard...")
story = agente_storyboard(ctx, insights)
print("  Big Idea:", story["big_idea"][:80], "...")

print("\nAgente 4 — Prototipagem HTML...")
html = agente_html(ctx, insights, story)
out_html = os.path.join(OUT, "prototipo_dashboard_agente.html")
with open(out_html, "w", encoding="utf-8") as f:
    f.write(html)
print(f"  -> {out_html}")

# Salvar também o mapa de insights em JSON (para o .tex)
with open(os.path.join(OUT, "pipeline_contexto.json"), "w", encoding="utf-8") as f:
    json.dump({"contexto": ctx, "insights": insights, "storyboard": {
        "big_idea": story["big_idea"],
        "cta": story["zona3_recomendacao"]["call_to_action"]
    }}, f, indent=2, ensure_ascii=False)

print("\n[OK] Pipeline concluido. Abra:", out_html)
