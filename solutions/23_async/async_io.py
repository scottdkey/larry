"""Exercise: asyncio basics."""

import asyncio
from collections.abc import Awaitable, Callable


async def double(x: int) -> int:
    """Return x * 2 after yielding to the event loop once."""
    await asyncio.sleep(0)
    return x * 2


async def double_all(numbers: list[int]) -> list[int]:
    """Double every number concurrently, preserving input order."""
    return list(await asyncio.gather(*(double(n) for n in numbers)))


async def with_default[T](
    make: Callable[[], Awaitable[T]], timeout: float, default: T
) -> T:
    """Await make(); return default if it takes longer than timeout seconds."""
    try:
        return await asyncio.wait_for(make(), timeout)
    except TimeoutError:
        return default


async def run_limited[T](
    makers: list[Callable[[], Awaitable[T]]], limit: int
) -> list[T]:
    """Run all makers with at most `limit` in flight; results in input order."""
    sem = asyncio.Semaphore(limit)

    async def run(make: Callable[[], Awaitable[T]]) -> T:
        async with sem:
            return await make()

    return list(await asyncio.gather(*(run(m) for m in makers)))


async def collect_successes[T](
    makers: list[Callable[[], Awaitable[T]]],
) -> tuple[list[T], list[Exception]]:
    """Run all makers; return (results of those that worked, exceptions)."""
    outcomes = await asyncio.gather(*(m() for m in makers), return_exceptions=True)
    good = [o for o in outcomes if not isinstance(o, BaseException)]
    bad = [o for o in outcomes if isinstance(o, Exception)]
    return good, bad


async def squares_in_group(numbers: list[int]) -> list[int]:
    """Square numbers using asyncio.TaskGroup; results in input order.

    If any task fails, TaskGroup raises an ExceptionGroup; let it propagate.
    """
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(_square(n)) for n in numbers]
    return [t.result() for t in tasks]


async def _square(n: int) -> int:
    await asyncio.sleep(0)
    if n < 0:
        raise ValueError(f"negative: {n}")
    return n * n
