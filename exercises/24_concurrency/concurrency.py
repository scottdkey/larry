"""Exercise: threads, processes, concurrent.futures.

Run tests: uv run pytest exercises/24_concurrency
"""

from collections.abc import Callable, Iterable


def count_primes(limit: int) -> int:
    """Count primes below limit (CPU-bound; trial division is fine)."""
    raise NotImplementedError


def map_threads[T, R](
    func: Callable[[T], R], items: Iterable[T], workers: int
) -> list[R]:
    """Apply func to items on a ThreadPoolExecutor; results in input order."""
    raise NotImplementedError


def map_processes[T, R](
    func: Callable[[T], R], items: Iterable[T], workers: int
) -> list[R]:
    """Apply func to items on a ProcessPoolExecutor; results in input order.

    func must be a top-level (picklable) function.
    """
    raise NotImplementedError


def try_all[T, R](
    func: Callable[[T], R], items: list[T], workers: int
) -> tuple[list[R], list[tuple[T, Exception]]]:
    """Run func on every item in threads; one failure must not stop the others.

    Return (results of successes in input order, [(item, exception), ...]).
    Hint: pool.submit gives Futures; future.exception() is None on success.
    """
    raise NotImplementedError


class SafeCounter:
    """A counter that stays correct when many threads call increment()."""

    def __init__(self) -> None:
        raise NotImplementedError

    @property
    def value(self) -> int:
        raise NotImplementedError

    def increment(self, by: int = 1) -> None:
        """Add `by` to the counter. Protect the update with a threading.Lock."""
        raise NotImplementedError


def hammer(counter: SafeCounter, threads: int, times: int) -> None:
    """Start `threads` threads that each call counter.increment() `times` times.

    Wait for all of them to finish before returning.
    """
    raise NotImplementedError
