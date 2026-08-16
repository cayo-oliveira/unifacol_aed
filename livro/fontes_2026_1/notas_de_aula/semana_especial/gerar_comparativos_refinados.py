from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, FancyArrowPatch
import numpy as np


BASE = Path(__file__).resolve().parent
OUT = BASE / "outputs"
HTML = BASE / "comparativos"
OUT.mkdir(exist_ok=True)
HTML.mkdir(exist_ok=True)

BLUE = "#2563EB"
ORANGE = "#E35D22"
GREEN = "#16A34A"
RED = "#DC2626"
AMBER = "#EAB308"
SLATE = "#334155"
MUTED = "#64748B"
LIGHT = "#F8FAFC"
BORDER = "#CBD5E1"


def setup(title):
    fig, ax = plt.subplots(figsize=(11.4, 4.25), dpi=170)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 44)
    ax.axis("off")
    ax.add_patch(Rectangle((0, 0), 100, 44, facecolor="white", edgecolor="none"))
    ax.text(50, 41.5, title, ha="center", va="center", fontsize=15, weight="bold", color=SLATE)
    for x, label, color in [(2.5, "ANTES: problema", RED), (51.5, "DEPOIS: solucao", GREEN)]:
        ax.add_patch(FancyBboxPatch((x, 4), 46, 35, boxstyle="round,pad=0.6,rounding_size=1.2",
                                    facecolor=LIGHT, edgecolor=BORDER, linewidth=1.0))
        ax.text(x + 1.6, 37.0, label, fontsize=9.5, weight="bold", color=color)
    return fig, ax


def save(fig, name):
    path = OUT / name
    fig.savefig(path, bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)
    return path


def label(ax, x, y, text, size=8.2, color=SLATE, weight="normal", ha="left"):
    ax.text(x, y, text, fontsize=size, color=color, weight=weight, ha=ha, va="center")


def bar(ax, x, y, w, h, color, text=None):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=color, edgecolor="none"))
    if text:
        ax.text(x + w + 1, y + h / 2, text, fontsize=7.5, color=SLATE, va="center")


def cards(ax, x, y, values, colors):
    for i, (title, val) in enumerate(values):
        xx = x + i * 10.5
        ax.add_patch(FancyBboxPatch((xx, y), 9.2, 7, boxstyle="round,pad=0.3,rounding_size=0.7",
                                    facecolor="white", edgecolor=BORDER, linewidth=0.8))
        ax.text(xx + 0.7, y + 5.1, title, fontsize=5.8, color=MUTED)
        ax.text(xx + 0.7, y + 2.5, val, fontsize=9.5, color=colors[i], weight="bold")


def html(name, title, body):
    content = f"""<!doctype html>
<html lang="pt-br">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
body{{margin:0;font-family:Arial, sans-serif;background:#f8fafc;color:#1e293b}}
main{{max-width:1120px;margin:28px auto;padding:0 20px}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:18px}}
.panel{{background:white;border:1px solid #cbd5e1;border-radius:8px;padding:18px;min-height:360px}}
.bad{{border-top:6px solid #dc2626}} .good{{border-top:6px solid #16a34a}}
.kpi{{font-size:34px;font-weight:800;margin:8px 0}} .muted{{color:#64748b}}
.bar{{height:20px;background:#e2e8f0;margin:10px 0;border-radius:3px;overflow:hidden}}
.fill{{height:100%;background:#2563eb}} .hot{{background:#e35d22}}
table{{width:100%;border-collapse:collapse;margin-top:12px}}td,th{{border-bottom:1px solid #e2e8f0;padding:8px;text-align:left}}
</style>
</head>
<body><main><h1>{title}</h1><div class="grid">{body}</div></main></body></html>"""
    (HTML / name).write_text(content, encoding="utf-8")


