import pytest
from testing_skills import (
    check_clamp,
    check_leap_year,
    clamp,
    greeting,
    mean,
    read_settings,
    slugify,
)


@pytest.mark.parametrize(
    ("value", "expected"), [(5, 5), (-3, 0), (42, 10), (0, 0), (10, 10)]
)
def test_clamp(value, expected):
    assert clamp(value, 0, 10) == expected


def test_clamp_bad_range():
    with pytest.raises(ValueError):
        clamp(1, 10, 0)


def test_mean():
    assert mean([1, 2, 3, 4]) == 2.5
    assert mean([0.1, 0.2]) == pytest.approx(0.15)


def test_mean_empty():
    with pytest.raises(ValueError, match="empty"):
        mean([])


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("  Hello,   World! ", "hello-world"),
        ("Python 3.13", "python-3-13"),
        ("---", ""),
        ("already-slugged", "already-slugged"),
    ],
)
def test_slugify(text, expected):
    assert slugify(text) == expected


def test_read_settings(tmp_path):
    f = tmp_path / "app.conf"
    f.write_text("# comment\n\nname = larry\n debug=true \nurl = a=b\n")
    assert read_settings(f) == {"name": "larry", "debug": "true", "url": "a=b"}


def test_read_settings_malformed(tmp_path):
    f = tmp_path / "bad.conf"
    f.write_text("oops\n")
    with pytest.raises(ValueError):
        read_settings(f)


def test_greeting_env(monkeypatch):
    monkeypatch.setenv("GREET_NAME", "Ada")
    assert greeting() == "Hello, Ada!"


def test_greeting_default(monkeypatch):
    monkeypatch.delenv("GREET_NAME", raising=False)
    assert greeting() == "Hello, stranger!"


# Mutation checks: your checkers must accept the good function and reject bugs.


def good_leap(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)


LEAP_MUTANTS = {
    "only mod 4": lambda y: y % 4 == 0,
    "no 400 rule": lambda y: y % 4 == 0 and y % 100 != 0,
    "no century rule": lambda y: y % 4 == 0 or y % 400 == 0,
    "mod 2": lambda y: y % 2 == 0 and (y % 100 != 0 or y % 400 == 0),
}


def test_leap_checker_accepts_correct():
    check_leap_year(good_leap)


@pytest.mark.parametrize("name", LEAP_MUTANTS)
def test_leap_checker_catches_bug(name):
    with pytest.raises(AssertionError):
        check_leap_year(LEAP_MUTANTS[name])


def good_clamp(v, lo, hi):
    return max(lo, min(v, hi))


CLAMP_MUTANTS = {
    "no lower bound": lambda v, lo, hi: min(v, hi),
    "no upper bound": lambda v, lo, hi: max(v, lo),
    "swapped bounds": lambda v, lo, hi: max(hi, min(v, lo)),
    "exclusive low edge": lambda v, lo, hi: lo + 1 if v <= lo else min(v, hi),
    "exclusive high edge": lambda v, lo, hi: hi - 1 if v >= hi else max(v, lo),
}


def test_clamp_checker_accepts_correct():
    check_clamp(good_clamp)


@pytest.mark.parametrize("name", CLAMP_MUTANTS)
def test_clamp_checker_catches_bug(name):
    with pytest.raises(AssertionError):
        check_clamp(CLAMP_MUTANTS[name])
