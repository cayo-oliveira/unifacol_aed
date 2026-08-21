# Gabaritos privados — Análise Exploratória de Dados — 2026.2

Não publicar com as provas.

## Avaliação da I Unidade

| ID / origem | Pos. A | Gab. A | Pos. B | Gab. B | Permutação B |
|---|---:|:---:|---:|:---:|---|
| AED-C01-O01-ADP | 1 | C | 4 | D | A→B, B→E, C→D, D→A, E→C |
| AED-C02-O09-ADP | 2 | — | 3 | — | — |
| AULA-P60-C02-O06-ADP | 3 | A | 8 | C | A→C, B→E, C→A, D→D, E→B |
| AED-C07-O03-ADP | 4 | B | 2 | B | A→D, B→B, C→E, D→C, E→A |
| AED-C04-O03-ADP | 5 | A | 6 | D | A→D, B→B, C→E, D→A, E→C |
| AED-C05-O03-ADP | 6 | C | 1 | E | A→C, B→A, C→E, D→B, E→D |
| AED-C06-O09-ADP | 7 | B | 5 | C | A→D, B→C, C→A, D→E, E→B |
| AED-C08-D11-ADP | 8 | — | 7 | — | — |

### Resoluções e critérios privados

- **Q1 / AED-C01-O01-ADP:** alternativa C. É a única que conecta a dor observada a uma pergunta com recorte, evidência investigável e decisão de priorização.
- **Q2 / AED-C02-O09-ADP:** espera-se reconhecer que o dispositivo preferencial é variável qualitativa nominal; celular e notebook empatam com frequência 12, portanto a distribuição é bimodal. Média e mediana não possuem interpretação estatística adequada para categorias nominais sem ordem e distância mensurável. Aceitar redações equivalentes bem justificadas.
- **Q3 / AULA-P60-C02-O06-ADP:** o registro de 7 minutos não integra a população analítica; restam `2, 4, 5, 6, 8, 10, 12, 14`, logo `n=8`. Pela convenção declarada, `L=(60/100)(8+1)=5,4`. Interpolando entre o 5º valor (8) e o 6º (10): `8 + 0,4(10-8)=8,8`. Alternativa A na versão A e C na versão B.
- **Q4 / AED-C07-O03-ADP:** alternativa B. `r=0,78` descreve associação linear agregada forte, mas não identifica efeito causal; frequência, entregas, curso e outras variáveis podem confundir a relação. `r²≈0,61` também não autoriza atribuição causal exclusiva.
- **Q5 / AED-C04-O03-ADP:** alternativa A. Diferença absoluta: `81%-79%=2` pontos percentuais. Variação relativa: `(81-79)/79 × 100 ≈ 2,53%`. A representação não deve amplificar artificialmente a diferença por eixo truncado.
- **Q6 / AED-C05-O03-ADP:** alternativa C. O grão é item de pedido, mas `total_pedido` pertence ao pedido; é preciso obter uma ocorrência por identificador de pedido e então somar `120+80+120=320`. `DISTINCT` no valor erra porque pedidos diferentes podem ter o mesmo total.
- **Q7 / AED-C06-O09-ADP:** alternativa B. A narrativa deve partir de contexto e problema decisório, apresentar evidência e limitações antes da recomendação condicionada.
- **Q8 / AED-C08-D11-ADP:** avaliar a coerência do processo de AED de ponta a ponta. Uma resposta forte conecta dor e problema de negócio; pergunta analítica e decisão; fontes, unidade de análise, grão e integração; qualidade e preparação; tipos de variáveis e estatística descritiva; exploração de distribuições, segmentos, relações e extremos; cautela com correlação/causalidade; escolha de indicadores e visuais; dashboard e narrativa; insight, limitações, recomendação e decisão. Não exigir ordem textual idêntica, desde que o encadeamento seja justificável e auditável.

## Avaliação da II Unidade

| ID | Pos. A | Gab. A | Pos. B | Gab. B | Permutação B |
|---|---:|:---:|---:|:---:|---|
| AED-C09-O03 | 1 | D | 4 | E | C→A, B→B, A→C, E→D, D→E |
| AED-C10-D13 | 2 | — | 3 | — | — |
| AED-C14-O05 | 3 | B | 1 | B | E→A, B→B, D→C, A→D, C→E |
| AED-C11-D13 | 4 | — | 8 | — | — |
| AED-C12-O07 | 5 | B | 5 | B | D→A, B→B, E→C, C→D, A→E |
| AED-C11-O03 | 6 | D | 6 | A | D→A, B→B, C→C, E→D, A→E |
| AED-C10-O01 | 7 | C | 7 | D | E→A, D→B, A→C, C→D, B→E |
| AED-C13-O01 | 8 | B | 2 | A | B→A, A→B, C→C, E→D, D→E |

