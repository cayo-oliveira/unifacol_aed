#!/usr/bin/env python3
"""Valida a estrutura pública de capítulos do caderno ENADE UNIFACOL."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ITEM = re.compile(r"\\ItemHeader\{(\d+)\}\{(Objetiva|Discursiva)\}")
ANSWER = re.compile(r"\\paragraph\{Questão\s+(\d+)\s+[^}]*\}")


def validate(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    items = [(int(number), kind) for number, kind in ITEM.findall(text)]
    answers = [int(number) for number in ANSWER.findall(text)]
    errors: list[str] = []

    if len(items) != 15:
        errors.append(f"esperados 15 itens; encontrados {len(items)}")
    numbers = [number for number, _ in items]
    if numbers != list(range(1, 16)):
        errors.append(f"numeração deve ser 1..15; encontrada {numbers}")
    objectives = sum(kind == "Objetiva" for _, kind in items)
    discursive = sum(kind == "Discursiva" for _, kind in items)
    if (objectives, discursive) != (10, 5):
        errors.append(
            f"esperados 10 objetivos e 5 discursivos; encontrados {objectives} e {discursive}"
        )
    if answers != [2, 4, 6, 8, 10, 12, 14]:
        errors.append(
            "respostas públicas devem ser exatamente 2,4,6,8,10,12,14; "
            f"encontradas {answers}"
        )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("chapters", type=Path, help="diretório com os .tex do caderno")
    args = parser.parse_args()
    files = sorted(args.chapters.glob("*.tex"))
    if not files:
        print(f"ERRO: nenhum .tex encontrado em {args.chapters}")
        return 2

    failed = False
    for path in files:
        errors = validate(path)
        if errors:
            failed = True
            for error in errors:
                print(f"ERRO {path.name}: {error}")
        else:
            print(f"OK {path.name}: 15 itens (10+5), respostas pares")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
