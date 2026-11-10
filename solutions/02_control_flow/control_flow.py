"""Lesson 2 exercises: if, match, loops, range."""


def fizzbuzz(n: int) -> str:
    """Return "FizzBuzz" for multiples of 15, "Fizz" for 3, "Buzz" for 5, else n."""
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def http_class(status: int) -> str:
    """Use `match` to classify a status code.

    200-299 -> "success", 300-399 -> "redirect", 400-499 -> "client error",
    500-599 -> "server error", anything else -> "unknown".
    """
    match status:
        case n if 200 <= n < 300:
            return "success"
        case n if 300 <= n < 400:
            return "redirect"
        case n if 400 <= n < 500:
            return "client error"
        case n if 500 <= n < 600:
            return "server error"
        case _:
            return "unknown"


def sum_of_evens(limit: int) -> int:
    """Sum the even numbers from 0 up to but not including `limit`."""
    total = 0
    for n in range(0, limit, 2):
        total += n
    return total


def primes_below(limit: int) -> list[int]:
    """Return all primes less than `limit`, in ascending order."""
    primes = []
    for n in range(2, limit):
        for d in range(2, int(n**0.5) + 1):
            if n % d == 0:
                break
        else:
            primes.append(n)
    return primes


def collatz_steps(n: int) -> int:
    """Count steps to reach 1: even -> n // 2, odd -> 3n + 1. collatz_steps(1) == 0."""
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps


def find_pair(numbers: list[int], target: int) -> tuple[int, int] | None:
    """Return the first pair (a, b), a listed before b, with a + b == target.

    "First" means smallest index of a, then of b. Return None if no pair exists.
    """
    for i, a in enumerate(numbers):
        for b in numbers[i + 1 :]:
            if a + b == target:
                return a, b
    return None
