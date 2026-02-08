# Contexto do Dataset: Desempenho Acadêmico dos Estudantes

## Introdução ao Dataset
Este dataset, intitulado "Student Academic Performance Dataset" (Dataset de Desempenho Acadêmico dos Estudantes), foi baixado do Kaggle e criado por A. O propósito principal é examinar as principais variáveis que afetam o desempenho acadêmico dos estudantes, especialmente suas notas em exames. Ele foca em como o ambiente educacional, recursos de aprendizagem, histórico familiar e comportamentos individuais influenciam os resultados dos alunos. O dataset é útil para modelos de aprendizado de máquina, pesquisas educacionais e iniciativas de ciência de dados que buscam compreender o desempenho acadêmico e identificar tendências de alto e baixo rendimento. É adequado para análise exploratória de dados (EDA) e modelagem preditiva, pois oferece uma visão realista da vida e dos ambientes de aprendizagem dos estudantes.

### Conteúdo
O dataset inclui horas de estudo dos estudantes, frequência às aulas, nível de motivação, disponibilidade de recursos de aprendizagem, participação parental, qualidade do professor, influência dos colegas e histórico familiar. Também inclui elementos ambientais e de estilo de vida, como acesso à internet, padrões de sono e tipo de escola. A variável alvo representa as notas dos exames dos estudantes. Juntas, essas características criam um dataset abrangente para analisar os diversos fatores que influenciam o desempenho acadêmico.

### Usabilidade e Licença
- **Usabilidade**: 10.00 (muito alta, dados limpos e bem estruturados).
- **Licença**: CC0: Domínio Público.
- **Frequência de Atualização Esperada**: Semanal.
- **Tags**: Educação, Análise de Dados, Visualização de Dados, Análise Exploratória de Dados.

## Metadados Detalhados
O dataset está em formato CSV (`StudentPerformanceFactors.csv`, ~642 KB) com aproximadamente 6.600 linhas e 20 colunas. Cada linha representa um estudante único. Os metadados seguem o formato Croissant (MLCommons), com descrições estruturadas de cada campo. Abaixo, uma tradução completa para pt-br das colunas, tipos de dados, descrições e exemplos de valores.

### Colunas e Descrições (Traduzidas)
1. **Horas_Estudadas** (Hours_Studied) - Tipo: Inteiro  
   Descrição: Horas diárias de estudo.  
   Valores: 1 a 44 (média ~19-20).  
   Exemplo: 23.

2. **Frequencia** (Attendance) - Tipo: Inteiro  
   Descrição: Percentual de frequência às aulas.  
   Valores: 60 a 100 (média ~80-85).  
   Exemplo: 84.

3. **Envolvimento_Parental** (Parental_Involvement) - Tipo: Texto  
   Descrição: Suporte acadêmico dos pais.  
   Valores: Baixo (Low), Médio (Medium), Alto (High).  
   Exemplo: Baixo.

4. **Acesso_a_Recursos** (Access_to_Resources) - Tipo: Texto  
   Descrição: Disponibilidade de recursos de aprendizagem.  
   Valores: Baixo, Médio, Alto.  
   Exemplo: Alto.

5. **Atividades_Extracurriculares** (Extracurricular_Activities) - Tipo: Booleano  
   Descrição: Participação em atividades extracurriculares.  
   Valores: Sim (Yes), Não (No).  
   Exemplo: Não.

6. **Horas_Sono** (Sleep_Hours) - Tipo: Inteiro  
   Descrição: Duração média de sono.  
   Valores: 4 a 10 (média ~7-8).  
   Exemplo: 7.

7. **Notas_Anteriores** (Previous_Scores) - Tipo: Inteiro  
   Descrição: Desempenho acadêmico passado.  
   Valores: 50 a 100 (média ~75-80).  
   Exemplo: 73.

8. **Nivel_Motivacao** (Motivation_Level) - Tipo: Texto  
   Descrição: Nível de motivação do estudante.  
   Valores: Baixo, Médio, Alto.  
   Exemplo: Baixo.

9. **Acesso_Internet** (Internet_Access) - Tipo: Booleano  
   Descrição: Status de disponibilidade de internet.  
   Valores: Sim, Não.  
   Exemplo: Sim.

10. **Sessoes_Tutoria** (Tutoring_Sessions) - Tipo: Inteiro  
    Descrição: Frequência de tutoria extra.  
    Valores: 0 a 8 (média ~1-2).  
    Exemplo: 0.

11. **Renda_Familiar** (Family_Income) - Tipo: Texto  
    Descrição: Renda familiar.  
    Valores: Baixo, Médio, Alto.  
    Exemplo: Baixo.

12. **Qualidade_Professor** (Teacher_Quality) - Tipo: Texto  
    Descrição: Qualidade do professor.  
    Valores: Baixo, Médio, Alto.  
    Exemplo: Médio.

