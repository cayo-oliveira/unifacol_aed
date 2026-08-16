---
name: trilha-unifacol
description: Planejar, integrar, escrever, revisar e compilar materiais didáticos da UNIFACOL para Tópicos Integradores, Inteligência Artificial e Análise Exploratória de Dados. Usar ao trabalhar com calendário e plano de ensino, livro-aula semanal em LaTeX, leitura guiada, caderno de exercícios, caderno de atividades, questões e provas no padrão ENADE, versões A/B, simulados, artigos científicos, Memory Bank e migração incremental dos semestres 2026.1 para 2026.2 nesses três repositórios.
---

# Trilha UNIFACOL

Produzir uma única trilha coerente: calendário → plano → caderno de exercícios → livro-aula → atividades → provas.

## Começar sempre pelo estado do projeto

1. Ler o arquivo `.mb` mais recente em `memory-bank/` ou `Memoria/`.
2. Ler `context.md`, `opus.md`, `calendario.md` e `mudancas_2026_2.md`.
3. Verificar `git status --short`. Preservar alterações do professor.
4. Identificar a disciplina pelo repositório.
5. Atualizar o Memory Bank ao concluir cada parte relevante.

Ler [disciplinas.md](references/disciplinas.md) para ementa, direção curricular e dinâmica específica. Ler [calendario-2026-2.md](references/calendario-2026-2.md) ao planejar datas. Ler [avaliacao-enade.md](references/avaliacao-enade.md) e [matriz-enade-autentica.md](references/matriz-enade-autentica.md) integralmente antes de escrever exercícios, atividades ou provas. A matriz autêntica prevalece sobre templates legados quando houver conflito. Ler [escrita-guiada.md](references/escrita-guiada.md) antes de escrever capítulos. Ler [engenharia-agentica.md](references/engenharia-agentica.md) ao tratar SDD, contexto, arquitetura, agentes, skills, playbooks, MCP, multiagente ou Memory Banking. Ler [bi-agentic.md](references/bi-agentic.md) ao comparar plataformas de BI, análise conversacional, Text-to-SQL, NL2Vis ou agentes de dados.
Ler [planejamento-e-diario.md](references/planejamento-e-diario.md) sempre que criar ou alterar plano de aula, cronograma, tabela do Capítulo 1 ou diário de classe.
Ler [apresentacoes-cientificas.md](references/apresentacoes-cientificas.md) sempre que planejar ou produzir o caderno de atividades das quatro apresentações da Unidade I.
Ler [revisao-preservadora-enade.md](references/revisao-preservadora-enade.md) ao aprofundar um caderno existente sem trocar as questões.
Ler [capitulo-progressivo.md](references/capitulo-progressivo.md) antes de criar ou revisar capítulos conceituais, matemáticos, de regressão, classificação, métricas, redes neurais ou LLMs.

## Modo excepcional Grazi — leitura autoral

Ativar somente quando Cayo pedir uma leitura científica dirigida a ele, e não ao aluno. Ler [leitura-autoral-grazi.md](references/leitura-autoral-grazi.md) e tratar suas regras como exceção local aos vocativos e às conexões curriculares de `escrita-guiada.md`. Preservar a estrutura documental cinza, explicação azul e síntese laranja, mas conversar com Cayo como autor/pesquisador e limitar as conexões ao problema, método, evidência, resultados, limites e próximos testes do próprio artigo. Não propagar automaticamente esse modo aos capítulos regulares da UNIFACOL.

## Fluxo obrigatório de produção

1. Mapear fontes antigas por seção; nunca substituir sem inventário.
2. Criar primeiro o caderno de exercícios ENADE: 15 itens por capítulo, sendo 10 objetivos e 5 discursivos, com respostas explicadas somente para os itens pares na edição do estudante e gabarito integral privado.
   Executar `scripts/validate_workbook.py <diretório-dos-capítulos>` antes de compilar ou reservar itens.
3. Usar a matriz desse caderno para calibrar livro-aula e provas.
4. Integrar livro e notas de aula em um capítulo por encontro de três horas.
5. Remover do texto do aluno bastidores de professor, respostas e referências a prova.
6. Criar atividades da disciplina conforme `disciplinas.md`.
7. Derivar provas apenas de objetivos e conteúdos efetivamente cobertos.
8. Compilar cada capítulo e o `main.tex` com Tectonic.
9. Examinar erros, `Overfull \hbox` e elementos fora das margens.
10. Atualizar o `.mb` com fontes incorporadas, arquivos gerados, testes e pendências.

## Contrato do plano e do diário

