# TEMPLATE DE PROVA NO FORMATO ENADE — GENÉRICO PARA QUALQUER MATÉRIA

Este arquivo é um template genérico para criar provas no estilo ENADE. Inclui orientações para diferentes tipos de prova (I Unidade, II Unidade, II Chamada, Final) com variações de dificuldade e formato.

---

## TIPOS DE PROVA — RESUMO

| Tipo | Questões | Dificuldade | Tamanho Texto | Conteúdo |
|------|----------|-------------|---------------|----------|
| **I Unidade** | 5 | DIFÍCIL (anti-IA) | GRANDE (tabelas, cenários complexos) | Semanas 01-07 |
| **II Unidade** | 5 | FÁCIL | GRANDE (contextual) | Semanas 08-12 |
| **II Chamada** | 10 | MUITO DIFÍCIL | MÉDIO | Todo semestre |
| **Final** | 10 | FÁCIL (monitoria) | CURTO (1-2 parágrafos) | Todo semestre |

---

## ESPECIFICAÇÕES DETALHADAS POR TIPO

### PROVA I UNIDADE (Difícil)

**Características:**
- 5 questões × 2,0 pontos = 10,0 pontos
- Textos GRANDES: 3-5 parágrafos por questão
- Tabelas com dados reais para análise
- Cenários contextuais complexos (ex.: empresa, secretaria, pesquisa)

**Estratégias Anti-IA:**
- Questões que exigem múltiplos passos de raciocínio
- Cálculos com interpretação intermediária (não basta aplicar fórmula)
- Alternativas que parecem corretas mas têm sutilezas
- Contextos que dependem de análise crítica, não apenas definição

**Exemplo de Estrutura de Questão:**
```
[3-5 parágrafos descrevendo cenário real com dados]
[Tabela com dados numéricos ou categóricos]
[Parágrafo adicional com análise parcial ou debate]
[Pergunta que exige integração de múltiplos conceitos]
```

### PROVA II UNIDADE (Fácil)

**Características:**
- 5 questões × 2,0 pontos = 10,0 pontos
- Textos GRANDES: 3-4 parágrafos por questão
- Cenários narrativos (storytelling)
- Perguntas diretas com resposta clara

**Foco:**
- Storytelling e Big Idea
- Design de dashboards
- Tableau (filtros, parâmetros, ações)
- Apresentação de resultados

**Exemplo de Estrutura de Questão:**
```
[Cenário de trabalho: analista precisa apresentar/criar dashboard]
[Descrição do problema de comunicação]
[Opções de design ou abordagem]
[Pergunta sobre qual opção segue as boas práticas]
```

### PROVA II CHAMADA (Muito Difícil)

**Características:**
- 10 questões × 1,0 ponto = 10,0 pontos
- Textos MÉDIOS: 1-2 parágrafos por questão
- Todo o conteúdo do semestre
- Questões que integram múltiplos conceitos

**Estratégias de Dificuldade:**
- Armadilhas conceituais (confundir correlação/causalidade)
- Cálculos que exigem raciocínio (não apenas fórmula)
- Alternativas numericamente próximas
- Cenários que exigem análise crítica

### PROVA FINAL (Fácil - Estilo Monitoria)

**Características:**
- 10 questões × 1,0 ponto = 10,0 pontos
- Textos CURTOS: 1-2 frases de contexto
- Todo o conteúdo do semestre
- Questões conceituais diretas

**Objetivo:**
- Verificar conhecimento básico
- Permitir recuperação
- Perguntas sem armadilhas

---

## REGRAS GERAIS PARA CRIAR A PROVA

### 1. Estrutura Geral

- **Cabeçalho Institucional**: Informações da faculdade, curso e disciplina
- **Título**: "PROVA [TIPO] — [DISCIPLINA] [ANO].[SEMESTRE]"
- **Informações**: Disciplina, curso, período, data, professor, nome do aluno
- **Instruções**: Tempo, materiais, pontuação
- **Questões**: Numeradas com peso indicado
- **Gabarito**: Tabela para uso do professor
- **Notas**: Explicações dos cálculos e armadilhas