13. **Tipo_Escola** (School_Type) - Tipo: Texto  
    Descrição: Tipo de escola.  
    Valores: Público (Public), Privado (Private).  
    Exemplo: Público.

14. **Influencia_Colegas** (Peer_Influence) - Tipo: Texto  
    Descrição: Influência dos colegas.  
    Valores: Positivo (Positive), Negativo (Negative), Neutro (Neutral).  
    Exemplo: Positivo.

15. **Atividade_Fisica** (Physical_Activity) - Tipo: Inteiro  
    Descrição: Nível de atividade física.  
    Valores: 0 a 8 (média ~2-3).  
    Exemplo: 3.

16. **Deficiencias_Aprendizagem** (Learning_Disabilities) - Tipo: Booleano  
    Descrição: Presença de deficiências de aprendizagem.  
    Valores: Sim, Não.  
    Exemplo: Não.

17. **Educacao_Parental** (Parental_Education_Level) - Tipo: Texto  
    Descrição: Nível de educação dos pais.  
    Valores: Ensino Médio (High School), Faculdade (College), Pós-Graduação (Postgraduate).  
    Exemplo: Ensino Médio.

18. **Distancia_Casa** (Distance_from_Home) - Tipo: Texto  
    Descrição: Distância da casa até a escola.  
    Valores: Perto (Near), Moderado (Moderate), Longe (Far).  
    Exemplo: Perto.

19. **Genero** (Gender) - Tipo: Texto  
    Descrição: Gênero do estudante.  
    Valores: Masculino (Male), Feminino (Female).  
    Exemplo: Masculino.

20. **Nota_Exame** (Exam_Score) - Tipo: Inteiro  
    Descrição: Pontuação do exame (variável alvo).  
    Valores: 60 a 100 (média ~67-70).  
    Exemplo: 67.

### Estatísticas Gerais
- **Linhas**: ~6.607 (sem nulos, dados limpos).
- **Distribuições Principais**:
  - Nota_Exame: Concentrado entre 65-75, com pico em 70.
  - Frequencia: Maioria acima de 80%.
  - Horas_Estudadas: Média ~19, variando de 1 a 44.
- **Correlações Chave** (com Nota_Exame): Frequencia (0.58), Horas_Estudadas (0.45), Notas_Anteriores (0.18).

## Pergunta Estratégica e Direcionadora
**Quais são os fatores acadêmicos, comportamentais, familiares e escolares mais influentes no desempenho dos estudantes em exames?**

Essa pergunta guia toda a análise exploratória de dados (AED), dashboards e storytelling no Tableau, focando em insights acionáveis para educadores e pais.

## Outras Perguntas que a AED Vai Responder
1. Qual é a distribuição das notas dos exames e quais fatores correlacionam mais fortemente com o desempenho?
2. Como o envolvimento parental e o acesso a recursos afetam as notas?
3. Há diferenças significativas no desempenho por gênero, renda familiar ou tipo de escola?
4. Quais variáveis comportamentais (como sono, motivação e atividades físicas) impactam mais as notas?
5. Podemos prever notas altas com base em fatores como frequência e horas de estudo?

## Protótipo do Dashboard
O dashboard no Tableau será dividido em seções interativas, com filtros globais (ex.: gênero, renda). Layout sugerido: KPIs à esquerda, gráficos no centro, tabela final à direita.

### Pergunta: Quais são os KPIs principais do desempenho acadêmico?
- **KPIs Iniciais**: Média de Nota_Exame (ex.: 67.7), Taxa de Aprovação (>70: 60%), Correlação Máxima (Frequencia: 0.58).
- **Insights dos KPIs**: Alunos com frequência >80% têm notas 15% maiores; renda alta correlaciona com acesso a recursos.

### Pergunta: Como as variáveis numéricas se relacionam com as notas?
- **Gráficos**:
  - Scatter plot: Horas_Estudadas vs. Nota_Exame (tendência positiva).
  - Box plot: Frequencia por faixas vs. Nota_Exame.
  - Heatmap: Correlação entre todas as numéricas.

### Pergunta: Quais fatores categóricos influenciam mais o desempenho?
- **Gráficos**:
  - Bar chart: Média de Nota_Exame por Envolvimento_Parental.
  - Violin plot: Distribuição de Nota_Exame por Genero.
  - Stacked bar: Nota_Exame por Renda_Familiar e Tipo_Escola.

### Pergunta: Qual é o resumo consolidado dos insights?
- **Tabela Final**: Tabela dinâmica com médias por grupo (ex.: filtro por gênero), destacando top fatores.

