#!/usr/bin/env python3
"""Valida estrutura, rastreabilidade A/B e compilação das provas geradas."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


INSTRUMENTS = ("prova_i_unidade", "prova_ii_unidade", "segunda_chamada", "final", "simulado")


def chapter_set(value: str) -> set[int]:
    result: set[int] = set()
    for part in value.split(","):
        if "-" in part:
            first, last = map(int, part.split("-", 1))
            result.update(range(first, last + 1))
        else:
            result.add(int(part))
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--u1", required=True)
    parser.add_argument("--u2", required=True)
    args = parser.parse_args()
    u1, u2 = chapter_set(args.u1), chapter_set(args.u2)
    root = args.repo / "provas" / "2026.2"
    manifest = json.loads((root / "professor" / "manifesto_selecao.json").read_text(encoding="utf-8"))
    rows = list(csv.DictReader((root / "professor" / "matriz_rastreabilidade.csv").open(encoding="utf-8")))
    failures: list[str] = []
    used: list[str] = []

    for name in INSTRUMENTS:
        items = manifest["instruments"].get(name, [])
        kinds = [item["type"] for item in items]
        if len(items) != 8 or kinds.count("O") != 6 or kinds.count("D") != 2:
            failures.append(f"{name}: esperado 8 itens (6O+2D)")
        used.extend(item["id"] for item in items)
        chapters = {int(item["chapter"]) for item in items}
        if name == "prova_i_unidade" and not chapters <= u1:
            failures.append(f"{name}: capítulo fora da I unidade")
        if name == "prova_ii_unidade" and not chapters <= u2:
            failures.append(f"{name}: capítulo fora da II unidade")
        if name in {"segunda_chamada", "final", "simulado"} and not (chapters & u1 and chapters & u2):
            failures.append(f"{name}: não cobre as duas unidades")

        orders: dict[str, list[str]] = {}
        for version in "AB":
            tex = root / name / f"prova_{version}.tex"
            pdf = root / name / f"prova_{version}.pdf"
            log = root / name / f"prova_{version}.log"
            if not tex.exists() or not pdf.exists() or not log.exists():
                failures.append(f"{name}/{version}: artefato ausente")
                continue
            orders[version] = re.findall(r"^% origem: (\S+)", tex.read_text(encoding="utf-8"), re.M)
            bad = re.search(r"Overfull|Missing character|Undefined control sequence|Fatal error|Emergency stop", log.read_text(encoding="utf-8"), re.I)
            if bad:
                failures.append(f"{name}/{version}: log contém {bad.group(0)}")
        if set(orders.get("A", [])) != set(orders.get("B", [])):
            failures.append(f"{name}: A/B não usam os mesmos IDs")
        if orders.get("A") == orders.get("B"):
            failures.append(f"{name}: A/B mantiveram a mesma ordem")

    if len(used) != 40 or len(set(used)) != 40:
        failures.append("seleção deveria conter 40 IDs únicos")
    objective_rows = [row for row in rows if row["tipo"] == "O"]
    if any(row["permutacao_B"] in {"—", "A→A, B→B, C→C, D→D, E→E"} for row in objective_rows):
        failures.append("há objetiva sem permutação real na versão B")
    scores = {name: [float(row["dificuldade_score"]) for row in rows if row["instrumento"] == name] for name in INSTRUMENTS}
    if sum(scores["final"]) / 8 > sum(scores["segunda_chamada"]) / 8:
        failures.append("a Final ficou mais difícil que a Segunda Chamada")

    if failures:
        print("FALHOU")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"OK: 5 instrumentos, 10 versões, 40 IDs únicos; Final <= Segunda Chamada — {args.repo.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
