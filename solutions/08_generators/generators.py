"""Lesson 8 reference solution."""

from collections.abc import Iterable, Iterator
from itertools import islice


def countdown(n: int) -> Iterator[int]:
    while n > 0:
        yield n
        n -= 1


def running_total(nums: Iterable[int]) -> Iterator[int]:
    total = 0
    for n in nums:
        total += n
        yield total


def clean_lines(lines: Iterable[str]) -> Iterator[str]:
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            yield line


def fibonacci() -> Iterator[int]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def take(n: int, items: Iterable[int]) -> list[int]:
    return list(islice(items, n))


class Repeater:
    def __init__(self, value: str, times: int) -> None:
        self.value = value
        self.times = times
        self._emitted = 0

    def __iter__(self) -> "Repeater":
        return self

    def __next__(self) -> str:
        if self._emitted >= self.times:
            raise StopIteration
        self._emitted += 1
        return self.value
