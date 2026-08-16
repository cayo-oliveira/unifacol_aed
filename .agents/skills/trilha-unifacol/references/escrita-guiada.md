# Escrita guiada do livro-aula

## Leitor e voz

Escrever para aluno noturno que trabalhou durante o dia e para o professor que conduzirá três horas de encontro. Usar português brasileiro simples, calor humano, exemplos reais e precisão técnica. Explicar primeiro “para que serve”, depois “como funciona” e, por último, o formalismo necessário.

## Estrutura de cada capítulo semanal

1. Cena ou problema real que abre a história.
2. Mapa do encontro e resultados de aprendizagem.
3. Blocos conceituais com exemplo, representação visual e decisão.
4. Demonstração guiada ou estudo de caso.
5. Ponte entre os conceitos do capítulo.
6. Síntese final e preparação para a próxima semana.

Planejar 180 minutos, incluindo interação e pausa. O capítulo deve conter matéria suficiente para o professor ler, explicar, exemplificar e discutir durante esse período e também funcionar em leitura autônoma. Usar 5.000 palavras de prosa como piso dos capítulos iniciais; capítulos matemáticos podem demonstrar profundidade equivalente com derivações comentadas.

## Regra de profundidade por título

Toda seção, subseção e subsubseção deve conter pelo menos cinco parágrafos substantivos próprios. Um parágrafo substantivo desenvolve uma ideia, relação, exemplo, consequência ou limite; listas, tabelas, caixas e frases de transição não entram na contagem. Não abrir uma subdivisão apenas para colocar uma lista. O validador deve reprovar o capítulo se qualquer título ficar abaixo desse mínimo.

## Três caixas com funções distintas

### Caixa laranja — síntese conversada

Usar depois de uma seção ou conceito. Começar naturalmente com variação de:

> Então, aluno, veja só o que você aprendeu aqui...

Resumir relação, consequência e decisão. Não colocar exercício nem gabarito.

### Caixa azul — explicação guiada

Usar em ponto difícil. Começar naturalmente com variação de:

> Aluno, preste atenção aqui, porque esta parte é importante...

Reexplicar com analogia, decomposição ou contraexemplo. Evitar infantilização e excesso de caixas.

### Caixa cinza — leitura do artigo

Usar no estudo de caso para mostrar uma parte identificável da fonte e interpretá-la. O título informa a seção ou a natureza do material, por exemplo `No artigo — resumo (paráfrase)`. Se houver citação, ela deve ser curta, fiel e marcada como citação; se apenas resumo/abstract estiver disponível, usar paráfrase explícita. Depois da caixa, explicar em prosa o que a parte afirma, o que não permite concluir e como se conecta ao curso. Um capítulo de abertura baseado em artigo deve ter ao menos três caixas cinza distribuídas na narrativa.

Com o PDF completo disponível, a leitura deve atravessar todas as partes estruturais relevantes, e não somente o abstract: problema e motivação; método ou arquitetura; dados e preparação; avaliação e resultados; desafios ou limitações; implicações, conclusão e pesquisa futura. Cada caixa contém um trecho real coerente de um ou dois parágrafos em inglês, com seção e página impressa; uma frase isolada não atende ao padrão. Logo abaixo, desenvolver obrigatoriamente `Leitura guiada` e `Ligação com o semestre` em português. Anexar o artigo integral ao capítulo para uso offline dos estudantes.

Depois da seção de leitura integral, continuar usando o artigo como fio narrativo. Cada seção conceitual posterior retoma uma passagem, resultado, limitação ou pergunta do texto e explicita como o assunto estudado responde a ela. Em calendário, avaliação e dinâmica de sala, conectar o método de leitura e apresentação científica, sem inventar uma ligação técnica apenas para cumprir formato.

Em LaTeX, os títulos das caixas são brancos, as faixas têm alto contraste e `before skip`/`after skip` garantem separação do parágrafo anterior e do seguinte.

## Recursos visuais

- Usar uma imagem quando ela reduzir esforço cognitivo, não por decoração.
- Preferir diagramas de uma ideia, fluxos com até sete nós e tabelas com poucas colunas.
- Escrever legenda que diga o que observar.
- Manter paleta limpa, alto contraste e leitura em impressão.
- Garantir imagem dentro de `0.95\textwidth`; quebrar tabelas grandes em duas.

## Integração sem perda

Criar antes uma matriz `fonte | seção original | destino | ação`. Marcar cada item como preservado, reescrito, atualizado, movido ao apêndice, movido ao caderno ou removido com justificativa. Comparar cobertura ao final. Não copiar redundâncias nem apagar conteúdo silenciosamente.

## O que retirar do livro-aula

- instruções internas ao professor;
- respostas esperadas e plano B de sala;
- logística de fiscalização e dicas de prova;
- exercícios, gabaritos e caixas de questão;
- cronogramas antigos e trabalhos substituídos.

Manter plano, critérios e política do curso apenas no Capítulo 1, em linguagem destinada ao aluno.