### Critérios originais das discursivas

- **AED-C10-D13:** | AED-C10-D13 | Padrão criterial | Cumprir cada produto solicitado: Defina catálogo mínimo de métrica com fórmula, grão, dimensões, filtros, owner, versão e testes. Aceitar caminho equivalente quando cálculos, premissas, evidência, limite e decisão forem coerentes. |
- **AED-C11-D13:** \Disc{AED-C11-D13}{Identidade do usuário atravessa app e BI; consulta usa camada semântica/RLS; serviço isolado faz simulação; estado guarda rascunho, revisão e aprovação; saída traz consulta, snapshot e parâmetros; assinatura vincula artefato; logs minimizados, testes de contrato, canário e rollback.}{2: identidade/RLS; 2: semântica; 2: simulação/estado; 2: evidência/assinatura; 2: testes/rollback. Conta administrativa ou CSV irrestrito elimina os critérios de acesso.} \Disc{AED-C11-D14}{Disponibilidade 96\%; cauda até 5 s $17.600/19.200\approx91{,}7\%$; correção citada 84\%; oito exposições. Só a meta de cauda passa; exposição bloqueia publicação e exige contenção, causa, correção e reteste.}{2: disponibilidade; 2: cauda com denominador correto; 2: correção; 2: acesso; 2: decisão não compensatória.} \Disc{AED-C11-D15}{Extrair contratos de métricas, políticas e identidade; criar testes dourados e adaptadores por produto; exportar traces/evidências em formato portável; executar paralelo e comparar por item; cortar após gates e manter rollback. Visuais e otimizações podem ficar específicos se não redefinirem significado ou acesso.}{2: contratos; 2: testes; 2: adaptadores/identidade; 2: paralelo/gates; 2: justificativa do que pode permanecer específico.} \section{Capítulo 12 --- Streamlit e Llama} \Obj{AED-C12-O01}{B}{Separar UI, domínio, adaptador e dados torna a fórmula testável e impede que mudança visual altere regra analítica.}{A: comentários não isolam; B: separação correta; C: LLM não é motor certificado; D: duplicação cria divergência; E: congelar entrada não corrige arquitetura.} \Obj{AED-C12-O02}{B}{Margem $819{,}2$; saldo $3.372{,}8$; $\lfloor3.372{,}8/420\rfloor=8$.}{A: arredonda de forma indevida; B: conta integral; C: ignora saída; D: interpreta janela incorretamente; E: ignora reservas.} \Obj{AED-C12-O03}{C}{Ferramentas permitidas e validadas reduzem a superfície; código livre, se indispensável, precisa isolamento sem segredo, rede ou escrita ampla.}{A: revisão posterior; B: segredo acessível ao processo; C: controle técnico; D: promessa não contém efeito; E: determinismo não é autorização.} \Obj{AED-C12-O04}{A}{$2.000(0{,}40)(0{,}75)=600$ hits; $600(0{,}08)=48$.}{A: correta; B: assume 100\% de hit; C: confunde não repetidas; D e E: produtos incompletos.} \Obj{AED-C12-O05}{B}{Formulário evita submissão em qualquer rerun; estado e idempotência identificam o efeito; cache precisa incluir dados e versão.}{A: destrói interação; B: correto; C: mistura usuários; D: timeout não evita duplicata; E: apaga evidência sem conter efeito.} \Obj{AED-C12-O06}{A}{Etapas externas somam 2,5 s, restando 2,5 s ao modelo no p95.}{A: completa; B: omite validação; C: omite etapas; D: cálculo participa da percepção; E: orçamento não é exclusivo do modelo.} \Obj{AED-C12-O07}{B}{Validação semântica deve seguir a sintática: esquema, enumeração de gráficos, colunas existentes e tipos antes de renderizar.}{A: JSON válido pode ser semanticamente inválido; B: completo; C: executa código; D: mais contexto não garante validade; E: remove controles.} \Obj{AED-C12-O08}{A}{$450/500=90\%$, $405/450=90\%$ e $360/500=72\%$.}{A: denominadores corretos; B, C, D e E: misturam taxa condicional, contagem intermediária e total.} \Obj{AED-C12-O09}{B}{A finalidade requer apenas unidade e vendas; seleção e agregação locais, retenção definida e logs mínimos reduzem exposição.}{A: upload não amplia finalidade; B: minimização; C: nome também identifica; D: temperatura não protege; E: transmissão continua excessiva.}

