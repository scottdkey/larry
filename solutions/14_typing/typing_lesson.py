"""Lesson 14 exercises: type hints. The solution must pass `uv run ty check`."""

from collections.abc import Callable
from typing import Literal, Protocol, TypedDict


def first_or_none[T](items: list[T]) -> T | None:
    """Return the first item, or None when the list is empty."""
    return items[0] if items else None


class Stack[T]:
    """A generic stack."""

    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        """Remove and return the top item; raise IndexError when empty."""
        return self._items.pop()

    def __len__(self) -> int:
        return len(self._items)


class User(TypedDict):
    name: str
    age: int


def adult_names(users: list[User]) -> list[str]:
    """Names of users aged 18 or over, in order."""
    return [u["name"] for u in users if u["age"] >= 18]


type Direction = Literal["left", "right"]


def turn(heading: int, direction: Direction) -> int:
    """Turn a compass heading by 90 degrees; right adds, left subtracts, mod 360."""
    delta = 90 if direction == "right" else -90
    return (heading + delta) % 360


class Speaker(Protocol):
    def speak(self) -> str: ...


def chorus(speakers: list[Speaker]) -> str:
    """Join every speaker's speak() with ' & '."""
    return " & ".join(s.speak() for s in speakers)


def group_by[K, V](items: list[V], key: Callable[[V], K]) -> dict[K, list[V]]:
    """Group items by key(item), preserving order."""
    groups: dict[K, list[V]] = {}
    for item in items:
        groups.setdefault(key(item), []).append(item)
    return groups
