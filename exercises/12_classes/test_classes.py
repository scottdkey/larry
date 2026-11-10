import pytest
from classes import Animal, Car, Counter, Dog, Engine, Puppy, Temperature, Vector


def test_counter():
    c = Counter()
    c.increment()
    c.increment()
    assert c.value == 2
    assert Counter(5).value == 5


def test_counter_value_read_only():
    with pytest.raises(AttributeError):
        Counter().value = 3  # type: ignore[misc]


def test_temperature():
    t = Temperature(100)
    assert t.fahrenheit == 212
    t.fahrenheit = 32
    assert t.celsius == 0


def test_vector():
    v = Vector(3, 4)
    assert v + Vector(1, 1) == Vector(4, 5)
    assert abs(v) == 5
    assert repr(v) == "Vector(3, 4)"
    assert v != Vector(0, 0)
    assert v != "nope"


def test_vector_truthiness():
    assert not Vector(0, 0)
    assert Vector(0, 1)


def test_inheritance():
    assert Dog("Rex").speak() == "Rex says woof"
    assert Puppy("Bit").speak() == "Bit says yip!"
    assert isinstance(Puppy("Bit"), Animal)
    with pytest.raises(NotImplementedError):
        Animal("x").speak()


def test_composition():
    assert Car("Mini", Engine(100)).describe() == "Mini (100 hp)"
