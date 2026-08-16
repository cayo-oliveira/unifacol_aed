# PROVA II CHAMADA — ANÁLISE EXPLORATÓRIA DE DADOS 2026.1

Credenciada e Autorizada pelo MEC, Portaria n.º 644 de 28 de março de 2001 – Publicado no D.O.U. em 02/04/2001  
Curso de Sistemas de Informação – Reconhecido pela Portaria nº 286 de 21/12/2012

---

**Disciplina:** Análise Exploratória de Dados | **Curso:** Sistemas de Informação  
**Período:** 2026.1 | **Data:** ___/___/2026  
**Prof(a).** Cayo Medeiros | **Aluno(a):** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

### Instruções

- O aluno dispõe de **2 horas** para realizar esta prova.
- A interpretação cabe exclusivamente ao aluno. Dirija-se ao professor apenas em caso de texto ilegível.
- Manter desligado e guardado aparelho celular ou qualquer dispositivo eletrônico.
- Proibido solicitar material por empréstimo. Guardar todo material didático sob a cadeira.
- Serão consideradas apenas as respostas escritas com caneta preta ou azul.
- Cada questão vale **1,0 ponto**. Total: **10,0 pontos**.
- **Esta prova cobre todo o conteúdo do semestre.**

---

## Questões

---

### Questão 1 (1,0 ponto) — Qualidade de Dados

Um dataset de transações bancárias possui 50.000 registros. A coluna `valor_transacao` contém: 47.500 valores numéricos válidos, 1.200 valores como "R$ 150,00" (string), 800 valores NULL, e 500 valores negativos (estornos legítimos). A coluna `cpf_cliente` tem 3.200 valores duplicados, sendo que cada cliente pode ter múltiplas transações.

Quantos registros apresentam **problemas reais de qualidade** que precisam de tratamento (excluindo casos válidos como estornos e múltiplas transações do mesmo cliente)?

A) 2.000 registros (1.200 com tipo inconsistente + 800 NULL)

B) 52.700 registros (todos os valores não-numéricos e duplicados)

C) 800 registros (apenas os NULL)

D) 5.700 registros (1.200 + 800 + 500 + 3.200)

E) 1.200 registros (apenas os com tipo inconsistente)

---

### Questão 2 (1,0 ponto) — Medidas de Tendência Central

Uma distribuidora analisou o tempo de entrega (em horas) de 9 pedidos: 2, 3, 3, 4, 4, 4, 5, 6, 24. O gestor quer reportar o "tempo típico" de entrega. Considere: Média = 55/9 ≈ 6,11h; Mediana = 4h (5º valor ordenado); Moda = 4h.

Qual medida é **mais apropriada** e por quê?

A) Mediana ou Moda (4h), porque a distribuição tem um outlier (24h) que distorce a média; 8 dos 9 pedidos levaram no máximo 6h

B) Média (6,11h), porque considera todos os valores e é sempre a melhor medida

C) Moda (4h), porque é o único valor que aparece 3 vezes e isso a torna mais precisa matematicamente

D) Média (6,11h), porque outliers devem ser incluídos em todas as análises sem exceção

E) Um valor intermediário (5h), porque é a média entre a média e a mediana

---

### Questão 3 (1,0 ponto) — Desvio-Padrão e Variabilidade

Dois processos de produção foram comparados:

| Processo | Média (kg) | Desvio-Padrão (kg) | CV (Coef. Variação) |
|----------|------------|--------------------|--------------------|
| A | 100 | 5 | 5% |
| B | 50 | 5 | 10% |

Qual processo apresenta **maior consistência relativa** (menos variável proporcionalmente à sua média)?

A) Processo A, porque seu coeficiente de variação (5%) é menor que o do Processo B (10%), indicando menor variabilidade relativa

B) Ambos são igualmente consistentes porque têm o mesmo desvio-padrão (5 kg)

C) Processo B, porque produz menos quantidade

D) Não é possível comparar porque as médias são diferentes

E) Processo B, porque 50 kg é mais fácil de controlar que 100 kg

---

### Questão 4 (1,0 ponto) — Boxplot e Outliers

Para um conjunto de dados: Q1 = 20, Q3 = 40, IQR = 20. Os limites para detecção de outliers pelo método 1,5×IQR são:

- Limite inferior = Q1 − 1,5 × IQR = ?
- Limite superior = Q3 + 1,5 × IQR = ?

Um valor de **-15** e um valor de **75** são classificados como:

A) Limite inferior = -10, Limite superior = 70; -15 é outlier (abaixo de -10), 75 é outlier (acima de 70)

B) Limite inferior = 0, Limite superior = 60; ambos são outliers

C) Limite inferior = -10, Limite superior = 70; apenas 75 é outlier

D) Limite inferior = 20, Limite superior = 40; ambos são outliers

E) Limite inferior = -10, Limite superior = 70; nenhum é outlier

---

### Questão 5 (1,0 ponto) — Dados Ausentes

Um dataset de pesquisa de satisfação tem 10.000 respostas. A variável `renda_familiar` tem 25% de valores ausentes. A analista suspeita que pessoas de alta renda evitam responder essa pergunta (missing não-aleatório - MNAR).

Qual estratégia é **mais problemática** neste cenário?

A) Imputar pela média, porque se o missing é MNAR (alta renda não responde), a média dos que responderam subestima a renda real, gerando viés sistemático

B) Criar uma categoria "Não informado" para análise descritiva

C) Documentar o percentual de missing no relatório

D) Analisar se há diferenças entre respondentes e não-respondentes em outras variáveis

E) Manter os valores ausentes e usar técnicas que lidam com missing

---

### Questão 6 (1,0 ponto) — Correlação

