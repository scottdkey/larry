import pytest
from control_flow import (
    collatz_steps,
    find_pair,
    fizzbuzz,
    http_class,
    primes_below,
    sum_of_evens,
)


@pytest.mark.parametrize(
    ("n", "expected"),
    [(1, "1"), (3, "Fizz"), (5, "Buzz"), (15, "FizzBuzz"), (30, "FizzBuzz"), (7, "7")],
)
def test_fizzbuzz(n, expected):
    assert fizzbuzz(n) == expected


@pytest.mark.parametrize(
    ("status", "expected"),
    [
        (200, "success"),
        (299, "success"),
        (301, "redirect"),
        (404, "client error"),
        (503, "server error"),
        (100, "unknown"),
        (600, "unknown"),
    ],
)
def test_http_class(status, expected):
    assert http_class(status) == expected


def test_sum_of_evens():
    assert sum_of_evens(0) == 0
    assert sum_of_evens(1) == 0
    assert sum_of_evens(10) == 20
    assert sum_of_evens(11) == 30


def test_primes_below():
    assert primes_below(2) == []
    assert primes_below(3) == [2]
    assert primes_below(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


@pytest.mark.parametrize(("n", "steps"), [(1, 0), (2, 1), (6, 8), (27, 111)])
def test_collatz_steps(n, steps):
    assert collatz_steps(n) == steps


def test_find_pair():
    assert find_pair([1, 2, 3, 4], 5) == (1, 4)
    assert find_pair([3, 1, 4, 2], 6) == (4, 2)
    assert find_pair([1, 2], 10) is None
    assert find_pair([5], 10) is None
    assert find_pair([5, 5], 10) == (5, 5)
