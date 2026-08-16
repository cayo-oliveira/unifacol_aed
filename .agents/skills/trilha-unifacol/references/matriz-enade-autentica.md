# Matriz de itens ENADE autênticos — UNIFACOL 2026.2

Esta referência operacionaliza a criação e a revisão de questões para Tópicos Integradores, Inteligência Artificial e Análise Exploratória de Dados. Ela prevalece sobre instruções legadas que tratem extensão artificial do texto, “armadilhas” ou “anti-IA” como características do ENADE.

## Sumário

1. Evidências auditadas
2. O que caracteriza um item ENADE
3. O que o caderno oficial de SI 2021 ensina
4. Auditoria do template legado local
5. Matriz de 15 itens por capítulo
6. Banco reservado e derivação das provas
7. Versões A/B
8. Resistência a respostas superficiais de IA
9. Checklist de autoria
10. Exemplos-modelo para validar o padrão

## Evidências auditadas

### Acervo local

- `provas/template_prova_enade/2021_PV_bacharelado_sistema_informacao.pdf`: caderno oficial do ENADE 2021 para Sistemas de Informação, com 40 páginas.
- `provas/template_prova_enade/2021_GB_bacharelado_sistema_informacao.pdf`: gabarito oficial.
- `provas/template_prova_enade/2021_bacharelado_sistema_de_informacao.pdf`: padrões oficiais das cinco respostas discursivas.
- `provas/template_prova_enade/template_prova_enade.md`: template legado local, útil para o cabeçalho institucional, mas desatualizado quanto a quantidade de questões, dificuldade e integridade dos distratores.
- Os templates homônimos nos repositórios de IA e AED repetem essencialmente o mesmo texto legado e não constituem evidência adicional de padrão oficial.

### Fontes oficiais do Inep/MEC

