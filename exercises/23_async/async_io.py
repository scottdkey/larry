"""Exercise: asyncio basics. Run tests: uv run pytest exercises/23_async"""

import asyncio
from collections.abc import Awaitable, Callable


async def double(x: int) -> int:
    """Return x * 2 after yielding to the event loop once (asyncio.sleep(0))."""
    raise NotImplementedError


async def double_all(numbers: list[int]) -> list[int]:
    """Double every number concurrently with asyncio.gather, keeping order."""
    raise NotImplementedError


async def with_default[T](
    make: Callable[[], Awaitable[T]], timeout: float, default: T
) -> T:
    """Await make(); return default if it takes longer than timeout seconds."""
    raise NotImplementedError


async def run_limited[T](
    makers: list[Callable[[], Awaitable[T]]], limit: int
) -> list[T]:
    """Run all makers with at most `limit` in flight (asyncio.Semaphore).

    Results come back in input order.
    """
    raise NotImplementedError


async def collect_successes[T](
    makers: list[Callable[[], Awaitable[T]]],
) -> tuple[list[T], list[Exception]]:
    """Run all makers concurrently without letting one failure stop the rest.

    Return (results of those that worked, exceptions from those that failed),
    each in input order. Hint: gather(..., return_exceptions=True).
    """
    raise NotImplementedError


async def squares_in_group(numbers: list[int]) -> list[int]:
    """Square numbers using asyncio.TaskGroup; results in input order.

    A negative number must make its task raise ValueError; the TaskGroup then
    raises an ExceptionGroup, which you should let propagate.
    """
    raise NotImplementedError


_ = asyncio  # remove once you use it
