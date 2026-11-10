import pytest
from typing_lesson import Stack, adult_names, chorus, first_or_none, group_by, turn


def test_first_or_none():
    assert first_or_none([3, 4]) == 3
    assert first_or_none([]) is None


def test_stack():
    s: Stack[int] = Stack()
    s.push(1)
    s.push(2)
    assert len(s) == 2
    assert s.pop() == 2
    assert s.pop() == 1
    with pytest.raises(IndexError):
        s.pop()


def test_adult_names():
    users = [
        {"name": "a", "age": 17},
        {"name": "b", "age": 18},
        {"name": "c", "age": 40},
    ]
    assert adult_names(users) == ["b", "c"]


def test_turn():
    assert turn(0, "left") == 270
    assert turn(270, "right") == 0
    assert turn(90, "right") == 180


def test_chorus():
    class Cat:
        def speak(self) -> str:
            return "meow"

    class Dog:
        def speak(self) -> str:
            return "woof"

    assert chorus([Cat(), Dog()]) == "meow & woof"
    assert chorus([]) == ""


def test_group_by():
    assert group_by(["a", "bb", "c", "dd"], len) == {1: ["a", "c"], 2: ["bb", "dd"]}
