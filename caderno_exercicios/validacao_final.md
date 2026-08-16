# Validação final — Caderno ENADE AED v2

Data: 2026-08-12. Escopo: pacote temporário; nenhum repositório foi editado.

## Estrutura preservada

- 14 capítulos aprovados por `validate_workbook.py`.
- 210 itens: 140 objetivos e 70 discursivos.
- Cada capítulo contém exatamente 15 itens, sendo 10 objetivos e 5 discursivos.
- Respostas públicas somente para os itens pares; gabaritos integrais permanecem em `professor/`.
- IDs, competências, procedimentos matemáticos e respostas conceituais preservados conforme `manifesto_preservacao.md`.

## Auditoria de riqueza

O script canônico `audit_workbook_richness.py` aprovou 14 de 14 capítulos. Médias de palavras dos textos-base por capítulo: C1 46,5; C2 55,3; C3 51,8; C4 45,3; C5 51,3; C6 45,1; C7 45,5; C8 45,1; C9 45,6; C10 45,5; C11 58,3; C12 48,3; C13 47,2; C14 45,0. Todos os capítulos apresentam ao menos dois tipos de suporte detectáveis e fonte em seus 15 itens.

A busca literal não encontrou `VozTexto`, comandos mecânicos do tipo “Use obrigatoriamente o Quadro/Figura/Tabela” nem os trechos de boilerplate editorial previamente identificados. Vozes de memorando, parecer, auditoria, incidente, reunião e caso profissional aparecem organicamente nos textos-base.

## Compilação e inspeção

- `tectonic main.tex`: compilação concluída sem mensagem de Overfull, Missing character, erro ou fatal.
- PDF: 114 páginas, A4, 350.896 bytes e 33.025 palavras extraídas.
- Inspeção visual ampla anterior: páginas 1, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96 e 114.
- Inspeção visual final após os últimos ajustes: páginas 1, 67, 75 e 114, cobrindo sumário, Capítulos 9 e 10 e respostas finais.
- Resultado visual: identidade consistente, tabelas e diagramas legíveis, alternativas alinhadas, fontes presentes, sem cortes, sobreposição ou conteúdo editorial exposto ao estudante.

## Artefatos

- `main.tex` e `main.pdf`.
- `caderno_enade_style.tex`.
- `capitulos/`: 14 capítulos.
- `professor/`: três blocos de gabarito privado e instruções de vínculo.
- `manifesto_preservacao.md`.
- `auditoria_oficial/`: extrações consultadas dos documentos oficiais.
- `inspecao/` e `inspecao_final/`: amostras rasterizadas da inspeção.
