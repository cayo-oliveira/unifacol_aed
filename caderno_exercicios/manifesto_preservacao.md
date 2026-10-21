# Manifesto de preservação old → new — AED ENADE v2

Origem integrada: fontes do caderno em `caderno_exercicios/capitulos/`; banco reservado: `provas/2026.2/banco_reservado/itens_selecionados.tex`; seleção e IDs: `provas/2026.2/professor/manifesto_selecao.json`.

O banco de trabalho contém 14 capítulos e 210 posições públicas, com 10 objetivas e 5 discursivas por capítulo. A seleção reservada usa 40 IDs ímpares: 8 para cada um dos instrumentos Prova I, Prova II, Segunda Chamada, Final e Simulado. Os itens selecionados foram preservados integralmente no banco reservado e removidos dos respectivos enunciados públicos. Cada posição recebeu novo cenário e ID privado `-S1`, mantendo número, tipo e competência ampla. Os substitutos não são itens de prova.

| Capítulos | Itens reservados | Substitutos públicos | Mapa e gabarito privado |
|---|---:|---:|---|
| 1–5 | 14 | 14 | `substituicoes_reservados_cap01_05.md`; `professor/gabarito_caps_01_05.md` |
| 6–10 | 12 | 12 | `substituicoes_reservados_cap06_10.md`; `professor/gabarito_caps_06_10.md` |
| 11–14 | 14 | 14 | `substituicoes_reservados_cap11_14.md`; `professor/gabarito_caps_11_14.tex` |
| **Total** | **40** | **40** | IDs originais permanecem no banco reservado e nas provas |

As posições, tipos e competências curriculares permanecem estáveis; enunciados, dados e gabaritos dos substitutos são distintos. Os três mapas documentam ID reservado → substituto, resposta e diferença do cenário. Gabaritos privados completos permanecem em `professor/`; o público recebe explicações somente nos itens pares 2, 4, 6, 8, 10, 12 e 14.

## Restrições que invalidam distratores

O diagnóstico privado deve relacionar cada opção à restrição concreta do cenário. As famílias recorrentes incluem grão/denominador, média que esconde cauda, correlação versus causalidade, acesso/finalidade, vigência/proveniência, custo/latência, correção semântica, ausência versus zero, visual/acessibilidade e efeitos externos sem autorização/idempotência. Uma opção válida em outro contexto pode ser inválida aqui quando viola uma premissa explícita.

## Verificação de integridade

Antes de publicar o pacote, conferir que os 40 IDs do manifesto coincidem com o banco reservado, não aparecem nos arquivos públicos e cada um possui um substituto `-S1` no mesmo número. Conferir também 15 itens por capítulo, respostas públicas apenas pares, versões A/B e a compilação do PDF público. O resultado atualizado está em `validacao_final.md`.
