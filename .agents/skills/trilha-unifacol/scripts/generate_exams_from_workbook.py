#!/usr/bin/env python3
"""Gerar provas A/B a partir de itens ímpares de um caderno ENADE em LaTeX."""

from __future__ import annotations

import argparse
import csv
import json
import random
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path


@dataclass
class Item:
    chapter: int
    number: int
    kind: str
    competence: str
    support: str
    block: str
    item_id: str
    answer: str | None
    score: float


def brace_arg(text: str, pos: int) -> tuple[str, int]:
    while pos < len(text) and text[pos].isspace():
        pos += 1
    if pos >= len(text) or text[pos] != "{":
        raise ValueError(f"argumento entre chaves esperado na posição {pos}")
    depth, start = 0, pos + 1
    for index in range(pos, len(text)):
        if text[index] == "{" and (index == 0 or text[index - 1] != "\\"):
            depth += 1
        elif text[index] == "}" and (index == 0 or text[index - 1] != "\\"):
            depth -= 1
            if depth == 0:
                return text[start:index], index + 1
    raise ValueError("chaves não balanceadas")


def clean_visible(text: str) -> str:
    text = re.sub(r"%.*", " ", text)
    text = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^]]*\])?", " ", text)
    return re.sub(r"[{}$&_~^\\]", " ", text)


def difficulty_score(block: str, competence: str) -> float:
    words = len(re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]+", clean_visible(block)))
    support = 2.0 * len(re.findall(r"\\begin\{(?:tabular|tabularx|longtable|tikzpicture|DocumentBox)", block))
    math = 1.2 * len(re.findall(r"\\\[|\\frac|\\sum|\\sqrt|\d+[,.]\d+%?", block))
    high = len(re.findall(r"integr|avali|projet|justific|diagnostic|critic|prioriz", competence, re.I))
    constraints = len(re.findall(r"restri|simult|custo|risco|privacidade|governan|causal|limite|evid[eê]ncia", block, re.I))
    return round(words / 70 + support + min(math, 5) + 1.4 * high + min(constraints, 5) * 0.45, 3)


def parse_answers(professor_dir: Path) -> tuple[dict[str, str], str]:
    files = sorted(list(professor_dir.glob("*.md")) + list(professor_dir.glob("*.tex")))
    corpus = "\n\n".join(path.read_text(encoding="utf-8", errors="ignore") for path in files)
    answers: dict[str, str] = {}
    patterns = [
        r"\|\s*([A-Z]+-C\d{2}-O\d{2})\s*\|\s*objetiva\s*\|\s*([A-E])(?:\s*\||\s*;)",
        r"\|\s*([A-Z]+-C\d{2}-O\d{2})\s*\|\s*([A-E])\s*:",
        r"\*\*([A-Z]+-C\d{2}-O\d{2})\s*[—-]+\s*([A-E])\.",
        r"###\s+([A-Z]+-C\d{2}-O\d{2})\s*[—-]+\s*resposta\s+([A-E])\b",
        r"###\s+([A-Z]+-C\d{2}-O\d{2})\b(?:(?!\n###).)*?\*\*Gabarito:\*\*\s*([A-E])\b",
        r"([A-Z]+-C\d{2}-O\d{2})[^\n]{0,180}?\bGabarito:\s*([A-E])\b",
        r"\\Obj\{([A-Z]+-C\d{2}-O\d{2})\}\{([A-E])\}",
    ]
    for pattern in patterns:
        for match in re.finditer(pattern, corpus, re.S):
            answers.setdefault(match.group(1), match.group(2))
    return answers, corpus


def answer_excerpt(item_id: str, corpus: str) -> str:
    lines = corpus.splitlines()
    for index, line in enumerate(lines):
        if item_id not in line:
            continue
        if line.lstrip().startswith("|"):
            return line.strip()
        chosen = [line.strip()]
        for extra in lines[index + 1 : index + 14]:
            if re.match(r"^#{2,3}\s+|^- \*\*[A-Z]+-C\d{2}-[OD]\d{2}", extra):
                break
            if extra.strip():
                chosen.append(extra.strip())
        return " ".join(chosen)
    return "Padrão privado não localizado automaticamente; consultar gabarito integral do caderno."


