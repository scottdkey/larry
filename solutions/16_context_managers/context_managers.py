"""Lesson 16 exercises: context managers."""

from collections.abc import Generator, Iterator
from contextlib import contextmanager
from pathlib import Path
from types import TracebackType


class Tracker:
    """Class-based context manager that records events into `self.events`.

    On enter append 'enter'; on exit append 'exit'. Exceptions must propagate.
    `__enter__` returns the tracker itself.
    """

    def __init__(self) -> None:
        self.events: list[str] = []

    def __enter__(self) -> "Tracker":
        self.events.append("enter")
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> bool:
        self.events.append("exit")
        return False


@contextmanager
def temporary_value(target: dict[str, int], key: str, value: int) -> Generator[None]:
    """@contextmanager: set target[key]=value inside the block, then restore.

    Restore the old value, or remove the key if it was absent -- even on error.
    """
    missing = key not in target
    old = target.get(key)
    target[key] = value
    try:
        yield
    finally:
        if missing:
            del target[key]
        else:
            target[key] = old  # ty: ignore[invalid-assignment]


class Suppress:
    """Class-based: swallow exceptions of the given type, let others through."""

    def __init__(self, exc_type: type[BaseException]) -> None:
        self.exc_type = exc_type

    def __enter__(self) -> None:
        return None

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> bool:
        return exc_type is not None and issubclass(exc_type, self.exc_type)


def read_lines(path: Path) -> Iterator[str]:
    """Generator that yields stripped lines, using `with` so the file always closes."""
    with path.open() as f:
        for line in f:
            yield line.strip()


@contextmanager
def timer_log(log: list[str], label: str) -> Generator[None]:
    """@contextmanager: append 'start <label>' on entry and 'end <label>' on exit
    (also when the block raises)."""
    log.append(f"start {label}")
    try:
        yield
    finally:
        log.append(f"end {label}")
