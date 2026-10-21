# Revisão profunda de capítulos

Usar este modo quando o professor pedir para refazer, aprofundar, elevar ao padrão de capítulos-modelo ou revisar vários capítulos de IA, AED ou Tópicos. Ele complementa `capitulo-progressivo.md`; não substitui as regras gerais da Trilha.

## Estado, fontes e escopo

1. Ler o Memory Bank e os arquivos obrigatórios do repositório antes de editar.
2. Preservar capítulos e fontes fora do escopo declarado. Registrar explicitamente artefatos que não podem ser tocados.
3. Escolher como referência os dois capítulos fortes indicados pelo professor ou, na ausência de indicação, os dois capítulos adjacentes mais bem validados. Comparar arco narrativo, contas, recursos visuais, densidade, caixas e transições; contagens são diagnóstico, não quota mecânica.
4. Inventariar por conceito as fontes preservadas do semestre anterior, a matriz de cobertura, o caderno de exercícios e a rastreabilidade das avaliações. Não transportar teleprompter, gabarito, contradição ou código que antecipe a matemática.
5. Se um item reservado ou aplicado ainda aparecer em material público, registrar falha de integridade e tratá-la como gate separado. No livro, ensinar a mesma competência com contexto, dados e valores isomórficos; nunca copiar enunciado, figura, alternativas ou solução literal de item reservado.

## Papéis multiagente

Quando a revisão profunda for solicitada e delegação estiver disponível, usar pelo menos dois olhares independentes além da síntese do agente principal:

- **auditor de paridade:** compara o capítulo-alvo aos capítulos-modelo e lista lacunas por seção;
- **auditor matemático e visual:** recalcula exemplos, verifica símbolos, unidades, tabelas, figuras, rótulos e coerência entre texto e resultado;
- **autor por arquivo:** em revisões de vários capítulos, pode editar um capítulo isolado sem tocar arquivos compartilhados, evitando colisões;
- **revisor final:** relê os PDFs e aplica a rubrica depois das correções, sem receber apenas o parecer anterior como resposta esperada.

O agente principal lê as instruções da skill, decide a arquitetura comum, integra os pareceres, revisa os diffs e executa os gates finais. Agentes não atualizam simultaneamente Memory Bank, skill, matriz compartilhada ou `main.tex`.

## Contrato pedagógico da reescrita

Cada conceito central precisa completar o arco necessidade → intuição → fórmula/representação → símbolos e unidades → dados organizados → substituição → conta ou construção passo a passo → interpretação → segundo exemplo → limite/contraexemplo → decisão → ponte.

O caso condutor deve evoluir entre as seções. Um capítulo matemático não pode apenas citar uma fórmula em linha corrida: as equações centrais ficam visualmente isoladas, têm cada símbolo explicado e reaparecem com valores substituídos. Figuras e tabelas precisam ser citadas antes, carregar evidência e ser interpretadas depois. Código entra somente após a matemática e reproduz um exemplo já verificável à mão.

Para modelos supervisionados, manter separadas três ações: aprender parâmetros, produzir previsão e avaliar generalização. Explicar importância de variável como pergunta, não como ranking automático: coeficiente bruto, coeficiente padronizado, impacto numa faixa substantiva, ablação/permutação e efeito causal respondem a questões diferentes.

### Regressão

- Resolver regressão simples integralmente, incluindo reta, resíduos, SSE, coeficientes, previsão e diagnóstico visual.
- Resolver pelo menos um caso de regressão múltipla à mão. Mostrar a matriz ou uma estrutura balanceada que permita obter os coeficientes sem saltos, interpretar variável contínua e dummy e comparar contribuições em unidades declaradas.
- Incluir gráfico dos dados e da reta ou plano, resíduos e efeito de mais de uma variável. Corrigir todas as tabelas por recálculo independente.
- Tratar MAE, MSE, RMSE e $R^2$ com unidade, baseline, consequência e limite; $R^2$ pode ser negativo fora da amostra.

### Classificação

- Construir explicitamente o alvo binário a partir de uma regra de negócio ou corte estatístico, declarando classe positiva, horizonte, empate e instante de disponibilidade do rótulo.
- Distinguir indicador-alvo de dummy preditora e declarar categoria de referência.
- Mostrar honestamente que regressão linear pode rodar sobre 0/1, mas não garante probabilidade em $[0,1]$ nem variância adequada; não afirmar que sempre erra mais.
- Desenvolver escore linear, logit, sigmoide, probabilidade, limiar, classe, log-loss e odds ratio com contas pequenas. Em caso multivariado, percorrer uma linha inteira até a decisão e interpretar quais variáveis mais alteram a previsão naquele contexto.

### Métricas

- Começar pelos resíduos de regressão e calcular MAE, MSE, RMSE e $R^2$ sobre o mesmo conjunto, incluindo um contraexemplo que diferencie erro típico, pico e baseline.
- Desenhar a matriz de confusão $2\times2$ com eixos **Real** e **Predito**, rótulos 0/1 e células VP, FN, FP e VN. Construir as células a partir de casos antes de aplicar fórmulas.
- Destacar acurácia, precisão, recall/sensibilidade, especificidade e F1; explicar cada denominador em linguagem natural. Usar vários contextos para contrastar precisão e recall.
- Construir ROC a partir de escores ordenados e limiares, com tabela de TPR/FPR e curva em degraus. Calcular AUC por área/trapézios e por pares quando o conjunto pequeno permitir; deixar claro que AUC mede ranking, não acurácia nem calibração.

## Rubrica de paridade

Pontuar cada critério de 0 a 2 e exigir pelo menos 21/24, sem zero em correção matemática, conta central, recurso visual ou código após a matemática:

1. caso condutor e necessidade profissional;
2. progressão e pré-requisitos sem repetição longa;
3. fórmulas/representações com símbolos e unidades;
4. conta ou construção central integral;
5. segundo exemplo e contraexemplo;
6. interpretação, decisão e limite;
7. figuras/tabelas funcionais, citadas e interpretadas;
8. importância de variáveis ou critérios de escolha corretamente delimitados;
9. competências avaliadas ensinadas sem expor itens reservados;
10. código somente depois da compreensão manual;
11. correção aritmética, notacional e coerência texto–figura–tabela;
12. densidade de três horas e cinco parágrafos substantivos por subdivisão.

Após a primeira compilação, o revisor final aplica a rubrica. Se o capítulo não atingir o gate, corrigir e repetir auditoria e compilação; não declarar paridade com base apenas em contagem de palavras.

## Gates de entrega

1. Executar `scripts/validate_chapter.py` em cada capítulo alterado.
2. Compilar cada wrapper individual e depois `livro/main.tex`.
3. Buscar erro fatal, referência indefinida, caractere ausente e `Overfull \\hbox` nos logs.
4. Inspecionar visualmente páginas com cada figura, tabela larga, sequência de equações, código e transição entre capítulos.
5. Conferir que arquivos fora do escopo permanecem inalterados.
6. Atualizar a matriz de cobertura e o Memory Bank com palavras, seções, figuras, equações centrais, PDFs, resultado dos logs, auditoria e pendências de integridade.
