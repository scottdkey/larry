"""Lesson 6 exercises: arguments, defaults, keyword-only, closures, lambda."""

from collections.abc import Callable


def add_item(item: str, items: list[str] | None = None) -> list[str]:
    """Append item to items and return the list; start a fresh list if items is None.

    Separate calls without `items` must never share state.

    ES: Agrega item a items y devuelve la lista; crea una nueva si items es None.
    Llamadas separadas sin `items` nunca comparten estado.
    """
    raise NotImplementedError


def join_words(*words: str, sep: str = " ", upper: bool = False) -> str:
    """Join any number of words with `sep`; `sep` and `upper` are keyword-only.

    ES: Une cualquier cantidad de palabras con `sep`; `sep` y `upper` son solo
    por nombre.
    """
    raise NotImplementedError


def describe(name: str, /, **attrs: str) -> str:
    """Return "name: k1=v1, k2=v2" with attrs in given order, or just "name" if none.

    `name` is positional-only so an attribute may itself be called "name".

    ES: Devuelve "name: k1=v1, k2=v2" (o solo "name" sin attrs). `name` es solo
    posicional, así que un atributo puede llamarse "name".
    """
    raise NotImplementedError


def make_multiplier(factor: int) -> Callable[[int], int]:
    """Return a function that multiplies its argument by `factor`.

    ES: Devuelve una función que multiplica su argumento por `factor`.
    """
    raise NotImplementedError


def make_counter(start: int = 0) -> Callable[[], int]:
    """Return a function that returns start, start + 1, ... on successive calls.

    Each counter keeps its own state (use a closure and `nonlocal`).

    ES: Devuelve una función que da start, start + 1, ... en llamadas sucesivas.
    Cada contador conserva su propio estado (closure y `nonlocal`).
    """
    raise NotImplementedError


def compose(*funcs: Callable[[int], int]) -> Callable[[int], int]:
    """Return f(x) applying funcs left to right: compose(f, g)(x) == g(f(x)).

    With no funcs, the result returns its input unchanged.

    ES: Devuelve f(x) aplicando funcs de izquierda a derecha. Sin funcs,
    devuelve la entrada.
    """
    raise NotImplementedError


def sort_people(
    people: list[dict[str, str | int]], key: str, reverse: bool = False
) -> list[dict[str, str | int]]:
    """Return people sorted by the given dict key, using a lambda as the sort key.

    ES: Devuelve people ordenado por la clave de dict dada, usando una lambda.
    """
    raise NotImplementedError
