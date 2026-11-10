from functions import (
    add_item,
    compose,
    describe,
    join_words,
    make_counter,
    make_multiplier,
    sort_people,
)


def test_add_item_uses_given_list():
    items = ["a"]
    assert add_item("b", items) == ["a", "b"]
    assert items == ["a", "b"]


def test_add_item_no_shared_default():
    assert add_item("x") == ["x"]
    assert add_item("y") == ["y"]


def test_join_words():
    assert join_words("a", "b", "c") == "a b c"
    assert join_words("a", "b", sep="-") == "a-b"
    assert join_words("a", "b", upper=True) == "A B"
    assert join_words() == ""


def test_join_words_keyword_only():
    assert join_words("a", "b", "-") == "a b -"
    assert join_words("sep", "upper") == "sep upper"


def test_describe():
    assert describe("Ada") == "Ada"
    assert (
        describe("Ada", born="1815", job="mathematician")
        == "Ada: born=1815, job=mathematician"
    )
    assert describe("Ada", name="x") == "Ada: name=x"


def test_make_multiplier():
    triple = make_multiplier(3)
    double = make_multiplier(2)
    assert triple(5) == 15
    assert double(5) == 10


def test_make_counter():
    a = make_counter()
    b = make_counter(10)
    assert [a(), a(), a()] == [0, 1, 2]
    assert [b(), b()] == [10, 11]
    assert a() == 3


def test_compose():
    inc = lambda x: x + 1  # noqa: E731
    dbl = lambda x: x * 2  # noqa: E731
    assert compose(inc, dbl)(5) == 12
    assert compose(dbl, inc)(5) == 11
    assert compose()(7) == 7


def test_sort_people():
    people = [
        {"name": "Bo", "age": 30},
        {"name": "Al", "age": 25},
        {"name": "Cy", "age": 35},
    ]
    assert [p["name"] for p in sort_people(people, "age")] == ["Al", "Bo", "Cy"]
    assert [p["name"] for p in sort_people(people, "name", reverse=True)] == [
        "Cy",
        "Bo",
        "Al",
    ]
    assert people[0]["name"] == "Bo"