- Manter `plano_2026_2.md` na raiz como fonte humana do cronograma aprovado.
- Inserir no início do Capítulo 1 uma tabela legível com data, unidade, tema e marco, acompanhada de texto que explique a progressão do curso.
- Gerar `plano_e_diario_2026_2.xlsx` na raiz com uma linha por encontro e campos planejados e realizados lado a lado.
- Manter vazios os campos do diário até o professor registrar a aula; nunca inventar presença, conteúdo ministrado ou link do Classroom.
- Regenerar e conferir a planilha quando data, tema, avaliação ou capítulo mudar.
- Tratar feriado, avaliação, EXPOFACOL, segunda chamada e final como tipos distintos de encontro.
- Usar `scripts/generate_plan_workbook.py` para preservar filtros, congelamento, validações, cores e larguras.

## Estrutura canônica dos repositórios

- `.agents/skills/trilha-unifacol/`: este skill, suas referências, ativos e validadores.
- `livro/`: material único para professor e aluno; nunca recriar uma pasta `aula/` na raiz.
- `livro/capitulos/capitulo_NN/`: `conteudo.tex`, `capitulo_NN.tex` e `capitulo_NN.pdf`.
- `livro/fontes_2026_1/`: livro e notas antigos preservados como fontes da integração.
- `caderno_exercicios/`: questões ENADE e respostas explicadas; não duplicar no livro.
- `caderno_atividades/`: dinâmica avaliativa específica da disciplina.
- `provas/2026.1/`: arquivo histórico preservado.
- `provas/2026.2/`: provas novas, versões A/B, gabaritos e matriz de rastreabilidade.
- `memory-bank/`: estado incremental e decisões do projeto.

Usar nomes minúsculos e sem variantes concorrentes. Não aceitar `prova` e `Provas`, `chapters` e `capitulos`, nem `aula` e `livro` na raiz. Migrar sem perda: mover originais para `fontes_2026_1`, registrar a origem na matriz de cobertura e só então integrar.

## Guardrails pedagógicos

- Planejar exatamente três horas por encontro, das 19h às 22h.
- Escrever cada capítulo para sustentar 180 minutos de leitura, explicação, análise visual, discussão e síntese. Um roteiro que apenas soma 180 minutos não substitui conteúdo suficiente.
- Exigir pelo menos cinco parágrafos substantivos em toda `section`, `subsection` e `subsubsection`. Ao criar uma subdivisão, ela herda integralmente essa regra. Listas, tabelas, títulos e caixas não contam como parágrafo.
- Usar como piso de profundidade 5.000 palavras de prosa por capítulo inicial de três horas, salvo capítulo matemático cujo desenvolvimento equivalente esteja em equações comentadas. Explicar conceitos, decisões, exemplos, limites e conexões; não inflar o texto com repetição.
- Fazer chamada às 20h30. Quem desejar pode sair, mas a aula continua.
- Se não restar nenhum aluno depois das 20h30, o conteúdo daquele bloco não entra na aula de revisão.
- Explicar intenção e situação real antes de formalismo ou ferramenta.
- Preferir leitura limpa, exemplos reais, tabelas curtas, fluxos simples e imagens legíveis.
- Não transformar o livro-aula em teleprompter nem mencionar respostas, fiscalização ou estratégia de prova.
- Tratar LLM como ferramenta de estudo e programação com verificação, não como autoridade.
- Nunca prometer que uma questão é “à prova de IA”. Avaliar raciocínio aplicado com dados, premissas e justificativas verificáveis.

### Sequência dos capítulos matemáticos

Nas Semanas 2 e 3 de AED e IA, ensinar estatística sem código. Para cada conceito, seguir a sequência narrativa: necessidade histórica ou problema que motivou a medida; finalidade; fórmula; significado de cada símbolo; cálculo completo linha a linha; explicação em linguagem simples do número obtido; ponte para o conceito seguinte. Usar exemplos resolvidos, não listas de exercícios dentro do livro. O caderno separado recebe os exercícios.

O núcleo estatístico dessas duas semanas é compartilhado integralmente entre AED e IA para manter fórmulas, convenções e exemplos coerentes. Em IA, o início do Capítulo 2 acrescenta, antes desse núcleo, a história dos LLMs preservada de 2026.1, com linha do tempo, datas e marcos. Não inserir nessa abertura histórica uma história genérica de toda a IA, pois o universo geral já pertence ao Capítulo 1.

Para qualquer capítulo posterior com formalismo, aplicar o mesmo padrão pedagógico dos Capítulos 2 e 3: inventariar pré-requisitos já ensinados; não reensinar estatística básica; partir de uma necessidade; introduzir e ler a fórmula; nomear símbolos e unidades; resolver a conta linha a linha; interpretar o resultado; apresentar outro exemplo e um contraexemplo; usar visual funcional citado e interpretado; encerrar com decisão e ponte. Confrontar as fontes preservadas de 2026.1 e aproveitar o que estiver mais bem explicado, sem copiar exercícios, gabaritos ou contradições. O plano e o capítulo precisam mudar juntos quando a progressão curricular mudar.

