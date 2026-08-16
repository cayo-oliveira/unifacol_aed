# Roteiro da Aula: Introdução ao Tableau com Dataset de Desempenho Acadêmico

## Data: Amanhã (9 de fevereiro de 2026)
## Duração: 3 horas
- 1 hora: Apresentações dos alunos
- 2 horas: Treinamento prático em Tableau

## Objetivos da Aula
- Entender conceitos básicos de Tableau (conexão de dados, visualizações, dashboards, storytelling).
- Aplicar análise exploratória de dados (AED) no dataset de desempenho acadêmico.
- Criar perguntas estratégicas, protótipos de dashboards e narrativas visuais.

## Materiais Necessários
- Tableau Desktop/Public instalado (versão gratuita disponível).
- Dataset: `StudentPerformanceFactors_transformado.csv` (preparado com transformações em Python).
- Contexto: `context.md` para referência.
- Notebook de preparação: `python/preparacao_tableau.ipynb` (já executado).

## Roteiro Detalhado

### Parte 1: Apresentações (1 hora)
- Cada aluno apresenta-se brevemente (nome, curso, interesses em dados/visualização).
- Discussão inicial: O que vocês sabem sobre Tableau? Expectativas para a aula.

### Parte 2: Treinamento em Tableau (2 horas)

#### 2.1 Introdução e Conexão de Dados (15 min)
- O que é Tableau? Diferenças entre Desktop/Public/Online.
- Conectar ao CSV transformado (`StudentPerformanceFactors_transformado.csv`).
- Explorar metadados: tipos de dados, colunas traduzidas.

#### 2.2 Criando Visualizações Básicas (30 min)
- Arrastar campos para Rows/Columns.
- Criar gráficos simples:
  - Histograma de `Nota_Exame`.
  - Scatter plot: `Horas_Estudadas` vs. `Nota_Exame`.
  - Bar chart: Média de `Nota_Exame` por `Envolvimento_Parental`.
- Aplicar filtros e cores.

#### 2.3 Dashboards Interativos (45 min)
- Combinar gráficos em um dashboard.
- Adicionar filtros globais (ex.: por `Genero`, `Renda_Familiar`).
- Criar KPIs: Média de `Nota_Exame`, Taxa de Aprovação.
- Protótipo baseado no `context.md`: KPIs, gráficos numéricos, categóricos, tabela consolidada.

#### 2.4 Storytelling e Narrativa (20 min)
- Criar uma história: "Fatores que influenciam o desempenho acadêmico".
- Adicionar anotações, títulos e fluxo narrativo.
- Exportar como PDF ou compartilhar online.

#### 2.5 Atividades Práticas e Discussão (10 min)
- Alunos experimentam criar suas próprias visualizações.
- Discussão: Insights do dataset, aplicações reais.

## Perguntas-Chave para Guiar a Aula
1. Quais fatores mais correlacionam com notas altas?
2. Há diferenças por gênero ou renda?
3. Como melhorar a frequência para elevar desempenho?

## Próximos Passos
- Após a aula, integrar ao livro de notas (semana02).
- Enviar feedback ou dúvidas.

## Notas Adicionais
- Se Tableau não estiver instalado, usar a versão web gratuita.
- Referência: `context.md` para detalhes do dataset e protótipo.
- Tempo flexível; ajustar conforme ritmo da turma.