- [Guia de Elaboração e Revisão de Itens do BNI-Enade, 3ª edição, Inep/MEC, 2026](https://download.inep.gov.br/bni/enade/guia_de_elaboracao_revisao_de_itens_v1.pdf).
- [Portal oficial de provas, gabaritos e padrões de resposta do Enade](https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/enade/provas-e-gabaritos).
- [Provas, gabaritos e padrões de resposta do Enade 2023, incluindo Engenharia da Computação](https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/enade/provas-e-gabaritos/2023).
- [Diretrizes do Enade 2021, incluindo Sistemas de Informação, Ciência da Computação e ADS](https://www.gov.br/inep/pt-br/centrais-de-conteudo/legislacao/enade/2021).
- [Legislação do Enade, incluindo as Portarias nº 168 e nº 169 de 2026 para Sistemas de Informação e ADS](https://www.gov.br/inep/pt-br/centrais-de-conteudo/legislacao/enade).

Consulta realizada em 7 de agosto de 2026. Quando houver nova edição oficial, conferir se o Guia ou as portarias foram substituídos antes de gerar uma avaliação.

## O que caracteriza um item ENADE

O ponto de partida é a **encomenda**, e não um tema solto. Para cada item, definir previamente:

1. perfil profissional mobilizado;
2. competência a observar;
3. objeto de conhecimento necessário;
4. dificuldade pretendida;
5. tipo de item;
6. informação complementar, como a necessidade de tabela, gráfico, diagrama ou código.

Um item objetivo constitui uma unidade textual formada por:

1. **texto-base ou situação-estímulo**, verbal ou não verbal;
2. **enunciado/comando**, que explicita a tarefa cognitiva;
3. **cinco opções**, com uma única resposta correta e quatro distratores plausíveis;
4. **justificativas privadas**, uma para o gabarito e uma para cada distrator.

Um item discursivo constitui uma unidade textual formada por:

1. **texto-base ou situação-estímulo**;
2. **enunciado**, com uma ou mais tarefas compatíveis com resposta de até 15 linhas;
3. **padrão de resposta privado**, com critérios independentes e respostas alternativas admissíveis.

### Texto-base e suporte visual

O texto-base pode ser notícia, fragmento de relatório, estudo de caso, situação-problema, tabela, quadro, gráfico, figura, mapa, esquema, diagrama, pseudocódigo, trecho de programa ou combinação desses recursos. O suporte precisa fornecer informação necessária à resolução; se puder ser removido sem alterar o raciocínio, ele é decoração e deve ser retirado.

Textos de terceiros devem vir de fonte fidedigna, possuir referência e respeitar direitos autorais. Textos e dados criados para o item devem ser identificados como `elaborado para fins didáticos`. Dados reais não podem ser alterados silenciosamente. Toda tabela ou figura deve ser citada no texto e interpretável em impressão em escala de cinza.

O ENADE não é definido por um “cabeçalho gigante”. O caderno oficial de Sistemas de Informação de 2021 alterna bases extensas, bases breves e suportes técnicos. A extensão é consequência do problema e das evidências necessárias. Alongar um enunciado sem função produz fadiga e diminui a validade do item.

### Comando

O comando deve indicar uma ação observável: analisar, selecionar, calcular, comparar, justificar, propor, diagnosticar, priorizar ou avaliar. A resposta não pode depender de adivinhar a intenção do autor. Evitar negativas como `incorreta`, `exceto` e `não`, salvo quando forem indispensáveis; nesse caso, dar destaque tipográfico à negação e revisar a carga cognitiva extra.

O texto-base não pode entregar a resposta por repetição literal, e o comando não pode ser respondido corretamente sem mobilizar a competência prevista. Cada dado do cenário deve ser relevante ou realisticamente necessário, jamais ruído criado para confundir.

### Opções e distratores

As cinco opções devem ser homogêneas em forma, extensão, precisão, regência e nível de detalhe. O gabarito representa a única melhor solução sob todas as premissas explícitas. Cada distrator deve corresponder a uma hipótese de raciocínio diagnosticável, por exemplo:

- usar a métrica errada para a decisão;
- trocar treino por teste ou correlação por causalidade;
- arredondar antes da etapa correta;
- ignorar uma restrição explícita;
- inverter numerador e denominador;
- selecionar uma arquitetura tecnicamente possível, mas incompatível com o requisito apresentado.

O guia oficial distingue distrator plausível de “pegadinha”: o primeiro atrai quem apresenta uma dificuldade real; a segunda pode induzir ao erro até quem domina a competência. Portanto, são proibidos:

- ambiguidade deliberada ou duas respostas defensáveis;
- informação escondida;
- jogo de palavras, exceção obscura ou detalhe irrelevante;
- alternativa absurda usada apenas para completar cinco opções;
- absolutos como `sempre` e `nunca` quando servem de pista;
- gabarito consistentemente mais longo, mais técnico ou mais cauteloso;
- “todas as anteriores” e “nenhuma das anteriores”;
- alterar fatos, valores ou premissas entre as versões A e B.

### Discursivas

A discursiva deve avaliar algo que não seria adequadamente observado por múltipla escolha. Bons produtos incluem diagnóstico justificado, comparação orientada por critérios, cálculo acompanhado de interpretação, proposta com restrições, desenho de arquitetura ou defesa de decisão com evidências.

O padrão de resposta distribui pontos por elementos independentes. Ele deve declarar:

- o que precisa aparecer;
- a evidência que sustenta cada elemento;
- a pontuação parcial;
- erros conceituais que impedem a pontuação naquele critério;
- caminhos alternativos tecnicamente corretos.

Não premiar quantidade de palavras. Não exigir um grande número de tarefas incompatível com o espaço de resposta.

## O que o caderno oficial de SI 2021 ensina

O caderno oficial contém duas discursivas e oito objetivas de Formação Geral, além de três discursivas e 27 objetivas de Componente Específico. As objetivas possuem cinco opções. As discursivas dispõem de até 15 linhas.

Na parte específica aparecem situações e suportes de natureza profissional: UML, gráfico, arquitetura de sistemas, segurança, bancos de dados, esquema relacional, SQL, Big Data, modelo entidade-relacionamento, sistema especialista, diagrama de sequência, tabela de dispersão e pseudocódigo. O conjunto combina resposta única, blocos de afirmações e asserção–razão. Essa variedade é útil, mas não obriga a repetir mecanicamente formatos de afirmações em todos os capítulos.

As cinco discursivas mostram quatro características reutilizáveis:

1. texto-base e comando formam uma única situação;
2. tarefas são separadas em itens quando possuem produtos diferentes;
3. o padrão de resposta explicita os componentes esperados e aceita formulações equivalentes;
4. figuras e diagramas integram o raciocínio quando a competência é representar ou interpretar sistemas.

## Auditoria do template legado local

Preservar do template:

- identidade e cabeçalho institucional;
- campos de disciplina, turma, data, professor e estudante;
- instruções de aplicação;
- separação visual clara entre itens.

Substituir ou ignorar:

- quantidades antigas de 5 ou 10 questões; as provas UNIFACOL 2026.2 têm 8 itens, sendo 6 objetivos e 2 discursivos;
- descrições fixas como Unidade I “difícil” e Unidade II “fácil”; usar a calibração definida em `avaliacao-enade.md`;
- exigência automática de três a cinco parágrafos; usar somente o contexto necessário;
- rótulos “anti-IA”, “armadilha” e alternativas intencionalmente dúbias;
- exemplo que posiciona previamente o gabarito em A;
- gabarito e notas do professor no mesmo arquivo entregue ao estudante.

## Matriz de 15 itens por capítulo

Cada capítulo publicado no caderno contém exatamente 15 questões:

| Faixa | Tipo | Quantidade | Solução na edição do estudante |
|---|---|---:|---|
| 01–10 | objetiva, cinco opções | 10 | somente 02, 04, 06, 08 e 10 |
| 11–15 | discursiva, até 15 linhas | 5 | somente 12 e 14 |

Logo, a edição do estudante apresenta respostas explicadas apenas para as questões pares: 02, 04, 06, 08, 10, 12 e 14. A edição privada do professor guarda gabarito, justificativas e padrão de resposta de todos os itens.

### Distribuição cognitiva recomendada

Não confundir dificuldade com extensão. Para cada grupo de 15, usar como referência:

| Operação predominante | Quantidade aproximada | Evidência esperada |
|---|---:|---|
| compreender em contexto | 3 | interpretar conceito sem simples cópia |
| aplicar procedimento | 5 | executar cálculo, regra ou técnica e ler o resultado |
| analisar evidências | 5 | relacionar tabela, gráfico, código ou restrições |
| avaliar/propor | 2 | justificar decisão ou solução sob critérios |

Em IA e AED, pelo menos quatro itens do capítulo devem exigir cálculo, leitura quantitativa ou interpretação de saída quando isso for aplicável. Em Tópicos, pelo menos quatro devem integrar duas decisões, como valor + evidência, arquitetura + requisito, dados + governança ou IA + qualidade.

### Registro privado obrigatório

Cada item recebe identificador permanente, como `IA-C03-O07`, e uma linha privada com:

| Campo | Conteúdo |
|---|---|
| disciplina, unidade e capítulo | cobertura curricular |
| perfil/competência | desempenho profissional observado |
| objetos de conhecimento | conceitos necessários |
| tipo e operação cognitiva | objetiva/discursiva e ação solicitada |
| dificuldade | 1, 2, 3 ou calibração ENADE |
| fonte e licença | origem de texto, dados e imagem |
| gabarito/padrão | solução integral privada |
| diagnóstico A–E | razão de acerto ou erro de cada opção |
| evidência no livro | seção, exemplo, tabela ou atividade em que foi ensinada |
| visibilidade | público, candidato, reservado ou aplicado |
| elegibilidade | instrumento e unidade em que pode ser usado |
| revisão | conteúdo, linguagem, acessibilidade e resolução independente |

## Banco reservado e derivação das provas

Questões de prova só podem vir de questões ímpares, portanto sem resposta na edição do estudante. O fluxo é:

1. produzir e revisar os 15 itens do capítulo;
2. resolver todos de modo independente e preencher a matriz privada;
3. selecionar aleatoriamente, com estratificação por competência, dificuldade, capítulo e tipo, os candidatos para cada instrumento;
4. mover cada item selecionado integralmente para `provas/2026.2/banco_reservado/` antes da publicação final do caderno;
5. substituir o espaço público por uma nova questão ímpar equivalente, preservando 15 questões no capítulo;
6. registrar semente, data, identificadores e substituições em manifesto privado;
7. impedir que item `reservado` ou `aplicado` reapareça em PDF público, README, código de exemplo ou histórico de soluções;
8. montar cada prova com 6 objetivas e 2 discursivas, respeitando cobertura e dificuldade do instrumento.

A aleatoriedade escolhe entre itens previamente equivalentes; ela não substitui a matriz de cobertura. A prova precisa continuar representando o que foi ensinado.

## Versões A/B

A versão B difere da A somente pela ordem dos oito itens e pela permutação das cinco opções objetivas. Permanecem idênticos:

- texto-base, fonte e suporte visual;
- comando;
- valores, premissas e unidade de medida;
- competência, conteúdo e dificuldade;
- resposta conceitual;
- texto e critérios das discursivas.

Gerar e armazenar uma tabela privada:

| Item | posição A | posição B | correta A | correta B | permutação B |
|---|---:|---:|---|---|---|
| `TOP-C02-O03` | 3 | 6 | C | E | C→E, A→B, B→D, D→A, E→C |

Depois da permutação, reler cada alternativa ligada ao comando para verificar concordância e paralelismo. Resolver A e B separadamente. A troca de posição nunca pode alterar a semântica.

## Resistência a respostas superficiais de IA

Não prometer item “à prova de IA”. A resistência pedagógica vem de tarefas que exigem:

- combinar duas ou mais evidências do próprio cenário;
- explicitar cálculo intermediário ou cadeia de decisão;
- justificar por que uma alternativa ou arquitetura atende às restrições;
- interpretar dado local, tabela, gráfico, código ou artefato fornecido;
- confrontar uma recomendação com custo, risco, privacidade ou governança;
- produzir desenho, consulta, hipótese ou intervenção verificável;
- defender oralmente o raciocínio quando isso fizer parte da atividade.

Uma IA pode errar porque faz leitura superficial ou ignora uma restrição, assim como um estudante que não dominou a competência. Ela não deve errar porque o item tem duas respostas corretas, dados insuficientes ou redação ardilosa.

## Checklist de autoria

### Antes de escrever

- [ ] O capítulo e as seções efetivamente ensinadas estão identificados.
- [ ] Perfil, competência, objeto, operação cognitiva e dificuldade estão definidos.
- [ ] Há uma situação profissional ou social genuína, não um tema decorativo.
- [ ] Foi decidido se tabela, gráfico, figura, código ou diagrama é realmente necessário.

### Texto-base e comando

- [ ] Todo dado apresentado participa da resolução ou da compreensão realista do caso.
- [ ] Toda fonte externa é fidedigna, referenciada e usada dentro dos limites autorais.
- [ ] Tabela e figura são citadas explicitamente e continuam legíveis em cinza.
- [ ] O comando contém verbo observável e produto inequívoco.
- [ ] É impossível acertar apenas copiando uma frase do texto-base.
- [ ] O tamanho decorre da tarefa, sem inflação artificial.

### Objetivas

- [ ] Existem cinco opções e uma única melhor resposta.
- [ ] As opções mantêm paralelismo sintático e extensão comparável.
- [ ] Cada distrator representa um erro real e está documentado privadamente.
- [ ] Não há pista lexical, absoluta, gráfica ou de extensão para o gabarito.
- [ ] Não há pegadinha, informação escondida ou ambiguidade deliberada.
- [ ] Um segundo revisor resolveu o item sem consultar o gabarito.

### Discursivas

- [ ] A competência exige produção livre e não seria melhor medida por objetiva.
- [ ] As tarefas cabem em até 15 linhas.
- [ ] O padrão distribui pontos por critérios independentes.
- [ ] Há previsão de respostas alternativas tecnicamente válidas.
- [ ] Dados, unidades e restrições necessárias estão explícitos.

### Publicação e prova

- [ ] O capítulo público tem 10 objetivas e 5 discursivas.
- [ ] Apenas pares têm resposta explicada na edição do estudante.
- [ ] Itens reservados foram removidos integralmente e substituídos antes da publicação.
- [ ] A prova tem 6 objetivas e 2 discursivas e possui matriz de cobertura.
- [ ] A versão B altera apenas a ordem das opções.
- [ ] A e B foram resolvidas de modo independente.
- [ ] Gabaritos, justificativas, sementes e manifestos privados não entraram no PDF do estudante.

## Exemplos-modelo para validar o padrão

Os exemplos abaixo servem para validar estrutura e não devem ser reutilizados literalmente em prova.

### Modelo objetivo — evidências e restrições

**Situação-estímulo.** Uma equipe comparou três formas de apoiar a revisão de código. A linha de base realizou 12 implantações no mês. A diretoria permite ampliar o uso de IA somente se a alternativa alcançar pelo menos 15 implantações, não ultrapassar três defeitos que chegaram à produção e mantiver revisão humana obrigatória.

| Alternativa de processo | Implantações | Defeitos em produção | Cobertura de testes | Revisão humana |
|---|---:|---:|---:|---|
| assistente de código | 14 | 2 | 78% | sim |
| agente autônomo | 19 | 6 | 61% | não |
| agente com portões de qualidade | 16 | 2 | 84% | sim |

*Fonte: dados elaborados para fins didáticos.*

**Comando.** Considerando conjuntamente a meta de fluxo, o limite de qualidade e a regra de governança, a decisão coerente é

A) adotar o assistente de código, porque apresenta menos defeitos que o limite e mantém revisão humana.  
B) adotar o agente autônomo, porque maximiza implantações, mesmo sem atender às demais restrições.  
C) adotar o agente com portões de qualidade, porque satisfaz simultaneamente as três restrições.  
D) manter a linha de base, porque nenhuma alternativa pode aumentar fluxo sem aumentar defeitos.  
E) adotar assistente e agente autônomo, porque a média dos resultados atende ao limite de qualidade.

