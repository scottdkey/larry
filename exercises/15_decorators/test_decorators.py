import pytest
from decorators import apply_twice, count_calls, memoize, repeat, retry, shout


def test_apply_twice():
    assert apply_twice(lambda x: x * 2, 3) == 12
    assert apply_twice(str.strip, "  a ") == "a"


def test_shout_keeps_metadata():
    @shout
    def greet(name: str) -> str:
        """Say hi."""
        return f"hi {name}"

    assert greet("bo") == "HI BO"
    assert greet.__name__ == "greet"
    assert greet.__doc__ == "Say hi."


def test_count_calls():
    @count_calls
    def f(x: int) -> int:
        return x + 1

    assert f.calls == 0  # type: ignore[attr-defined]
    assert f(1) == 2
    f(2)
    assert f.calls == 2  # type: ignore[attr-defined]


def test_repeat():
    seen: list[int] = []

    @repeat(3)
    def f() -> int:
        seen.append(1)
        return len(seen)

    assert f() == 3
    assert len(seen) == 3


def test_memoize():
    calls = []

    @memoize
    def slow(a: int, b: int) -> int:
        calls.append((a, b))
        return a + b

    assert slow(1, 2) == 3
    assert slow(1, 2) == 3
    assert slow(2, 2) == 4
    assert calls == [(1, 2), (2, 2)]


def test_retry_succeeds_eventually():
    state = {"n": 0}

    @retry(3)
    def flaky() -> str:
        state["n"] += 1
        if state["n"] < 3:
            raise ValueError("no")
        return "ok"

    assert flaky() == "ok"
    assert state["n"] == 3


def test_retry_gives_up_and_filters():
    state = {"n": 0}

    @retry(2, (ValueError,))
    def bad() -> None:
        state["n"] += 1
        raise ValueError("x")

    with pytest.raises(ValueError):
        bad()
    assert state["n"] == 2

    @retry(5, (ValueError,))
    def other() -> None:
        state["n"] += 100
        raise KeyError("x")

    with pytest.raises(KeyError):
        other()
    assert state["n"] == 102