def cmp_cores():
    fig, ax = setup("Cores: de decoracao para linguagem visual")
    for i, c in enumerate(["#DC2626", "#2563EB", "#16A34A", "#7C3AED", "#EAB308", "#06B6D4"]):
        bar(ax, 7, 30 - i * 4, 24 - i, 2.2, c, ["A", "B", "C", "D", "E", "F"][i])
    label(ax, 7, 7.5, "Se tudo grita, nada vira prioridade.", 8, RED, "bold")
    for i, (txt, w, c) in enumerate([("Base neutra 60%", 31, "#CBD5E1"), ("Marca 30%", 22, BLUE), ("Acao 10%", 8, ORANGE)]):
        bar(ax, 57, 29 - i * 6, w, 3.1, c, txt)
    label(ax, 57, 8, "Uma cor viva fica reservada ao dado que pede acao.", 8, GREEN, "bold")
    save(fig, "cmp_cap1_cores.png")
    html("cap1_cores.html", "Cores em dashboards", '<section class="panel bad"><h2>Antes</h2><p>Multiplas cores competem pela atencao.</p><div class="bar"><div class="fill hot" style="width:90%"></div></div><div class="bar"><div class="fill" style="width:84%;background:#7c3aed"></div></div><div class="bar"><div class="fill" style="width:70%;background:#16a34a"></div></div></section><section class="panel good"><h2>Depois</h2><p>Base neutra, marca consistente e destaque unico.</p><div class="kpi">Gap -18%</div><div class="bar"><div class="fill hot" style="width:78%"></div></div><p class="muted">Prioridade visual clara.</p></section>')


def cmp_olhar():
    fig, ax = setup("Caminho do olhar: ordem visual por audiencia")
    rng = np.random.default_rng(3)
    for i in range(16):
        ax.add_patch(Rectangle((6 + rng.random()*34, 10 + rng.random()*22), 7, 4,
                               facecolor="white", edgecolor=BORDER))
    pts = [(9,34),(35,14),(15,18),(42,31),(18,27)]
    for a, b in zip(pts, pts[1:]):
        ax.add_patch(FancyArrowPatch(a,b,arrowstyle="->",color=RED,mutation_scale=10,linewidth=1.3))
    label(ax, 7, 7, "O leitor monta a historia sozinho.", 8, RED, "bold")
    cards(ax, 56, 29, [("Meta", "R$ 2,4M"), ("Gap", "-12%"), ("Risco", "Alto")], [BLUE, RED, AMBER])
    ax.add_patch(FancyArrowPatch((57,27),(91,27),arrowstyle="->",color=SLATE,mutation_scale=11))
    ax.add_patch(FancyArrowPatch((91,27),(61,12),arrowstyle="->",color=SLATE,mutation_scale=11))
    ax.add_patch(FancyArrowPatch((61,12),(91,12),arrowstyle="->",color=SLATE,mutation_scale=11))
    for n,(x,y) in enumerate([(57,27),(91,27),(61,12),(91,12)],1):
        ax.add_patch(Circle((x,y),1.5,facecolor=ORANGE,edgecolor="white"))
        ax.text(x,y,str(n),ha="center",va="center",fontsize=7,color="white",weight="bold")
    label(ax, 57, 7, "Z executivo: contexto, diagnostico, decisao.", 8, GREEN, "bold")
    save(fig, "cmp_cap1_olhar.png")
    html("cap1_olhar.html", "Caminho do olhar", '<section class="panel bad"><h2>Antes</h2><p>Cards espalhados sem hierarquia.</p></section><section class="panel good"><h2>Depois</h2><p>Fluxo em Z: KPI, causa, recomendacao.</p></section>')


def cmp_carga():
    fig, ax = setup("Carga cognitiva: menos decodificacao, mais decisao")
    colors = [RED, BLUE, GREEN, AMBER, "#7C3AED", "#06B6D4"]
    for r in range(4):
        for c in range(5):
            ax.add_patch(Rectangle((6+c*8, 28-r*5), 6, 3, facecolor=colors[(r+c)%6], edgecolor="white"))
    label(ax, 7, 7, "Carga extrinseca: legenda, cor e excesso competem.", 8, RED, "bold")
    cards(ax, 56, 28, [("Receita", "2,4M"), ("Margem", "8,1%"), ("Churn", "12%")], [BLUE, GREEN, RED])
    for i,w in enumerate([29,22,16]):
        bar(ax, 57, 19-i*4.7, w, 2.4, [BLUE, "#94A3B8", ORANGE][i], ["Canal digital", "Loja fisica", "Atacado"][i])
    label(ax, 57, 7, "Carga util: o esforco vai para interpretar o negocio.", 8, GREEN, "bold")
    save(fig, "cmp_cap1_carga.png")
    html("cap1_carga.html", "Carga cognitiva", '<section class="panel bad"><h2>Antes</h2><p>Excesso visual aumenta a carga extrinseca.</p></section><section class="panel good"><h2>Depois</h2><p>Hierarquia e agrupamento reduzem esforco mental.</p></section>')


