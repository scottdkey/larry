"""Lesson 10 reference solution."""

import json
from pathlib import Path


def write_lines(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(f"{line}\n" for line in lines), encoding="utf-8")


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def append_line(path: Path, line: str) -> None:
    with path.open("a", encoding="utf-8") as f:
        f.write(f"{line}\n")


def count_words(path: Path) -> int:
    with path.open(encoding="utf-8") as f:
        return sum(len(line.split()) for line in f)


def files_with_suffix(directory: Path, suffix: str) -> list[str]:
    return sorted(p.name for p in directory.rglob(f"*{suffix}") if p.is_file())


def save_json(path: Path, data: dict[str, object]) -> None:
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def load_json(
    path: Path, default: dict[str, object] | None = None
) -> dict[str, object]:
    if not path.exists():
        return {} if default is None else default
    return json.loads(path.read_text(encoding="utf-8"))
