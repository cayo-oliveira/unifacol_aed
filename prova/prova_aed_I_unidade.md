# PROVA I UNIDADE — ANÁLISE EXPLORATÓRIA DE DADOS 2026.1

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

### Questão 1 (2,0 pontos) — Qualidade de Dados e Dicionário de Dados

A Secretaria Municipal de Saúde de uma cidade do interior de Pernambuco contratou uma consultoria para analisar dados de atendimentos em Unidades Básicas de Saúde (UBS). O arquivo recebido, `atendimentos_ubs_2025.csv`, contém 47.832 registros e as seguintes colunas:

| Coluna | Descrição informada | Exemplo de valores encontrados |
|--------|---------------------|-------------------------------|
| `id_atend` | Identificador único | 1, 2, 3, ..., 47832 |
| `data_atend` | Data do atendimento | "15/03/2025", "2025-03-16", "março/2025" |
| `cpf_paciente` | CPF do paciente | "123.456.789-00", "12345678900", NULL |
| `idade` | Idade em anos | 25, "32 anos", -5, 150, NULL |
| `sexo` | Sexo do paciente | "M", "F", "Masculino", "feminino", "1", "2" |
| `cid` | Código CID-10 | "J11", "j11", "GRIPE", NULL |
| `ubs_codigo` | Código da UBS | 101, 102, 103, 999 |
| `profissional` | Nome do profissional | "Dr. Silva", "DRA SILVA", "dr silva" |

A equipe de análise identificou que 2.341 registros possuem o mesmo `cpf_paciente` repetido em datas diferentes (o que é esperado, pois um paciente pode ter múltiplos atendimentos). Porém, 847 registros possuem exatamente o mesmo `cpf_paciente`, `data_atend` e `cid` — caracterizando duplicatas reais. Além disso, 12% dos registros possuem `cpf_paciente` como NULL.

Antes de iniciar qualquer análise exploratória, a consultoria precisa criar um documento formal que especifique, para cada coluna: o nome padronizado, o tipo de dado esperado, o domínio de valores válidos, a regra de preenchimento (obrigatório ou opcional) e como tratar inconsistências.

Considerando o cenário descrito e as boas práticas de preparação de dados, qual alternativa apresenta **corretamente** a sequência de ações que a consultoria deve executar **antes** de calcular qualquer estatística descritiva?

A) Criar dicionário de dados → padronizar formatos (datas, CPF, sexo, CID) → remover 847 duplicatas reais → decidir estratégia para os 12% de CPF nulos → validar domínios (idade entre 0-120, UBS existentes)

B) Calcular média de idade → criar dicionário de dados → remover todos os 2.341 registros com CPF repetido → padronizar formatos

C) Remover imediatamente todos os registros com qualquer valor NULL → criar dicionário de dados → calcular estatísticas

D) Criar dicionário de dados → remover os 12% de registros com CPF nulo → manter as 847 duplicatas para não perder dados → calcular estatísticas

E) Padronizar formatos → calcular estatísticas com os dados brutos → criar dicionário de dados ao final para documentar as decisões tomadas

---

### Questão 2 (2,0 pontos) — Medidas de Tendência Central e Dispersão

Uma rede de supermercados com 8 lojas na Região Metropolitana do Recife está avaliando o desempenho de vendas do setor de hortifrúti. O gerente regional coletou os dados de faturamento mensal (em R$) de cada loja referentes a janeiro de 2026:

| Loja | Localização | Faturamento Jan/2026 (R$) |
|------|-------------|---------------------------|
| L1 | Boa Viagem | 45.000 |
| L2 | Casa Forte | 52.000 |
| L3 | Olinda Centro | 38.000 |
| L4 | Paulista | 41.000 |
| L5 | Piedade | 39.000 |
| L6 | Jaboatão | 36.000 |
| L7 | Camaragibe | 35.000 |
| L8 | Derby (flagship) | 142.000 |

O gerente precisa apresentar um relatório para a diretoria sobre o "faturamento típico" das lojas. Um estagiário calculou a média aritmética e obteve R$ 53.500. Porém, o analista sênior argumentou que essa medida não representa adequadamente a realidade da maioria das lojas, sugerindo o uso da mediana.

Adicionalmente, a diretoria solicitou uma análise de dispersão para entender a variabilidade entre as lojas. O analista calculou os seguintes valores:
- Ordenando os faturamentos: 35.000, 36.000, 38.000, 39.000, 41.000, 45.000, 52.000, 142.000
- Q1 (primeiro quartil): 37.000
- Q3 (terceiro quartil): 48.500
- IQR (intervalo interquartil): 11.500

