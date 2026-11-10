"""Lesson 2 exercises: if, match, loops, range."""


def fizzbuzz(n: int) -> str:
    """Return "FizzBuzz" for multiples of 15, "Fizz" for 3, "Buzz" for 5, else n.

    ES: Devuelve "FizzBuzz" para múltiplos de 15, "Fizz" de 3, "Buzz" de 5; si no, n.
    """
    raise NotImplementedError


def http_class(status: int) -> str:
    """Use `match` to classify a status code.

    200-299 -> "success", 300-399 -> "redirect", 400-499 -> "client error",
    500-599 -> "server error", anything else -> "unknown".

    ES: Usa `match` para clasificar un código de estado (rangos arriba;
    otro -> "unknown").
    """
    raise NotImplementedError


def sum_of_evens(limit: int) -> int:
    """Sum the even numbers from 0 up to but not including `limit`.

    ES: Suma los números pares desde 0 hasta `limit` sin incluirlo.
    """
    raise NotImplementedError


def primes_below(limit: int) -> list[int]:
    """Return all primes less than `limit`, in ascending order.

    ES: Devuelve todos los primos menores que `limit`, en orden ascendente.
    """
    raise NotImplementedError


def collatz_steps(n: int) -> int:
    """Count steps to reach 1: even -> n // 2, odd -> 3n + 1. collatz_steps(1) == 0.

    ES: Cuenta los pasos hasta llegar a 1: par -> n // 2, impar -> 3n + 1.
    """
    raise NotImplementedError


def find_pair(numbers: list[int], target: int) -> tuple[int, int] | None:
    """Return the first pair (a, b), a listed before b, with a + b == target.

    "First" means smallest index of a, then of b. Return None if no pair exists.

    ES: Devuelve el primer par (a, b), con a antes que b, tal que a + b == target.
    "Primero" = menor índice de a, luego de b. Devuelve None si no existe.
    """
    raise NotImplementedError
