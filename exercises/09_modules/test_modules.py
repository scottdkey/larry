import subprocess
import sys
from pathlib import Path

import modules
from modules import (
    days_between,
    load_callable,
    main,
    slugify,
    to_sorted_json,
    top_words,
)


def test_days_between():
    assert days_between("2024-01-01", "2024-03-01") == 60
    assert days_between("2024-03-01", "2024-01-01") == -60


def test_top_words():
    text = "The cat and the hat. The END, and fin"
    assert top_words(text, 2) == [("the", 3), ("and", 2)]


def test_slugify():
    assert slugify("  Hello, World! 2024 ") == "hello-world-2024"
    assert slugify("") == ""


def test_to_sorted_json():
    assert to_sorted_json({"b": 1, "a": [1]}) == '{\n  "a": [\n    1\n  ],\n  "b": 1\n}'


def test_load_callable():
    assert load_callable("math:sqrt")(9) == 3.0
    assert load_callable("os.path:basename")("/a/b.txt") == "b.txt"


def test_main_sums(capsys):
    assert main(["1", "2", "39"]) == 0
    assert capsys.readouterr().out.strip() == "total: 42"


def test_main_rejects_non_integers(capsys):
    assert main(["1", "x"]) == 1
    assert "error: arguments must be integers" in capsys.readouterr().out


def test_runs_as_script():
    result = subprocess.run(
        [sys.executable, str(Path(modules.__file__)), "2", "3"],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "total: 5"
