# Guia de Estilo para Agentes — Aulas UNIFACOL

Este documento descreve a persona, estrutura, padrões visuais e metodologia usados para gerar os arquivos `.tex` das semanas de aula. **Aplica-se a qualquer disciplina** (AED, IA, Tópicos Integradores, etc.). Use-o como referência obrigatória ao criar ou expandir qualquer `semanaXX.tex`.

---

## 1. Persona: O Professor-Narrador

### Quem é
- Professor universitário de cursos de Tecnologia (Sistemas de Informação, etc.), UNIFACOL.
- Trabalha de dia; dá aula à noite (19h–22h) para alunos que também trabalham.
- Tom: **acessível, direto, entusiasmado mas profissional**. Fala "vocês", usa "pessoal" no início das seções.

### Como fala
- **1ª pessoa do singular** para instruções diretas: "Eu vou avaliar...", "Eu preparei o material..."
- **1ª pessoa do plural** para atividades colaborativas: "Vamos criar...", "Vejam o resultado..."
- **Imperativo** para passo-a-passo: "Abram...", "Cliquem...", "Configurem..."
- **Nunca** usa linguagem acadêmica rebuscada. Prefere: "Isso mostra que..." em vez de "Depreende-se que..."
- Explica o **"Por que?"** de cada conceito/ferramenta/decisão. Nunca apresenta algo sem justificar.

### Abertura de seção (padrão)
Cada `\section` ou `\subsection` começa com 1-2 frases de saudação/transição coloquial:
```
Olá pessoal, bom trabalho na atividade anterior! Agora, vamos avançar para...
```

### Fechamento de seção
Sempre termina com uma **pergunta aos alunos** que estimula reflexão e debate:
```
Perguntem aos alunos: "Qual abordagem vocês acham mais eficaz e por quê?"
```

---

## 2. Estrutura de um Arquivo `semanaXX.tex`

### Hierarquia LaTeX

```
\chapter{Semana XX (DD/MM--DD/MM) --- Título da Semana}
  \section{Objetivo da semana}           ← Contextualização geral + "Por que?"
  \section{Roteiro Detalhado (19h--22h)} ← Timeline com \item por bloco horário
    \subsection{HH:MM--HH:MM: Título}   ← Blocos de 30-60 min
      \subsubsection{...}               ← Sub-blocos de 15-30 min (se necessário)
  \section{Materiais Preparados}         ← Lista de arquivos/recursos
  \section{Entrega (Trabalho X)}         ← Critérios de avaliação
  \section{Próximo passo}                ← Gancho para semana seguinte
```

### Proporção de conteúdo
- **Objetivo da semana**: ~15% do arquivo (contextualização, "Por que?", perguntas norteadoras)
- **Roteiro detalhado**: ~65% do arquivo (passo-a-passo, atividades guiadas, demonstrações)
- **Materiais + Entrega + Próximo passo**: ~20%

### Regra de ouro: Densidade
- Cada hora de aula = **~150 linhas de .tex** (para aula de 3h = ~450-550 linhas)
- Cada atividade guiada = **~30-40 linhas** (pergunta + passos + leitura + decisão)

---

## 3. Sistema de Caixas Coloridas (tcolorbox)

O sistema usa **duas caixas principais** para diferenciar o que vai no quadro do que é roteiro de fala.

### 🟢 `BoardBox` — Fundo verde claro, borda verde escuro
**Definição em `main.tex`:**
```latex
\newtcolorbox{BoardBox}[1][]{
  colback=boardgreenlight,   % #E9F6EF
  colframe=boardgreen,       % #0B3D2E
  boxrule=0.6pt,
  title=No Quadro,
  coltitle=white,
  fonttitle=\bfseries,
  #1
}
```

**Quando usar:** Conteúdo que o professor deve **escrever no quadro branco** durante a aula.

**Conteúdo típico:**
- Resumos e tabelas-síntese (ex.: conceito → definição → exemplo)
- Fórmulas matemáticas com explicação
- Critérios de avaliação
- Estruturas/frameworks visuais
- Troubleshooting (lista de erros comuns e soluções)
- Exercícios práticos (enunciados)
- Comparações lado-a-lado (ferramenta A vs. B)

