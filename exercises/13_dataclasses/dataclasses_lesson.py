"""Lesson 13 exercises: dataclasses, enums, NamedTuple.
ES: Ejercicios de la lección 13: dataclasses, enums, NamedTuple."""

from dataclasses import dataclass
from enum import Enum
from typing import NamedTuple


@dataclass
class Book:
    """A book with a title, author and page count (default 100).
    ES: Un libro con título, autor y número de páginas (por defecto 100)."""


@dataclass
class Playlist:
    """A named playlist. `songs` defaults to a fresh empty list per instance.
    ES: Una playlist con nombre. `songs` es por defecto una list vacía nueva
    por instancia."""

    def add(self, song: str) -> None:
        raise NotImplementedError


@dataclass(frozen=True)
class Point:
    """Immutable x, y. Add a `distance_to(other)` method (Euclidean).
    ES: x, y inmutables. Agrega un método `distance_to(other)` (euclidiana)."""

    def distance_to(self, other: "Point") -> float:
        raise NotImplementedError


class Color(Enum):
    """RED='red', GREEN='green', BLUE='blue'.
    ES: RED='red', GREEN='green', BLUE='blue' (mismos valores)."""


def parse_color(text: str) -> Color:
    """Case-insensitive lookup by value; raise ValueError if unknown.
    ES: Búsqueda por valor sin distinguir mayúsculas; lanza ValueError si no
    existe."""
    raise NotImplementedError


class Rect(NamedTuple):
    """width and height (floats).
    ES: width y height (floats)."""


def area(rect: Rect) -> float:
    raise NotImplementedError


@dataclass
class Rating:
    """A 1-5 `stars` rating; __post_init__ raises ValueError otherwise.
    ES: Una calificación `stars` de 1 a 5; si no, __post_init__ lanza ValueError."""