## Segunda Chamada

| ID | Pos. A | Gab. A | Pos. B | Gab. B | Permutação B |
|---|---:|:---:|---:|:---:|---|
| AED-C11-D11 | 1 | — | 7 | — | — |
| AED-C10-O09 | 2 | A | 2 | B | E→A, A→B, D→C, B→D, C→E |
| AED-C07-O09 | 3 | A | 3 | C | E→A, D→B, A→C, C→D, B→E |
| AED-C13-O09 | 4 | B | 6 | C | D→A, E→B, B→C, A→D, C→E |
| AED-C07-D11 | 5 | — | 4 | — | — |
| AED-C02-O07 | 6 | A | 5 | C | E→A, D→B, A→C, C→D, B→E |
| AED-C03-O03 | 7 | B | 8 | B | E→A, B→B, A→C, D→D, C→E |
| AED-C11-O01 | 8 | C | 1 | E | A→A, E→B, B→C, D→D, C→E |

### Critérios originais das discursivas

- **AED-C11-D11:** \Disc{AED-C11-D11}{Piloto com conjunto estratificado de perguntas acadêmicas/financeiras, perfis e identidades; mesmas fontes/snapshots e rubrica; referência para métrica, filtros e consulta; medição de correção, evidência, p95 e custo; teste de RLS e supressão para grupos $<5$; zero acesso indevido como gate; decisão sem marca prévia.}{2: conjunto/perfis; 2: semântica/evidência; 2: acesso e grupos pequenos; 2: custo/latência; 2: gates e comparabilidade. Erro impeditivo no critério de acesso: admitir consulta protegida antes de filtrar.} \Disc{AED-C11-D12}{A=R\$4.500 e $4.500/[60.000(0{,}89)]\approx$R\$0,0843; B=R\$3.900 e $\approx$R\$0,0756; C=R\$6.030 e $\approx$R\$0,1196. A e B passam 85\%; B lidera sob os dados. C exige melhoria e reteste comparável.}{2: custos; 2: corretas citadas; 2: custos úteis; 2: gates; 2: decisão condicionada.} \Disc{AED-C11-D13}{Identidade do usuário atravessa app e BI; consulta usa camada semântica/RLS; serviço isolado faz simulação; estado guarda rascunho, revisão e aprovação; saída traz consulta, snapshot e parâmetros; assinatura vincula artefato; logs minimizados, testes de contrato, canário e rollback.}{2: identidade/RLS; 2: semântica; 2: simulação/estado; 2: evidência/assinatura; 2: testes/rollback. Conta administrativa ou CSV irrestrito elimina os critérios de acesso.} \Disc{AED-C11-D14}{Disponibilidade 96\%; cauda até 5 s $17.600/19.200\approx91{,}7\%$; correção citada 84\%; oito exposições. Só a meta de cauda passa; exposição bloqueia publicação e exige contenção, causa, correção e reteste.}{2: disponibilidade; 2: cauda com denominador correto; 2: correção; 2: acesso; 2: decisão não compensatória.} \Disc{AED-C11-D15}{Extrair contratos de métricas, políticas e identidade; criar testes dourados e adaptadores por produto; exportar traces/evidências em formato portável; executar paralelo e comparar por item; cortar após gates e manter rollback. Visuais e otimizações podem ficar específicos se não redefinirem significado ou acesso.}{2: contratos; 2: testes; 2: adaptadores/identidade; 2: paralelo/gates; 2: justificativa do que pode permanecer específico.} \section{Capítulo 12 --- Streamlit e Llama} \Obj{AED-C12-O01}{B}{Separar UI, domínio, adaptador e dados torna a fórmula testável e impede que mudança visual altere regra analítica.}{A: comentários não isolam; B: separação correta; C: LLM não é motor certificado; D: duplicação cria divergência; E: congelar entrada não corrige arquitetura.} \Obj{AED-C12-O02}{B}{Margem $819{,}2$; saldo $3.372{,}8$; $\lfloor3.372{,}8/420\rfloor=8$.}{A: arredonda de forma indevida; B: conta integral; C: ignora saída; D: interpreta janela incorretamente; E: ignora reservas.} \Obj{AED-C12-O03}{C}{Ferramentas permitidas e validadas reduzem a superfície; código livre, se indispensável, precisa isolamento sem segredo, rede ou escrita ampla.}{A: revisão posterior; B: segredo acessível ao processo; C: controle técnico; D: promessa não contém efeito; E: determinismo não é autorização.} \Obj{AED-C12-O04}{A}{$2.000(0{,}40)(0{,}75)=600$ hits; $600(0{,}08)=48$.}{A: correta; B: assume 100\% de hit; C: confunde não repetidas; D e E: produtos incompletos.} \Obj{AED-C12-O05}{B}{Formulário evita submissão em qualquer rerun; estado e idempotência identificam o efeito; cache precisa incluir dados e versão.}{A: destrói interação; B: correto; C: mistura usuários; D: timeout não evita duplicata; E: apaga evidência sem conter efeito.} \Obj{AED-C12-O06}{A}{Etapas externas somam 2,5 s, restando 2,5 s ao modelo no p95.}{A: completa; B: omite validação; C: omite etapas; D: cálculo participa da percepção; E: orçamento não é exclusivo do modelo.} \Obj{AED-C12-O07}{B}{Validação semântica deve seguir a sintática: esquema, enumeração de gráficos, colunas existentes e tipos antes de renderizar.}{A: JSON válido pode ser semanticamente inválido; B: completo; C: executa código; D: mais contexto não garante validade; E: remove controles.}
- **AED-C07-D11:** | AED-C07-D11 | Padrão criterial | Cumprir cada produto solicitado: Desenhe fluxo da fonte imperfeita à recomendação com testes de grão, qualidade, transformação, visual e auditoria. Aceitar caminho equivalente quando cálculos, premissas, evidência, limite e decisão forem coerentes. |

