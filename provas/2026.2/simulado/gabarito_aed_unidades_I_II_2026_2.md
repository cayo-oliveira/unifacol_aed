# Gabarito do simulado ENADE — Análise Exploratória de Dados

**Unidades I e II · 2026.2 · Uso docente**

Este arquivo acompanha o caderno de questões de AED. A resposta discursiva apresenta um caminho possível, em linguagem natural; não precisa ser reproduzida literalmente. Na correção, valorize a leitura conjunta dos indicadores, a escolha de visuais que respondam à pergunta e uma decisão proporcional à evidência.

## Questões objetivas

| Questão | Resposta | Justificativa para correção |
|---|---|---|
| 9 | **D** | A soma dos dez tempos é 140 minutos; média = 140 ÷ 10 = **14**. Ordenados, os valores centrais são 8 e 8, então a mediana é **8**. Os tempos altos, especialmente 27 e 50, puxam a média para cima. |
| 10 | **A** | A série do Centro é 80, 84, 82, 58, 61 e 83. Há queda acentuada na semana 4, pequena recuperação na 5 e retorno a 83 na 6: não é uma redução estável. A leitura exige comparar os pontos ao longo das semanas, não inferir tendência de um único valor. |
| 11 | **C** | Uma consulta em linguagem natural deve usar a camada semântica aprovada, excluir pedidos cancelados e respeitar o acesso regional da gerente (Norte e Sul, não Centro). A SQL e os filtros gerados precisam ser validados antes de apresentar o resultado. |

## Questão 12 — resposta-modelo

> Eu não concluiria que o chatbot melhorou o atendimento só porque a média caiu de 18 para 14 minutos. O P90 subiu de 34 para 49 minutos, as reaberturas foram de 9% para 17% e a resolução no primeiro contato caiu de 71% para 66%; então a média esconde uma piora importante para parte dos clientes e na qualidade. Além disso, houve uma campanha e não há grupo de controle, por isso a comparação antes/depois não prova que o chatbot causou a mudança. Eu manteria o piloto com supervisão e investigaria os casos longos e reabertos. Para visualizar, compararia as distribuições dos tempos por período, por exemplo com boxplots, e acompanharia semanalmente P90, reabertura e resolução no primeiro contato, sempre mostrando volume e denominador. Eu só ampliaria depois de algumas semanas com metas de qualidade definidas e resultados consistentes, comparando períodos equivalentes e registrando a campanha e outras mudanças.

### Rubrica de correção — 10 pontos

| Critério observável | Como atribuir os pontos | Pontos |
|---|---|---:|
| Interpreta os indicadores em conjunto | **1 ponto:** diz que a média caiu (18→14), mas o P90 subiu (34→49). **1 ponto:** nota aumento de reaberturas (9%→17%). **1 ponto:** nota queda da resolução no primeiro contato (71%→66%) e conclui que os indicadores não sustentam a frase “melhorou” baseada só na média. | 3 |
| Reconhece limite causal do antes/depois | **1 ponto:** menciona que não houve grupo de controle ou comparação equivalente. **1 ponto:** relaciona a campanha/aumento de contatos (ou outro fator concorrente) à impossibilidade de atribuir a mudança ao chatbot. | 2 |
| Escolhe visualizações adequadas | **1 ponto:** propõe boxplot, histograma ou visual equivalente que compare a distribuição dos tempos entre períodos/semanas. **1 ponto:** propõe gráfico de linhas/série temporal semanal para indicadores de qualidade (ou visual equivalente), com períodos identificados e taxas/denominadores interpretáveis. | 2 |
| Recomenda decisão proporcional | **1 ponto:** mantém/restringe o piloto sob supervisão ou condiciona a expansão; não recomenda expansão irrestrita só pela média. **1 ponto:** define meta observável ligada à linha de base (por exemplo, P90 ≤34 min, reaberturas ≤9% ou resolução no primeiro contato ≥71%). **1 ponto:** define janela/condição para reavaliar (por exemplo, resultados estáveis por algumas semanas) e/ou indica fonte e comparação dos dados. | 3 |
| **Total** |  | **10** |

**Orientação ao corretor — exemplos de formulações aceitáveis:** “a média melhorou, mas a cauda e a qualidade pioraram”; “não dá para saber se foi o chatbot ou a campanha”; “usaria boxplots para comparar os tempos e linhas semanais para reabertura e resolução”; “não ampliaria ainda; avaliaria de novo quando o P90 voltar a 34 minutos ou menos e a taxa de reabertura ficar em 9% ou menos por quatro semanas”. São exemplos, não resposta única. Aceite metas e gráficos equivalentes se forem claros e adequados. Não dê o ponto causal se o aluno afirmar que o chatbot causou a mudança com base somente nesse antes/depois.
