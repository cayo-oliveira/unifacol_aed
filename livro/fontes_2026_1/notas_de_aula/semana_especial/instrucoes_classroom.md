# Instruções para Apresentação em Grupo — Dashboard no Tableau

**Data de apresentação:** 18/05/2026  
**Tempo por grupo:** 3 minutos de pitch + 2 minutos de perguntas  
**Entrega prévia:** link do Tableau Public publicado, enviado até **17/05/2026 às 23h59**

---

## O que vocês vão fazer

Cada grupo recebeu um dataset real e um briefing de negócio. Vocês devem:

1. **Explorar o dataset** no Tableau (ou Python para pré-processamento)
2. **Construir um dashboard narrativo** com pelo menos 4 visualizações
3. **Formular uma Big Idea** — uma frase que resume a descoberta + impacto + ação
4. **Apresentar um pitch de 3 minutos** para a turma, como se fosse para um executivo

---

## Estrutura obrigatória do dashboard

O dashboard deve seguir as **3 zonas narrativas**:

| Zona | Conteúdo |
|------|----------|
| **1. Contexto** | Big Idea + Big Number + Insight de IA (gerado por ferramenta) |
| **2. Diagnóstico** | Gráficos que explicam o problema (mínimo 3 sheets) |
| **3. Recomendação** | Call to Action claro: quem faz, o quê, até quando |

**Regras visuais:**
- Títulos de gráfico devem ser **mensagens**, não rótulos (ex.: "Eletrônicos em SP concentram 34% dos atrasos", não "Gráfico de barras por categoria")
- Cor com propósito: destaque apenas o que é mais importante
- Pelo menos **1 filtro ou parâmetro** funcionando no Tableau
- Sem gráficos de pizza com mais de 3 fatias, sem 3D, sem gradientes desnecessários

---

## Template de Big Idea

Use este modelo para formular a Big Idea do seu grupo:

> **"[Segmento ou perfil específico] [faz/tem/concentra X%] — [ação concreta] pode [resultado mensurável] até [prazo]."**

Exemplo: *"Eletrônicos em SP concentram 34% dos atrasos e puxam o review médio para 3,2 estrelas — priorizar a logística nessa categoria pode elevar o review para 4,1 e reduzir o churn de vendedores em 15%."*

---

## Template do pitch (SCR — 3 minutos)

- **Situação (30s):** contexto do negócio e do dataset
- **Complicação (60s):** qual é o problema e o que os dados mostram
- **Resolução (60s):** Big Idea + evidência + Call to Action
- **Encerramento (30s):** próximo passo concreto e responsável

---

## Briefings por grupo

---

### 🔵 Grupo 1 — E-commerce (Olist)

**Dataset:** Brazilian E-Commerce Public Dataset  
🔗 https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

**Dor de negócio:** Atrasos na entrega derrubam as avaliações dos clientes e aumentam o churn de vendedores parceiros da plataforma.

**Perguntas a responder:**
1. Em quais estados e categorias os atrasos são mais críticos e qual o impacto nas avaliações (`review_score`)?
2. Como o tempo de entrega em dias se correlaciona com a avaliação do cliente?

**Big Idea sugerida:**  
*"Eletrônicos em SP concentram 34% dos atrasos e puxam o review médio para 3,2 estrelas — priorizar logística nessa categoria pode elevar o review para 4,1 e reduzir o churn de vendedores em 15%."*

**Transformações necessárias no Tableau:**
1. Join: `orders ⋈ order_items ⋈ products ⋈ customers` (chaves: `order_id` e `product_id`)
2. Campo calculado: `delivery_delay = order_delivered_customer_date − order_estimated_delivery_date`
3. Flag: `is_late = IF delivery_delay > 0 THEN "Atrasado" ELSE "No Prazo" END`
4. Traduzir categorias com `product_category_name_translation.csv`
5. Filtrar status `canceled` e `unavailable`

