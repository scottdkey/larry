from dicts import (
    group_anagrams,
    group_by_length,
    invert,
    merge_counts,
    top_words,
    word_counts,
)


def test_word_counts():
    assert word_counts("the cat The dog") == {"the": 2, "cat": 1, "dog": 1}
    assert word_counts("") == {}


def test_word_counts_returns_plain_dict():
    assert type(word_counts("a")) is dict


def test_invert():
    assert invert({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert invert({}) == {}


def test_group_by_length():
    result = group_by_length(["hi", "yo", "cat", "a", "dog"])
    assert result == {2: ["hi", "yo"], 3: ["cat", "dog"], 1: ["a"]}
    assert type(result) is dict
    assert group_by_length([]) == {}


def test_top_words():
    text = "b a b c a b d"
    assert top_words(text, 2) == [("b", 3), ("a", 2)]
    assert top_words(text, 10)[-1] == ("d", 1)
    assert top_words("x y", 2) == [("x", 1), ("y", 1)]
    assert top_words("", 3) == []


def test_merge_counts():
    a = {"x": 1, "y": 2}
    b = {"y": 3, "z": 4}
    assert merge_counts(a, b) == {"x": 1, "y": 5, "z": 4}
    assert a == {"x": 1, "y": 2}
    assert merge_counts() == {}


def test_group_anagrams():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    assert group_anagrams(words) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert group_anagrams([]) == []
