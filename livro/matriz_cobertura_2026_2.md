# Matriz de cobertura — AED

| Fonte 2026.1 | Conteúdo | Destino 2026.2 | Estado/ação |
|---|---|---|---|
| `livro/chapters/00_plano.tex` | plano antigo e biblioteca Python | Cap. 1, plano e apêndice | plano reescrito; código será triado |
| `aula/semana01/semana01.tex` | Big Idea, exploratória/explanativa, ETL e Tableau | Caps. 1, 2, 5 e 9 | conceitos do Cap. 1 preservados; contrato de dado e verificação do ETL integrados ao Cap. 2; fluxo fonte→transformação→consumo reescrito no Cap. 5 como arquitetura rastreável; tutoriais de ferramenta seguem para caps. próprios |
| `livro/chapters/01_aed.tex` | fluxo da AED, tipos, qualidade, medidas iniciais e ferramentas | Caps. 1, 2 e 3 | fundamentos e qualidade integrados aos Caps. 1–2; aprofundamento das medidas segue para o Cap. 3 |
| `02_uni.tex` | univariada, frequências, posição, quartis, distribuição e dispersão | Caps. 3 e 4 | frequências e posição integradas ao Cap. 3; amplitude, variância, desvio-padrão, IQR, histograma, assimetria, ausências e outliers reescritos e integrados ao Cap. 4; exercícios legados permanecem fora do livro |
| `03_bi.tex` | bivariada | Cap. 5 | pendente |
| `04_multi.tex` | multivariada | Caps. 6/7 | relações e múltiplos painéis introduzidos no Cap. 6; organização de múltiplos painéis, comparação e estado visual aprofundados no Cap. 7 |
| `05_fundamentos.tex` | Tableau, conexão, joins, granularidade, medidas e modelagem | Cap. 5 + apêndice/caps. 10/11 | grão, cardinalidade, relações, joins, dimensões, medidas, camada semântica e consumo integrados ao Cap. 5 sem centralidade da ferramenta; tutoriais específicos seguem para apêndice e caps. próprios |
| `06_gaficos.tex` | tipos de gráficos | Cap. 6 | conceitos preservados e ampliados por pergunta, percepção, escalas e incerteza; tutoriais e exercícios legados não foram transportados |
| `07_insights.tex` | insights Python/Tableau | Caps. 7/9/12 | critérios de destaque e verificação visual integrados ao Cap. 7; geração assistida, validação e resposta rastreável integradas ao Cap. 9; automação aprofundada segue para o Cap. 12 |
| `08_storytelling.tex` | storytelling | Caps. 7/8/10 | layout, hierarquia, grid, zonas, filtros e interatividade integrados ao Cap. 7; exploração versus explicação, Big Idea, storyboard, anotação e decisão integrados ao Cap. 8; pitch e publicação seguem para o Cap. 10 |
| `09_real_cases.tex` | projeto final e caso de evasão escolar | Cap. 8 + Caderno de atividades | cadeia curadoria→AED→narrativa e caso educacional reescritos no Cap. 8 como decisão verificável; entregáveis, rubrica, tutorial Tableau e exercício seguem para o caderno próprio |
| `10_tableau.tex` | resumo Tableau | apêndice de ferramentas | preservar como opção, não obrigação |
| `notas_de_aula/semana_especial/semana_especial.tex` | auto-EDA, insights, agentes, Big Idea e dashboards agentic | Caps. 7–9 e 12–13 | percepção e layout integrados ao Cap. 7; narrativa ao Cap. 8; níveis copiloto/conversacional/agentic, geração e validação ao Cap. 9; automação e multiagente seguem para Caps. 12–13; questões e respostas não foram transportadas |
| exercícios dos capítulos | prática | `Caderno_de_exercicios/` | mover e revisar em ENADE |

## Capítulo 1 concluído

Integra curso, avaliação, exploratória/explanativa, pergunta→dado→visual→decisão, percepção, papel da IA, escolha de ferramentas e artigo IEEE T-Vol. ETL detalhado e tutorial Tableau foram adiados aos capítulos adequados, não removidos.

## Capítulo 2 concluído

Integra pergunta operacional, população, amostra, unidade de observação/análise, variáveis e escalas, granularidade, chaves, junções, agregações, dimensões de qualidade, dicionário de dados, erros plausíveis, cálculo manual e conferência em pandas. Preserva o caso de desempenho acadêmico de 2026.1, mas desloca a ferramenta para depois do contrato semântico. Tutoriais de Tableau e aprofundamento de estatística permanecem destinados aos capítulos 3, 6 e 11.

