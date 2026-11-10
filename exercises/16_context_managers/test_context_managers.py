import pytest
from context_managers import Suppress, Tracker, read_lines, temporary_value, timer_log


def test_tracker():
    with Tracker() as t:
        assert t.events == ["enter"]
    assert t.events == ["enter", "exit"]


def test_tracker_propagates():
    t = Tracker()
    with pytest.raises(ValueError), t:
        raise ValueError("boom")
    assert t.events == ["enter", "exit"]


def test_temporary_value_restores():
    d = {"a": 1}
    with temporary_value(d, "a", 2):
        assert d["a"] == 2
    assert d == {"a": 1}


def test_temporary_value_removes_and_handles_error():
    d: dict[str, int] = {}
    with pytest.raises(LookupError), temporary_value(d, "k", 9):
        assert d == {"k": 9}
        raise LookupError
    assert d == {}


def test_suppress():
    with Suppress(KeyError):
        {}["x"]
    with pytest.raises(ValueError), Suppress(KeyError):
        raise ValueError
    with Suppress(ArithmeticError):
        _ = 1 / 0


def test_read_lines(tmp_path):
    p = tmp_path / "f.txt"
    p.write_text("a \n b\n")
    assert list(read_lines(p)) == ["a", "b"]


def test_timer_log():
    log: list[str] = []
    with timer_log(log, "x"):
        log.append("work")
    with pytest.raises(ValueError), timer_log(log, "y"):
        raise ValueError
    assert log == ["start x", "work", "end x", "start y", "end y"]