### 2. Formato das Questões

**Contexto:**
- CURTO: 1-2 frases (Final)
- MÉDIO: 1-2 parágrafos (II Chamada)
- GRANDE: 3-5 parágrafos + tabelas (I/II Unidade)

**Pergunta:**
- "Qual alternativa apresenta **corretamente**..."
- "Considerando o cenário, qual é..."
- "Qual afirmação está **incorreta**..." (para NÃO/EXCETO)

**Alternativas:**
- A) Geralmente correta (variar posição se desejar)
- B-E) Distratores plausíveis com erros específicos

### 3. Dicas para Questões Difíceis (Anti-IA)

1. **Múltiplos passos**: Exigir cálculo E interpretação
2. **Armadilhas conceituais**: Correlação ≠ causalidade, média vs mediana
3. **Análise crítica**: "A afirmação X está correta? Por quê?"
4. **Contexto específico**: Detalhes que mudam a resposta
5. **Cálculos encadeados**: Resultado intermediário afeta final

### 4. Dicas para Questões Fáceis

1. **Definições diretas**: "O que é X?"
2. **Aplicação simples**: "Dado X, calcule Y"
3. **Identificação**: "Qual gráfico é adequado para..."
4. **Boas práticas**: "Qual é a recomendação para..."

### 5. Formatação Markdown

- `#` para títulos
- `**negrito**` para ênfases
- `---` para separadores
- Tabelas para dados e gabarito
- Listas para alternativas

---

## EXEMPLOS DE TEXTO POR TAMANHO

### Texto CURTO (Final)

> Uma empresa precisa documentar o significado de cada coluna de um dataset. Qual documento deve ser criado?

### Texto MÉDIO (II Chamada)

> Um dataset de transações bancárias possui 50.000 registros. A coluna `valor_transacao` contém: 47.500 valores numéricos válidos, 1.200 valores como "R$ 150,00" (string), 800 valores NULL, e 500 valores negativos (estornos legítimos). Quantos registros apresentam problemas reais de qualidade?

### Texto GRANDE (I/II Unidade)

> A Secretaria Municipal de Saúde de uma cidade do interior de Pernambuco contratou uma consultoria para analisar dados de atendimentos em Unidades Básicas de Saúde (UBS). O arquivo recebido, `atendimentos_ubs_2025.csv`, contém 47.832 registros e as seguintes colunas:
>
> | Coluna | Descrição | Exemplos |
> |--------|-----------|----------|
> | `data_atend` | Data do atendimento | "15/03/2025", "2025-03-16" |
> | `cpf_paciente` | CPF do paciente | "123.456.789-00", NULL |
> | `idade` | Idade em anos | 25, "32 anos", -5, 150 |
>
> A equipe identificou que 847 registros possuem exatamente o mesmo CPF, data e CID — caracterizando duplicatas reais. Além disso, 12% dos registros possuem CPF como NULL.
>
> Considerando o cenário e as boas práticas de preparação de dados, qual sequência de ações deve ser executada ANTES de qualquer estatística?

---

## PERSONALIZAÇÃO

Substitua os placeholders:
- `[DISCIPLINA]` → Nome da disciplina
- `[CURSO]` → Nome do curso
- `[PROFESSOR]` → Nome do professor
- `[ANO].[SEMESTRE]` → Ex.: 2026.1
- `[NÚMERO]` e `[DATA]` → Dados da portaria do curso

---

# EXERCÍCIO DE APRENDIZAGEM E APROVEITAMENTO — MONITORIA [ANO].[SEMESTRE]

Credenciada e Autorizada pelo MEC, Portaria n.º 644 de 28 de março de 2001 – Publicado no D.O.U. em 02/04/2001  
Curso de [CURSO] – Reconhecido pela Portaria nº [NÚMERO] de [DATA]