Uma matriz de correlação mostra:

| | X | Y | Z |
|--|---|---|---|
| X | 1,00 | 0,92 | 0,88 |
| Y | 0,92 | 1,00 | 0,95 |
| Z | 0,88 | 0,95 | 1,00 |

Um analista conclui: "X causa Y, que por sua vez causa Z". Esta conclusão está:

A) Incorreta, porque correlação (mesmo alta) não implica causalidade; as três variáveis podem ser causadas por uma quarta variável não observada, ou a relação causal pode ser inversa

B) Correta, porque correlações acima de 0,90 sempre indicam causalidade

C) Correta, porque Y tem a maior correlação com Z

D) Incorreta apenas porque as correlações não são exatamente 1,00

E) Correta, porque a ordem X→Y→Z é a única possível matematicamente

---

### Questão 7 (1,0 ponto) — Variáveis Categóricas

Uma loja analisou 1.000 vendas por forma de pagamento:

| Forma Pagamento | Vendas | % Total | Ticket Médio |
|-----------------|--------|---------|--------------|
| PIX | 450 | 45% | R$ 85 |
| Crédito | 320 | 32% | R$ 210 |
| Débito | 180 | 18% | R$ 95 |
| Dinheiro | 50 | 5% | R$ 45 |

O gerente afirma: "PIX gera mais receita porque é a forma mais usada". Esta afirmação está:

A) Incorreta sem análise adicional; PIX tem mais volume (45%), mas Crédito pode gerar mais receita total (320 × R$210 = R$67.200) comparado ao PIX (450 × R$85 = R$38.250)

B) Correta, porque 45% é maior que 32%

C) Correta, porque qualquer produto com maior volume sempre gera maior receita

D) Incorreta porque dinheiro é a forma mais segura

E) Correta, porque PIX não tem taxa de cartão

---

### Questão 8 (1,0 ponto) — Big Idea

Uma analista precisa apresentar resultados sobre churn (cancelamento) de clientes. Ela tem os seguintes achados:

- Churn geral: 18% ao ano
- Clientes sem contato nos últimos 90 dias: 45% de churn
- Clientes com suporte recente: 8% de churn
- Custo de aquisição de novo cliente: R$ 500

Qual alternativa representa a **melhor Big Idea**?

A) "Devemos implementar contato proativo a cada 60 dias para clientes inativos, pois isso pode reduzir o churn de 45% para aproximadamente 8%, economizando R$ 185 mil/ano em custos de aquisição"

B) "O churn é de 18%"

C) "Analisamos 50.000 clientes durante 12 meses"

D) "Clientes cancelam por vários motivos"

E) "O gráfico mostra tendência de cancelamento"

---

### Questão 9 (1,0 ponto) — Design de Dashboard

Um dashboard executivo precisa mostrar se a meta de vendas foi atingida. Qual título é **mais eficaz** segundo o princípio "Teste do Relance"?

A) "Meta Superada: Vendas de R$ 2,3M excedem meta de R$ 2M em 15%"

B) "Dashboard de Vendas Q4"

C) "Gráfico 1: Vendas"

D) "Análise Trimestral"

E) "Dados de Performance"

---

### Questão 10 (1,0 ponto) — Tableau Interativo

Um usuário quer que, ao clicar em uma barra de um gráfico de vendas por região, outro gráfico no mesmo dashboard mostre automaticamente os detalhes daquela região. No Tableau, isso é feito usando:

A) Ação de Filtro (Filter Action), que permite que uma seleção em uma visualização filtre outra visualização no mesmo dashboard

B) Exportar para PDF e circular a região manualmente

C) Criar 50 dashboards separados, um para cada região

D) Usar apenas parâmetros sem nenhuma ação

E) Formatação condicional de células

---

## GABARITO (uso exclusivo do professor)

| Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 |
|----|----|----|----|----|----|----|----|----|-----|
| A | A | A | A | A | A | A | A | A | A |

---

## Distribuição de Conteúdo

| Questão | Tópico | Semana |
|---------|--------|--------|
| Q1 | ETL e qualidade de dados (tipos, ausências, duplicadas) | 01-02 |
| Q2 | Medidas de tendência central (média, mediana, moda) + outliers | 03 |
| Q3 | Dispersão: desvio-padrão, coeficiente de variação | 04 |
| Q4 | Boxplot, IQR, limites de outliers | 04-05 |
| Q5 | Dados ausentes (MCAR, MAR, MNAR) e estratégias | 05 |
| Q6 | Correlação ≠ causalidade, scatter plot | 06 |
| Q7 | Variáveis categóricas: frequência, proporções | 07 |
| Q8 | Storytelling: Big Idea + pergunta de decisão | 08 |
| Q9 | Design: Teste do Relance, hierarquia visual | 09 |
| Q10 | Tableau interativo: filtros, parâmetros, ações | 10 |

---

## Notas para o Professor

### Q1 - Qualidade
- Problemas reais: 1.200 (tipo) + 800 (NULL) = 2.000
- NÃO são problemas: estornos (válidos), duplicatas de CPF (múltiplas transações são esperadas)

### Q4 - Limites de Outlier
- LI = 20 − 1,5 × 20 = 20 − 30 = -10
- LS = 40 + 1,5 × 20 = 40 + 30 = 70
- -15 < -10 → outlier inferior
- 75 > 70 → outlier superior

### Q7 - Receita Total
- PIX: 450 × 85 = R$ 38.250
- Crédito: 320 × 210 = R$ 67.200
- Débito: 180 × 95 = R$ 17.100
- Dinheiro: 50 × 45 = R$ 2.250
- **Crédito gera mais receita** apesar de menor volume!
