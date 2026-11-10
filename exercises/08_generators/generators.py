"""Lesson 8 exercises: generators and the iterator protocol."""

from collections.abc import Iterable, Iterator


def countdown(n: int) -> Iterator[int]:
    """Yield n, n-1, ..., 1. Yield nothing if n <= 0. Use `yield`.

    list(countdown(3)) -> [3, 2, 1]

    ES: Produce n, n-1, ..., 1. No produce nada si n <= 0. Usa `yield`.
    """
    raise NotImplementedError


def running_total(nums: Iterable[int]) -> Iterator[int]:
    """Yield the cumulative sum after each number, lazily.

    list(running_total([1, 2, 3])) -> [1, 3, 6]

    ES: Produce la suma acumulada tras cada número, de forma perezosa (lazy).
    """
    raise NotImplementedError


def clean_lines(lines: Iterable[str]) -> Iterator[str]:
    """Yield stripped lines, skipping blank lines and lines starting with '#'.

    Must work lazily on any iterable (even an endless one).

    ES: Produce las líneas sin espacios sobrantes, omitiendo las vacías y las que
    empiezan con "#". Debe funcionar de forma lazy con cualquier iterable
    (incluso infinito).
    """
    raise NotImplementedError


def fibonacci() -> Iterator[int]:
    """Yield the Fibonacci numbers forever: 0, 1, 1, 2, 3, 5, ...

    ES: Produce los números de Fibonacci para siempre: 0, 1, 1, 2, 3, 5, ...
    """
    raise NotImplementedError


def take(n: int, items: Iterable[int]) -> list[int]:
    """Return the first n items as a list without consuming more than n.

    Hint: itertools.islice.

    ES: Devuelve los primeros n elementos como lista sin consumir más de n.
    Pista: itertools.islice.
    """
    raise NotImplementedError


class Repeater:
    """An iterator (not a generator) that yields `value` exactly `times` times.

    Implement __iter__ (return self) and __next__ (raise StopIteration when done).

    ES: Un iterador (no un generador) que produce `value` exactamente `times`
    veces. Implementa __iter__ (devuelve self) y __next__ (lanza StopIteration
    al terminar).
    """

    def __init__(self, value: str, times: int) -> None:
        raise NotImplementedError

    def __iter__(self) -> "Repeater":
        raise NotImplementedError

    def __next__(self) -> str:
        raise NotImplementedError
