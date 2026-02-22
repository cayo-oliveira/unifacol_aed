# PROVA II UNIDADE — ANÁLISE EXPLORATÓRIA DE DADOS 2026.1

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
- Cada questão vale **2,0 pontos**. Total: **10,0 pontos**.

---

## Questões

---

### Questão 1 (2,0 pontos) — Storytelling com Dados e Big Idea

Marina é analista de dados em uma rede de academias de ginástica com 15 unidades em Recife. Ela foi solicitada a apresentar os resultados de sua análise sobre cancelamentos de matrículas para a reunião trimestral de diretoria.

Após semanas de análise exploratória, Marina descobriu que:
- 68% dos cancelamentos ocorrem nos primeiros 3 meses de matrícula
- Alunos que frequentam pelo menos 2x por semana no primeiro mês têm 85% de chance de permanecer
- O programa "Amigo Indica" tem taxa de retenção 40% maior que matrículas espontâneas
- O horário de pico (18h-20h) está com ocupação de 95%, causando filas e insatisfação

Marina precisa estruturar sua apresentação de forma que a diretoria tome uma decisão clara ao final. Ela lembra do conceito de "Big Idea" aprendido em aula: uma frase que combina o ponto de vista único da análise com o que está em jogo para o público.

Considerando o contexto apresentado e o conceito de Big Idea para storytelling com dados, qual alternativa apresenta um exemplo de **Big Idea bem formulada** que Marina poderia usar?

A) "Devemos implementar um programa de acompanhamento intensivo nos 3 primeiros meses e expandir o horário de funcionamento das 6h às 23h, pois nossa análise mostra que essas ações podem reduzir cancelamentos em até 50% e aumentar a receita recorrente em R$ 180 mil/ano"

B) "Os dados mostram várias informações interessantes sobre cancelamentos"

C) "Analisamos 15.000 registros de matrículas e cancelamentos no período de 2024-2025"

D) "A taxa de cancelamento é de 32% ao ano"

E) "O gráfico de barras mostra a distribuição de cancelamentos por mês"

---

### Questão 2 (2,0 pontos) — Design de Dashboards e Hierarquia Visual

Pedro está criando um dashboard executivo no Tableau para o diretor financeiro de uma distribuidora de bebidas. O dashboard deve mostrar o desempenho de vendas do último trimestre e permitir identificar rapidamente se as metas foram atingidas.

O diretor tem apenas 5 minutos disponíveis por dia para olhar o dashboard. Pedro lembra do conceito de "Teste do Relance" discutido em aula: se alguém olhar para o dashboard por apenas 3 segundos, deve conseguir entender a mensagem principal.

Pedro está decidindo entre duas abordagens de design:

**Opção A**: 
- Título principal: "Vendas Q4 2025: Meta superada em 12% — foco em Cerveja Premium"
- KPI grande no centro mostrando "112%" em verde
- Gráfico de barras comparando categorias com a barra de Cerveja Premium destacada em azul escuro
- Cores: fundo branco, apenas 2-3 cores para destaques
- Espaço em branco generoso separando as seções

**Opção B**:
- Título: "Dashboard de Vendas"
- 12 gráficos diferentes (pizza, barras, linhas, área, etc.)
- Todas as 8 cores da paleta padrão do Tableau utilizadas
- Sem espaço vazio — "aproveitando" toda a tela
- Cada gráfico com título genérico: "Gráfico 1", "Gráfico 2", etc.

Considerando os princípios de design de informação e hierarquia visual para dashboards executivos, qual alternativa apresenta a avaliação **correta** das duas opções?

A) A Opção A é superior porque: o título comunica a mensagem (não apenas descreve), o uso restrito de cores direciona a atenção, o espaço em branco organiza a informação, e o dashboard passa no "Teste do Relance"

B) A Opção B é superior porque tem mais gráficos e mais cores, oferecendo mais informação

C) Ambas as opções são equivalentes em termos de eficácia comunicativa

D) A Opção A é inferior porque tem "muito espaço desperdiçado"

E) Títulos descritivos como "Dashboard de Vendas" são preferíveis porque são mais profissionais

---

### Questão 3 (2,0 pontos) — Tableau: Filtros e Parâmetros