## Capítulo 3 concluído

Integra frequências absoluta, relativa e acumulada; média simples e ponderada; mediana; moda; quartis; percentis; comparação entre grupos; composição; centros em séries temporais; casos de atendimento e salários; contas manuais e reprodução em pandas/NumPy. Preserva e reescreve as medidas de posição do antigo `02_uni.tex` e os casos densos da antiga Semana 3, sem levar exercícios ou teleprompter ao livro.

## Capítulo 4 concluído

Integra a parte pertinente de `02_uni.tex` e das Semanas 4 e 5: amplitude; desvios; variância populacional e amostral; desvio-padrão; IQR e cercas de Tukey; histograma, boxplot, forma, cauda, assimetria e multimodalidade; mecanismos MCAR, MAR e MNAR; estratégias e limites de imputação; investigação e análise de sensibilidade de outliers. O caso de entregas encadeia contas à mão, interpretação, código em pandas/matplotlib e relatório de tratamento justificável. Correlação, atividades, respostas, revisão de prova, entregas e teleprompter das fontes antigas não foram concatenados ao capítulo; exercícios permanecem destinados ao caderno próprio.

## Capítulo 5 concluído

Integra o ETL da antiga Semana 1 e os conceitos duráveis de `05_fundamentos.tex`, ampliando-os para arquitetura específica de AED. O fluxo pergunta→fonte→ingestão→SOR→SOT→SPEC→análise/dashboard inclui OLTP/OLAP, warehouse/lake/lakehouse, grão, chaves, cardinalidade, fanout, fatos/dimensões, qualidade por camada, catálogo, linhagem, camada semântica, fonte de verdade, acesso e frescor. O caso de receita multicanal apresenta divergência semântica, join manual com multiplicação, SQL e pandas depois do desenho, testes e contrato ponta a ponta. Tutoriais de Tableau, atividades, exercícios, respostas e teleprompter não foram concatenados ao livro.

## Capítulo 6 concluído

Integra e amplia `06_gaficos.tex` e a parte visual de `04_multi.tex` por meio do caso de uma central de atendimento. A escolha nasce da pergunta e percorre comparação, tendência, distribuição, relação e composição; posição, comprimento, área e cor; escalas lineares e logarítmicas; eixos, taxas, índices e normalização; múltiplos painéis, acessibilidade e incerteza. Há contas de razão, área, média móvel, Freedman--Diaconis, percentil, escore z, min--max e intervalo de confiança, além de redesign e reprodução em Python. Mapas e ferramentas aparecem somente quando participam da pergunta; atividades, respostas e teleprompter das fontes de 2026.1 permanecem fora do livro.

## Capítulo 7 concluído

Integra os princípios de cor e contraste de `06_gaficos.tex`, os critérios de destaque de `07_insights.tex`, a organização espacial e a interação de `08_storytelling.tex` e a parte pertinente da antiga Semana 8. O caso de uma rede de clínicas percorre paletas categóricas, sequenciais e divergentes; contraste e WCAG 2.2; redundância além da cor; Gestalt; hierarquia; carga cognitiva; grid, zonas e responsividade; filtros, parâmetros, drill-down e estados; redesign, teste do relance e auditoria. Storytelling, Big Idea, pitch, exercícios, respostas e teleprompter permanecem fora deste capítulo e nos destinos próprios.

## Capítulo 8 concluído

Integra `08_storytelling.tex`, a antiga Semana 8, o caso educacional de `09_real_cases.tex` e conceitos selecionados da semana especial. Um caso de permanência estudantil organiza exploração versus explicação, público e decisão, Big Idea contestável, cadeia problema→evidência→decisão, storyboard, anotação, ordem de leitura, incerteza, causalidade, ética e interpretação contextualizada em padrão ENADE. Fundamentos, estatística, SOR/SOT/SPEC, qualidade, gráficos, acessibilidade, cor e layout são retomados dentro da decisão. Exercícios, respostas, teleprompter, tutoriais específicos e rubrica de projeto permanecem fora do livro e em seus destinos próprios.

## Capítulo 9 concluído