---

**Disciplina:** [DISCIPLINA] | **Curso:** [CURSO]  
**Período:** [PERÍODO] | **Data:** ___/___/[ANO]  
**Prof(a).** [PROFESSOR] | **Aluno(a):** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

### Instruções

- O aluno dispõe de **[TEMPO]** para realizar este exercício de aprendizagem e aproveitamento.
- A interpretação cabe exclusivamente ao aluno. Dirija-se ao professor apenas em caso de texto ilegível.
- Manter desligado e guardado aparelho celular ou qualquer dispositivo eletrônico.
- Proibido solicitar material por empréstimo. Guardar todo material didático sob a cadeira.
- Serão consideradas apenas as respostas escritas com caneta preta ou azul.
- Cada questão vale **1,0 ponto**. Total: **10,0 pontos**.

---

## Questões

---

### Questão 1 (1,0 ponto) — [TÓPICO 1]

[PARÁGRAFO DE CONTEXTO: Descreva uma situação prática relacionada ao tópico.]

Qual alternativa apresenta **corretamente** [PERGUNTA]?

A) [ALTERNATIVA CORRETA]  
B) [DISTRATOR 1]  
C) [DISTRATOR 2]  
D) [DISTRATOR 3]  
E) [DISTRATOR 4]

---

### Questão 2 (1,0 ponto) — [TÓPICO 2]

[PARÁGRAFO DE CONTEXTO]

[PERGUNTA]

A) [ALTERNATIVA A]  
B) [ALTERNATIVA B]  
C) [ALTERNATIVA C]  
D) [ALTERNATIVA D]  
E) [ALTERNATIVA E]

---

### Questão 3 (1,0 ponto) — [TÓPICO 3]

[PARÁGRAFO DE CONTEXTO]

[PERGUNTA]

A) [ALTERNATIVA A]  
B) [ALTERNATIVA B]  
C) [ALTERNATIVA C]  
D) [ALTERNATIVA D]  
E) [ALTERNATIVA E]

---

### Questão 4 (1,0 ponto) — [TÓPICO 4]

[PARÁGRAFO DE CONTEXTO]

[PERGUNTA]

A) [ALTERNATIVA A]  
B) [ALTERNATIVA B]  
C) [ALTERNATIVA C]  
D) [ALTERNATIVA D]  
E) [ALTERNATIVA E]

---

### Questão 5 (1,0 ponto) — [TÓPICO 5]

[PARÁGRAFO DE CONTEXTO]

[PERGUNTA]

A) [ALTERNATIVA A]  
B) [ALTERNATIVA B]  
C) [ALTERNATIVA C]  
D) [ALTERNATIVA D]  
E) [ALTERNATIVA E]

---

### Questão 6 (1,0 ponto) — [TÓPICO 6]

[PARÁGRAFO DE CONTEXTO]

[PERGUNTA]

A) [ALTERNATIVA A]  
B) [ALTERNATIVA B]  
C) [ALTERNATIVA C]  
D) [ALTERNATIVA D]  
E) [ALTERNATIVA E]

---

### Questão 7 (1,0 ponto) — [TÓPICO 7]

[PARÁGRAFO DE CONTEXTO]

[PERGUNTA]

A) [ALTERNATIVA A]  
B) [ALTERNATIVA B]  
C) [ALTERNATIVA C]  
D) [ALTERNATIVA D]  
E) [ALTERNATIVA E]

---

### Questão 8 (1,0 ponto) — [TÓPICO 8]

[PARÁGRAFO DE CONTEXTO]

[PERGUNTA]

A) [ALTERNATIVA A]  
B) [ALTERNATIVA B]  
C) [ALTERNATIVA C]  
D) [ALTERNATIVA D]  
E) [ALTERNATIVA E]

---

### Questão 9 (1,0 ponto) — [TÓPICO 9]