Considerando os dados apresentados, os cálculos realizados e os conceitos de estatística descritiva aplicados à análise exploratória de dados, qual alternativa apresenta **corretamente** a mediana, a classificação da loja L8 quanto a outliers (usando o critério 1,5×IQR), e a justificativa para preferir a mediana neste contexto?

A) Mediana = R$ 40.000; L8 é outlier (limite superior = R$ 65.750); a mediana é preferível porque é resistente a valores extremos e representa melhor o faturamento típico das 7 lojas "normais"

B) Mediana = R$ 41.000; L8 não é outlier; a média é preferível porque considera todos os valores

C) Mediana = R$ 53.500; L8 é outlier; a média e a mediana são equivalentes neste caso

D) Mediana = R$ 40.000; L8 não é outlier (limite superior = R$ 142.000); deve-se usar a média para não ignorar a loja flagship

E) Mediana = R$ 39.000; L8 é outlier; a moda seria a medida mais adequada neste contexto

---

### Questão 3 (2,0 pontos) — Distribuições, Histogramas e Dados Ausentes

Uma fintech que oferece microcrédito para pequenos empreendedores do Nordeste está analisando sua base de clientes para desenvolver um modelo de score de crédito. O dataset `clientes_microcredito.csv` contém 15.000 registros com as seguintes características:

| Variável | Tipo | % Missing | Distribuição observada |
|----------|------|-----------|------------------------|
| `renda_mensal` | Numérica | 8% | Assimétrica à direita (cauda longa para valores altos) |
| `idade` | Numérica | 0% | Aproximadamente simétrica, centrada em 35 anos |
| `tempo_negocio_meses` | Numérica | 15% | Bimodal (picos em 6 e 36 meses) |
| `inadimplente` | Categórica | 0% | 18% "Sim", 82% "Não" |
| `segmento` | Categórica | 22% | "Alimentação" 40%, "Vestuário" 25%, "Serviços" 35% |

A analista de dados precisa preparar esse dataset para visualização no Tableau. Ela construiu histogramas para as variáveis numéricas e observou os seguintes padrões:

**Histograma de `renda_mensal`**: A maioria das observações está concentrada entre R$ 1.000 e R$ 3.000, mas há uma cauda que se estende até R$ 25.000, com poucos casos acima de R$ 15.000.

**Histograma de `tempo_negocio_meses`**: Há dois picos claros — um em torno de 6 meses (empreendedores iniciantes) e outro em torno de 36 meses (empreendedores estabelecidos). O vale entre os picos está em aproximadamente 18 meses.

A equipe está debatendo como tratar os dados ausentes antes de criar os dashboards. O gerente de produto argumenta que os 22% de missing em `segmento` são problemáticos porque essa variável é fundamental para segmentar os dashboards por tipo de negócio.

Considerando as características das distribuições, os percentuais de dados ausentes e o objetivo de criar visualizações no Tableau, qual alternativa apresenta **corretamente** a análise das distribuições e a estratégia mais apropriada para o tratamento dos dados ausentes na variável `segmento`?

A) A distribuição de `renda_mensal` indica que a mediana é mais representativa que a média; a distribuição bimodal de `tempo_negocio_meses` sugere dois grupos distintos de clientes; para `segmento`, deve-se criar uma categoria "Não informado" e incluí-la como filtro no Tableau, permitindo análises com e sem esses registros

B) A distribuição de `renda_mensal` é normal; a distribuição bimodal deve ser tratada removendo os valores do vale; deve-se imputar `segmento` com a moda ("Alimentação") para todos os 22% ausentes

C) A assimetria à direita indica que a média é mais representativa; a bimodalidade é um erro de coleta que deve ser corrigido; deve-se remover todos os registros com `segmento` ausente

D) Todas as distribuições são problemáticas e o dataset deve ser descartado; dados com mais de 10% de missing são inválidos para análise

E) A distribuição de `renda_mensal` é simétrica; `tempo_negocio_meses` tem distribuição uniforme; deve-se preencher `segmento` com valores aleatórios para manter o tamanho da amostra

---

### Questão 4 (2,0 pontos) — Correlação, Scatter Plot e Análise Bivariada

O Departamento de Educação de um estado brasileiro está investigando fatores associados ao desempenho de estudantes do Ensino Médio. Um pesquisador coletou dados de 500 escolas públicas e construiu a seguinte matriz de correlação (coeficiente de Pearson):