**Sheets sugeridas:**
1. Big Number (% atrasados por estado/categoria)
2. Mapa coroplético: estado × % atraso
3. Barras horizontais: Top 10 categorias × % atraso, líder em laranja
4. Scatter: dias de atraso × review_score + linha de tendência
5. Linha temporal de atrasos por mês

---

### 🔷 Grupo 2 — People Analytics (IBM HR)

**Dataset:** IBM HR Analytics Employee Attrition  
🔗 https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset

**Dor de negócio:** Turnover de 28% em TI custa R$450k/ano em recrutamento e perda de conhecimento institucional.

**Perguntas a responder:**
1. Qual perfil de funcionário tem maior risco de saída e em qual departamento o problema é mais crítico?
2. Satisfação no trabalho e faixa salarial influenciam o turnover?

**Big Idea sugerida:**  
*"Funcionários de TI com menos de 2 anos e sem promoção nos últimos 3 anos têm 3× mais chance de sair — mentoria focada nesse perfil pode reduzir o turnover de 28% para 15% e economizar R$270k/ano."*

**Transformações necessárias no Tableau:**
1. `Attrition_Num = IF [Attrition]="Yes" THEN 1 ELSE 0 END`
2. `Turnover_Rate = AVG(Attrition_Num) * 100`
3. Bins de salário: Baixo < 3k / Médio 3k–7k / Alto > 7k
4. `Perfil_Risco = IF [YearsAtCompany] < 2 AND [YearsSinceLastPromotion] > 2 THEN "Alto Risco" END`

**Sheets sugeridas:**
1. Big Number (turnover TI vs meta de 15%)
2. Barras por departamento com linha de meta
3. Heatmap satisfação × faixa salarial × turnover
4. Scatter anos na empresa × turnover
5. Bullet chart por departamento

---

### 🟢 Grupo 3 — Varejo (Superstore)

**Dataset:** Sample Superstore Dataset  
🔗 https://www.kaggle.com/datasets/vivek468/superstore-dataset-final

**Dor de negócio:** Margens negativas em Tecnologia/Sul drenam R$120k/trimestre do lucro operacional.

**Perguntas a responder:**
1. Quais combinações de subcategoria e região geram prejuízo consistente?
2. Existe correlação entre o desconto aplicado e a margem negativa?

**Big Idea sugerida:**  
*"Descontos acima de 20% em Máquinas e Copiadoras na Região Sul concentram 73% do prejuízo — capear o desconto em 12% pode reverter a margem de −4,2% para +5,8%, gerando R$85k adicionais por trimestre."*

**Transformações necessárias no Tableau:**
1. `Margem_Pct = SUM([Profit]) / SUM([Sales]) * 100`
2. Bins de desconto: Sem / 0–10% / 10–20% / Acima de 20%
3. `Prejuizo = IF [Profit] < 0 THEN "Prejuízo" ELSE "Lucro" END`

**Sheets sugeridas:**
1. Big Number (margem Tech/Sul vs parâmetro de meta 8%)
2. Mapa de calor subcategoria × região
3. Scatter desconto × lucro (linhas de referência: 0 no eixo Y; 20% no eixo X)
4. Barras agrupadas por região
5. Linha trimestral de margem

---

### 🔴 Grupo 4 — Saúde Pública (Heart Disease)

**Dataset:** Heart Disease UCI Dataset  
🔗 https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset

**Dor de negócio:** Doenças cardíacas representam 38% das internações municipais (custo médio R$12k/internação).

**Perguntas a responder:**
1. Quais fatores de risco têm maior correlação com diagnóstico de doença cardíaca?
2. Qual faixa etária e perfil clínico priorizar em campanhas preventivas?

**Big Idea sugerida:**  
*"Colesterol > 240 + pressão arterial > 140 + idade > 55 anos identificam 73% dos casos de alto risco com apenas 3 variáveis — triagem preventiva focada nesse perfil pode reduzir internações em 25% e gerar R$2,1M de economia anual."*