## Avaliação Final

| ID | Pos. A | Gab. A | Pos. B | Gab. B | Permutação B |
|---|---:|:---:|---:|:---:|---|
| AED-C09-O09 | 1 | A | 8 | B | C→A, A→B, E→C, D→D, B→E |
| AED-C05-O07 | 2 | B | 1 | D | A→A, E→B, D→C, B→D, C→E |
| AED-C14-D15 | 3 | — | 6 | — | — |
| AED-C03-D15 | 4 | — | 3 | — | — |
| AED-C02-O05 | 5 | B | 7 | C | D→A, A→B, B→C, E→D, C→E |
| AED-C08-O05 | 6 | E | 5 | D | B→A, A→B, D→C, E→D, C→E |
| AED-C12-O05 | 7 | B | 4 | C | E→A, A→B, B→C, C→D, D→E |
| AED-C13-O05 | 8 | B | 2 | C | A→A, E→B, B→C, C→D, D→E |

### Critérios originais das discursivas

- **AED-C14-D15:** \Disc{AED-C14-D15}{Congelar uso do relatório e conter novas decisões; corrigir estoque com responsáveis; preservar snapshot, consulta e registros sem alterar evidência; comunicar fatos separados de hipóteses; reconstruir com versões; apurar impacto e encaminhar compensação; implantar snapshot/versionamento obrigatório, frescor e gates; canário e rollback antes do retorno.}{2: contenção/correção; 2: evidência; 2: comunicação/apuração; 2: correção técnica; 2: gates/retorno.} \end{document}
- **AED-C03-D15:** - **AED-C03-D15.** Bernoulli para uma tentativa, binomial para contagem sob n/p/independência, uniforme para janela equiprovável, normal para erro simétrico aditivo (1,2); parâmetro e possível violação de cada escolha (0,8).

## Simulado ENADE

| ID | Pos. A | Gab. A | Pos. B | Gab. B | Permutação B |
|---|---:|:---:|---:|:---:|---|
| AED-C01-O07 | 1 | B | 7 | A | B→A, D→B, E→C, A→D, C→E |
| AED-C11-O07 | 2 | A | 4 | B | E→A, A→B, B→C, D→D, C→E |
| AED-C12-D15 | 3 | — | 2 | — | — |
| AED-C07-O01 | 4 | C | 8 | B | A→A, C→B, E→C, B→D, D→E |
| AED-C09-O05 | 5 | E | 3 | E | D→A, A→B, B→C, C→D, E→E |
| AED-C12-O03 | 6 | C | 6 | B | A→A, C→B, B→C, E→D, D→E |
| AED-C05-O09 | 7 | B | 1 | A | B→A, C→B, A→C, E→D, D→E |
| AED-C01-D11 | 8 | — | 5 | — | — |

