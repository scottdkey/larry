"""Lesson 15 exercises: decorators."""

from collections.abc import Callable
from functools import wraps


def apply_twice[T](func: Callable[[T], T], value: T) -> T:
    """Functions are values: return func(func(value))."""
    return func(func(value))


def shout[**P](func: Callable[P, str]) -> Callable[P, str]:
    """Decorator: upper-case the string result. Preserve the wrapped name/docstring."""

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> str:
        return func(*args, **kwargs).upper()

    return wrapper


def count_calls[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    """Decorator: expose the number of calls as `wrapper.calls` (starts at 0)."""

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        wrapper.calls += 1  # ty: ignore[missing-attribute]
        return func(*args, **kwargs)

    wrapper.calls = 0  # ty: ignore[missing-attribute]
    return wrapper


def repeat(times: int):
    """Decorator factory: call the wrapped function `times` times; return the last."""

    def decorator[**P, R](func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            result = func(*args, **kwargs)
            for _ in range(times - 1):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


def memoize[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    """Decorator: cache results by positional args (assume they are hashable)."""
    cache: dict[tuple, R] = {}

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        if args not in cache:
            cache[args] = func(*args, **kwargs)
        return cache[args]

    return wrapper


def retry(attempts: int, exceptions: tuple[type[Exception], ...] = (Exception,)):
    """Decorator factory: retry on `exceptions`, `attempts` calls max, then re-raise."""

    def decorator[**P, R](func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    if attempt == attempts:
                        raise
            raise AssertionError("unreachable")

        return wrapper

    return decorator
