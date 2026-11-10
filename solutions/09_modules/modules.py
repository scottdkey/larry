"""Lesson 9 reference solution."""

import importlib
import json
import re
import sys
from collections import Counter
from collections.abc import Callable, Sequence
from datetime import date


def days_between(start: str, end: str) -> int:
    return (date.fromisoformat(end) - date.fromisoformat(start)).days


def top_words(text: str, n: int) -> list[tuple[str, int]]:
    words = re.findall(r"[a-z']+", text.lower())
    return Counter(words).most_common(n)


def slugify(title: str) -> str:
    return "-".join(re.findall(r"[a-z0-9]+", title.lower()))


def to_sorted_json(data: dict[str, object]) -> str:
    return json.dumps(data, sort_keys=True, indent=2)


def load_callable(path: str) -> Callable[..., object]:
    module_name, _, attr = path.partition(":")
    return getattr(importlib.import_module(module_name), attr)


def main(argv: Sequence[str]) -> int:
    try:
        total = sum(int(a) for a in argv)
    except ValueError:
        print("error: arguments must be integers")
        return 1
    print(f"total: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
