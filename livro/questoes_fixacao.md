# Instruções para Inserir Questões de Fixação nos Capítulos do Livro

Este documento explica como integrar questões de fixação baseadas nas provas da disciplina nos capítulos do livro. O objetivo é reforçar o aprendizado com questões práticas similares às das avaliações, mas com variações para evitar cópia direta.

## Estrutura Geral

### 1. Localização das Questões
- **Posição:** Ao final de cada capítulo relevante, antes de `\end{appendices}` (se existir) ou antes do final do arquivo.
- **Formato:** Usar `\begin{SolvedBox}[title=Questão de Fixação]` para manter consistência visual (caixa laranja).
- **Quantidade:** 1 questão por capítulo, inspirada nas provas correspondentes.

### 2. Formato da Questão
Cada questão deve seguir este template:

```latex
\begin{SolvedBox}[title=Questão de Fixação]
\textbf{Questão:} [Texto contextual da questão, com variações nos números/cenários]

A) [Alternativa correta]  
B) [Distrator 1]  
C) [Distrator 2]  
D) [Distrator 3]  
E) [Distrator 4]

\textbf{Resposta:} \textbf{A}  
\textbf{Explicação:} [Breve justificativa, incluindo cálculos se necessário]
\end{SolvedBox}
```

### 3. Variações Necessárias
- **Números:** Alterar valores (ex.: 47.832 registros → 38.921 registros)
- **Cenários:** Manter similar mas não idêntico (ex.: UBS → posto de saúde)
- **Alternativas:** Preservar estrutura, ajustar distratores para manter dificuldade
- **Dificuldade:** Manter nível da prova original (difícil para I Unidade, fácil para Final)

### 4. Mapeamento Capítulo → Questões
Criar uma tabela específica para cada disciplina, mapeando:
- Capítulo do livro
- Questões das provas que correspondem
- Tipo de prova (I Unidade, II Unidade, II Chamada, Final)

### 5. Checklist de Implementação
- [ ] Todas as questões têm contexto suficiente
- [ ] Cálculos foram verificados
- [ ] Alternativas incorretas são plausíveis
- [ ] Respostas estão destacadas em negrito
- [ ] Variações foram aplicadas (não cópia direta)
- [ ] Formatação LaTeX correta (SolvedBox)
- [ ] Arquivo compila sem erros

## Exemplo de Questão Implementada

```latex
\begin{SolvedBox}[title=Questão de Fixação]
\textbf{Questão:} Uma empresa recebeu um dataset com 38.921 registros e 15 colunas. Qual documento deve ser criado para documentar o significado de cada coluna?

A) Dicionário de dados  
B) Relatório de vendas  
C) Dashboard executivo  
D) Matriz de correlação  
E) Histograma de frequências

\textbf{Resposta:} \textbf{A}  
\textbf{Explicação:} O dicionário de dados documenta o significado, tipo e domínio de cada coluna, essencial para AED.
\end{SolvedBox}
```

## Benefícios
- Reforça conceitos com aplicação prática
- Prepara alunos para o estilo das provas
- Mantém consistência visual com SolvedBox (laranja)
- Permite reutilização em outras disciplinas com ajustes mínimos

## Notas para Outras Disciplinas
- Adaptar cenários para o contexto da matéria (ex.: para Estatística, usar dados de pesquisa; para Programação, usar código)
- Manter proporção de questões por tipo de prova
- Verificar se SolvedBox está definido no preâmbulo do documento