"""Lesson 14 exercises: type hints. The solution must pass `uv run ty check`.
ES: Ejercicios de la lección 14: type hints. La solución debe pasar
`uv run ty check`."""

from collections.abc import Callable
from typing import Literal, Protocol, TypedDict


def first_or_none[T](items: list[T]) -> T | None:
    """Return the first item, or None when the list is empty.
    ES: Devuelve el primer elemento, o None si la list está vacía."""
    raise NotImplementedError


class Stack[T]:
    """A generic stack.
    ES: Una pila (stack) genérica."""

    def __init__(self) -> None:
        raise NotImplementedError

    def push(self, item: T) -> None:
        raise NotImplementedError

    def pop(self) -> T:
        """Remove and return the top item; raise IndexError when empty.
        ES: Quita y devuelve el elemento superior; lanza IndexError si está vacía."""
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError


class User(TypedDict):
    name: str
    age: int


def adult_names(users: list[User]) -> list[str]:
    """Names of users aged 18 or over, in order.
    ES: Nombres de los usuarios de 18 años o más, en orden."""
    raise NotImplementedError


type Direction = Literal["left", "right"]


def turn(heading: int, direction: Direction) -> int:
    """Turn a compass heading by 90 degrees; right adds, left subtracts, mod 360.
    ES: Gira un rumbo 90 grados; right suma, left resta, módulo 360."""
    raise NotImplementedError


class Speaker(Protocol):
    def speak(self) -> str: ...


def chorus(speakers: list[Speaker]) -> str:
    """Join every speaker's speak() with ' & '.
    ES: Une el speak() de cada speaker con ' & '."""
    raise NotImplementedError


def group_by[K, V](items: list[V], key: Callable[[V], K]) -> dict[K, list[V]]:
    """Group items by key(item), preserving order.
    ES: Agrupa los elementos por key(item), conservando el orden."""
    raise NotImplementedError
