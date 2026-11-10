import pytest
from strings import caesar, format_receipt, initials, is_palindrome, truncate, word_wrap


def test_initials():
    assert initials("ada king lovelace") == "AKL"
    assert initials("  grace   hopper ") == "GH"
    assert initials("") == ""


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("racecar", True),
        ("A man, a plan, a canal: Panama", True),
        ("hello", False),
        ("", True),
        ("No 'x' in Nixon", True),
    ],
)
def test_is_palindrome(text, expected):
    assert is_palindrome(text) is expected


def test_truncate():
    assert truncate("hello world", 8) == "hello..."
    assert truncate("hello", 5) == "hello"
    assert truncate("hello!", 5) == "he..."
    assert len(truncate("x" * 100, 10)) == 10


def test_caesar():
    assert caesar("abc", 1) == "bcd"
    assert caesar("xyz", 3) == "abc"
    assert caesar("Hello, World!", 5) == "Mjqqt, Btwqi!"
    assert caesar("Mjqqt, Btwqi!", -5) == "Hello, World!"
    assert caesar("abc", 52) == "abc"


def test_format_receipt():
    assert format_receipt([("tea", 2.5)], width=13) == "tea      2.50\nTOTAL    2.50"
    out = format_receipt([("apple", 1.0), ("melon", 3.25)])
    lines = out.split("\n")
    assert lines == [
        f"apple{1.0:>15.2f}",
        f"melon{3.25:>15.2f}",
        f"TOTAL{4.25:>15.2f}",
    ]
    assert all(len(line) == 20 for line in lines)


def test_format_receipt_empty():
    assert format_receipt([], width=13) == "TOTAL    0.00"


def test_word_wrap():
    assert word_wrap("the quick brown fox", 10) == ["the quick", "brown fox"]
    assert word_wrap("a b c", 100) == ["a b c"]
    assert word_wrap("", 10) == []
    assert word_wrap("extraordinary day", 5) == ["extraordinary", "day"]