|  | Nota ENEM | Horas Estudo/Sem | Renda Familiar | Escolaridade Pais | Acesso Internet |
|--|-----------|------------------|----------------|-------------------|-----------------|
| **Nota ENEM** | 1,00 | 0,72 | 0,68 | 0,65 | 0,45 |
| **Horas Estudo/Sem** | 0,72 | 1,00 | 0,31 | 0,28 | 0,22 |
| **Renda Familiar** | 0,68 | 0,31 | 1,00 | 0,78 | 0,71 |
| **Escolaridade Pais** | 0,65 | 0,28 | 0,78 | 1,00 | 0,62 |
| **Acesso Internet** | 0,45 | 0,22 | 0,71 | 0,62 | 1,00 |

O pesquisador também construiu scatter plots segmentados por região (urbana vs. rural) e observou que:
- Na região **urbana**: a correlação entre Horas de Estudo e Nota ENEM é r = 0,75
- Na região **rural**: a correlação entre Horas de Estudo e Nota ENEM é r = 0,58

Além disso, ao analisar o scatter plot de Renda Familiar vs. Nota ENEM, o pesquisador identificou um padrão interessante: a relação parece ser mais forte até aproximadamente R$ 10.000 de renda familiar, e depois "achata" (a nota não aumenta muito mesmo com renda muito maior).

Um secretário de educação, ao ver os resultados, afirmou: "Está provado que aumentar as horas de estudo causa melhoria nas notas do ENEM. Devemos implementar políticas de aumento obrigatório da carga horária."

Considerando os conceitos de correlação, causalidade e análise exploratória de dados, qual alternativa apresenta **corretamente** a interpretação dos resultados e a avaliação da afirmação do secretário?

A) A correlação de 0,72 indica associação positiva forte entre horas de estudo e nota, mas não prova causalidade; a diferença entre regiões (0,75 vs 0,58) sugere que o contexto modera essa relação; a alta correlação entre renda e escolaridade dos pais (0,78) indica possível confundidor; o secretário está cometendo a falácia de inferir causalidade de correlação

B) A correlação de 0,72 prova que mais horas de estudo causam notas maiores; o secretário está correto em sua conclusão; a diferença entre regiões é irrelevante

C) Correlações acima de 0,70 sempre indicam causalidade; o padrão de "achatamento" na relação renda-nota é um erro de medição

D) A matriz mostra que todas as variáveis têm correlação negativa com a nota ENEM; o secretário deveria reduzir as horas de estudo

E) A correlação de 0,72 é fraca e não permite nenhuma conclusão; scatter plots não são úteis para análise de correlação

---

### Questão 5 (2,0 pontos) — Variáveis Categóricas, Tabelas de Frequência e Análise Comparativa

Uma operadora de planos de saúde está analisando os motivos de cancelamento de contratos em 2025. O dataset contém 3.200 cancelamentos com as seguintes variáveis categóricas:

**Tabela 1: Distribuição por Motivo de Cancelamento**
| Motivo | Frequência Absoluta | Frequência Relativa |
|--------|---------------------|---------------------|
| Preço alto | 1.280 | 40,0% |
| Mudança de cidade | 640 | 20,0% |
| Insatisfação atendimento | 576 | 18,0% |
| Plano empresa encerrou | 416 | 13,0% |
| Óbito do titular | 192 | 6,0% |
| Outros | 96 | 3,0% |
| **Total** | **3.200** | **100,0%** |

**Tabela 2: Motivo de Cancelamento por Faixa Etária**
| Motivo | 18-30 anos | 31-50 anos | 51-65 anos | 65+ anos |
|--------|------------|------------|------------|----------|
| Preço alto | 55% | 42% | 35% | 22% |
| Mudança de cidade | 28% | 22% | 12% | 5% |
| Insatisfação atendimento | 10% | 18% | 22% | 25% |
| Plano empresa encerrou | 5% | 15% | 18% | 8% |
| Óbito do titular | 0% | 1% | 8% | 35% |
| Outros | 2% | 2% | 5% | 5% |

**Tabela 3: Tempo de Permanência no Plano antes do Cancelamento**
| Tempo | Frequência | % que citou "Preço alto" |
|-------|------------|--------------------------|
| < 1 ano | 960 | 52% |
| 1-3 anos | 1.120 | 45% |
| 3-5 anos | 640 | 32% |
| > 5 anos | 480 | 18% |

A diretoria está desenvolvendo estratégias de retenção e precisa entender os padrões de cancelamento para direcionar ações específicas. O gerente de marketing propôs focar exclusivamente em redução de preços, argumentando que "40% dos cancelamentos são por preço alto".

