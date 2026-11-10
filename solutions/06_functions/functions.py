"""Lesson 6 exercises: arguments, defaults, keyword-only, closures, lambda."""

from collections.abc import Callable


def add_item(item: str, items: list[str] | None = None) -> list[str]:
    """Append item to items and return the list; start a fresh list if items is None.

    Separate calls without `items` must never share state.
    """
    if items is None:
        items = []
    items.append(item)
    return items


def join_words(*words: str, sep: str = " ", upper: bool = False) -> str:
    """Join any number of words with `sep`; `sep` and `upper` are keyword-only."""
    joined = sep.join(words)
    return joined.upper() if upper else joined


def describe(name: str, /, **attrs: str) -> str:
    """Return "name: k1=v1, k2=v2" with attrs in given order, or just "name" if none.

    `name` is positional-only so an attribute may itself be called "name".
    """
    if not attrs:
        return name
    return f"{name}: " + ", ".join(f"{k}={v}" for k, v in attrs.items())


def make_multiplier(factor: int) -> Callable[[int], int]:
    """Return a function that multiplies its argument by `factor`."""
    return lambda x: x * factor


def make_counter(start: int = 0) -> Callable[[], int]:
    """Return a function that returns start, start + 1, ... on successive calls.

    Each counter keeps its own state (use a closure and `nonlocal`).
    """
    count = start - 1

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def compose(*funcs: Callable[[int], int]) -> Callable[[int], int]:
    """Return f(x) applying funcs left to right: compose(f, g)(x) == g(f(x)).

    With no funcs, the result returns its input unchanged.
    """

    def composed(x: int) -> int:
        for f in funcs:
            x = f(x)
        return x

    return composed


def sort_people(
    people: list[dict[str, str | int]], key: str, reverse: bool = False
) -> list[dict[str, str | int]]:
    """Return people sorted by the given dict key, using a lambda as the sort key."""
    return sorted(people, key=lambda p: p[key], reverse=reverse)