def parse_items(chapters_dir: Path, prefix: str, answers: dict[str, str]) -> list[Item]:
    result: list[Item] = []
    for path in sorted(chapters_dir.glob("*.tex")):
        cap_match = re.match(r"(\d{2})_", path.name)
        if not cap_match:
            continue
        chapter = int(cap_match.group(1))
        text = path.read_text(encoding="utf-8")
        response = re.search(r"\\(?:newpage\s*)?\\?subsection\{Respostas", text)
        if response:
            text = text[: response.start()]
        starts = [match.start() for match in re.finditer(r"\\ItemHeader\{", text)]
        for idx, start in enumerate(starts):
            pos = start + len("\\ItemHeader")
            args: list[str] = []
            for _ in range(4):
                arg, pos = brace_arg(text, pos)
                args.append(arg)
            end = starts[idx + 1] if idx + 1 < len(starts) else len(text)
            block = text[start:end]
            block = re.sub(r"\s*\\(?:newpage\s*)?subsection\{Questões discursivas\}\s*$", "", block)
            block = re.sub(r"\s*\\subsection\{Questões discursivas\}\s*", "\n", block)
            number = int(args[0])
            if number % 2 == 0:
                continue
            kind = "O" if args[1].lower().startswith("objet") else "D"
            item_id = f"{prefix}-C{chapter:02d}-{kind}{number:02d}"
            answer = answers.get(item_id) if kind == "O" else None
            result.append(Item(chapter, number, kind, args[2], args[3], block.strip(), item_id, answer,
                               difficulty_score(block, args[2])))
    return result


