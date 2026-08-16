#!/usr/bin/env python3
"""Valida profundidade estrutural de um capítulo LaTeX da Trilha UNIFACOL."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

HEADING = re.compile(r"\\(section|subsection|subsubsection)\*?\{([^}]*)\}")
ENVIRONMENTS = (
    "SummaryBox", "GuidedBox", "ArticleBox", "center", "table", "tabular",
    "tabularx", "enumerate", "itemize", "quote", "figure", "tikzpicture",
)


def strip_non_prose(text: str) -> str:
    text = re.sub(r"(?m)%.*$", "", text)
    for env in ENVIRONMENTS:
        text = re.sub(
            rf"\\begin\{{{env}\}}.*?\\end\{{{env}\}}",
            "\n\n",
            text,
            flags=re.S,
        )
    text = re.sub(r"\\(?:chapter|section|subsection|subsubsection)\*?\{[^}]*\}", "", text)
    text = re.sub(r"\\(?:label|href|url|textbf|textit|emph)\{[^}]*\}(?:\{([^}]*)\})?", r" \1 ", text)
    text = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^]]*\])?", " ", text)
    text = re.sub(r"[{}$&_^~]", " ", text)
    return text


def prose_paragraphs(text: str) -> list[str]:
    clean = strip_non_prose(text)
    blocks = re.split(r"\n\s*\n", clean)
    result = []
    for block in blocks:
        words = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]+", block)
        if len(words) >= 20:
            result.append(" ".join(words))
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("tex", type=Path)
    parser.add_argument("--min-paragraphs", type=int, default=5)
    parser.add_argument("--min-words", type=int, default=5000)
    args = parser.parse_args()

    source = args.tex.read_text(encoding="utf-8")
    matches = list(HEADING.finditer(source))
    if not matches:
        print("ERRO: nenhum título de seção encontrado.", file=sys.stderr)
        return 2

    failures = []
    total_words = len(re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]+", strip_non_prose(source)))
    print(f"Arquivo: {args.tex}")
    print(f"Palavras de prosa estimadas: {total_words} (mínimo {args.min_words})")
    if total_words < args.min_words:
        failures.append(f"capítulo tem {total_words} palavras de prosa; mínimo {args.min_words}")

    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(source)
        count = len(prose_paragraphs(source[match.end():end]))
        level, title = match.groups()
        print(f"- {level} '{title}': {count} parágrafos")
        if count < args.min_paragraphs:
            failures.append(f"{level} '{title}' tem {count}; mínimo {args.min_paragraphs}")

    article_boxes = len(re.findall(r"\\begin\{ArticleBox\}", source))
    if article_boxes and article_boxes < 3:
        failures.append(f"estudo de artigo tem {article_boxes} caixas cinza; mínimo 3")

    if failures:
        print("\nVALIDAÇÃO REPROVADA:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print("VALIDAÇÃO APROVADA")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