### Critérios originais das discursivas

- **AED-C12-D15:** \Disc{AED-C12-D15}{Congelar baseline e conjunto estratificado; versionar modelo/prompt/parser/cache; alterar um fator por ablação; testar esquema, cálculos de referência, segurança, latência, memória e custo; shadow, canário, limites e rollback automático.}{2: baseline/dados; 2: versões/ablação; 2: testes funcionais; 2: operação/segurança; 2: implantação/rollback.} \section{Capítulo 13 --- Agentes analíticos} \Obj{AED-C13-O01}{B}{Agente coordena estado e decisão; SQL é ferramenta; manual é skill/playbook; LLM apoia interpretação.}{A: troca papéis; B: correto; C: participação não define agência; D: inverte memória; E: skill não concede permissão.} \Obj{AED-C13-O02}{A}{$0{,}96(0{,}98)(0{,}95)=0{,}89376\approx89{,}4\%$.}{A: produto correto sob independência aproximada; B: média não representa sucesso conjunto; C: subtração arbitrária; D: verificador não repara dado; E: soma de erros ignora interseções.} \Obj{AED-C13-O03}{B}{Ferramentas separadas, escopos mínimos e validação aplicam menor privilégio; efeitos relevantes recebem aprovação.}{A e C: instrução/ocultação não revogam permissão; B: correto; D: memória não é controle; E: confiança não autoriza pagamento.} \Obj{AED-C13-O04}{B}{Três tentativas: R\$0,36 e $0{,}6+3(1{,}4)=4{,}8$ s; quatro violam ambos.}{A: terceira cabe; B: correto; C: orçamento não compensa; D: retry pode ser seguro com operação adequada; E: divisão incorreta.} \Obj{AED-C13-O05}{B}{Preferência é perfil revogável; política é artefato governado, versionado e aplicado por controle confiável.}{A: mistura autoridades; B: correto; C: usuário não revoga política; D: retenção excessiva; E: agente não escolhe vigência.} \Obj{AED-C13-O06}{C}{$1.500(0{,}20)=300$ revisões; $300(6)=1.800$ min; $1.800/360=5$.}{A: usa revisões como analistas; B: quatro cobrem 240; C: correto; D: operação dimensional inválida; E: trata todos como revisados.} \Obj{AED-C13-O07}{B}{Sem ganho medido ou especialização necessária, o fluxo simples é baseline mais econômico e observável.}{A: número de papéis não prova qualidade; B: evidência; C: remove fontes verificáveis; D: aleatoriedade não é experimento; E: duplicação aumenta custo.} \Obj{AED-C13-O08}{A}{$88/92=95{,}7\%$, $82/88=93{,}2\%$, $78/82=95{,}1\%$ e $78/100=78\%$.}{A: funil correto; B, C e D: usam contagens/denominadores diferentes; E: relata perdas, não taxas de sucesso pedidas.} \Obj{AED-C13-O09}{B}{Sem dado individual autorizado, o agente recusa a inferência e oferece alternativa agregada ou humana.}{A: inferência não autorizada; B: recusa útil; C: sintético com nomes reais continua danoso; D: repetição não cria evidência; E: memória não cria autorização.} \Obj{AED-C13-O10}{D}{Único passa 81\%, zero, 6,8 s e R\$0,31; cada multi viola um gate.}{A: ação indevida; B: p95; C: custo; D: todos; E: média não elimina violações.} \Disc{AED-C13-D11}{Estado inclui pergunta, identidade, plano, evidências e status; nós planejam, consultam SPEC/incidentes, calculam, verificam e redigem; ferramentas somente leitura; skill versionada; memória separa perfil de fatos; gates de evidência e HITL; recusa sem fonte; trace minimizado; parada por resposta sustentada, limite ou encaminhamento. Hipótese é explicação provisória, evidência é artefato verificável e decisão é ação autorizada.}{1 ponto por: estado; nós; ferramentas/skill; memória; gates/recusa; HITL; trace; parada; distinção hipótese/evidência; decisão/autorização.}
- **AED-C01-D11:** - **AED-C01-D11.** Até 2,0: pergunta com população/período/resultado/decisão (0,5); cadeia coerente com fontes e validação (0,5); dois riscos, como viés, privacidade ou falso positivo (0,5); duas evidências e revisão humana antes de contato (0,5). Erro impeditivo no critério: tratar previsão como certeza ou autorizar mensagem automática sem controle.

