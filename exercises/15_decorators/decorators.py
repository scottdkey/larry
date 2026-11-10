"""Lesson 15 exercises: decorators.
ES: Ejercicios de la lección 15: decoradores."""

from collections.abc import Callable


def apply_twice[T](func: Callable[[T], T], value: T) -> T:
    """Functions are values: return func(func(value)).
    ES: Las funciones son valores: devuelve func(func(value))."""
    raise NotImplementedError


def shout[**P](func: Callable[P, str]) -> Callable[P, str]:
    """Decorator: upper-case the string result. Preserve the wrapped name/docstring.
    ES: Decorador: pasa a mayúsculas el resultado. Conserva el nombre y docstring."""
    raise NotImplementedError


def count_calls[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    """Decorator: expose the number of calls as `wrapper.calls` (starts at 0).
    ES: Decorador: expone el número de llamadas como `wrapper.calls` (empieza en 0)."""
    raise NotImplementedError


def repeat(times: int):
    """Decorator factory: call the wrapped function `times` times; return the last.
    ES: Fábrica de decoradores: llama `times` veces a la función; devuelve la
    última."""
    raise NotImplementedError


def memoize[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    """Decorator: cache results by positional args (assume they are hashable).
    ES: Decorador: cachea resultados por args posicionales (asume que son hashables)."""
    raise NotImplementedError


def retry(attempts: int, exceptions: tuple[type[Exception], ...] = (Exception,)):
    """Decorator factory: retry on `exceptions`, `attempts` calls max, then re-raise.
    ES: Fábrica de decoradores: reintenta ante `exceptions`, máximo `attempts`
    llamadas, y luego relanza."""
    raise NotImplementedError
