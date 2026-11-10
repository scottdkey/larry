"""Lesson 12 exercises: classes."""

import math


class Counter:
    """A counter that starts at `start` and moves by one."""

    def __init__(self, start: int = 0) -> None:
        self._value = start

    def increment(self) -> None:
        """Add one to the count."""
        self._value += 1

    @property
    def value(self) -> int:
        """The current count (read-only)."""
        return self._value


class Temperature:
    """Stores Celsius; exposes Fahrenheit as a property with a setter."""

    def __init__(self, celsius: float) -> None:
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @property
    def fahrenheit(self) -> float:
        """celsius * 9 / 5 + 32"""
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        self._celsius = (value - 32) * 5 / 9


class Vector:
    """A 2D vector supporting +, ==, repr, len-free truthiness and abs()."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """Return e.g. 'Vector(1, 2)'."""
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __abs__(self) -> float:
        """The length: sqrt(x**2 + y**2)."""
        return math.hypot(self.x, self.y)

    def __bool__(self) -> bool:
        """False only for the zero vector."""
        return bool(self.x or self.y)


class Animal:
    """Base class. Subclasses override `sound`."""

    def __init__(self, name: str) -> None:
        self.name = name

    def sound(self) -> str:
        raise NotImplementedError

    def speak(self) -> str:
        """Return '<name> says <sound>'."""
        return f"{self.name} says {self.sound()}"


class Dog(Animal):
    """Sound is 'woof'."""

    def sound(self) -> str:
        return "woof"


class Puppy(Dog):
    """Like Dog, but sound is 'yip' and speak() ends with '!' (use super())."""

    def sound(self) -> str:
        return "yip"

    def speak(self) -> str:
        return super().speak() + "!"


class Engine:
    def __init__(self, horsepower: int) -> None:
        self.horsepower = horsepower


class Car:
    """Composition: a Car has an Engine, it is not one."""

    def __init__(self, name: str, engine: Engine) -> None:
        self.name = name
        self.engine = engine

    def describe(self) -> str:
        """Return '<name> (<horsepower> hp)'."""
        return f"{self.name} ({self.engine.horsepower} hp)"