Considerando as três tabelas apresentadas e os princípios de análise exploratória de dados categóricos, qual alternativa apresenta **corretamente** os insights derivados das tabelas e a avaliação da proposta do gerente de marketing?

A) A proposta é simplista: embora "preço alto" seja o motivo mais frequente no geral, a análise por faixa etária revela que esse motivo é mais relevante para jovens (55%) do que para idosos (22%); além disso, a Tabela 3 mostra que a sensibilidade a preço diminui com o tempo de permanência (52% vs 18%); uma estratégia eficaz deveria segmentar ações: descontos para jovens recém-ingressos, e melhoria de atendimento para idosos de longo prazo

B) A proposta está correta: 40% é um percentual muito alto e justifica foco exclusivo em preço; as análises por faixa etária e tempo são irrelevantes

C) Os dados mostram que "óbito do titular" é o principal motivo e deve ser o foco da estratégia de retenção

D) A Tabela 2 está incorreta porque os percentuais de cada coluna não somam 100%; os dados devem ser descartados

E) A análise de frequência relativa é inútil; apenas a frequência absoluta importa para decisões de negócio

---

## GABARITO (uso exclusivo do professor)

| Q1 | Q2 | Q3 | Q4 | Q5 |
|----|----|----|----|----|
| A | A | A | A | A |

---

## Distribuição de Conteúdo

| Questão | Tópico | Semanas |
|---------|--------|---------|
| Q1 | ETL, dicionário de dados, qualidade (ausências, duplicadas, tipos) | 01-02 |
| Q2 | Medidas de tendência central (média, mediana, moda), dispersão (IQR), outliers | 03-04 |
| Q3 | Distribuições (histogramas, assimetria), dados ausentes (missing) | 05 |
| Q4 | Correlação (scatter), segmentação por categoria, correlação ≠ causalidade | 06 |
| Q5 | Variáveis categóricas (proporções, frequência, barras), análise comparativa | 07 |

---

## Notas para o Professor

### Q1 - Dicionário de Dados
- **Por que A é correta**: Segue a sequência lógica de preparação de dados — documentar primeiro (dicionário), depois limpar (padronizar, remover duplicatas reais, tratar nulos), depois validar domínios.
- **Armadilhas**: B confunde múltiplos atendimentos do mesmo paciente (válido) com duplicatas reais; C remove dados prematuramente; D mantém duplicatas erroneamente; E inverte a ordem lógica.

### Q2 - Mediana e Outliers
- **Cálculo da mediana**: Com 8 valores ordenados, mediana = média do 4º e 5º valores = (39.000 + 41.000)/2 = R$ 40.000
- **Cálculo do limite superior**: Q3 + 1,5 × IQR = 48.500 + 1,5 × 11.500 = 48.500 + 17.250 = R$ 65.750
- **L8 (R$ 142.000)**: 142.000 > 65.750, portanto é outlier.
- **Armadilhas**: B erra a mediana e classificação; C confunde média com mediana; D erra o limite; E erra a mediana e sugere moda inadequadamente.

### Q3 - Distribuições e Missing
- **Assimetria à direita**: Cauda para valores altos = média > mediana, logo mediana é mais representativa.
- **Bimodal**: Dois grupos distintos, não é erro — é informação útil para segmentação.
- **Estratégia para missing categórico**: Criar categoria "Não informado" preserva os registros e permite análise transparente.
- **Armadilhas**: B imputa com moda (pode distorcer); C remove dados desnecessariamente; D é extremista; E descreve errado as distribuições.

### Q4 - Correlação vs Causalidade
- **0,72 é forte mas não é causalidade**: Associação não implica relação de causa-efeito.
- **Confundidor**: Renda e escolaridade dos pais (0,78) podem explicar parte da relação horas-nota.
- **Diferença urbano/rural**: Mostra que o contexto importa — a relação não é universal.
- **Armadilhas**: B comete falácia de causalidade; C inventa regra; D interpreta sinais errado; E subestima 0,72.

### Q5 - Análise Categórica Segmentada
- **Insight principal**: O percentual geral (40%) esconde variações importantes por segmento.
- **Jovens vs Idosos**: Padrões de cancelamento são muito diferentes — estratégias devem ser diferenciadas.
- **Tempo de permanência**: Clientes antigos são menos sensíveis a preço — fidelização importa.
- **Armadilhas**: B ignora segmentação; C é absurda; D não entende que cada coluna soma 100% separadamente (são proporções condicionais); E desvaloriza frequência relativa.