## Separar cadernos

- `caderno_atividades/` organiza as quatro apresentações, artigos, atribuições, datas e rubrica; não é banco de questões.
- `caderno_exercicios/` contém os itens ENADE por capítulo, respostas públicas pares e gabarito privado; é a fonte das provas.
- Não aplicar formato ENADE às tabelas administrativas de atribuição do caderno de atividades. Aplicar ENADE às perguntas de arguição, aos exercícios e às provas quando houver avaliação de competência.

## Caixas permitidas no livro-aula

Usar as duas caixas pedagógicas e a caixa documental definidas em [escrita-guiada.md](references/escrita-guiada.md):

- laranja: síntese conversada do trecho anterior;
- azul: explicação guiada de um ponto difícil.
- cinza: parte identificada do artigo, sempre distinguindo citação curta de paráfrase.

Os títulos das três caixas devem ser brancos sobre a faixa colorida. Toda caixa deve ter espaço vertical perceptível antes e depois. Nunca fabricar trecho de artigo: quando o texto integral não estiver disponível, declarar `paráfrase do resumo` e trabalhar apenas com o que a fonte sustenta.

Quando o PDF integral estiver disponível, percorrer introdução, método/arquitetura, dados, avaliação/resultados, limitações/desafios e conclusão/direções futuras. Respeitar limites autorais: usar citação curta quando permitido e completar a caixa com síntese fiel claramente identificada, nunca reproduzir longos trechos apenas porque o PDF está disponível. Identificar seção e página impressa. Imediatamente abaixo de cada caixa, escrever dois movimentos explícitos em português: `Leitura guiada`, explicando afirmação, evidência e limites; e `Ligação com o semestre`, antecipando os conceitos, decisões e semanas que aquele trecho ajuda a compreender. Não reduzir o artigo ao resumo.

O artigo não pode desaparecer depois da seção dedicada à leitura. Da seção seguinte até o fechamento, reutilizar passagens, conceitos, resultados ou limitações da fonte como liga narrativa para cada assunto conceitual do capítulo. A conexão precisa ser substantiva: mostrar por que o novo tema responde a uma pergunta aberta pelo artigo. Nas seções de logística, calendário e avaliação, usar o próprio procedimento de leitura do artigo para explicar a atividade acadêmica, sem forçar uma analogia técnica artificial.

Anexar o PDF integral ao final do capítulo com `pdfpages`, preservando também o link DOI. Informar no corpo que o artigo está no apêndice. Definir o caminho do PDF por macro no `main.tex` e no wrapper individual, pois os dois compilam a partir de diretórios diferentes. Se o PDF não puder ser obtido legalmente, registrar a pendência e pedir que o professor o coloque na pasta do capítulo; nunca anexar HTML renomeado como PDF.

Exercícios ficam fora do livro e dentro do caderno próprio.

## Provas e versões A/B

Seguir [avaliacao-enade.md](references/avaliacao-enade.md) e a matriz oficializada em [matriz-enade-autentica.md](references/matriz-enade-autentica.md). Derivar provas somente de itens ímpares sem resposta pública, mover os selecionados para o banco reservado e substituí-los no caderno antes de sua publicação final. Manter nas versões A/B o mesmo conjunto de itens, enunciado, competência, dificuldade e resposta conceitual. Para economizar reescrita, alterar somente a ordem das questões e das alternativas objetivas, registrando ambos os mapeamentos no gabarito. Não criar ambiguidade artificial, informação escondida nem pegadinha; a resistência a respostas superficiais de IA deve vir do raciocínio e das evidências exigidas.

Na prova, é permitido fazer uma revisão editorial preservadora do item reservado: ampliar a situação-estímulo, assumir voz de nota jornalística, reportagem adaptada, memorando, relatório, demanda de chefia ou estudo de caso, acrescentar subtítulo editorial e tornar as alternativas mais explicativas. Essa revisão não autoriza criar outra questão. Preservar obrigatoriamente o ID do caderno, a competência, os dados, o procedimento matemático, a única resposta conceitual correta e o diagnóstico de cada distrator. Não atribuir texto autoral a jornal, revista ou artigo inexistente; identificar simulações como elaboradas para fins didáticos.

Para a Prova da I Unidade, conferir a cobertura contra o plano vigente, sem aplicar uma matriz genérica às três disciplinas:

