# Storyteller AED com LLM

Protótipo simples da Unidade II: indicadores e gráfico são calculados deterministicamente; a LLM recebe a pergunta e o pacote de evidências para redigir uma narrativa.

## Executar

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY="sua-chave-local"
streamlit run app.py
```

Mantenha `OPENAI_API_KEY` no ambiente local ou em secrets do Streamlit. Não coloque uma chave real no código, em `.env`, no navegador, em screenshots ou no Git. O exemplo usa dados sintéticos, não possui autenticação e não deve ser conectado a dados pessoais ou corporativos.

O protótipo verifica que IDs de evidência mencionados existem. Para uso real, prefira saída estruturada com schema suportado pela API/SDK, testes de regressão, tratamento detalhado de erros, limites de custo e revisão de segurança e privacidade.
