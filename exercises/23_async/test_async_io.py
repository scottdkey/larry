import asyncio

import async_io
import pytest
from async_io import (
    collect_successes,
    double,
    double_all,
    run_limited,
    squares_in_group,
    with_default,
)


def test_double():
    assert asyncio.run(double(4)) == 8


def test_double_all_keeps_order():
    assert asyncio.run(double_all([3, 1, 2])) == [6, 2, 4]
    assert asyncio.run(double_all([])) == []


def test_double_all_runs_concurrently(monkeypatch):
    arrived = 0
    all_arrived = asyncio.Event()

    async def rendezvous_double(x: int) -> int:
        nonlocal arrived
        arrived += 1
        if arrived == 3:
            all_arrived.set()
        await all_arrived.wait()
        return x * 2

    monkeypatch.setattr(async_io, "double", rendezvous_double)

    async def main():
        async with asyncio.timeout(2):
            return await double_all([3, 1, 2])

    assert asyncio.run(main()) == [6, 2, 4]


def test_with_default_fast_and_slow():
    async def fast() -> str:
        return "ok"

    cancelled = False

    async def slow() -> str:
        nonlocal cancelled
        try:
            await asyncio.sleep(5)
        except asyncio.CancelledError:
            cancelled = True
            raise
        return "late"

    async def main():
        return (
            await with_default(fast, 1, "default"),
            await with_default(slow, 0.01, "default"),
        )

    assert asyncio.run(main()) == ("ok", "default")
    assert cancelled


def test_run_limited_respects_limit_and_order():
    running = 0
    peak = 0

    def maker(i: int):
        async def job() -> int:
            nonlocal running, peak
            running += 1
            peak = max(peak, running)
            await asyncio.sleep(0.01)
            running -= 1
            return i

        return job

    result = asyncio.run(run_limited([maker(i) for i in range(6)], limit=2))
    assert result == list(range(6))
    assert peak == 2


def test_collect_successes():
    def ok(value: int):
        async def job() -> int:
            await asyncio.sleep(0)
            return value

        return job

    def fail(message: str):
        async def job() -> int:
            raise ValueError(message)

        return job

    makers = [ok(10), fail("e1"), ok(20), fail("e2"), ok(30)]
    good_results, errors = asyncio.run(collect_successes(makers))
    assert good_results == [10, 20, 30]
    assert [str(e) for e in errors] == ["e1", "e2"]
    assert all(isinstance(e, ValueError) for e in errors)


def test_squares_in_group():
    assert asyncio.run(squares_in_group([1, 2, 3])) == [1, 4, 9]


def test_squares_in_group_failure_is_exception_group():
    with pytest.raises(ExceptionGroup) as info:
        asyncio.run(squares_in_group([1, -2]))
    assert info.group_contains(ValueError)