**Transformações necessárias no Tableau:**
1. `Diagnostico = IF [target]=1 THEN "Doença" ELSE "Sem Doença" END`
2. `Sexo = IF [sex]=1 THEN "Masculino" ELSE "Feminino" END`
3. Bins de faixa etária: < 45 / 45–54 / 55–64 / 65+
4. `Perfil_Risco = IF [chol]>240 AND [trestbps]>140 AND [age]>55 THEN "Alto Risco" END`
5. `Taxa_Doenca = AVG([target]) * 100`

**Sheets sugeridas:**
1. Big Number (taxa de doença em homens > 55)
2. Barras de correlação por fator de risco
3. Heatmap faixa etária × perfil × taxa de doença
4. Scatter colesterol × pressão (cor = diagnóstico, linhas em 240 e 140)
5. Boxplot de idade por grupo diagnóstico

---

### 🟣 Grupo 5 — Fintech (Credit Card Churn)

**Dataset:** Credit Card Customers Dataset  
🔗 https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers

**Dor de negócio:** Churn do cartão Premium custa R$2,1M/ano em receita perdida de juros e anuidade.

**Perguntas a responder:**
1. Qual perfil de cliente Premium tem maior propensão ao cancelamento?
2. Frequência de uso e limite de crédito influenciam significativamente o churn?

**Big Idea sugerida:**  
*"Clientes Premium com limite < R$10k e menos de 20 transações/ano têm 4× mais chance de cancelamento — engajamento proativo focado nesse perfil pode preservar R$1,2M em receita anual."*

**Transformações necessárias no Tableau:**
1. `Churned = IF [Attrition_Flag]="Attrited Customer" THEN 1 ELSE 0 END`
2. `Churn_Rate = AVG(Churned) * 100`
3. Bins de limite: < R$10k / R$10k–30k / > R$30k
4. Bins de uso: Baixa < 20 trans / Média 20–50 / Alta > 50
5. `Perfil_Risco = IF [Total_Trans_Ct] < 20 AND [Credit_Limit] < 10000 THEN "Alto Risco" END`

**Sheets sugeridas:**
1. Big Number (churn Premium com limite < R$10k vs benchmark 8%)
2. Barras faixa de limite × churn
3. Scatter frequência × valor médio (cor = churn, linha em 20 transações)
4. Linha temporal de churn por segmento
5. Heatmap frequência × limite × taxa de churn

---

## Rubrica de Avaliação

| Critério | Peso | O que será avaliado |
|----------|------|---------------------|
| Big Idea + Call to Action | 15% | Explicitada no pitch: ponto de vista + tensão + stake + prazo |
| Estrutura do dashboard | 20% | Pergunta → Big Number + Insight IA → Gráficos → Tabela |
| Qualidade dos visuais | 20% | Títulos-mensagem; cor com propósito; sem chartjunk |
| Insight de IA | 15% | Acionável; não genérico; apresentado ao lado do Big Number |
| Tableau funcional | 15% | Mínimo 1 filtro ou parâmetro funcionando |
| Pitch de 3 minutos | 15% | Estrutura SCR completa; dentro do tempo; call to action explícito |
| **Total** | **100%** | |

---

## Dicas finais

- **Teste do relance (5 segundos):** mostre o dashboard para alguém por 5 segundos e pergunte o que a pessoa entendeu. Se não souber a Big Idea, os títulos precisam de ajuste.
- **Não coloque tudo no dashboard.** Escolha as 3–5 métricas que mais importam para a dor do negócio.
- **Storyboard antes do Tableau.** Esboce no papel a sequência de visualizações antes de abrir o software.
- **O insight de IA deve ser acionável.** Não vale "os dados mostram que há correlação". Vale "reduzir o desconto de 25% para 12% nesse segmento pode recuperar R$85k por trimestre".
- **Publique no Tableau Public** antes da aula e envie o link pelo Classroom.

---

*Dúvidas? Poste no Classroom ou mande mensagem antes de 17/05/2026.*