Carolina trabalha como analista de BI em uma rede de farmácias com 50 lojas no Nordeste. Ela construiu um dashboard no Tableau que mostra vendas por categoria de produto, região e período.

A gerente regional pediu que o dashboard permitisse:
1. Ver apenas as lojas de uma região específica (ex.: só Pernambuco)
2. Escolher o período de análise (último mês, trimestre ou ano)
3. Comparar duas categorias de produtos lado a lado

Carolina precisa decidir quais recursos do Tableau utilizar para cada necessidade. Ela se lembra das funcionalidades aprendidas em aula:

- **Filtros**: Permitem que o usuário selecione subconjuntos dos dados (ex.: filtrar por estado, cidade, categoria)
- **Parâmetros**: Permitem que o usuário insira valores que controlam cálculos ou a lógica do dashboard (ex.: escolher qual métrica exibir, definir um limite)
- **Ações de dashboard**: Permitem interatividade entre visualizações (ex.: clicar em um gráfico filtra outro)

Considerando as necessidades apresentadas e os recursos do Tableau, qual alternativa apresenta **corretamente** a combinação de recursos que Carolina deve utilizar?

A) Filtro para selecionar região; Parâmetro para escolher o período (com cálculo que ajusta as datas); Parâmetro ou Ação de filtro para comparar categorias

B) Usar apenas gráficos estáticos sem nenhuma interatividade

C) Criar 50 dashboards separados, um para cada loja

D) Exportar os dados para Excel e fazer as análises manualmente

E) Usar apenas parâmetros para todas as necessidades, sem filtros

---

### Questão 4 (2,0 pontos) — Dashboards que Forçam Decisão

Lucas é gerente de produto em uma startup de delivery e precisa apresentar um dashboard para o CEO decidir se deve expandir a operação para uma nova cidade (Caruaru).

Ele estruturou o dashboard em três seções, seguindo o framework "Contexto → Diagnóstico → Recomendação":

**Seção 1 - Contexto**: 
- Mapa mostrando a área de cobertura atual (Recife) e a cidade-alvo (Caruaru)
- Indicadores de mercado: população de Caruaru, número de restaurantes, penetração de smartphones

**Seção 2 - Diagnóstico**:
- Comparativo de desempenho: tempo médio de entrega, ticket médio, taxa de cancelamento
- Gráfico de crescimento: pedidos/dia nos últimos 6 meses
- Análise de lucratividade por região atual

**Seção 3 - Recomendação**:
- Projeção: investimento necessário vs. retorno esperado em 12 meses
- Cenários: otimista, realista e pessimista
- Call-to-action claro: "Recomendação: Expandir para Caruaru no Q2 2026 com investimento de R$ 500 mil, ROI projetado de 180% em 18 meses"

O CEO, ao ver o dashboard, conseguiu tomar a decisão em 10 minutos porque todas as informações necessárias estavam organizadas de forma lógica e a recomendação era clara e acionável.

Considerando os princípios de dashboards que "forçam decisão", qual alternativa apresenta **corretamente** por que a estrutura de Lucas foi eficaz?

A) O framework "Contexto → Diagnóstico → Recomendação" funciona porque primeiro estabelece o cenário, depois apresenta a análise dos dados, e finaliza com uma ação clara; incluir cenários (otimista/realista/pessimista) reduz incerteza; a recomendação específica (quando, quanto, ROI) facilita a tomada de decisão

B) O dashboard foi eficaz apenas porque tinha muitos gráficos bonitos

C) A estrutura em três seções é irrelevante; qualquer ordem funcionaria igualmente

D) Dashboards não devem incluir recomendações; devem apenas mostrar dados brutos

E) O CEO tomou a decisão rápido porque não leu o dashboard com atenção

---

### Questão 5 (2,0 pontos) — Pitch de 3 Minutos e Apresentação de Resultados

Amanda foi selecionada para apresentar sua análise exploratória em uma competição de dados. Ela tem apenas **3 minutos** para convencer os jurados de que sua análise sobre evasão escolar em Pernambuco gera insights acionáveis.

Ela preparou a seguinte estrutura de pitch:

**Minuto 1 - O Problema (Gancho)**:
"A cada ano, 45 mil estudantes abandonam o Ensino Médio em Pernambuco. Isso representa R$ 270 milhões em investimento público perdido e milhares de jovens com futuro comprometido. Nossa análise identificou os 3 principais fatores preditivos de evasão."

**Minuto 2 - Os Insights (Dados)**:
- Mostrar visualização 1: Mapa de calor das escolas com maior evasão
- Mostrar visualização 2: Correlação entre frequência no 1º bimestre e evasão
- Insight-chave: "Alunos com frequência abaixo de 75% no primeiro bimestre têm 4x mais chance de evadir"

**Minuto 3 - A Recomendação (Call-to-Action)**:
"Propomos um sistema de alerta precoce que identifica alunos em risco já no primeiro bimestre. Com intervenção nesse momento, projetamos redução de 30% na evasão, beneficiando 13 mil estudantes por ano. Próximo passo: piloto em 10 escolas no segundo semestre."

Amanda termina dentro do tempo e os jurados conseguem entender claramente o problema, os insights e a proposta de ação.

Considerando as boas práticas de apresentação de resultados e pitch de análise de dados, qual alternativa apresenta **corretamente** os elementos que tornaram o pitch de Amanda eficaz?

A) O pitch foi eficaz porque: começou com um gancho emocional e números impactantes para capturar atenção; usou apenas 2 visualizações-chave (não sobrecarregou); traduziu o insight em ação concreta com métricas de impacto; e terminou com próximo passo claro

B) O pitch foi eficaz porque durou exatamente 3 minutos, independentemente do conteúdo

C) O pitch deveria ter mostrado todas as 47 visualizações que Amanda criou durante a análise

D) Pitches de dados não devem ter "gancho emocional"; devem começar direto com tabelas de dados

E) A recomendação final é desnecessária; os jurados deveriam decidir sozinhos o que fazer com os dados

---

## GABARITO (uso exclusivo do professor)

| Q1 | Q2 | Q3 | Q4 | Q5 |
|----|----|----|----|----|
| A | A | A | A | A |

---

## Distribuição de Conteúdo

| Questão | Tópico | Semana |
|---------|--------|--------|
| Q1 | Storytelling: AED vs explanativa, Big Idea, pergunta de decisão | 08 |
| Q2 | Design de informação: Teste do Relance, hierarquia visual (cor, tamanho, espaço em branco) | 09 |
| Q3 | Tableau interativo: filtros, parâmetros, ações de dashboard | 10 |
| Q4 | Dashboards que forçam decisão: estrutura (contexto → diagnóstico → recomendação) | 11 |
| Q5 | Pitch de 3 minutos: história + decisão + próximo passo | 11-12 |

---

## Notas para o Professor

### Q1 - Big Idea
- **Por que A é correta**: É específica (ações concretas), quantificada (50%, R$ 180 mil), e conecta análise com decisão.
- **Outras alternativas**: B é vaga; C é descritiva (não acionável); D é apenas um número; E descreve um gráfico.

### Q2 - Hierarquia Visual
- **Por que A é correta**: Opção A segue todos os princípios: título-mensagem, cores restritas, espaço em branco, passa no Teste do Relance.
- **Opção B falha**: Muitos gráficos, muitas cores, títulos genéricos = confusão visual.

### Q3 - Filtros e Parâmetros
- **Por que A é correta**: Filtro é ideal para subconjuntos (região); Parâmetro é ideal para controlar lógica (período); Comparação pode usar ambos.
- **Outras alternativas**: B, C, D são absurdas; E ignora a funcionalidade de filtros.

### Q4 - Dashboards que Forçam Decisão
- **Por que A é correta**: A estrutura C→D→R é um framework comprovado; cenários reduzem incerteza; recomendação clara acelera decisão.
- **Outras alternativas**: B é superficial; C ignora estrutura; D é errada (dashboards podem recomendar); E é absurda.

### Q5 - Pitch de 3 Minutos
- **Por que A é correta**: Estrutura Problema→Insights→Ação é eficaz; gancho captura atenção; foco em poucas visualizações; call-to-action claro.
- **Outras alternativas**: B ignora conteúdo; C é overload; D ignora psicologia de apresentação; E ignora objetivo do pitch.