## O que Precisamos Fazer a Partir dos Dados
Para transformar os dados e atingir os objetivos (responder perguntas, criar dashboards):
1. **Limpeza (ETL)**: Remover nulos (raros), padronizar textos (ex.: "Low" → "Baixo"), converter tipos (numéricos para float se necessário).
2. **Agregações**: Calcular médias, correlações e percentis por grupos (ex.: média de Nota_Exame por Genero).
3. **Normalização**: Escalar variáveis numéricas para comparações (ex.: z-score para Horas_Estudadas).
4. **Feature Engineering**: Criar novas colunas (ex.: "Categoria_Desempenho" baseado em Nota_Exame: Baixo <65, Médio 65-80, Alto >80).
5. **Validação**: Verificar consistência (ex.: Frequencia <=100), outliers (ex.: Horas_Estudadas >40).
Objetivo: Dados prontos para Tableau, focando em visualizações que respondam às perguntas estratégicas.

## Tableau - Montar os Gráficos
Usaremos o Tableau Desktop/Public. Passos gerais: Conectar ao CSV, arrastar campos para prateleiras (Rows/Columns), aplicar filtros e formatação.

### 1. Gráfico: Distribuição de Notas dos Exames (Histograma)
   - **Pergunta Respondida**: Qual é a distribuição das notas?
   - **Como Construir**:
     1. Conectar ao `StudentPerformanceFactors.csv`.
     2. Arrastar `Nota_Exame` para Columns (como dimensão contínua).
     3. Tableau cria automaticamente bins; ajustar para 10 intervalos.
     4. Adicionar linha de média (Analysis > Add Reference Line).
   - **Configurações**: Cor azul, título "Distribuição de Notas dos Exames". Mostra pico em 70, assimetria à esquerda.

### 2. Gráfico: Correlação Horas de Estudo vs. Notas (Scatter Plot)
   - **Pergunta Respondida**: Há relação entre horas de estudo e notas?
   - **Como Construir**:
     1. Arrastar `Horas_Estudadas` para Columns, `Nota_Exame` para Rows.
     2. Adicionar linha de tendência (Analysis > Trend Lines > Linear).
     3. Cor por `Genero` para diferenciação.
   - **Configurações**: Eixo X: 0-50, Y: 50-100. Mostra correlação positiva (~0.45).

### 3. Gráfico: Média de Notas por Envolvimento Parental (Bar Chart)
   - **Pergunta Respondida**: Como o envolvimento parental afeta as notas?
   - **Como Construir**:
     1. Arrastar `Envolvimento_Parental` para Columns, `Nota_Exame` (média) para Rows.
     2. Ordenar barras decrescente.
   - **Configurações**: Cores: Verde para Alto, Vermelho para Baixo. Mostra diferença de ~10 pontos entre Alto e Baixo.

### 4. Gráfico: Heatmap de Correlações
   - **Pergunta Respondida**: Quais variáveis numéricas correlacionam?
   - **Como Construir**:
     1. Criar campo calculado para correlação (usar Tableau's correlation matrix ou importar de Python).
     2. Usar `Heatmap` chart type; Rows/Columns com variáveis numéricas.
   - **Configurações**: Escala de cores vermelho-azul. Destaque Frequencia-Nota_Exame (0.58).

### 5. Gráfico: Distribuição por Gênero (Violin Plot)
   - **Pergunta Respondida**: Há diferenças por gênero?
   - **Como Construir**:
     1. Arrastar `Genero` para Columns, `Nota_Exame` para Rows.
     2. Mudar para Violin Plot (se disponível; senão, usar Box Plot).
   - **Configurações**: Comparar medianas; adicionar tooltips com médias.

### 6. Tabela: Resumo por Grupos
   - **Pergunta Respondida**: Qual é o resumo consolidado?
   - **Como Construir**:
     1. Criar sheet com `Genero`, `Renda_Familiar` em Rows.
     2. `Nota_Exame` (média) em Text.
     3. Adicionar filtros interativos.
   - **Configurações**: Formatação condicional (verde para >70).

Esses gráficos formarão o dashboard interativo, com storytelling: "Da correlação à ação – melhore a frequência para elevar notas!"

## Verificação de Omissões
- **Limitações**: Dataset sintético (não real), possível viés em categorias (ex.: mais alunos de renda média). Não inclui fatores externos como saúde mental.
- **Ética**: Dados anônimos, mas evitar generalizações por gênero/renda.
- **Próximos Passos**: Após dashboard, testar modelos preditivos (ex.: regressão linear no Python) e integrar ao storytelling.
- **Falta Algo?**: Se precisar de mais gráficos (ex.: mapas por Distancia_Casa) ou ajustes, avise!

## Arquivos e Transformações para Tableau
- **Notebook de Preparação**: `python/preparacao_tableau.ipynb` - Contém todas as transformações em Python, incluindo padronização de textos para português, criação de colunas como `Categoria_Desempenho` e `Faixa_Frequencia`, e normalização de `Horas_Estudadas` com z-score.
- **Arquivo Transformado**: `StudentPerformanceFactors_transformado.csv` - Versão otimizada do dataset original, pronta para importação no Tableau com labels em português e novas features para dashboards interativos.