def choose(candidates: list[Item], count: int, band: str, rng: random.Random) -> list[Item]:
    if len(candidates) < count:
        raise ValueError(f"candidatos insuficientes: {len(candidates)} para {count}")
    ordered = sorted(candidates, key=lambda item: (item.score, item.item_id))
    if band == "easy":
        pool = ordered[: max(count, (len(ordered) + 1) // 2)]
    elif band == "hard":
        pool = ordered[-max(count, (len(ordered) + 1) // 2) :]
    elif band == "medium":
        low, high = len(ordered) // 5, max(len(ordered) // 5 + count, (4 * len(ordered)) // 5)
        pool = ordered[low:high]
    else:
        pool = ordered

    # Cobrir o maior número possível de capítulos antes de repetir capítulo.
    by_chapter: dict[int, list[Item]] = {}
    for item in pool:
        by_chapter.setdefault(item.chapter, []).append(item)
    selected: list[Item] = []
    chapters = list(by_chapter)
    rng.shuffle(chapters)
    for chapter in chapters:
        if len(selected) == count:
            break
        selected.append(rng.choice(by_chapter[chapter]))
    if len(selected) < count:
        remaining = [item for item in pool if item not in selected]
        selected.extend(rng.sample(remaining, count - len(selected)))
    return selected


def item_options(block: str) -> tuple[list[str], tuple[int, int]]:
    env = re.search(r"\\begin\{enumerate\}\[label=\\Alph\*\)\](.*?)\\end\{enumerate\}", block, re.S)
    if not env:
        raise ValueError("bloco objetivo sem alternativas A--E")
    parts = re.split(r"\\item\s+", env.group(1))
    options = [part.strip() for part in parts[1:]]
    if len(options) != 5:
        raise ValueError(f"esperadas 5 alternativas, encontradas {len(options)}")
    return options, env.span(1)


def render_item(item: Item, position: int, version: str, rng: random.Random) -> tuple[str, str | None, str]:
    block = item.block
    block = re.sub(
        r"\\ItemHeader\{\d+\}\{[^{}]*\}\{[^{}]*\}\{[^{}]*\}",
        lambda _m: f"\\ItemHeader{{{position}}}{{{'Objetiva' if item.kind == 'O' else 'Discursiva'}}}"
        f"{{{item.competence}}}{{{item.support}}}",
        block,
        count=1,
    )
    if item.kind == "D":
        space = "" if "\\EspacoDiscursiva" in block else "\n\\EspacoDiscursiva"
        return f"% origem: {item.item_id}\n{block}{space}\n", None, "—"
    options, span = item_options(block)
    permutation = list(range(5))
    if version == "B":
        rng.shuffle(permutation)
        if permutation == list(range(5)):
            permutation = permutation[1:] + permutation[:1]
    shuffled = [options[index] for index in permutation]
    new_body = "\n" + "\n".join(f"  \\item {option}" for option in shuffled) + "\n"
    block = block[: span[0]] + new_body + block[span[1] :]
    original_correct = ord(item.answer) - ord("A") if item.answer else None
    correct = chr(ord("A") + permutation.index(original_correct)) if original_correct is not None else "?"
    mapping = ", ".join(f"{chr(65 + old)}→{chr(65 + new)}" for new, old in enumerate(permutation))
    return f"% origem: {item.item_id}\n{block}\n", correct, mapping


def exam_tex(discipline: str, title: str, version: str, items: list[Item], seed: int) -> tuple[str, list[dict[str, str]]]:
    rng = random.Random(seed + (0 if version == "A" else 100_003))
    ordered = list(items)
    rng.shuffle(ordered)
    if version == "B" and [x.item_id for x in ordered] == [x.item_id for x in items]:
        ordered = ordered[1:] + ordered[:1]
    rows: list[dict[str, str]] = []
    body: list[str] = []
    for position, item in enumerate(ordered, start=1):
        rendered, correct, permutation = render_item(item, position, version, rng)
        body.append(rendered)
        rows.append({"id": item.item_id, "position": str(position), "correct": correct or "—", "permutation": permutation})
    preamble = rf"""\documentclass[12pt,a4paper]{{article}}
\newcommand{{\CadernoDisciplina}}{{{discipline}}}
\newcommand{{\CadernoCorHex}}{{17365D}}
\input{{../../../caderno_exercicios/caderno_enade_style.tex}}
\setcounter{{secnumdepth}}{{0}}
\begin{{document}}
\begin{{center}}
{{\Large\bfseries UNIFACOL}}\\[2mm]
{{\large {title}}}\\[1mm]
{{\Large\bfseries VERSÃO {version}}}
\end{{center}}
\begin{{DocumentBox}}[Identificação]
\begin{{tabularx}}{{\textwidth}}{{@{{}}p{{.48\textwidth}}p{{.48\textwidth}}@{{}}}}
Estudante: \hrulefill & Turma: \hrulefill\\[3mm]
Professor: Cayo Oliveira & Data: \rule{{2.7cm}}{{.2pt}}/2026
\end{{tabularx}}
\end{{DocumentBox}}
\textbf{{Instruções.}} Esta avaliação contém seis questões objetivas e duas discursivas. Nas objetivas, assinale uma única alternativa. Nas discursivas, mostre cálculos intermediários e justifique decisões com as evidências do texto-base. Respostas sem desenvolvimento podem não receber pontuação integral.
\bigskip
"""
    return preamble + "\n".join(body) + "\n\\end{document}\n", rows


def allocate(items: list[Item], u1: set[int], u2: set[int], seed: int) -> dict[str, list[Item]]:
    rng = random.Random(seed)
    available = {item.item_id: item for item in items}

    def take(scope: set[int], objectives: int, discursives: int, band: str) -> list[Item]:
        chosen: list[Item] = []
        for kind, count in (("O", objectives), ("D", discursives)):
            pool = [item for item in available.values() if item.chapter in scope and item.kind == kind]
            part = choose(pool, count, band, rng)
            chosen.extend(part)
            for item in part:
                available.pop(item.item_id)
        return chosen

    result: dict[str, list[Item]] = {}
    result["prova_i_unidade"] = take(u1, 6, 2, "medium")
    result["prova_ii_unidade"] = take(u2, 6, 2, "medium")

    def comprehensive(name: str, band: str) -> None:
        result[name] = take(u1, 3, 1, band) + take(u2, 3, 1, band)

    comprehensive("segunda_chamada", "hard")
    comprehensive("final", "easy")
    comprehensive("simulado", "all")
    return result


def parse_range(value: str) -> set[int]:
    result: set[int] = set()
    for piece in value.split(","):
        if "-" in piece:
            start, end = map(int, piece.split("-", 1))
            result.update(range(start, end + 1))
        else:
            result.add(int(piece))
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--discipline", required=True)
    parser.add_argument("--prefix", required=True)
    parser.add_argument("--u1", required=True)
    parser.add_argument("--u2", required=True)
    parser.add_argument("--seed", type=int, default=20260816)
    args = parser.parse_args()

    workbook = args.repo / "caderno_exercicios"
    answers, corpus = parse_answers(workbook / "professor")
    items = parse_items(workbook / "capitulos", args.prefix, answers)
    odd_objectives = [item for item in items if item.kind == "O"]
    missing = [item.item_id for item in odd_objectives if not item.answer]
    if missing:
        raise SystemExit("gabaritos objetivos ausentes: " + ", ".join(missing))

    u1, u2 = parse_range(args.u1), parse_range(args.u2)
    allocation = allocate(items, u1, u2, args.seed)
    output = args.repo / "provas" / "2026.2"
    titles = {
        "prova_i_unidade": "Avaliação da I Unidade",
        "prova_ii_unidade": "Avaliação da II Unidade",
        "segunda_chamada": "Segunda Chamada",
        "final": "Avaliação Final",
        "simulado": "Simulado ENADE",
    }
    output.mkdir(parents=True, exist_ok=True)
    rows_all: list[dict[str, str]] = []
    manifest: dict[str, object] = {"seed": args.seed, "generated_at": str(date.today()), "discipline": args.discipline, "instruments": {}}
    gabarito_lines = [f"# Gabaritos privados — {args.discipline} — 2026.2", "", "Não publicar com as provas.", ""]

    for index, (name, selected) in enumerate(allocation.items(), start=1):
        folder = output / name
        folder.mkdir(parents=True, exist_ok=True)
        version_rows: dict[str, list[dict[str, str]]] = {}
        for version in ("A", "B"):
            tex, rows = exam_tex(args.discipline, titles[name], version, selected, args.seed + index * 1_009)
            (folder / f"prova_{version}.tex").write_text(tex, encoding="utf-8")
            version_rows[version] = rows
        map_a = {row["id"]: row for row in version_rows["A"]}
        map_b = {row["id"]: row for row in version_rows["B"]}
        gabarito_lines.extend([f"## {titles[name]}", "", "| ID | Pos. A | Gab. A | Pos. B | Gab. B | Permutação B |", "|---|---:|:---:|---:|:---:|---|"])
        for item in selected:
            a, b = map_a[item.item_id], map_b[item.item_id]
            gabarito_lines.append(f"| {item.item_id} | {a['position']} | {a['correct']} | {b['position']} | {b['correct']} | {b['permutation']} |")
            rows_all.append({"instrumento": name, "id": item.item_id, "capitulo": str(item.chapter), "tipo": item.kind,
                             "competencia": item.competence, "suporte": item.support, "dificuldade_score": str(item.score),
                             "posicao_A": a["position"], "gabarito_A": a["correct"], "posicao_B": b["position"],
                             "gabarito_B": b["correct"], "permutacao_B": b["permutation"]})
        gabarito_lines.extend(["", "### Critérios originais das discursivas", ""])
        for item in selected:
            if item.kind == "D":
                gabarito_lines.append(f"- **{item.item_id}:** {answer_excerpt(item.item_id, corpus)}")
        gabarito_lines.append("")
        manifest["instruments"][name] = [{"id": item.item_id, "score": item.score, "chapter": item.chapter, "type": item.kind} for item in selected]

    professor = output / "professor"
    professor.mkdir(parents=True, exist_ok=True)
    (professor / "gabaritos.md").write_text("\n".join(gabarito_lines) + "\n", encoding="utf-8")
    (professor / "manifesto_selecao.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (professor / "matriz_rastreabilidade.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows_all[0]))
        writer.writeheader()
        writer.writerows(rows_all)

    reserved = output / "banco_reservado"
    reserved.mkdir(parents=True, exist_ok=True)
    unique = {item.item_id: item for selected in allocation.values() for item in selected}
    reserved_text = ["% Banco reservado — não publicar", ""]
    for item_id in sorted(unique):
        reserved_text.extend([f"% {item_id}", unique[item_id].block, ""])
    (reserved / "itens_selecionados.tex").write_text("\n".join(reserved_text), encoding="utf-8")
    (reserved / "README.md").write_text(
        f"# Banco reservado — {args.discipline}\n\n"
        f"Seleção reprodutível com semente `{args.seed}`. Contém {len(unique)} itens ímpares distintos. "
        "Não publicar este diretório nem os gabaritos. O caderno público precisa receber substitutos equivalentes antes de sua publicação final.\n",
        encoding="utf-8",
    )
    print(f"{args.discipline}: {len(items)} candidatos ímpares; {len(unique)} reservados; 5 instrumentos A/B gerados")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
