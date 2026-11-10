"""Lesson 7 reference solution."""

from collections.abc import Iterable, Iterator
from itertools import batched, combinations


def squares_of_evens(nums: list[int]) -> list[int]:
    return [n * n for n in nums if n % 2 == 0]


def word_lengths(words: list[str]) -> dict[str, int]:
    return {w: len(w) for w in words}


def unique_initials(words: list[str]) -> set[str]:
    return {w[0].lower() for w in words if w}


def flatten(matrix: list[list[int]]) -> list[int]:
    return [x for row in matrix for x in row]


def pairs_summing_to(nums: list[int], target: int) -> list[tuple[int, int]]:
    return [(a, b) for a, b in combinations(nums, 2) if a + b == target]


def chunked(items: Iterable[int], size: int) -> list[list[int]]:
    return [list(chunk) for chunk in batched(items, size, strict=False)]


def lazy_squares(nums: Iterable[int]) -> Iterator[int]:
    return (n * n for n in nums)
