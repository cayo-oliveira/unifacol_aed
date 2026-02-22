# EXERCÍCIO DE APRENDIZAGEM E APROVEITAMENTO — AED 2026.1

Credenciada e Autorizada pelo MEC, Portaria n.º 644 de 28 de março de 2001 – Publicado no D.O.U. em 02/04/2001  
Curso de Sistemas de Informação – Reconhecido pela Portaria nº 286 de 21/12/2012

---

**Disciplina:** Análise Exploratória de Dados | **Curso:** Sistemas de Informação  
**Período:** 2026.1 | **Data:** ___/___/2026  
**Prof(a).** Cayo Medeiros | **Aluno(a):** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

### Instruções

- O aluno dispõe de **1 hora e 30 minutos** para realizar este exercício de aprendizagem e aproveitamento.
- A interpretação cabe exclusivamente ao aluno. Dirija-se ao professor apenas em caso de texto ilegível.
- Manter desligado e guardado aparelho celular ou qualquer dispositivo eletrônico.
- Proibido solicitar material por empréstimo. Guardar todo material didático sob a cadeira.
- Serão consideradas apenas as respostas escritas com caneta preta ou azul.
- Cada questão vale **1,0 ponto**. Total: **10,0 pontos**.

---

## Questões

---

### Questão 1 (1,0 ponto) — Dados Retangulares e Dicionário de Dados

Uma analista recebeu um arquivo CSV com informações de vendas contendo 5.000 registros e 12 colunas. Antes de iniciar qualquer análise, ela precisa documentar o significado de cada coluna, seus tipos e valores esperados.

Qual alternativa apresenta **corretamente** o nome do documento que a analista deve criar para essa documentação?

A) Dicionário de dados  
B) Relatório de outliers  
C) Dashboard executivo  
D) Matriz de correlação  
E) Histograma de frequências

---

### Questão 2 (1,0 ponto) — Qualidade de Dados

Um cientista de dados está avaliando a qualidade de um dataset de clientes e encontrou os seguintes problemas: a coluna "idade" contém valores como "25", "trinta" e "NULL"; a coluna "CPF" tem 150 registros repetidos; e a coluna "email" está vazia em 30% dos casos.

Qual alternativa apresenta **corretamente** os três tipos de problemas de qualidade identificados, respectivamente?

A) Tipos inconsistentes, dados duplicados e dados ausentes  
B) Outliers, dados duplicados e dados ausentes  
C) Tipos inconsistentes, outliers e dados duplicados  
D) Dados ausentes, tipos inconsistentes e outliers  
E) Dados duplicados, dados ausentes e tipos inconsistentes

---

### Questão 3 (1,0 ponto) — Medidas de Tendência Central

Um professor analisou as notas de uma turma de 7 alunos em uma prova: 4, 5, 6, 6, 7, 8, 10. Ele precisa escolher a medida que melhor representa o valor "mais típico" da turma, considerando que não há outliers extremos.

Qual alternativa apresenta **corretamente** os valores da média, mediana e moda dessa distribuição?

A) Média ≈ 6,57; Mediana = 6; Moda = 6  
B) Média = 6; Mediana ≈ 6,57; Moda = 6  
C) Média = 6; Mediana = 6; Moda ≈ 6,57  
D) Média ≈ 6,57; Mediana = 7; Moda = 5  
E) Média = 7; Mediana = 6; Moda = 6

---

### Questão 4 (1,0 ponto) — Medidas de Dispersão

Uma empresa comparou os salários de dois departamentos e obteve os seguintes resultados: Departamento A tem média salarial de R$ 5.000 e desvio-padrão de R$ 500; Departamento B tem média salarial de R$ 5.000 e desvio-padrão de R$ 2.000.

Qual alternativa apresenta **corretamente** a interpretação dessa comparação?

A) O Departamento B tem salários mais heterogêneos (maior variabilidade) que o Departamento A  
B) O Departamento A tem salários mais heterogêneos (maior variabilidade) que o Departamento B  
C) Ambos os departamentos têm a mesma variabilidade salarial  
D) O desvio-padrão não permite comparar variabilidade entre grupos  
E) O Departamento B tem média salarial maior que o Departamento A

---

### Questão 5 (1,0 ponto) — Boxplot e Outliers

Um analista construiu um boxplot para visualizar a distribuição de preços de produtos e observou que o IQR (Intervalo Interquartil) é R$ 100, Q1 = R$ 200 e Q3 = R$ 300. Um produto com preço de R$ 500 aparece como um ponto isolado acima do "bigode" superior.

Qual alternativa apresenta **corretamente** a classificação desse produto e o limite superior do bigode?

A) Outlier; limite superior = R$ 450  
B) Valor normal; limite superior = R$ 500  
C) Outlier; limite superior = R$ 400  
D) Valor normal; limite superior = R$ 450  
E) Outlier; limite superior = R$ 300

---

### Questão 6 (1,0 ponto) — Tratamento de Dados Ausentes