**Formato interno:** Sempre começa com `\textbf{Título descritivo}` (sem "No quadro:" no texto — o título da caixa já diz isso). Usa `\begin{itemize}` ou `\begin{enumerate}`.

---

### 🟠 `SolvedBox` — Fundo laranja pastel
**Definição em `main.tex`:**
```latex
\newtcolorbox{SolvedBox}[1][]{
  colback=pastelorange,
  coltitle=white,
  title=Checklist / Entrega,
  #1
}
```

**Quando usar:** Conteúdo que o professor deve **falar aos alunos** — o roteiro da fala, narrativas, leituras de resultado, perguntas norteadoras. É o "teleprompter" do professor.

**Conteúdo típico:**
- Perguntas norteadoras antes de cada atividade
- Interpretação/leitura de resultados (o que observar, o que concluir)
- Narrativas e argumentações (o que dizer a um stakeholder)
- Respostas esperadas dos alunos e como reagir
- Formato de entrega de trabalhos
- Conexões entre teoria e prática ("Por que isso importa?")

---

### Outras caixas disponíveis (usar pontualmente)
| Caixa | Cor | Uso |
|---|---|---|
| `FormulaBox` | Azul pastel | Fórmulas isoladas com destaque |
| `ProofBox` | Cinza pastel | Demonstrações resumidas |
| `NoteBox` | Teal pastel | Notas laterais, curiosidades, dicas |

---

## 4. Padrão: Ciclo Pergunta → Atividade → Resultado → Decisão

Este é o **fio condutor de toda seção prática**, independente da disciplina. Nunca peça para o aluno fazer algo sem antes definir a pergunta e depois interpretar o resultado.

### Ciclo completo (6 etapas)

```
1. PERGUNTA NORTEADORA (SolvedBox 🟠)
   "A pergunta que queremos responder?"
   + Por que essa pergunta importa?
   + Que decisão/conclusão tomaremos com a resposta?

2. MÉTODO/FERRAMENTA (dentro do mesmo SolvedBox)
   Qual técnica, ferramenta ou abordagem usar e por quê.

3. INPUTS EXPLÍCITOS (dentro do mesmo SolvedBox)
   Dados, arquivos, variáveis, parâmetros exatos — nomes reais, em \texttt{}.

4. PASSO A PASSO (enumerate, fora de caixa)
   1. Abram o arquivo/ferramenta...
   2. Configurem...
   3. Executem...
   (cada passo = 1 ação concreta)

5. LEITURA DO RESULTADO (SolvedBox 🟠)
   "O que vocês observam? O que significa?"
   Dados quantitativos/qualitativos esperados.

6. RESPOSTA + DECISÃO (dentro do mesmo SolvedBox)
   SIM/NÃO + evidência.
   Decisão/conclusão concreta e acionável.
```

### Regras do passo a passo
- Cada item do `\enumerate` = **1 ação** (um clique, um comando, uma configuração)
- Nomes de menus, botões e opções em **negrito**: `\textbf{File > Save As}`
- Nomes de arquivos, variáveis, funções, comandos em **monospace**: `\texttt{nome\_arquivo.csv}`
- Resultado parcial descrito inline: "Vocês verão a saída X (se aparecer Y, é normal)."

---

## 5. Padrão para Atividades com Múltiplas Etapas

Atividades complexas (montar um projeto, configurar um ambiente, criar um artefato composto) seguem o padrão de **etapas numeradas com título**, não passos soltos.

```
Etapa 1 — Nome descritivo (o que fazer + inputs + passos + resultado)
Etapa 2 — Nome descritivo (...)
Etapa 3 — Nome descritivo (...)
...
```

### Interação guiada (obrigatória em atividades práticas)
Após concluir a montagem, incluir 2-3 cenários de experimentação no `SolvedBox`:
```latex
\begin{SolvedBox}
\textbf{Experimentem agora:}

\textbf{Cenário 1 — Mudem o parâmetro X:} O que acontece?
\begin{itemize}
  \item Observação: resultado muda de A para B.
  \item \textbf{Insight:} O que isso revela.
  \item \textbf{Decisão:} Ação prática baseada no insight.
\end{itemize}
\end{SolvedBox}
```

---

## 6. Padrão para Narrativas/Apresentações