**Registro privado de validação.** Gabarito C. A ignora a meta mínima de 15 implantações; B ignora defeitos e revisão; D contradiz a terceira linha; E agrega processos sem que o cenário autorize essa combinação. A competência é selecionar solução a partir de múltiplas restrições, não reconhecer uma definição.

### Modelo discursivo — análise quantitativa e decisão visual

**Situação-estímulo.** Após a implantação de um assistente conversacional em uma central de atendimento, o dashboard apresentou os resultados abaixo.

| Período | Tempo médio | Percentil 90 | Reabertura | Resolução no primeiro contato |
|---|---:|---:|---:|---:|
| antes | 18 min | 34 min | 9% | 71% |
| depois | 14 min | 49 min | 17% | 66% |

*Fonte: dados elaborados para fins didáticos.*

**Comando.** Redija uma recomendação de até 15 linhas para a gerência. Em sua resposta: a) interprete por que a redução da média não basta para declarar melhora; b) indique uma visualização para comparar a distribuição dos tempos e outra para acompanhar qualidade; e c) proponha uma decisão operacional condicionada a uma evidência mensurável.

**Padrão privado de resposta.** Distribuir os pontos entre: contraste entre média e cauda/reabertura/resolução; escolha justificada de histograma, boxplot ou curva de distribuição para tempos; escolha de série temporal ou painel simples para reabertura e resolução; decisão prudente, como manter piloto e investigar atendimentos da cauda, acompanhada de limiar ou meta. Aceitar visualizações equivalentes quando a justificativa demonstrar adequação.