Abre a Unidade II com um fluxo completo linguagem natural→intenção→métrica/dimensão→camada semântica→SQL restrito→execução→validação→resposta/visual. O caso de receita regional desenvolve ambiguidade, grão, joins, segurança, cálculo manual, invariantes, reparo seguro, tokens, contexto, custo, alucinação e condição de recusa. Diferencia copiloto, analytics conversacional e BI agentic e compara Tableau/Fabric, Amazon Quick (incluindo páginas legadas QuickSight), Looker com Gemini, Databricks AI/BI/Genie Agents e Python/Streamlit por responsabilidades, sem catálogo de marcas. Integra `07_insights.tex`, semana especial, Phebe e analytics agentic governado; exercícios e respostas permanecem fora do livro.

## Refinamento da Unidade II — 21/10/2026

| Frente | Cobertura refinada | Estado |
|---|---|---|
| Cap. 9 | Automação clássica de AED, Auto-EDA, limites de LLM, papéis de mensagens, arquitetura de aplicação em camadas, segredo/API, evidência e storytelling | Validador aprovado: 6.513 palavras; PDF individual A4 de 18 páginas recompilado; bibliografia inclui fundamentos e API |
| Cap. 10 | Linguagem natural, intenção tipada, Text-to-SQL, NL2Vis, camada semântica, grão, métricas, SQL restrito, conta comparativa e storytelling sustentado | Validador aprovado: 5.124 palavras; PDF individual A4 de 14 páginas, referências em página própria; figura, cálculo e código conferidos |
| Cap. 11 | GenBI/BI agentic; comparação de mercado datada; teste pareado; avaliação de fornecedores; governança semântica e storytelling | Validador aprovado: 5.229 palavras; PDF individual A4 de 14 páginas; bibliografia atualizada para Quick/QuickSight e Genie Agents; sem Overfull |
| Cap. 12 | Arquitetura Streamlit em camadas; Responses API; mensagem e evidência estruturada; segredo, validação, estado, cache e falhas | Validador aprovado: 5.031 palavras; PDF individual A4 de 13 páginas, referências primárias; protótipo Python criado |
| Cap. 13 | RAG lexical/vetorial/híbrido, GraphRAG, SQL determinístico, Agentic RAG, recall/precision@k, segurança e parada | Validador aprovado: 5.025 palavras; PDF individual A4 de 13 páginas, referências RAG/GraphRAG/ferramentas |
| Cap. 14 | Agentic BI, suíte representativa, funil com denominadores, auditoria por camada, gates, segurança e operação | Validador aprovado: 5.044 palavras; PDF individual A4 de 14 páginas, referências para avaliação e governança |
| Dinâmicas | Quatro cenários simples, um responsável por cada um dos quatro estudantes: cantina, métrica ambígua, narrativa com evidência e resposta/esclarecimento/recusa. Código apresentado na aula seguinte: 15→22/10, 22→29/10, 29/10→05/11, 05→19/11 após EXPOFACOL. | PDF aluno 2 páginas; chave professor 3 páginas. Pedidos, dados pequenos, respostas e código de referência foram conferidos visualmente. |
| Avaliações | IDs de caderno preservados; cabeçalhos genéricos contextualizados; cobertura/dificuldade registrada | Seis PDFs A/B da II Unidade, Segunda Chamada e Final recompilados; validador confirma 5 instrumentos, 10 versões, 40 IDs únicos e Final <= Segunda Chamada. A Segunda Chamada tem dificuldade média 3,68/5 e a Final 1,52/5. Integridade do caderno público concluída: 40 itens reservados substituídos por itens públicos `-S1`, com gabaritos privados e mapas. |

Os capítulos 9–14 passam pelo validador local de profundidade com piso de 5.000 palavras e mínimo de cinco parágrafos por subdivisão. Os wrappers individuais foram compilados com Tectonic usando o bundle/format locais; seus logs não apresentam Overfull, controle indefinido, caractere ausente ou erro fatal. O livro completo recompilado tem 251 páginas A4. Permanecem avisos Underfull de paginação e âncoras duplicadas de PDFs integrados herdadas de seções anteriores; não impedem a geração. O validador das provas aprova IDs/versões; a auditoria manual complementar agora confirma também as 40 substituições públicas. A média de dificuldade é indicativa e não garante, isoladamente, o nível pretendido em cada item.

**Nota de calendário:** 12/11 é semana institucional da EXPOFACOL e não representa encontro regular. O encontro de 29/10 ensina ecossistemas GenBI e recupera fundamentos do Cap. 13 por pré-leitura; em 19/11 o quarto aluno demonstra seu código e a turma integra os incrementos, enquanto estuda avaliação Agentic BI. São quatro cenários para os quatro alunos, sem cenário novo em 19/11.