[PARÁGRAFO DE CONTEXTO]

[PERGUNTA]

A) [ALTERNATIVA A]  
B) [ALTERNATIVA B]  
C) [ALTERNATIVA C]  
D) [ALTERNATIVA D]  
E) [ALTERNATIVA E]

---

### Questão 10 (1,0 ponto) — [TÓPICO 10]

[PARÁGRAFO DE CONTEXTO]

[PERGUNTA]

A) [ALTERNATIVA A]  
B) [ALTERNATIVA B]  
C) [ALTERNATIVA C]  
D) [ALTERNATIVA D]  
E) [ALTERNATIVA E]

---

## GABARITO (uso exclusivo do professor)

| Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 |
|----|----|----|----|----|----|----|----|----|-----|
| [GABARITO Q1] | [GABARITO Q2] | [GABARITO Q3] | [GABARITO Q4] | [GABARITO Q5] | [GABARITO Q6] | [GABARITO Q7] | [GABARITO Q8] | [GABARITO Q9] | [GABARITO Q10] |

---

## Notas Adicionais

- **Adaptação**: Para outras matérias, substitua os tópicos pelos conteúdos específicos (ex.: para Matemática, use teoremas; para História, eventos).
- **Validação**: Sempre verifique cálculos e lógica das alternativas.
- **Uso**: Copie este template, preencha os placeholders e salve como .md ou converta para .tex se necessário.

---

## EXEMPLOS DE QUESTÕES COMPLETAS

### Exemplo: Questão DIFÍCIL (I Unidade / II Chamada)

**Questão X (2,0 pontos) — Medidas de Tendência Central e Dispersão**

Uma rede de supermercados com 8 lojas está avaliando o faturamento mensal do setor de hortifrúti:

| Loja | Faturamento (R$) |
|------|------------------|
| L1 | 45.000 |
| L2 | 52.000 |
| L3 | 38.000 |
| L4 | 41.000 |
| L5 | 39.000 |
| L6 | 36.000 |
| L7 | 35.000 |
| L8 | 142.000 |

O gerente calculou: Q1 = R$ 37.000, Q3 = R$ 48.500, IQR = R$ 11.500.

Considerando os dados e o critério 1,5×IQR para outliers, qual alternativa apresenta **corretamente** a mediana e a classificação da loja L8?

A) Mediana = R$ 40.000; L8 é outlier (limite superior = R$ 65.750)  
B) Mediana = R$ 41.000; L8 não é outlier  
C) Mediana = R$ 53.500; L8 é outlier  
D) Mediana = R$ 40.000; L8 não é outlier  
E) Mediana = R$ 39.000; L8 é outlier

**Resposta: A**  
*Cálculo: Mediana = (39.000 + 41.000)/2 = 40.000; LS = 48.500 + 1,5×11.500 = 65.750; 142.000 > 65.750 → outlier*

---

### Exemplo: Questão FÁCIL (II Unidade / Final)

**Questão Y (1,0 ponto) — Big Idea**

Uma analista precisa apresentar resultados para a diretoria.

Qual frase representa uma Big Idea bem formulada?

A) "Devemos investir R$ 100 mil em marketing, pois a análise mostra retorno de 3x"  
B) "O gráfico mostra vendas"  
C) "Analisamos 10.000 registros"  
D) "Os dados são interessantes"  
E) "Tabela 1: Distribuição por região"

**Resposta: A**  
*A Big Idea é específica, quantificada e acionável.*

---

## CHECKLIST PARA REVISÃO DA PROVA

- [ ] Todas as questões têm contexto?
- [ ] Os cálculos foram verificados manualmente?
- [ ] As alternativas incorretas são plausíveis?
- [ ] O gabarito está preenchido?
- [ ] O tempo é adequado para o número de questões?
- [ ] A distribuição de conteúdo cobre todas as semanas?
- [ ] O nível de dificuldade está adequado ao tipo de prova?