def cmp_simple(name, title, left, right, kind):
    fig, ax = setup(title)
    if kind == "insight_info":
        bar(ax, 8, 27, 29, 3, BLUE, "Churn janeiro 12%")
        bar(ax, 8, 20, 18, 3, "#94A3B8", "media 8%")
        label(ax, 7, 11, left, 8, RED, "bold")
        bar(ax, 58, 27, 27, 3, BLUE, "padrao")
        bar(ax, 58, 20, 15, 3, ORANGE, "segmento critico")
        label(ax, 57, 11, right, 8, GREEN, "bold")
    elif kind == "action":
        label(ax, 8, 28, "Sul caiu 8%", 15, RED, "bold")
        label(ax, 8, 20, "Sem causa, dono, prazo ou impacto.", 8, SLATE)
        label(ax, 57, 31, "Reduzir desconto Sul", 13, ORANGE, "bold")
        for i, t in enumerate(["Responsavel: Comercial", "Prazo: 30/jun", "Impacto: +R$85k tri"]):
            label(ax, 58, 24 - i*5, t, 9, SLATE)
    elif kind == "dac":
        xs = [8,18,28,38]
        for x,t in zip(xs,["Excel","Print","Email","Prod"]):
            ax.add_patch(Circle((x,25),3,facecolor="white",edgecolor=RED,linewidth=1.3)); label(ax,x,25,t,6,SLATE,ha="center")
        for a,b in zip(xs,xs[1:]): ax.add_patch(FancyArrowPatch((a+3,25),(b-3,25),arrowstyle="->",color=RED))
        label(ax,7,12,left,8,RED,"bold")
        xs = [57,66,75,84,93]
        for x,t in zip(xs,["Git","CI","Homol","Aprov","Prod"]):
            ax.add_patch(Circle((x,25),3,facecolor="white",edgecolor=GREEN,linewidth=1.3)); label(ax,x,25,t,5.8,SLATE,ha="center")
        for a,b in zip(xs,xs[1:]): ax.add_patch(FancyArrowPatch((a+3,25),(b-3,25),arrowstyle="->",color=GREEN))
        label(ax,57,12,right,8,GREEN,"bold")
    elif kind == "autoeda":
        for i in range(5): bar(ax, 8, 30-i*4.2, 30-i*2, 2, "#94A3B8", None)
        label(ax,7,9,left,8,RED,"bold")
        for i,(t,c) in enumerate([("Distribuicao estranha",ORANGE),("Correlacao forte",BLUE),("Outlier relevante",RED)]):
            ax.add_patch(FancyBboxPatch((57,27-i*7),31,4.5,boxstyle="round,pad=0.25",facecolor="white",edgecolor=c))
            label(ax,58,29.2-i*7,t,8,c,"bold")
        label(ax,57,7,right,8,GREEN,"bold")
    elif kind == "agents":
        ax.add_patch(Circle((24,25),5,facecolor="white",edgecolor=RED,linewidth=1.5))
        label(ax,24,25,"Analista\nunico",8,SLATE,ha="center")
        label(ax,7,11,left,8,RED,"bold")
        xs=[56,65,74,83,92]; names=["Regra","SQL","EDA","Dash","Homol"]
        for x,t in zip(xs,names):
            ax.add_patch(Circle((x,26),3,facecolor="white",edgecolor=BLUE,linewidth=1.2)); label(ax,x,26,t,6,SLATE,ha="center")
        for a,b in zip(xs,xs[1:]): ax.add_patch(FancyArrowPatch((a+3,26),(b-3,26),arrowstyle="->",color=BLUE))
        label(ax,57,10,right,8,GREEN,"bold")
    save(fig, name)
    html(name.replace("cmp_", "").replace(".png", ".html"), title,
         f'<section class="panel bad"><h2>Antes</h2><p>{left}</p><div class="bar"><div class="fill hot" style="width:76%"></div></div><div class="bar"><div class="fill" style="width:42%;background:#94a3b8"></div></div><p class="muted">Exemplo propositalmente incompleto para discutir em aula.</p></section><section class="panel good"><h2>Depois</h2><p>{right}</p><div class="kpi">Decisao clara</div><table><tr><th>Componente</th><th>Resultado</th></tr><tr><td>Evidencia</td><td>quantificada</td></tr><tr><td>Acao</td><td>dono + prazo</td></tr></table></section>')