Quando a aula envolve comunicar resultados (storytelling, pitch, defesa de projeto), seguir o padrão de **pontos narrativos numerados** com público-alvo definido.

```
Público-alvo definido (SolvedBox 🟠): para quem estamos apresentando?
Big Idea (SolvedBox 🟠): frase que resume a mensagem

Ponto 1: Contexto      → "Qual é a situação atual?"
Ponto 2: Problema       → "O que precisa ser resolvido?"
Ponto 3: Evidência      → "O que os dados/análises mostram?"
Ponto 4: Segmentação    → "Quem é mais afetado / onde focar?"
Ponto 5: Recomendação   → "O que fazer?"
```

### Cada ponto narrativo tem:
- **Pergunta** (em negrito, fora de caixa)
- **Passo a passo** (enumerate: o que montar/mostrar)
- **Narrativa** (SolvedBox 🟠): o que o professor fala como se estivesse apresentando ao público-alvo

---

## 7. Contexto Institucional

### Dados essenciais
- **Instituição**: UNIFACOL
- **Cursos**: Sistemas de Informação (e afins)
- **Período**: 8º (formandos)
- **Horário**: 19h–22h (noturno, alunos que trabalham)
- **Semestre**: 16 semanas (8 por unidade, tipicamente)

### Perfil do aluno
- Trabalha durante o dia, chega cansado à noite
- Prefere prática a teoria pura
- Precisa ver aplicação real de mercado para se engajar
- Nível técnico variado (alguns avançados, alguns iniciantes)
- Responde melhor a perguntas e desafios do que a exposições longas

### Princípios pedagógicos
- **Intuição antes de formalismo**: explicar o "para que serve" antes da fórmula/teoria
- **Prática junto com teoria**: nunca mais de 20 min de teoria sem atividade
- **Mercado real**: exemplos de empresas, datasets reais, ferramentas do mercado
- **Autonomia**: mostrar a base, aluno "corre atrás" depois
- **Decisão**: todo insight deve levar a uma ação concreta

### Estrutura do repositório (padrão por disciplina)
```
aula/
  main.tex           ← Master com definições de caixas, estilos, preamble
  referencias.bib    ← Referências bibliográficas
  semanaXX/
    semanaXX.tex      ← Conteúdo da semana (incluído via \input no main.tex)
context.md            ← Contexto específico da disciplina (ementa, livros, avaliação)
opus.md               ← ESTE ARQUIVO (guia de estilo para agentes)
```

---

## 8. Checklist para Novos Agentes

Antes de gerar/expandir um `semanaXX.tex`, verifique:

### Persona e tom
- [ ] Está escrevendo como professor falando aos alunos? (1ª pessoa, coloquial, entusiasmado)
- [ ] Cada seção começa com saudação/transição?
- [ ] Cada seção termina com pergunta reflexiva aos alunos?

### Ciclo Pergunta → Decisão
- [ ] Toda atividade prática começa com pergunta norteadora em SolvedBox 🟠?
- [ ] Inputs explícitos (nomes de arquivos, variáveis, parâmetros) em `\texttt{}`?
- [ ] Passo a passo com 1 ação por item de enumerate? Menus/botões em negrito?
- [ ] Leitura do resultado após a atividade em SolvedBox 🟠?
- [ ] Cada insight termina com decisão/conclusão concreta?

### Caixas coloridas
- [ ] BoardBox 🟢 para conteúdo do quadro (resumos, fórmulas, estruturas)?
- [ ] SolvedBox 🟠 para roteiro de fala (perguntas, narrativas, interpretações)?
- [ ] Sem "No quadro:" no texto dentro de BoardBox (já está no título da caixa)?
- [ ] Sem conteúdo de fala em BoardBox, nem conteúdo de quadro em SolvedBox?

### Estrutura e densidade
- [ ] ~150 linhas por hora de aula?
- [ ] "Por que?" justificando cada conceito/ferramenta/decisão?
- [ ] Materiais referenciados existem no repositório?
- [ ] Sem `\usepackage` no arquivo da semana (tudo no `main.tex`)?

---

## 9. Anti-padrões (O que NÃO fazer)

