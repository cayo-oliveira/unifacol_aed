# PROVA FINAL — ANÁLISE EXPLORATÓRIA DE DADOS 2026.1

Credenciada e Autorizada pelo MEC, Portaria n.º 644 de 28 de março de 2001 – Publicado no D.O.U. em 02/04/2001  
Curso de Sistemas de Informação – Reconhecido pela Portaria nº 286 de 21/12/2012

---

**Disciplina:** Análise Exploratória de Dados | **Curso:** Sistemas de Informação  
**Período:** 2026.1 | **Data:** ___/___/2026  
**Prof(a).** Cayo Medeiros | **Aluno(a):** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

### Instruções

- O aluno dispõe de **1 hora e 30 minutos** para realizar esta prova.
- A interpretação cabe exclusivamente ao aluno. Dirija-se ao professor apenas em caso de texto ilegível.
- Manter desligado e guardado aparelho celular ou qualquer dispositivo eletrônico.
- Proibido solicitar material por empréstimo. Guardar todo material didático sob a cadeira.
- Serão consideradas apenas as respostas escritas com caneta preta ou azul.
- Cada questão vale **1,0 ponto**. Total: **10,0 pontos**.

---

## Questões

---

### Questão 1 (1,0 ponto) — Dicionário de Dados

Uma empresa recebeu um arquivo CSV e precisa documentar o que cada coluna significa, quais valores são válidos e qual o tipo de dado esperado.

Qual documento deve ser criado para essa finalidade?

A) Dicionário de dados  
B) Dashboard  
C) Histograma  
D) Boxplot  
E) Scatter plot

---

### Questão 2 (1,0 ponto) — Qualidade de Dados

Uma analista encontrou os seguintes problemas em um dataset: a coluna "salário" tem valores como "5000", "cinco mil" e "NULL"; a coluna "email" tem 20% de células vazias.

Quais tipos de problemas de qualidade foram identificados?

A) Tipos inconsistentes e dados ausentes  
B) Apenas outliers  
C) Apenas dados duplicados  
D) Dados ausentes e correlação  
E) Histograma e boxplot incorretos

---

### Questão 3 (1,0 ponto) — Média, Mediana e Moda

Um professor calculou as notas de 5 alunos: 6, 7, 7, 8, 12. A média é 8,0 (40÷5), a mediana é 7 (valor central) e a moda é 7 (mais frequente).

Qual medida é mais afetada pelo valor extremo (12)?

A) Média  
B) Mediana  
C) Moda  
D) Todas são igualmente afetadas  
E) Nenhuma é afetada

---

### Questão 4 (1,0 ponto) — Desvio-Padrão

Duas turmas fizeram a mesma prova. Turma A: média 7,0 e desvio-padrão 0,5. Turma B: média 7,0 e desvio-padrão 2,5.

Qual turma tem notas mais homogêneas (mais parecidas entre si)?

A) Turma A, porque menor desvio-padrão indica menor variabilidade  
B) Turma B, porque maior desvio-padrão indica menor variabilidade  
C) Ambas são iguais porque têm a mesma média  
D) Turma B, porque 2,5 é maior que 0,5  
E) Não é possível comparar

---

### Questão 5 (1,0 ponto) — Boxplot e Outliers

Em um boxplot, Q1 = 10, Q3 = 30, portanto IQR = 20. O limite superior para outliers é Q3 + 1,5 × IQR.

Qual é o limite superior?

A) 60  
B) 50  
C) 40  
D) 30  
E) 20

---

### Questão 6 (1,0 ponto) — Dados Ausentes

Um dataset tem 15% de valores ausentes na coluna "idade". Uma estratégia válida é criar uma categoria "Não informado" para análise.

Qual estratégia é geralmente considerada **inadequada** por poder distorcer a análise?

A) Substituir todos os ausentes por zero sem considerar o contexto  
B) Imputar pela mediana  
C) Remover registros com muitos ausentes  
D) Documentar os ausentes no relatório  
E) Manter os ausentes e usar técnicas que lidam com eles

---

### Questão 7 (1,0 ponto) — Correlação

Um analista calculou a correlação entre "horas de estudo" e "nota na prova" e obteve r = 0,85. Seu chefe disse: "Então mais horas de estudo causam notas maiores".

Essa afirmação está:

A) Incorreta, porque correlação não implica causalidade  
B) Correta, porque 0,85 é muito alto  
C) Correta, porque a correlação é positiva  
D) Incorreta, porque 0,85 é muito baixo  
E) Correta, porque estudo sempre causa aprendizado

---

### Questão 8 (1,0 ponto) — Big Idea

Uma analista precisa apresentar resultados para a diretoria. Qual frase representa uma Big Idea bem formulada?

A) "Devemos investir R$ 100 mil em marketing digital, pois a análise mostra retorno de 3x em 6 meses"  
B) "O gráfico mostra vendas"  
C) "Analisamos 10.000 registros"  
D) "Os dados são interessantes"  
E) "Tabela 1: Distribuição por região"

---

### Questão 9 (1,0 ponto) — Design de Dashboard

Qual prática é recomendada para criar um dashboard executivo eficaz?

A) Títulos que comunicam a mensagem principal, uso restrito de cores e espaço em branco para organização  
B) Usar todas as cores disponíveis para deixar mais bonito  
C) Colocar o máximo de gráficos possível  
D) Eliminar todo espaço em branco  
E) Usar títulos genéricos como "Gráfico 1"

---

### Questão 10 (1,0 ponto) — Tableau

No Tableau, qual recurso permite que o usuário selecione dinamicamente quais dados visualizar (ex.: filtrar por região ou período)?

A) Filtros e parâmetros  
B) Exportar para PDF  
C) Imprimir o relatório  
D) Copiar os dados para Excel  
E) Usar apenas gráficos estáticos

---

## GABARITO (uso exclusivo do professor)

| Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 |
|----|----|----|----|----|----|----|----|----|-----|
| A | A | A | A | A | A | A | A | A | A |

---

## Distribuição de Conteúdo

| Questão | Tópico | Semana |
|---------|--------|--------|
| Q1 | Dicionário de dados | 01-02 |
| Q2 | Qualidade de dados (tipos, ausências) | 02 |
| Q3 | Média, mediana, moda (tendência central) | 03 |
| Q4 | Desvio-padrão (variabilidade) | 04 |
| Q5 | Boxplot, IQR, outliers | 04-05 |
| Q6 | Dados ausentes (missing) | 05 |
| Q7 | Correlação ≠ causalidade | 06 |
| Q8 | Big Idea (storytelling) | 08 |
| Q9 | Design de dashboard (Teste do Relance) | 09 |
| Q10 | Tableau (filtros, parâmetros) | 10 |

---

## Notas para o Professor

- **Q5**: Limite superior = Q3 + 1,5 × IQR = 30 + 1,5 × 20 = 30 + 30 = 60
- Prova com questões diretas e conceituais, adequada para avaliação final de recuperação
