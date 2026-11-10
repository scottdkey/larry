"""Lesson 7 exercises: comprehensions, generator expressions, itertools."""

from collections.abc import Iterable, Iterator


def squares_of_evens(nums: list[int]) -> list[int]:
    """Return the squares of the even numbers, keeping order.

    squares_of_evens([1, 2, 3, 4]) -> [4, 16]

    ES: Devuelve los cuadrados de los números pares, conservando el orden.
    """
    raise NotImplementedError


def word_lengths(words: list[str]) -> dict[str, int]:
    """Map each word to its length.

    word_lengths(["hi", "python"]) -> {"hi": 2, "python": 6}

    ES: Asocia cada palabra con su longitud.
    """
    raise NotImplementedError


def unique_initials(words: list[str]) -> set[str]:
    """Return the set of lowercase first letters. Skip empty strings.

    unique_initials(["Apple", "avocado", "Bean", ""]) -> {"a", "b"}

    ES: Devuelve el set de primeras letras en minúscula. Omite cadenas vacías.
    """
    raise NotImplementedError


def flatten(matrix: list[list[int]]) -> list[int]:
    """Flatten a list of rows into one list, row by row.

    flatten([[1, 2], [3], []]) -> [1, 2, 3]

    ES: Aplana una lista de filas en una sola lista, fila por fila.
    """
    raise NotImplementedError


def pairs_summing_to(nums: list[int], target: int) -> list[tuple[int, int]]:
    """Return every pair (a, b) of items at different positions, a before b
    in the list, where a + b == target. Hint: itertools.combinations.

    pairs_summing_to([1, 2, 3, 4], 5) -> [(1, 4), (2, 3)]

    ES: Devuelve cada par (a, b) de elementos en posiciones distintas, con a antes
    de b en la lista, donde a + b == target. Pista: itertools.combinations.
    """
    raise NotImplementedError


def chunked(items: Iterable[int], size: int) -> list[list[int]]:
    """Split items into lists of `size`; the last may be shorter.
    Hint: itertools.batched.

    chunked(range(5), 2) -> [[0, 1], [2, 3], [4]]

    ES: Divide items en listas de `size`; la última puede ser más corta.
    Pista: itertools.batched.
    """
    raise NotImplementedError


def lazy_squares(nums: Iterable[int]) -> Iterator[int]:
    """Return a generator expression (not a list) of squares.

    It must not consume `nums` until iterated.

    ES: Devuelve una expresión generadora (no una lista) de cuadrados. No debe
    consumir `nums` hasta que se itere.
    """
    raise NotImplementedError
