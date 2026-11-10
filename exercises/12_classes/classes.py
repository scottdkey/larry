"""Lesson 12 exercises: classes.
ES: Ejercicios de la lección 12: clases."""


class Counter:
    """A counter that starts at `start` and moves by one.
    ES: Un contador que empieza en `start` y avanza de uno en uno."""

    def __init__(self, start: int = 0) -> None:
        raise NotImplementedError

    def increment(self) -> None:
        """Add one to the count.
        ES: Suma uno al conteo."""
        raise NotImplementedError

    @property
    def value(self) -> int:
        """The current count (read-only).
        ES: El conteo actual (solo lectura)."""
        raise NotImplementedError


class Temperature:
    """Stores Celsius; exposes Fahrenheit as a property with a setter.
    ES: Guarda Celsius; expone Fahrenheit como property con setter."""

    def __init__(self, celsius: float) -> None:
        raise NotImplementedError

    @property
    def celsius(self) -> float:
        raise NotImplementedError

    @property
    def fahrenheit(self) -> float:
        """celsius * 9 / 5 + 32"""
        raise NotImplementedError

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        raise NotImplementedError


class Vector:
    """A 2D vector supporting +, ==, repr, len-free truthiness and abs().
    ES: Un vector 2D con +, ==, repr, veracidad sin len y abs()."""

    def __init__(self, x: float, y: float) -> None:
        raise NotImplementedError

    def __repr__(self) -> str:
        """Return e.g. 'Vector(1, 2)'.
        ES: Devuelve, por ejemplo, 'Vector(1, 2)'."""
        raise NotImplementedError

    def __eq__(self, other: object) -> bool:
        raise NotImplementedError

    def __add__(self, other: "Vector") -> "Vector":
        raise NotImplementedError

    def __abs__(self) -> float:
        """The length: sqrt(x**2 + y**2).
        ES: La longitud: sqrt(x**2 + y**2)."""
        raise NotImplementedError

    def __bool__(self) -> bool:
        """False only for the zero vector.
        ES: False solo para el vector cero."""
        raise NotImplementedError


class Animal:
    """Base class. Subclasses override `sound`.
    ES: Clase base. Las subclases sobrescriben `sound`."""

    def __init__(self, name: str) -> None:
        raise NotImplementedError

    def sound(self) -> str:
        raise NotImplementedError

    def speak(self) -> str:
        """Return '<name> says <sound>'.
        ES: Devuelve '<name> says <sound>'."""
        raise NotImplementedError


class Dog(Animal):
    """Sound is 'woof'.
    ES: El sonido es 'woof'."""


class Puppy(Dog):
    """Like Dog, but sound is 'yip' and speak() ends with '!' (use super()).
    ES: Como Dog, pero el sonido es 'yip' y speak() termina con '!' (usa super())."""


class Engine:
    def __init__(self, horsepower: int) -> None:
        raise NotImplementedError


class Car:
    """Composition: a Car has an Engine, it is not one.
    ES: Composición: un Car tiene un Engine, no es un Engine."""

    def __init__(self, name: str, engine: Engine) -> None:
        raise NotImplementedError

    def describe(self) -> str:
        """Return '<name> (<horsepower> hp)'.
        ES: Devuelve '<name> (<horsepower> hp)'."""
        raise NotImplementedError
