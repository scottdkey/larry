import inspect

from generators import (
    Repeater,
    clean_lines,
    countdown,
    fibonacci,
    running_total,
    take,
)


def test_countdown():
    assert list(countdown(3)) == [3, 2, 1]
    assert list(countdown(0)) == []
    assert inspect.isgenerator(countdown(2))


def test_running_total():
    assert list(running_total([1, 2, 3])) == [1, 3, 6]
    assert list(running_total([])) == []


def test_running_total_is_lazy():
    consumed = []

    def source():
        for n in (1, 2, 3):
            consumed.append(n)
            yield n

    gen = running_total(source())
    assert consumed == []
    assert next(gen) == 1
    assert consumed == [1]


def test_clean_lines():
    lines = ["  a ", "", "# note", "   ", "b"]
    assert list(clean_lines(lines)) == ["a", "b"]


def test_fibonacci_and_take():
    assert take(8, fibonacci()) == [0, 1, 1, 2, 3, 5, 8, 13]
    assert take(0, fibonacci()) == []


def test_take_does_not_over_consume():
    it = iter(range(10))
    assert take(3, it) == [0, 1, 2]
    assert next(it) == 3


def test_repeater():
    assert list(Repeater("ab", 3)) == ["ab", "ab", "ab"]
    assert list(Repeater("x", 0)) == []


def test_repeater_is_its_own_iterator():
    r = Repeater("z", 2)
    assert iter(r) is r
    assert next(r) == "z"
    assert next(r) == "z"
    try:
        next(r)
    except StopIteration:
        pass
    else:
        raise AssertionError("expected StopIteration")