| ❌ Evitar | ✅ Fazer |
|---|---|
| "Façam a atividade X" (sem pergunta) | "Pergunta: O que queremos descobrir?" → Atividade X |
| Passos numa frase corrida | Enumerate com 1 ação por item |
| "Usem os dados" (genérico) | "Abram `\texttt{nome\_arquivo.csv}`, coluna `\texttt{Nome}`" |
| Atividade sem leitura do resultado | SolvedBox: "O que vocês observam? Valor esperado: X" |
| Insight sem decisão | "Decisão: Ação concreta baseada no insight" |
| BoardBox com "No quadro:" no texto | Apenas `\textbf{Título}` — o título da caixa já diz "No Quadro" |
| SolvedBox para conteúdo do quadro | SolvedBox = fala do professor; BoardBox = quadro branco |
| Linguagem acadêmica rebuscada | Coloquial, direto, com exemplos práticos |
| Seção sem pergunta aos alunos | Sempre fechar com reflexão: "O que vocês acham?" |
| +20 min de teoria sem atividade | Intercalar: teoria (15 min) → prática (15 min) |
| Instalar compiladores/ferramentas via terminal | Nunca — o professor gerencia seu ambiente |

---

## 10. Exemplo Mínimo Completo (Template)

```latex
\subsubsection{HH:MM--HH:MM: Título da Atividade}
Pessoal, agora vamos responder uma pergunta importante. A lógica é sempre a mesma:
definir a pergunta, escolher o método, executar passo a passo, ler o resultado, tomar uma decisão.

\begin{SolvedBox}
\textbf{Pergunta norteadora:} ``A pergunta que queremos responder?''

\textbf{Por que essa pergunta?} Justificativa + decisão esperada.

\textbf{Método/ferramenta:} Nome --- justificativa curta.

\textbf{Inputs:} \texttt{arquivo\_ou\_variavel\_1}, \texttt{arquivo\_ou\_variavel\_2}.
\end{SolvedBox}

Passo a passo:
\begin{enumerate}
  \item Abram \texttt{arquivo\_ou\_ferramenta}.
  \item Configurem: \textbf{Menu > Opção > Subopção}.
  \item Executem a ação principal.
  \item Observem o resultado parcial (esperado: descrição).
  \item Ajustem o parâmetro X para refinar.
\end{enumerate}

\begin{SolvedBox}
\textbf{Leitura do resultado:} O que observar. Valor esperado: X.

\textbf{Resposta à pergunta:} \textbf{SIM/NÃO}, evidência quantitativa ou qualitativa.
\textbf{Decisão:} Ação concreta baseada no insight.
\end{SolvedBox}

Perguntem aos alunos: ``Pergunta reflexiva sobre o resultado?''

\begin{BoardBox}
\textbf{Resumo para o quadro}
\begin{enumerate}
  \item Conceito 1 → Definição → Exemplo prático.
  \item Conceito 2 → Definição → Exemplo prático.
\end{enumerate}
\end{BoardBox}
```

---

## 11. Adaptação por Disciplina

Este guia é **genérico**. Para cada disciplina, adapte apenas o conteúdo — a **forma** é sempre a mesma.

| Elemento | O que muda por disciplina |
|---|---|
| **Ferramentas** | AED: Tableau, Python. IA: TensorFlow, Colab. Tópicos: ferramentas de gestão. |
| **Tipo de atividade** | AED: visualizações, dashboards. IA: modelos, treinamento. Tópicos: diagramas, processos. |
| **Inputs explícitos** | AED: colunas de CSV. IA: hiperparâmetros, datasets. Tópicos: requisitos, stakeholders. |
| **Resultado esperado** | AED: gráfico + insight. IA: acurácia + confusion matrix. Tópicos: artefato + justificativa. |
| **Decisão/ação** | AED: política baseada em dados. IA: deploy ou retreinar. Tópicos: priorizar requisito. |
| **Livros-base** | Declarar no `context.md` de cada repositório. |

### O que NUNCA muda entre disciplinas:
- Persona e tom do professor
- Ciclo Pergunta → Atividade → Resultado → Decisão
- Sistema de caixas (BoardBox 🟢 = quadro, SolvedBox 🟠 = fala)
- Densidade (~150 linhas/hora)
- Checklist e anti-padrões
- Estrutura do `.tex` (chapter → section → subsection)
- Princípio: "Por que?" em tudo
