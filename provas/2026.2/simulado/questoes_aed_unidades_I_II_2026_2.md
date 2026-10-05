# Simulado ENADE — Análise Exploratória de Dados — Unidades I e II (2026.2)

Material temático extraído do simulado integrado de Sistemas de Informação. Os casos, organizações e dados são simulados para fins didáticos. Questões discursivas devem ser respondidas em até 15 linhas.

---

## Questão 9 — O resumo do LLM chamou de “típico” o tempo médio

### Radar de atendimento | Central Conecta, publicação simulada

Uma central de atendimento lançou um painel em que um LLM resume indicadores para a reunião diária da operação. Ao analisar dez chamados encerrados durante um turno de teste, o assistente publicou: “o chamado típico é resolvido em 14 minutos; portanto, a maioria das pessoas espera aproximadamente esse tempo”. A frase foi copiada para um canal interno antes da conferência. A analista observou que a média podia estar calculada corretamente, mas questionou se descrevia um chamado típico ou a experiência da maioria.

Para revisar a mensagem, a equipe isolou dez tempos, todos em minutos e referentes ao mesmo tipo de solicitação. O gráfico de barras apresenta, para cada duração observada, quantos chamados tiveram aquele tempo; o eixo horizontal preserva a distância entre os valores e o vertical mostra a frequência. O resumo será usado para discutir escala de pessoal, não para avaliar atendentes individualmente; por isso, a equipe precisa comunicar o centro do conjunto e a influência de valores distantes, sem apagar observações válidas só por serem incomuns.

**Figura 1 — Frequência dos tempos de resolução dos chamados**

![Gráfico de barras: eixo horizontal com duração em minutos e eixo vertical com frequência. A barra de 8 minutos tem altura 2; as barras de 4, 5, 6, 7, 10, 15, 27 e 50 minutos têm altura 1.](figuras/simulado_enade_aed/aed_q09_frequencia_tempos.png)

*Fonte: dados simulados para fins didáticos.*

Qual revisão do texto do LLM descreve melhor o conjunto e reduz o risco de induzir a gerência a uma interpretação equivocada?

A) Manter a frase, pois a média sempre corresponde ao tempo de um chamado observado.

B) Trocar a média por 50 minutos, pois o maior valor representa melhor o desempenho de toda a central.

C) Excluir os registros de 27 e 50 minutos antes de calcular qualquer resumo, pois pontos distantes não pertencem ao conjunto.

D) Informar que a mediana é 8 minutos e que a média de 14 minutos é influenciada pelos chamados de 27 e 50 minutos; as duas medidas respondem a perguntas diferentes.

E) Informar que 8 minutos é a moda e, por isso, a média de 14 minutos está necessariamente errada.
## Questão 10 — O copiloto anunciou recuperação em todas as lojas

### Pauta de dados | Rede BomVizinho, cenário simulado

Uma rede de mercados incorporou um copiloto ao painel usado nas reuniões regionais. Ao receber a pergunta “como evoluíram as vendas nas últimas seis semanas?”, o LLM produziu a síntese: “as vendas se mantiveram estáveis em todas as lojas”. O texto seria incluído no boletim das gerências, mas a diretora pediu que a equipe verificasse se a frase descrevia as trajetórias individuais ou escondia diferenças num total agregado.

O conjunto compara o índice semanal de três lojas com perfis distintos: uma unidade central de alto fluxo, uma loja de bairro e uma unidade próxima a uma rodovia. Antes de compartilhar o comentário, a analista abriu o gráfico de linhas construído a partir dos mesmos registros. A decisão importa porque a diretoria pretende direcionar estoque e equipe para o mês seguinte; um resumo que apaga uma queda localizada pode levar a uma intervenção inadequada, mesmo quando o valor final parece próximo ao inicial.

**Figura 2 — Vendas semanais por loja (índice)**