- **AED:** problema, dor ou necessidade decisória; Estatística I; Estatística II; gráfico funcional; arquitetura de dados voltada à AED; dashboard/storytelling e integração, quando previstos no plano.
- **IA:** universo da IA; história dos LLMs; Estatística I; Estatística II; regressão com cálculo; classificação com gráfico ou tabela; métricas de regressão e classificação, incluindo matriz de confusão, MAE, RMSE e $R^2$ conforme o item selecionado.
- **Tópicos:** seguir a progressão aprovada no plano, cobrindo problema/MVP/ágil, prototipação, arquitetura de software, contratos, arquitetura de dados, LGPD/governança e integração da Unidade I.

Uma tabela ou um gráfico inserido na revisão da prova só pode reorganizar os mesmos dados do item de origem. Ele deve ser citado no texto e participar da resolução; não acrescentar fatos, variáveis ou valores que transformem a identidade pedagógica do item.

## Revisão preservadora do caderno ENADE

Quando o professor pedir para melhorar questões existentes, preservar o identificador, a competência, o objeto de conhecimento, o procedimento matemático e a resposta conceitual de cada item. Não substituir silenciosamente o banco por novas questões. A revisão pode reescrever cenário, comando, suporte e alternativas, desde que a identidade pedagógica permaneça rastreável no gabarito privado.

Variar a voz dos textos-base: fragmento jornalístico ou institucional adaptado, memorando de chefia, chamado técnico, relatório de auditoria, caso profissional, fala de stakeholder, norma, tabela, gráfico, mapa, arquitetura, código ou diagrama. Dados autorais devem ser identificados como elaborados para fins didáticos; fontes externas precisam ser reais e referenciadas. Não simular autoria de jornal, site ou artigo inexistente.

O suporte não verbal só entra quando participa da resolução. Tabela, gráfico, mapa, diagrama, fluxo, esquema, pseudocódigo ou programa deve ser citado no texto-base e necessário para calcular, comparar, diagnosticar ou decidir. Buscar variedade comparável ao caderno oficial, sem impor quantidade mecânica de figuras e sem decoração.

Nas objetivas, preferir distratores que seriam defensáveis em outro contexto, mas falham diante de premissa explícita: finalidade, grão, prazo, custo, acesso, risco, causalidade, métrica, evidência, versão ou qualidade. Documentar privadamente qual restrição invalida cada opção. Continuam proibidas duas respostas defensáveis, informação escondida, alternativa absurda e pegadinha.

AED, IA e Tópicos devem compartilhar identidade visual, hierarquia de item, legenda de fonte, estilo de resposta explicada, margens, cabeçalho, tipografia e tratamento de tabelas e figuras. A disciplina muda o conteúdo e a cor de identificação, não a qualidade editorial.

## LaTeX e compilação

- Preferir `tabularx`, colunas `p{}` e `\adjustbox{max width=\textwidth}` para conteúdo largo.
- Definir largura e quebra de texto em nós TikZ; evitar texto longo sem `text width`.
- Usar imagens com `width<=0.95\textwidth` e altura limitada quando necessário.
- Evitar URLs extensas em tabelas; usar `\url{}` fora delas ou rótulos com `\href`.
- Executar `scripts/validate_chapter.py CAMINHO_DO_CONTEUDO_TEX` antes de compilar.
- Executar `scripts/build_tex.sh livro/capitulos/capitulo_NN/capitulo_NN.tex` e depois `scripts/build_tex.sh livro/main.tex`.
- Manter o PDF individual dentro da pasta do capítulo e `livro/main.pdf` como volume integral.
- Não considerar pronto se houver erro fatal ou conteúdo ultrapassando margens.
- Ao finalizar, reler o capítulo como roteiro de aula e registrar no Memory Bank: palavras, seções, parágrafos por seção, duração planejada, PDFs gerados e resultado do log.

## Trabalhar incrementalmente

Priorizar a semana solicitada, entregar um capítulo compilável e registrar o que ainda falta. Para a migração inicial de 2026.2, priorizar Capítulo 1 de Tópicos e Capítulo 1 de AED; depois completar Tópicos, AED e IA.

Na revisão iniciada em 12/08/2026, a ordem de prioridade é AED, IA e Tópicos. A fase corrente termina primeiro os cadernos de atividades e de exercícios das três disciplinas, nessa ordem; somente depois retoma o aprofundamento dos capítulos, confrontando cada tema com as fontes preservadas de 2026.1. Dentro de cada disciplina, concluir e revisar o caderno ENADE antes de reservar, substituir ou transportar itens ímpares para provas. A urgência da aula seguinte pode antecipar a reescrita de um capítulo semanal, sem inverter a dependência entre banco público e prova.
