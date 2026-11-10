"""Lesson 17: functions to implement, plus checkers you write yourself."""

import os
import re
from collections.abc import Callable
from pathlib import Path


def clamp(value: float, low: float, high: float) -> float:
    if low > high:
        raise ValueError("low must not exceed high")
    return max(low, min(value, high))


def mean(values: list[float]) -> float:
    if not values:
        raise ValueError("mean of empty list")
    return sum(values) / len(values)


def slugify(text: str) -> str:
    return "-".join(re.findall(r"[a-z0-9]+", text.lower()))


def read_settings(path: Path) -> dict[str, str]:
    settings: dict[str, str] = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, sep, value = line.partition("=")
        if not sep:
            raise ValueError(f"bad line: {line!r}")
        settings[key.strip()] = value.strip()
    return settings


def greeting() -> str:
    return f"Hello, {os.environ.get('GREET_NAME', 'stranger')}!"


def check_leap_year(is_leap_year: Callable[[int], bool]) -> None:
    assert is_leap_year(2024)
    assert not is_leap_year(2023)
    assert not is_leap_year(2022)
    assert not is_leap_year(1900)
    assert is_leap_year(2000)


def check_clamp(clamp_fn: Callable[[float, float, float], float]) -> None:
    assert clamp_fn(5, 0, 10) == 5
    assert clamp_fn(-1, 0, 10) == 0
    assert clamp_fn(11, 0, 10) == 10
    assert clamp_fn(0, 0, 10) == 0
    assert clamp_fn(10, 0, 10) == 10
