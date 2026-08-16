# Estrutura editorial dos capítulos — AED 2026.2

Esta matriz é um contrato de produção, não substitui os capítulos. Cada capítulo final deverá sustentar 180 minutos, alcançar o piso de profundidade do skill e incorporar as fontes de 2026.1 indicadas na matriz de cobertura.

| Cap. | Título | Núcleo conceitual | Demonstração / caso | Produto de leitura |
|---:|---|---|---|---|
| 1 | Ver, perguntar e decidir: dataviz com IA | fundamentos, exploratória × explanativa, cadeia analítica, percepção e panorama GenBI | leitura guiada de Phebe e de analytics agentic governado | mapa do semestre e critérios para contestar resposta automática |
| 2 | Antes da média: que dado representa o problema? | população, amostra, observação, variável, tipo, unidade, granularidade, qualidade | dados acadêmicos em granularidades incompatíveis | dicionário e contrato da pergunta analítica |
| 3 | Centro não é história completa | frequência, proporção, média, mediana, moda, quartis, percentis e ponderação | tempos de atendimento e notas com assimetria | contas à mão → planilha/Python → interpretação |
| 4 | Variabilidade, distribuição e incerteza | amplitude, variância amostral, desvio-padrão, IQR, histograma, ausência e outliers | operação com picos, caudas e dados faltantes | diagnóstico com decisão de tratamento justificada |
| 5 | Da fonte ao visual: arquitetura de dados para AED | OLTP/OLAP, ingestão, SOR/SOT/SPEC, lake, warehouse, lakehouse, modelo dimensional/semântico, catálogo, linhagem e governança | arquitetura de vendas multicanal | desenho rastreável e pontos de controle |
| 6 | O gráfico como operação perceptiva | perguntas de comparação, distribuição, composição e relação; posição, comprimento, área, escala e eixos | mesmo conjunto representado por gráficos adequados e inadequados | escolha de visual baseada na tarefa |
| 7 | Cor e espaço também argumentam | cor sequencial/divergente/categórica, contraste, daltonismo, hierarquia, Gestalt, carga cognitiva, grid e zonas de dashboard | redesign de painel saturado | antes/depois com teste do relance e acessibilidade |
| 8 | Da exploração à história verificável | Big Idea, público, contexto, storyboard, anotação, incerteza e ação | evasão estudantil ou operação de atendimento | narrativa com evidência e revisão ENADE |
| 9 | IA como assistente do ciclo analítico | geração de código, resumo, hipótese, limites, prompt, contexto, validação e rastreabilidade | EDA manual comparada à assistida | protocolo de verificação com casos de recusa |
| 10 | Da pergunta em português à consulta e ao visual | Text-to-SQL, NL2Vis, schema linking, camada semântica, ambiguidade, execução e correção ponta a ponta | pergunta ambígua sobre receita e margem | trilha auditável pergunta→SQL→dados→visual |
| 11 | BI com copilotos e agentes | Tableau, Power BI/Fabric, Quick Sight, Looker/Looker Studio, Databricks Genie; identidade, RLS, semântica, auditoria | mesma pergunta em arquiteturas de plataforma | matriz de comparação sem torcida por ferramenta |
| 12 | Dashboard como aplicação: Streamlit + Llama | estado, componentes, cache, conexão, modelo local/gratuito, saída estruturada, validação e publicação | protótipo conversacional reproduzível | aplicação com resposta, visual, fonte e aviso de limite |
| 13 | Quando um agente vira equipe | orquestrador, ferramenta, memória, multiagente, planejamento, observabilidade, custo e fallback | Phebe reconstituído como fluxo agentic governado | diagrama de responsabilidades e política de recusa |
| 14 | Como saber se a GenBI está certa? | conjuntos de teste, execução válida × resposta correta, groundedness, segurança, privacidade, latência, custo e revisão humana | auditoria de respostas conflitantes | checklist de decisão contestável e síntese do curso |

## Molde interno obrigatório

Cada capítulo deverá desenvolver, com pelo menos cinco parágrafos substantivos por título:

1. uma cena real e a decisão em risco;
2. mapa do encontro e resultados de aprendizagem;
3. conceitos em sequência causal, com vocabulário definido no primeiro uso;
4. exemplo numérico ou material, seguido de interpretação;
5. representação visual citada no texto;
6. demonstração manual antes da ferramenta, quando aplicável;
7. demonstração em código/plataforma e verificação independente;
8. limitações, erros comuns e condições de recusa;
9. síntese laranja e explicações azuis apenas onde reduzirem esforço cognitivo;
10. fechamento que conecta a próxima semana.

## Densidade planejada

O Capítulo 1 atual possui aproximadamente 11 mil palavras no arquivo LaTeX e 45 páginas porque inclui dois artigos completos em apêndice. Os demais capítulos devem buscar densidade de prosa comparável, mas não precisam reproduzir o número bruto de páginas dos apêndices. Para evitar capítulos artificialmente inflados, comparar separadamente: palavras de prosa, páginas do conteúdo autoral, quantidade de exemplos resolvidos, tempo de demonstração e tempo de discussão.
