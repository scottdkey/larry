"""Lesson 16 exercises: context managers.
ES: Ejercicios de la lección 16: context managers."""

from collections.abc import Iterator
from pathlib import Path
from types import TracebackType


class Tracker:
    """Class-based context manager that records events into `self.events`.

    On enter append 'enter'; on exit append 'exit'. Exceptions must propagate.
    `__enter__` returns the tracker itself.

    ES: Context manager basado en clase que registra eventos en `self.events`.
    Al entrar agrega 'enter'; al salir agrega 'exit'. Las excepciones deben
    propagarse. `__enter__` devuelve el propio tracker.
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def __enter__(self) -> "Tracker":
        raise NotImplementedError

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> bool:
        raise NotImplementedError


def temporary_value(target: dict[str, int], key: str, value: int):
    """@contextmanager: set target[key]=value inside the block, then restore.

    Restore the old value, or remove the key if it was absent -- even on error.

    ES: @contextmanager: asigna target[key]=value dentro del bloque y luego
    restaura. Restaura el valor anterior, o quita la clave si no existía,
    incluso si hay error.
    """
    raise NotImplementedError


class Suppress:
    """Class-based: swallow exceptions of the given type, let others through.
    ES: Basado en clase: suprime excepciones del tipo dado, deja pasar las demás."""

    def __init__(self, exc_type: type[BaseException]) -> None:
        raise NotImplementedError

    def __enter__(self) -> None:
        raise NotImplementedError

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> bool:
        raise NotImplementedError


def read_lines(path: Path) -> Iterator[str]:
    """Generator that yields stripped lines, using `with` so the file always closes.
    ES: Generador que produce líneas sin espacios, usando `with` para que el
    archivo siempre se cierre."""
    raise NotImplementedError


def timer_log(log: list[str], label: str):
    """@contextmanager: append 'start <label>' on entry and 'end <label>' on exit
    (also when the block raises).

    ES: @contextmanager: agrega 'start <label>' al entrar y 'end <label>' al salir
    (también cuando el bloque lanza una excepción).
    """
    raise NotImplementedError