Uma cientista de dados está preparando um dataset para análise e encontrou 15% de valores ausentes na coluna "renda_mensal". Ela precisa decidir como tratar esses dados antes de criar visualizações.

Qual alternativa **NÃO** representa uma estratégia válida para tratamento de dados ausentes?

A) Substituir todos os valores ausentes por zero, independentemente do contexto  
B) Imputar pela média ou mediana da coluna  
C) Remover as linhas com valores ausentes  
D) Criar uma categoria "Não informado" para análises categóricas  
E) Manter os valores ausentes e sinalizar no relatório

---

### Questão 7 (1,0 ponto) — Correlação

Um analista de marketing criou um gráfico de dispersão (scatter plot) comparando "investimento em publicidade" e "vendas mensais" e observou que os pontos formam uma tendência ascendente da esquerda para a direita. O coeficiente de correlação calculado foi r = 0,85.

Qual alternativa apresenta **corretamente** a interpretação desse resultado?

A) Há correlação positiva forte, mas isso não prova que publicidade causa aumento nas vendas  
B) A publicidade definitivamente causa aumento nas vendas  
C) Há correlação negativa forte entre as variáveis  
D) Não há relação entre as variáveis  
E) A correlação de 0,85 indica causalidade comprovada

---

### Questão 8 (1,0 ponto) — Storytelling e Big Idea

Uma analista precisa apresentar os resultados de sua análise para a diretoria. Ela decide estruturar sua apresentação usando o conceito de "Big Idea", que deve comunicar a mensagem principal de forma clara e acionável.

Qual alternativa apresenta **corretamente** um exemplo de Big Idea bem formulada?

A) "Devemos investir R$ 50 mil em treinamento de vendas no próximo trimestre, pois nossa análise mostra que vendedores treinados têm 40% mais conversões"  
B) "Os dados mostram muitas informações interessantes sobre vendas"  
C) "A média de vendas é R$ 10.000 por mês"  
D) "Foram analisados 5.000 registros de vendas no período"  
E) "O gráfico de barras mostra a distribuição por região"

---

### Questão 9 (1,0 ponto) — Design de Dashboards

Um designer de informação está criando um dashboard executivo e precisa garantir que a mensagem principal seja compreendida rapidamente. Ele decide aplicar o "Teste do Relance" e princípios de hierarquia visual.

Qual alternativa apresenta **corretamente** as práticas recomendadas para um dashboard eficaz?

A) Títulos que comunicam a mensagem (não apenas descrevem), uso estratégico de cor para destaque e espaço em branco para organização  
B) Usar todas as cores disponíveis para tornar o dashboard mais atrativo  
C) Incluir o máximo de gráficos possível para mostrar todos os dados  
D) Títulos genéricos como "Gráfico 1" e "Tabela de dados"  
E) Eliminar todo espaço em branco para aproveitar melhor a tela

---

### Questão 10 (1,0 ponto) — Tableau Interativo

Uma analista está construindo um dashboard no Tableau para permitir que os usuários explorem dados de vendas por região, período e categoria de produto. Ela quer que os usuários possam filtrar os dados dinamicamente sem precisar criar múltiplas versões do dashboard.

Qual alternativa apresenta **corretamente** os recursos do Tableau que ela deve utilizar?

A) Filtros, parâmetros e ações de dashboard  
B) Apenas gráficos estáticos exportados como imagem  
C) Somente tabelas de dados sem visualizações  
D) Criar um dashboard separado para cada combinação de filtros  
E) Usar apenas o recurso de impressão do Tableau

---

## GABARITO (uso exclusivo do professor)

| Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 |
|----|----|----|----|----|----|----|----|----|-----|
| A | A | A | A | A | A | A | A | A | A |

---

## Distribuição de Conteúdo

| Questão | Tópico | Semana |
|---------|--------|--------|
| Q1 | Dados retangulares e dicionário de dados | 02 |
| Q2 | Qualidade de dados (tipos, ausências, duplicadas) | 02 |
| Q3 | Estatística descritiva I (média, mediana, moda) | 03 |
| Q4 | Estatística descritiva II (desvio-padrão, variabilidade) | 04 |
| Q5 | Boxplot, IQR e outliers | 04 |
| Q6 | Tratamento de dados ausentes | 05 |
| Q7 | Correlação vs causalidade | 06 |
| Q8 | Storytelling e Big Idea | 08 |
| Q9 | Design de informação e hierarquia visual | 09 |
| Q10 | Tableau interativo | 10 |

---

## Notas para o Professor

- **Cálculo Q3**: Média = (4+5+6+6+7+8+10)/7 = 46/7 ≈ 6,57; Mediana = 6 (valor central); Moda = 6 (mais frequente)
- **Cálculo Q5**: Limite superior = Q3 + 1,5 × IQR = 300 + 1,5 × 100 = 450; como 500 > 450, é outlier
- **Q6**: A alternativa A é incorreta porque substituir por zero sem contexto pode distorcer a análise (ex.: renda zero é diferente de renda não informada)
