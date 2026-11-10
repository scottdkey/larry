"""Lesson 13 exercises: dataclasses, enums, NamedTuple."""

import math
from dataclasses import dataclass, field
from enum import Enum
from typing import NamedTuple


@dataclass
class Book:
    """A book with a title, author and page count (default 100)."""

    title: str
    author: str
    pages: int = 100


@dataclass
class Playlist:
    """A named playlist. `songs` defaults to a fresh empty list per instance."""

    name: str
    songs: list[str] = field(default_factory=list)

    def add(self, song: str) -> None:
        self.songs.append(song)


@dataclass(frozen=True)
class Point:
    """Immutable x, y. Add a `distance_to(other)` method (Euclidean)."""

    x: float
    y: float

    def distance_to(self, other: "Point") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)


class Color(Enum):
    """RED='red', GREEN='green', BLUE='blue'."""

    RED = "red"
    GREEN = "green"
    BLUE = "blue"


def parse_color(text: str) -> Color:
    """Case-insensitive lookup by value; raise ValueError if unknown."""
    return Color(text.lower())


class Rect(NamedTuple):
    """width and height (floats)."""

    width: float
    height: float


def area(rect: Rect) -> float:
    return rect.width * rect.height


@dataclass
class Rating:
    """A 1-5 `stars` rating; __post_init__ raises ValueError otherwise."""

    stars: int

    def __post_init__(self) -> None:
        if not 1 <= self.stars <= 5:
            raise ValueError(f"stars must be 1-5, got {self.stars}")