![Gráfico de linhas com eixo horizontal Semana de acompanhamento (1 a 6) e eixo vertical Índice de vendas (pontos), em escala de 0 a 100. Centro: 80, 84, 82, 58, 61 e 83; Norte: 62, 65, 67, 68, 66 e 69; Sul: 45, 57, 42, 59, 39 e 61.](figuras/simulado_enade_aed/aed_q10_series_vendas.png)

*Fonte: dados simulados para fins didáticos. No PDF, os valores são apresentados em gráfico de linhas.*

Qual revisão da resposta do copiloto corresponde melhor às evidências?

A) Informar que Centro caiu de 82 para 58 entre as semanas 3 e 4, recuperou-se nas semanas seguintes e terminou em 83; a trajetória não foi estável.

B) Confirmar que todas as lojas ficaram estáveis, pois os valores finais são próximos dos valores iniciais.

C) Afirmar que Norte sofreu a maior queda, pois sua série contém uma redução entre as semanas 4 e 5.

D) Concluir que Sul vendeu mais em todo o período, pois sua variação semanal foi maior.

E) Somar as três séries em um único total e manter a frase original, pois o agregado substitui a comparação entre lojas.
## Questão 11 — O LLM montou uma consulta, mas quem autorizou os dados?

### Nota de governança | Grupo Varejo Vivo, empresa fictícia

Uma rede varejista implantou uma interface em que gerentes consultam o desempenho das lojas em linguagem natural. Para a solicitação “compare o valor médio dos pedidos por região no trimestre”, o LLM gerou SQL e apresentou uma tabela com totais e uma narrativa segura. A gerente percebeu que os valores não batiam com o painel financeiro oficial e abriu um chamado. A equipe constatou dois problemas: a consulta contou pedidos cancelados, embora a definição corporativa de “pedido concluído” os exclua, e a credencial de serviço consultou uma região não liberada para aquela gerente.

A organização não quer retirar o recurso conversacional, que pode facilitar a exploração por pessoas sem domínio de SQL. Porém, uma explicação em linguagem natural sobre o código produzido não garante que a consulta respeitou o significado do indicador, os filtros de negócio ou a autorização do usuário. Antes da publicação, o resultado precisa ser verificável contra definições mantidas pela área de dados e permissões já aplicadas aos relatórios oficiais.

O registro de auditoria resumiu a divergência:

| Evidência da auditoria | Definição aprovada ou execução observada |
|---|---|
| Métrica oficial | Valor médio somente de pedidos concluídos; pedidos cancelados são excluídos. |
| Escopo autorizado à gerente | Regiões Norte e Sul. |
| Consulta produzida pelo LLM | Incluiu pedidos cancelados e consultou também a região Centro. |

*Fonte: dados elaborados para fins didáticos.*

*Fonte: nota de governança simulada.*

Qual controle deve ser priorizado antes de exibir a resposta como resultado oficial?

A) Pedir ao LLM que explique o SQL em linguagem simples e considerar a explicação suficiente para validar a consulta.

B) Dar ao assistente acesso de administrador para que ele encontre a tabela mais completa e decida qual definição parece adequada.

C) Usar camada semântica e definições aprovadas, aplicar as permissões do usuário à consulta e validar SQL, filtros e resultado antes da publicação.

D) Ocultar o nome da tabela no resultado, mantendo a consulta e as permissões atuais.

E) Trocar SQL por uma resposta textual livre, pois linguagem natural não consulta registros restritos.
## Questão 12 — O dashboard gerado por IA melhorou a experiência?

### Painel de resultados | Central Conecta, dados simulados

Após o primeiro mês de um chatbot com LLM, uma central de atendimento recebeu um resumo automático: “o chatbot melhorou o atendimento porque o tempo médio diminuiu”. O texto usava um único indicador e recomendava ampliar a automação para todos os chamados. A gerente pediu uma revisão: além da média, a equipe acompanha a cauda da distribuição, chamados reabertos e resolução no primeiro contato, pois respostas rápidas que exigem correções podem aumentar o trabalho total.

