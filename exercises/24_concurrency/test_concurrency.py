import os
import sys
import threading

from concurrency import (
    SafeCounter,
    count_primes,
    hammer,
    map_processes,
    map_threads,
    try_all,
)


def test_count_primes():
    assert count_primes(2) == 0
    assert count_primes(10) == 4
    assert count_primes(100) == 25


def test_map_threads_order_and_overlap():
    barrier = threading.Barrier(4, timeout=5)

    def meet(x: int) -> int:
        barrier.wait()
        return x + 1

    assert map_threads(meet, [1, 2, 3, 4], workers=4) == [2, 3, 4, 5]


def _pid_of(_: int) -> int:
    return os.getpid()


def test_map_processes():
    assert map_processes(count_primes, [10, 100, 2], workers=2) == [4, 25, 0]
    pids = map_processes(_pid_of, [1, 2, 3, 4], workers=2)
    assert os.getpid() not in pids


def _inverse(x: int) -> float:
    return 1 / x


def test_try_all_collects_errors():
    results, errors = try_all(_inverse, [1, 0, 2, 0], workers=2)
    assert results == [1.0, 0.5]
    assert [item for item, _ in errors] == [0, 0]
    assert all(isinstance(e, ZeroDivisionError) for _, e in errors)


def test_safe_counter_basic():
    c = SafeCounter()
    assert c.value == 0
    c.increment()
    c.increment(by=4)
    assert c.value == 5


def test_hammer_is_exact():
    before = threading.active_count()
    old = sys.getswitchinterval()
    sys.setswitchinterval(1e-6)
    try:
        c = SafeCounter()
        hammer(c, threads=8, times=100000)
    finally:
        sys.setswitchinterval(old)
    assert c.value == 800000
    assert threading.active_count() == before
