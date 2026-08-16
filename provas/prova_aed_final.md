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

A) Dashboard  
B) Histograma  
C) Boxplot  
D) Scatter plot  
E) Dicionário de dados

---

### Questão 2 (1,0 ponto) — Qualidade de Dados

Uma analista encontrou os seguintes problemas em um dataset: a coluna "salário" tem valores como "5000", "cinco mil" e "NULL"; a coluna "email" tem 20% de células vazias.

Quais tipos de problemas de qualidade foram identificados?

A) Apenas outliers  
B) Apenas dados duplicados  
C) Dados ausentes e correlação  
D) Tipos inconsistentes e dados ausentes  
E) Histograma e boxplot incorretos

---

### Questão 3 (1,0 ponto) — Média, Mediana e Moda

Um professor calculou as notas de 5 alunos: 6, 7, 7, 8, 12. A média é 8,0 (40÷5), a mediana é 7 (valor central) e a moda é 7 (mais frequente).

Qual medida é mais afetada pelo valor extremo (12)?

A) Mediana  
B) Moda  
C) Todas são igualmente afetadas  
D) Nenhuma é afetada  
E) Média

---

### Questão 4 (1,0 ponto) — Desvio-Padrão

Duas turmas fizeram a mesma prova. Turma A: média 7,0 e desvio-padrão 0,5. Turma B: média 7,0 e desvio-padrão 2,5.

Qual turma tem notas mais homogêneas (mais parecidas entre si)?

A) Turma B, porque maior desvio-padrão indica menor variabilidade  
B) Ambas são iguais porque têm a mesma média  
C) Turma A, porque menor desvio-padrão indica menor variabilidade  
D) Turma B, porque 2,5 é maior que 0,5  
E) Não é possível comparar

---

### Questão 5 (1,0 ponto) — Boxplot e Outliers

Em um boxplot, Q1 = 10, Q3 = 30, portanto IQR = 20. O limite superior para outliers é Q3 + 1,5 × IQR.

Qual é o limite superior?

A) 50  
B) 40  
C) 30  
D) 20  
E) 60

---

### Questão 6 (1,0 ponto) — Dados Ausentes

Um dataset tem 15% de valores ausentes na coluna "idade". Uma estratégia válida é criar uma categoria "Não informado" para análise.

Qual estratégia é geralmente considerada **inadequada** por poder distorcer a análise?

A) Imputar pela mediana  
B) Remover registros com muitos ausentes  
C) Documentar os ausentes no relatório  
D) Manter os ausentes e usar técnicas que lidam com eles  
E) Substituir todos os ausentes por zero sem considerar o contexto

---

### Questão 7 (1,0 ponto) — Correlação

Um analista calculou a correlação entre "horas de estudo" e "nota na prova" e obteve r = 0,85. Seu chefe disse: "Então mais horas de estudo causam notas maiores".

Essa afirmação está:

A) Correta, porque 0,85 é muito alto  
B) Correta, porque a correlação é positiva  
C) Incorreta, porque 0,85 é muito baixo  
D) Incorreta, porque correlação não implica causalidade  
E) Correta, porque estudo sempre causa aprendizado

---

### Questão 8 (1,0 ponto) — Big Idea

Uma analista precisa apresentar resultados para a diretoria. Qual frase representa uma Big Idea bem formulada?

A) "O gráfico mostra vendas"  
B) "Analisamos 10.000 registros"  
C) "Os dados são interessantes"  
D) "Devemos investir R$ 100 mil em marketing digital, pois a análise mostra retorno de 3x em 6 meses"  
E) "Tabela 1: Distribuição por região"

---

### Questão 9 (1,0 ponto) — Design de Dashboard

Qual prática é recomendada para criar um dashboard executivo eficaz?

A) Usar todas as cores disponíveis para deixar mais bonito  
B) Colocar o máximo de gráficos possível  
C) Títulos que comunicam a mensagem principal, uso restrito de cores e espaço em branco para organização  
D) Eliminar todo espaço em branco  
E) Usar títulos genéricos como "Gráfico 1"

---

### Questão 10 (1,0 ponto) — Tableau

No Tableau, qual recurso permite que o usuário selecione dinamicamente quais dados visualizar (ex.: filtrar por região ou período)?

A) Exportar para PDF  
B) Imprimir o relatório  
C) Copiar os dados para Excel  
D) Usar apenas gráficos estáticos  
E) Filtros e parâmetros

---

## GABARITO (uso exclusivo do professor)

| Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 |
|----|----|----|----|----|----|----|----|----|-----|
| E | D | E | C | E | E | D | D | C | E |

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
