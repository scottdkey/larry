"""Exercise: threads, processes and concurrent.futures."""

import threading
from collections.abc import Callable, Iterable
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def count_primes(limit: int) -> int:
    """Count primes below limit (deliberately CPU-bound trial division)."""
    count = 0
    for n in range(2, limit):
        if all(n % d for d in range(2, int(n**0.5) + 1)):
            count += 1
    return count


def map_threads[T, R](
    func: Callable[[T], R], items: Iterable[T], workers: int
) -> list[R]:
    """Apply func to items on a thread pool; results in input order."""
    with ThreadPoolExecutor(max_workers=workers) as pool:
        return list(pool.map(func, items))


def map_processes[T, R](
    func: Callable[[T], R], items: Iterable[T], workers: int
) -> list[R]:
    """Apply func to items on a process pool; func must be a top-level function."""
    with ProcessPoolExecutor(max_workers=workers) as pool:
        return list(pool.map(func, items))


def try_all[T, R](
    func: Callable[[T], R], items: list[T], workers: int
) -> tuple[list[R], list[tuple[T, Exception]]]:
    """Run func on every item in threads; one failure must not stop the others.

    Return (results of successes in input order, [(item, exception), ...]).
    """
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [(item, pool.submit(func, item)) for item in items]
    results: list[R] = []
    errors: list[tuple[T, Exception]] = []
    for item, future in futures:
        exc = future.exception()
        if exc is None:
            results.append(future.result())
        elif isinstance(exc, Exception):
            errors.append((item, exc))
    return results, errors


class SafeCounter:
    """A counter that stays correct when many threads call increment()."""

    def __init__(self) -> None:
        self._value = 0
        self._lock = threading.Lock()

    @property
    def value(self) -> int:
        return self._value

    def increment(self, by: int = 1) -> None:
        with self._lock:
            current = self._value
            self._value = current + by


def hammer(counter: SafeCounter, threads: int, times: int) -> None:
    """Start `threads` threads that each call counter.increment() `times` times.

    Wait for all of them to finish before returning.
    """

    def work() -> None:
        for _ in range(times):
            counter.increment()

    workers = [threading.Thread(target=work) for _ in range(threads)]
    for t in workers:
        t.start()
    for t in workers:
        t.join()
