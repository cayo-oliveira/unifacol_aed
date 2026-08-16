# BI e dataviz na transição agentic

Última verificação das interfaces: 2026-08-05. Confirmar novamente a documentação oficial antes de publicar nomes, disponibilidade, licença ou status de preview.

## Escada conceitual

Não misturar:

1. BI visual: autoria manual de gráficos, relatórios e dashboards.
2. Copiloto: assistência ao autor ou consumidor dentro de uma interface.
3. Análise conversacional: perguntas em linguagem natural com tabelas, texto e visuais.
4. BI agentic: planejamento em várias etapas, seleção de fontes/ferramentas, consultas, teste de hipóteses e eventual ação.

Uma plataforma pode ocupar mais de um nível. Avaliar sempre semântica, identidade/permissão, execução, evidência, visualização, auditoria e possibilidade de contestação.

## Referências científicas

- Phebe: *A Multi-Agent Natural Language Interface for Interactive Data Visualization* (ACM IAIT 2026, DOI 10.1145/3816713.3819784): limpeza, orquestração, Text-to-SQL, estatística e recomendação visual.
- Singh et al.: *Beyond Text-to-SQL: An Agentic LLM System for Governed Enterprise Analytics APIs* (arXiv:2605.21027, 2026): APIs governadas, resolução de entidades, permissões, visualização estruturada e diferença entre execução válida e correção ponta a ponta.
- Como apoio: *nvAgent: Automated Data Visualization from Natural Language via Collaborative Agent Workflow* (ACL 2025) e *Talking to Data: A Systematic Review of the Rise of Conversational Agents for Visual Analytics* (IEEE Access 2025).

## Plataformas verificadas

- Tableau clássico: Desktop/Cloud/Server para autoria e publicação. Tableau Agent auxilia criação/leitura dentro do contexto suportado. Tableau Next é apresentado como plataforma agentic no ecossistema Salesforce, com Tableau Semantics e Agentforce Tableau.
  - <https://help.tableau.com/current/online/en-us/web_author_einstein.htm>
  - <https://help.tableau.com/current/tableau-next/en-us/tableau_next_tableau_product_overview.htm>
- Power BI/Fabric: modelo semântico, DAX, relatórios e segurança. Copilot atende criação/consumo; Fabric data agents consultam fontes autorizadas; Power BI Agentic fornece skills e MCP para agentes de desenvolvimento.
  - <https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction>
  - <https://learn.microsoft.com/en-us/fabric/data-science/data-agent-copilot-powerbi>
  - <https://learn.microsoft.com/en-us/power-bi/developer/agentic/power-bi-agentic-overview>
- AWS: usar `Amazon Quick Sight` e `Amazon Q em Quick Sight` conforme documentação vigente; reconhecer que o produto foi conhecido como QuickSight Q. Generative BI cobre Q&A, autoria de visuais/cálculos, resumos e histórias.
  - <https://docs.aws.amazon.com/quick/latest/userguide/quicksight-gen-bi.html>
- Google: distinguir Looker Studio, voltado a relatórios conectados mais acessíveis, de Looker, plataforma empresarial com LookML e governança. Gemini in Looker oferece Conversational Analytics e data agents; dashboard agents e fluxos agentic dependem de versão/status.
  - <https://docs.cloud.google.com/looker/docs/conversational-analytics-overview>
  - <https://docs.cloud.google.com/looker/docs/gemini-overview-looker>
- Databricks: `AI/BI Genie Agent`, anteriormente Genie Space. Configuração combina Unity Catalog, SQL warehouse, instruções, exemplos SQL e trusted assets. Agent mode planeja e executa investigação com múltiplas consultas.
  - <https://docs.databricks.com/aws/en/genie/set-up>
  - <https://docs.databricks.com/aws/en/genie/agent-mode>
- Python/Streamlit: opção programável para tornar arquitetura e validação visíveis; não presumir que catálogo, camada semântica, RLS, auditoria e operação corporativa vêm prontos.

## Pergunta pedagógica

Usar `Para que dataviz se a IA responde diretamente?` sem resposta defensiva. O dashboard pode deixar de ser a única porta de entrada e a autoria manual rotineira pode diminuir. Dataviz continua como mecanismo de percepção, comparação, inspeção, contestação e comunicação compartilhada. Conversa orienta a investigação; visual externaliza relações e permite conferir a resposta.

Ao comparar ferramentas, o aluno deve demonstrar mais do que geração bem-sucedida: fonte de verdade, consulta/filtro, cálculo manual de referência, tratamento de ambiguidade, restrições de acesso, escolha perceptiva e condição de recusa do agente.
