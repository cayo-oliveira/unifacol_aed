# Engenharia agentic aplicada ao software

## Regra de precisão

Separar princípio de interface de produto. `contexto.md`, `arquitetura.md`, `specs/`, `playbooks/` e `memory-bank/*.mb` podem ser convenções pedagógicas do repositório; não anunciá-los como padrão universal ou comando nativo. Quando citar caminho ou comando de uma ferramenta, conferir documentação oficial e registrar a data ou versão relevante.

## SDD

Usar como referência científica principal de 2026: *Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants* (arXiv:2602.00180). Ensinar o espectro `spec-first` → `spec-anchored` → `spec-as-source` e o fluxo especificar → planejar → implementar → validar.

Todo caso prático deve tornar visíveis:

- contexto: problema, atores, estado atual, vocabulário, fontes e dúvidas;
- requisitos: comportamento, regras, exceções e critérios de aceitação;
- arquitetura: componentes, fronteiras, dados, interfaces e requisitos não funcionais;
- plano e tarefas: incrementos pequenos, dependências e responsável;
- validação: testes e evidências que comparam implementação, plano e intenção.

Não prescrever rigor máximo para todo projeto. Discutir sobre-especificação, subespecificação e divergência. Em IA, adicionar protocolo experimental, baseline, métrica, reprodução e análise de erro.

## Taxonomia agentic

- LLM: modelo que interpreta e gera sequências.
- ferramenta: operação delimitada que produz efeito ou dado.
- agente: modelo + contexto + ferramentas + laço de decisão orientado a objetivo.
- subagente: executor com contexto próprio que reporta a um coordenador.
- multiagente: composição de papéis/sessões para paralelismo, especialização, isolamento ou crítica independente.
- skill: conhecimento procedural reutilizável, descoberto e carregado progressivamente.
- playbook: sequência operacional para um cenário recorrente; não possui um único formato universal.
- MCP: camada de conectividade com ferramentas e dados; não substitui procedimento.
- Memory Bank: convenção versionada do projeto para decisões, estado, evidências e próximo passo; não confundir com memória nativa de produto.

Usar como referência científica principal de 2026: *Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward* (arXiv:2602.12430). Cobrir divulgação progressiva, Skills versus MCP, aquisição/composição, limites da conversão multiagente→skills e segurança.

## Estruturas atuais a comparar

- Codex: `AGENTS.md`, `.agents/skills/<nome>/SKILL.md`, `.codex/config.toml` para configurações de agentes.
- Claude Code: `CLAUDE.md`, `.claude/skills/`, `.claude/agents/`.
- GitHub Copilot: `.github/copilot-instructions.md`, `.github/instructions/`, `.github/prompts/`, `.github/agents/` e caminhos de skills aceitos pela documentação.
- Kiro: `.kiro/steering/` e specs de requisitos, desenho e tarefas.

Não criar tabela de ferramenta sem verificar documentação atual. Links-base:

- Codex customization: <https://learn.chatgpt.com/docs/customization/overview#skills>
- Claude Code subagents: <https://code.claude.com/docs/en/sub-agents>
- GitHub Copilot customization: <https://docs.github.com/en/copilot/reference/customization-cheat-sheet>
- Kiro steering/specs: <https://kiro.dev/docs/steering/> e <https://kiro.dev/docs/cli/v3/specs/>

## Segurança e avaliação

Tratar skill como dependência: verificar origem e versão, ler instruções e scripts, limitar arquivos/rede/ferramentas, testar isoladamente e registrar permissões. Comparar agente único com skills e multiagente usando as mesmas tarefas: sucesso, qualidade, custo, latência, rastreabilidade e consequência do erro. Mais agentes ou mais skills não são, isoladamente, evidência de melhor arquitetura.
