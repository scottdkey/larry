import pytest
from sequences import chunks, dedupe, min_max, rotate, shared_sorted, sort_words


def test_dedupe():
    assert dedupe([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert dedupe([]) == []


@pytest.mark.parametrize(
    ("k", "expected"),
    [
        (0, [1, 2, 3, 4]),
        (1, [4, 1, 2, 3]),
        (-1, [2, 3, 4, 1]),
        (4, [1, 2, 3, 4]),
        (6, [3, 4, 1, 2]),
    ],
)
def test_rotate(k, expected):
    original = [1, 2, 3, 4]
    assert rotate(original, k) == expected
    assert original == [1, 2, 3, 4]


def test_rotate_empty():
    assert rotate([], 3) == []


def test_chunks():
    assert chunks([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunks([1, 2], 5) == [[1, 2]]
    assert chunks([], 3) == []


def test_min_max():
    assert min_max([3, -1, 7, 2]) == (-1, 7)
    assert min_max([4]) == (4, 4)
    with pytest.raises(ValueError):
        min_max([])


def test_shared_sorted():
    assert shared_sorted(["b", "a", "a", "c"], ["c", "a", "z"]) == ["a", "c"]
    assert shared_sorted(["x"], ["y"]) == []


def test_sort_words():
    words = ["pear", "Fig", "apple", "kiwi", "Date", "fig"]
    assert sort_words(words) == ["Fig", "fig", "Date", "kiwi", "pear", "apple"]
    assert words[0] == "pear"
