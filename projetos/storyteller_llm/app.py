"""Protótipo didático de storytelling analítico com evidências determinísticas."""
import json
import os
import pandas as pd
import plotly.express as px
import streamlit as st

DATA = pd.DataFrame([
    ("2026-W01", "chat", 120, 84, 11), ("2026-W01", "telefone", 90, 72, 7),
    ("2026-W02", "chat", 132, 99, 18), ("2026-W02", "telefone", 94, 78, 8),
    ("2026-W03", "chat", 141, 106, 23), ("2026-W03", "telefone", 102, 86, 9),
    ("2026-W04", "chat", 150, 120, 28), ("2026-W04", "telefone", 107, 91, 10),
], columns=["semana", "canal", "atendimentos", "resolvidos_primeiro_contato", "reaberturas"])


def build_evidence(channel: str) -> dict:
    frame = DATA if channel == "Todos" else DATA[DATA.canal == channel]
    total = int(frame.atendimentos.sum())
    resolved = int(frame.resolvidos_primeiro_contato.sum())
    reopened = int(frame.reaberturas.sum())
    weekly = frame.groupby("semana", as_index=False).sum(numeric_only=True)
    weekly["resolucao_1o_contato"] = weekly.resolvidos_primeiro_contato / weekly.atendimentos
    return {
        "evidence": [
            {"id": "E1", "name": "atendimentos", "value": total, "unit": "casos"},
            {"id": "E2", "name": "resolução no primeiro contato", "value": round(100 * resolved / total, 1), "unit": "%", "numerator": resolved, "denominator": total},
            {"id": "E3", "name": "reaberturas", "value": reopened, "unit": "casos"},
            {"id": "E4", "name": "taxa de reabertura", "value": round(100 * reopened / total, 1), "unit": "%", "numerator": reopened, "denominator": total},
        ],
        "weekly": weekly.to_dict(orient="records"),
        "caveat": "Dados didáticos sintéticos; associação temporal não demonstra causa.",
    }


def generate_story(question: str, evidence: dict) -> tuple[str, str]:
    if not os.getenv("OPENAI_API_KEY"):
        return "Configure OPENAI_API_KEY no ambiente local. Os indicadores e o gráfico continuam disponíveis.", "sem chamada"
    try:
        from openai import OpenAI
        client = OpenAI()
        response = client.responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-5-mini"),
            instructions=("Escreva uma narrativa curta de AED em português usando somente o JSON. "
                "Não infira causalidade. Retorne JSON com headline, narrative, evidence_ids e caveat. "
                "Se faltar evidência, diga isso."),
            input=json.dumps({"question": question, **evidence}, ensure_ascii=False),
        )
        result = json.loads(response.output_text)
        allowed = {row["id"] for row in evidence["evidence"]}
        if not set(result.get("evidence_ids", [])).issubset(allowed):
            raise ValueError("ID de evidência desconhecido")
        story = f"**{result.get('headline', 'Leitura dos dados')}**\n\n{result.get('narrative', '')}\n\n_{result.get('caveat', '')}_"
        return story, "resposta validada"
    except Exception as exc:
        return f"Resposta rejeitada na validação ({type(exc).__name__}). Consulte os indicadores calculados.", "resposta rejeitada"


st.set_page_config(page_title="Storyteller AED", page_icon="📊", layout="wide")
st.title("Uma história que volta aos dados")
st.caption("Protótipo didático: o código calcula; a LLM ajuda a narrar.")
channel = st.selectbox("Canal", ["Todos", *sorted(DATA.canal.unique())])
evidence = build_evidence(channel)
frame = DATA if channel == "Todos" else DATA[DATA.canal == channel]
chart = frame.groupby("semana", as_index=False).sum(numeric_only=True)
chart["Resolução no primeiro contato (%)"] = 100 * chart.resolvidos_primeiro_contato / chart.atendimentos
left, right = st.columns(2)
with left:
    st.subheader("Indicadores calculados no aplicativo")
    st.dataframe(pd.DataFrame(evidence["evidence"]), hide_index=True, use_container_width=True)
    st.caption(evidence["caveat"])
with right:
    st.subheader("Tendência semanal")
    st.plotly_chart(px.line(chart, x="semana", y="Resolução no primeiro contato (%)", markers=True), use_container_width=True)
question = st.text_input("Pergunta para a narrativa", "O que merece atenção nesta série?")
if st.button("Gerar narrativa"):
    story, status = generate_story(question, evidence)
    st.subheader("Narrativa assistida")
    st.markdown(story)
    st.caption(f"Status: {status}. Evidências válidas: E1–E4.")
with st.expander("Ver dados didáticos"):
    st.dataframe(DATA, hide_index=True, use_container_width=True)