def cap2(name, title, mode):
    fig, ax = setup(title)
    if mode == "story":
        for i in range(6):
            ax.add_patch(Rectangle((7+(i%3)*12, 24-(i//3)*9), 9, 6, facecolor="white", edgecolor=BORDER))
        label(ax,7,9,"Pecas boas, mas sem sequencia narrativa.",8,RED,"bold")
        for i,t in enumerate(["1. Contexto","2. Problema","3. Causa","4. Acao"]):
            ax.add_patch(FancyBboxPatch((57+i*9.1,22),8,9,boxstyle="round,pad=0.25",facecolor="white",edgecolor=BLUE))
            label(ax,57.5+i*9.1,26.5,t,6.2,SLATE)
        label(ax,57,9,"A historia guia a decisao em quatro passos.",8,GREEN,"bold")
    elif mode == "kpi":
        label(ax,17,27,"28%",24,RED,"bold",ha="center")
        label(ax,7,15,"Numero isolado: bom ou ruim em relacao a que?",8,RED,"bold")
        label(ax,57,31,"Turnover TI",8,MUTED)
        label(ax,57,26,"28%",22,RED,"bold")
        bar(ax,57,20,30,3,"#E2E8F0"); bar(ax,57,20,16,3,RED)
        ax.plot([57,64,69,75,82,88],[13,14,13,16,18,21],color=RED,linewidth=2)
        label(ax,57,9,"Meta 15% | Gap +13pp | tendencia piorando.",8,GREEN,"bold")
    elif mode == "chartjunk":
        for i,w in enumerate([24,19,15,10]): bar(ax,10,29-i*5,w,3,["#7C3AED",AMBER,RED,BLUE][i])
        ax.add_patch(Circle((31,16),6,facecolor="#FDE68A",edgecolor=RED,alpha=.6))
        label(ax,7,7,"Efeito visual compete com o dado.",8,RED,"bold")
        for i,w in enumerate([31,23,18,11]): bar(ax,57,29-i*5,w,3,[ORANGE,"#94A3B8","#94A3B8","#94A3B8"][i])
        label(ax,57,7,"Menos tinta, comparacao mais rapida.",8,GREEN,"bold")
    elif mode == "pitch":
        for i,t in enumerate(["Contexto longo","Metodologia","Graficos","Talvez acao"]):
            label(ax,8,31-i*6,t,8,SLATE)
        label(ax,7,7,"Tempo gasto antes da mensagem principal.",8,RED,"bold")
        widths=[7,10,13,10]; labels=["30s\nSituacao","45s\nComplicacao","60s\nResolucao","45s\nProximo passo"]
        x=57
        for w,t,c in zip(widths,labels,[BLUE,ORANGE,GREEN,SLATE]):
            ax.add_patch(Rectangle((x,22),w,8,facecolor=c,edgecolor="white")); label(ax,x+w/2,26,t,6,"white","bold",ha="center"); x+=w
        label(ax,57,9,"SCR transforma apresentacao em pedido claro.",8,GREEN,"bold")
    else:
        # generic varied dashboard comparison
        for i,w in enumerate([26,22,18,14]): bar(ax,8,30-i*5,w,2.5,["#94A3B8",BLUE,AMBER,RED][i])
        label(ax,7,8,"Explora muito, decide pouco.",8,RED,"bold")
        cards(ax,57,28,[("KPI","-18%"),("Meta","95%"),("Acao","Q3")],[RED,BLUE,GREEN])
        bar(ax,58,18,28,3,ORANGE,"causa principal")
        label(ax,57,8,"Resumo, evidencia e acao no mesmo fluxo.",8,GREEN,"bold")
    save(fig, name)


def groups():
    fig, ax = setup("Apresentacoes em grupo: prototipos diferentes, mesma disciplina")
    themes=[("Olist","logistica",ORANGE),("RH","turnover",BLUE),("Varejo","margem",GREEN),("Saude","risco",RED),("Fintech","churn",AMBER)]
    for i,(a,b,c) in enumerate(themes):
        x=6+i*8.2
        ax.add_patch(FancyBboxPatch((x,16),7.1,14,boxstyle="round,pad=0.25",facecolor="white",edgecolor=c,linewidth=1.2))
        label(ax,x+0.6,26.5,a,6.5,c,"bold")
        label(ax,x+0.6,22.5,b,5.8,SLATE)
        bar(ax,x+0.7,18,4.7,1.5,c)
    label(ax,7,8,"Antes: prototipos pareciam iguais no PDF.",8,RED,"bold")
    for i,(a,b,c) in enumerate(themes):
        x=56+i*8.2
        if i in [0,2,4]:
            for j,w in enumerate([5,4,3]): bar(ax,x+0.5,26-j*3,w,1.5,c)
        elif i==1:
            ax.plot([x+1,x+2.5,x+4,x+6],[20,24,23,28],color=c,linewidth=2)
        else:
            ax.scatter([x+1.5,x+3,x+5.5],[21,27,24],s=35,color=c)
        label(ax,x+0.2,16.5,a,5.7,c,"bold")
    label(ax,57,8,"Depois: cada briefing usa visual coerente com a dor.",8,GREEN,"bold")
    save(fig, "cmp_grupos_preview.png")


def main():
    cmp_cores()
    cmp_olhar()
    cmp_carga()
    cmp_simple("cmp_cap1_insight_info.png", "Insight informativo: entender antes de prescrever",
               "Mostra um fato, mas ainda nao orienta a acao.", "Explica o padrao e prepara a proxima pergunta.", "insight_info")
    cmp_simple("cmp_cap1_insight_acionavel.png", "Insight acionavel: dado com dono, prazo e impacto",
               "Observacao solta nao muda comportamento.", "Recomendacao operacional com impacto estimado.", "action")
    cmp_simple("cmp_cap1_dac.png", "Dashboard as Code: fluxo, nao bloco de codigo",
               "Processo manual dificil de auditar.", "Pipeline versionado ate producao.", "dac")
    cmp_simple("cmp_cap1_autoeda.png", "AED automatica: relatorio vira triagem analitica",
               "Relatorio bruto vira despejo de graficos.", "Alertas priorizam o que merece investigacao.", "autoeda")
    cmp_simple("cmp_cap1_agentes.png", "Engenheiro de Analytics Virtual: agentes por etapa",
               "Um analista vira gargalo end-to-end.", "Agentes especializados produzem artefatos validaveis.", "agents")
    cmp_simple("cmp_cap1_base_insights.png", "Base especializada: memoria de decisoes e exemplos",
               "Insights soltos nao melhoram o proximo projeto.", "Casos validados alimentam recomendacoes futuras.", "autoeda")
    for file, title, mode in [
        ("cmp_cap2_aed_explanatoria.png","AED vs analise explanatoria","generic"),
        ("cmp_cap2_big_idea.png","Big Idea Framework","generic"),
        ("cmp_cap2_storyboard.png","Storyboard e estrutura narrativa","story"),
        ("cmp_cap2_preatencao.png","Pre-atencao e atributos visuais","chartjunk"),
        ("cmp_cap2_relance.png","Teste do relance e titulo-mensagem","generic"),
        ("cmp_cap2_chartjunk.png","Data-ink ratio e chartjunk","chartjunk"),
        ("cmp_cap2_tableau.png","Filtros, parametros e acoes","generic"),
        ("cmp_cap2_decisorio.png","Dashboard que forca decisao","story"),
        ("cmp_cap2_kpi.png","KPI com meta, gap e tendencia","kpi"),
        ("cmp_cap2_pitch.png","Pitch de 3 minutos","pitch"),
    ]:
        cap2(file, title, mode)
        html(file.replace("cmp_", "").replace(".png", ".html"), title,
             '<section class="panel bad"><h2>Antes</h2><p>Exemplo com problema de estrutura, excesso ou falta de mensagem.</p><div class="bar"><div class="fill" style="width:80%"></div></div><div class="bar"><div class="fill hot" style="width:55%"></div></div></section><section class="panel good"><h2>Depois</h2><p>Exemplo com hierarquia, evidencia e decisao clara.</p><div class="kpi">Acao prioritaria</div><table><tr><th>Evidencia</th><th>Impacto</th></tr><tr><td>Causa principal</td><td>+R$85k</td></tr></table></section>')
    groups()


if __name__ == "__main__":
    main()
