from itertools import count, islice

from comprehensions import (
    chunked,
    flatten,
    lazy_squares,
    pairs_summing_to,
    squares_of_evens,
    unique_initials,
    word_lengths,
)


def test_squares_of_evens():
    assert squares_of_evens([1, 2, 3, 4]) == [4, 16]
    assert squares_of_evens([]) == []
    assert squares_of_evens([-2, 5]) == [4]


def test_word_lengths():
    assert word_lengths(["hi", "python"]) == {"hi": 2, "python": 6}
    assert word_lengths([]) == {}


def test_unique_initials():
    assert unique_initials(["Apple", "avocado", "Bean", ""]) == {"a", "b"}


def test_flatten():
    assert flatten([[1, 2], [3], []]) == [1, 2, 3]
    assert flatten([]) == []


def test_pairs_summing_to():
    assert pairs_summing_to([1, 2, 3, 4], 5) == [(1, 4), (2, 3)]
    assert pairs_summing_to([2, 2, 2], 4) == [(2, 2)] * 3
    assert pairs_summing_to([1], 2) == []


def test_chunked():
    assert chunked(range(5), 2) == [[0, 1], [2, 3], [4]]
    assert chunked([], 3) == []


def test_lazy_squares_is_lazy():
    result = lazy_squares(count(1))
    assert not isinstance(result, list)
    assert list(islice(result, 4)) == [1, 4, 9, 16]