O painel abaixo compara o mês anterior ao lançamento com o primeiro mês de uso. As escalas horizontais mantêm unidades distintas em dois painéis para não misturar minutos e percentuais. Os períodos têm duração semelhante e as definições dos indicadores foram mantidas, mas o piloto não teve grupo de controle nem implantação aleatória; nesse intervalo também houve uma campanha que elevou o volume de contatos. Assim, os dados descrevem mudanças observadas, mas não isolam por si sós o efeito causal do chatbot. A central mantém os tempos e desfechos de cada chamado e os agregados semanais, embora o painel apresente apenas os dois períodos. A equipe precisa interpretar evidências, escolher visualizações que revelem distribuição e evolução e propor uma decisão operacional que possa ser revista com novos dados.

![Comparação em dois painéis: tempos em minutos e qualidade em porcentagens, cada qual com seu eixo horizontal e os indicadores no eixo vertical. Antes/depois: média 18/14 min; percentil 90 34/49 min; reabertos 9/17%; resolvidos no primeiro contato 71/66%.](figuras/simulado_enade_aed/aed_q12_comparacao_indicadores.png)

*Fonte: painel e dados elaborados para fins didáticos.*

Em até 15 linhas, revise a conclusão gerada pelo assistente. Interprete conjuntamente os indicadores, indique uma visualização para acompanhar a distribuição dos tempos e outra para a evolução da qualidade ao longo das semanas, e proponha uma decisão para o piloto com uma condição verificável para nova avaliação.

---

---

# Gabarito e critérios — uso docente

| Questão | Gabarito | Raciocínio central e erros diagnosticados |
|---|---|---|
| 9 | D | A mediana é 8; a soma dos dez registros é 140 e a média é 14. Os valores 27 e 50 elevam a média, que não significa que a maioria dos chamados durou esse tempo. |
| 10 | A | Centro cai de 82 para 58 entre as semanas 3 e 4 e termina em 83, após se recuperar; a série não ficou estável. |
| 11 | C | Semântica aprovada, autorização herdada do usuário e validação da consulta e do resultado são necessárias antes da publicação. |

## Padrão de resposta — Questão 12 (10 pontos)

- **3 pontos:** corrige a conclusão: a média caiu, mas P90 e reaberturas subiram e a resolução no primeiro contato caiu; reconhece que o desenho antes/depois, com campanha concomitante e sem controle, não demonstra causalidade.
- **2 pontos:** sugere boxplot ou histograma comparativo para a distribuição dos tempos.
- **2 pontos:** sugere série temporal para reabertura e resolução no primeiro contato.
- **3 pontos:** recomenda manter/restringir o piloto até atingir metas verificáveis e avaliar periodicamente as respostas e fontes usadas pelo assistente.

Aceitar limiares diferentes quando definidos com base na linha anterior e acompanhados de prazo e fonte de dados.

## Base e limites

Os cenários são simulados; preços e resultados são dados didáticos. A seleção relaciona usos atuais de LLM a objetos previstos nas diretrizes de Sistemas de Informação para 2026 — probabilidade e estatística, engenharia de software, gestão da informação, segurança, banco de dados, visualização e ciência de dados — sem afirmar que LLM seja um objeto explicitamente listado nem prever itens futuros. Este caderno temático de 12 questões também não reproduz a composição oficial de 2026.

Referências: [Diretrizes de Sistemas de Informação para o Enade 2026 — Portaria Inep nº 168/2026](https://www.in.gov.br/web/dou/-/portaria-n-168-de-14-de-abril-de-2026-699946315); [provas e gabaritos oficiais de Sistemas de Informação — Inep, incluindo 2021](https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/enade/provas-e-gabaritos/2021); [Guia de Elaboração e Revisão de Itens — Inep, 2026](https://download.inep.gov.br/bni/enade/guia_de_elaboracao_revisao_de_itens_v1.pdf); matriz curricular local em `.agents/skills/trilha-unifacol/references/disciplinas.md`.
