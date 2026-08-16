# Padrão progressivo do livro-aula

Usar este padrão em capítulos conceituais e matemáticos de AED, IA e Tópicos. A referência empírica são os Capítulos 2 e 3 compartilhados de AED/IA e as fontes preservadas de 2026.1.

## Antes de escrever

1. Inventariar o que os capítulos anteriores já ensinaram, com seção e exemplo.
2. Mapear as fontes 2026.1 por conceito, fórmula, exemplo, figura e explicação aproveitável.
3. Definir o conhecimento realmente novo e a pergunta profissional que sustenta o capítulo.
4. Atualizar plano, matriz de cobertura e título quando houver mudança de progressão.
5. Proibir revisão longa de pré-requisitos: retomar em um parágrafo ou caixa azul e avançar.

## Unidade narrativa de cada conceito

Cada conceito importante segue um arco completo, sem virar uma lista de fórmulas:

1. **Necessidade e origem:** qual problema tornou a ideia necessária e para que ela serve.
2. **Intuição:** explicar o mecanismo em linguagem comum antes da notação.
3. **Fórmula:** apresentar isoladamente apenas quando o leitor já sabe a pergunta respondida.
4. **Símbolos e unidades:** nomear termo por termo, incluindo denominador, índice, domínio e unidade.
5. **Dados organizados:** usar conjunto pequeno, tabela curta ou figura citada explicitamente.
6. **Substituição:** trocar símbolos pelos valores do caso sem saltar operações.
7. **Conta linha a linha:** mostrar resultados intermediários, arredondamento e unidade.
8. **Leitura:** dizer em português simples o que o número significa e o que não significa.
9. **Segundo exemplo:** variar valores, contexto ou estrutura para testar transferência.
10. **Contraexemplo ou limite:** mostrar quando a técnica, fórmula ou interpretação deixa de servir.
11. **Decisão:** conectar o resultado a uma escolha verificável no caso.
12. **Ponte:** terminar explicando por que o próximo conceito se tornou necessário.

## Storytelling e recursos visuais

- Sustentar o capítulo em um caso principal que evolui; usar casos secundários somente para contraste.
- Alternar prosa, fórmula, tabela/figura e interpretação. Não empilhar caixas, tabelas ou equações.
- Citar toda tabela e figura antes de mostrá-la e interpretá-la depois. Um visual precisa reduzir esforço cognitivo ou carregar evidência.
- Incluir exemplos e contraexemplos suficientes para que o capítulo sustente três horas, sem deslocar exercícios formais para o livro.
- Usar caixa azul para decompor ponto difícil e laranja para sintetizar a relação construída, não para repetir a frase anterior.

## Regressão, classificação e modelos

- Regressão começa na ponte já construída `Cov(X,Y)/Var(X)`, sem reensinar média, variância ou covariância.
- Construir primeiro reta, resíduo, soma de quadrados, coeficientes e previsão manual; depois ampliar para múltiplas variáveis e somente então reproduzir em código.
- Classificação começa pela natureza do alvo e pelo custo do erro; construir escore linear, função logística, probabilidade, limiar, classe, odds e odds ratio com contas pequenas antes do código.
- Métricas começam em decisões e custos: montar matriz de confusão, calcular cada célula e denominador, interpretar trade-offs e só depois tratar ROC/AUC. Para regressão, derivar resíduos, MAE, MSE, RMSE e R² sobre o mesmo caso.
- Distinguir aprender parâmetros, produzir previsão e avaliar generalização. Código confirma o raciocínio; não o substitui.

## LLMs e capítulos conceituais

Aplicar o mesmo arco mesmo quando não houver uma fórmula central: necessidade → mecanismo → representação → exemplo pequeno → artefato/fluxo → resultado → limite → decisão. Para tokens, embeddings, atenção, custos e avaliação, abrir contas pequenas. Para mensagens, RAG, ferramentas, agentes e skills, mostrar estruturas, estados, contratos e falhas verificáveis.

## Uso de 2026.1

Preservar explicações, derivações, exemplos e conexões que funcionem bem, reescrevendo-os no storytelling atual. Conferir convenções matemáticas e corrigir contradições antes de incorporar. Não transportar exercícios, gabaritos, teleprompter, calendário antigo, código antes da matemática ou repetição de conteúdo já ensinado.

## Gate de aceite

- O início declara o novo problema e não repete um capítulo anterior.
- Cada conceito central completa o arco necessidade → decisão.
- Fórmulas têm símbolos, unidades, substituição e conta reproduzível.
- Há segundo exemplo e limite/contraexemplo nos conceitos de maior risco.
- Figuras e tabelas estão citadas e interpretadas.
- O capítulo possui densidade compatível com três horas e mantém cinco parágrafos por subdivisão.
- Plano, capítulo e matriz de cobertura contam a mesma progressão.
