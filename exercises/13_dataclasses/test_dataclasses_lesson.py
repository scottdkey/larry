import dataclasses

import pytest
from dataclasses_lesson import (
    Book,
    Color,
    Playlist,
    Point,
    Rating,
    Rect,
    area,
    parse_color,
)


def test_book_defaults():
    b = Book("Dune", "Herbert")
    assert b.pages == 100
    assert b == Book("Dune", "Herbert", 100)
    assert Book("A", "B", 5).pages == 5


def test_playlist_no_shared_default():
    a, b = Playlist("a"), Playlist("b")
    a.add("x")
    assert a.songs == ["x"]
    assert b.songs == []


def test_point_frozen():
    p = Point(0, 0)
    assert p.distance_to(Point(3, 4)) == 5
    with pytest.raises(dataclasses.FrozenInstanceError):
        p.x = 1  # type: ignore[misc]
    assert {p: 1}[Point(0, 0)] == 1


def test_color():
    assert Color.RED.value == "red"
    assert parse_color("Blue") is Color.BLUE
    with pytest.raises(ValueError):
        parse_color("pink")


def test_rect():
    r = Rect(2, 3)
    assert area(r) == 6
    w, h = r
    assert (w, h) == (2, 3)
    assert r.width == 2


def test_rating_validation():
    assert Rating(5).stars == 5
    for bad in (0, 6):
        with pytest.raises(ValueError):
            Rating(bad)
