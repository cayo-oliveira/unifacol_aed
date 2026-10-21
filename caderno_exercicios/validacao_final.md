# Validação final — Caderno ENADE AED v2

Data de revisão: 2026-10-21. Escopo: integração do caderno público, reserva de questões e materiais da Unidade II.

## Integridade do banco

- 14 capítulos, 210 posições públicas: 140 objetivas e 70 discursivas (15 por capítulo: 10+5).
- 40 IDs ímpares únicos permanecem no banco reservado e nos cinco instrumentos (8 por instrumento).
- Os 40 itens reservados foram substituídos nos mesmos números por itens públicos distintos `-S1`; nenhum ID reservado original aparece nos arquivos públicos de capítulo.
- Respostas do estudante permanecem somente nos itens pares 2, 4, 6, 8, 10, 12 e 14.
- Respostas e justificativas dos substitutos estão nos três gabaritos privados; mapas de correspondência por faixa estão nos arquivos `substituicoes_reservados_*.md`.

## Validadores e PDFs

Em 21/10/2026:

- `validate_workbook.py caderno_exercicios/capitulos`: aprovado, 14/14 capítulos.
- `validate_generated_exams.py --repo . --u1 1-8 --u2 9-14`: aprovado, 5 instrumentos, 10 versões, 40 IDs únicos e Final ≤ Segunda Chamada.
- Auditoria de integridade adicional: 40/40 IDs do manifesto têm substituto `-S1` único; nenhum ID reservado original aparece nas fontes públicas; os 15 itens e a resposta de pares foram preservados em cada capítulo.
- Tectonic compilou `main.tex` com o bundle local. PDF A4 de 114 páginas, sem `Overfull`, erro LaTeX, controle indefinido ou caractere ausente no log.
- Gabarito privado dos Capítulos 11–14 compilado em PDF A4 de 10 páginas. Cenários dos estudantes: 2 páginas; chave docente refeita para quatro situações e compilada em 3 páginas A4. Logs sem `Overfull` ou erros; a chave docente tem avisos `Underfull` localizados em alinhamento/parágrafo, sem corte visual na amostra conferida.
- Inspeção visual amostral: abertura dos Capítulos 9 e 10; os quatro pedidos, tabelas e avaliação no PDF dos estudantes; cálculos e código de referência nas três páginas da chave docente. Conteúdo legível, sem cortes visíveis.
- A dinâmica foi reduzida e clarificada para quatro alunos: um cenário simples por aluno, planejamento de 10–15 minutos no encontro, implementação em casa e apresentação na aula seguinte. Mapeamento 15→22/10, 22→29/10, 29/10→05/11 e 05→19/11 (12/11 EXPOFACOL).
- `git diff --check`: aprovado após restaurar o log gerado da compilação do livro.

## Artefatos

- `main.tex` e `main.pdf` — caderno público compilado.
- `Caderno de Exercícios.pdf` — cópia de distribuição.
- `capitulos/` — 14 capítulos; `professor/` — gabaritos privados.
- `manifesto_preservacao.md` e três mapas de substituição.
- `caderno_atividades/dinamicas_ii_unidade/` — cenários dos estudantes e chave docente em PDFs separados.

Limite da auditoria: o script opcional `audit_workbook_richness.py` mencionado em uma validação histórica de agosto não existe mais neste checkout; a estrutura, integridade, compilação e inspeção visual foram conferidas pelos meios listados acima.
