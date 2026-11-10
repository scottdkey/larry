"""Lesson 5 exercises: dicts, Counter, defaultdict, grouping."""

from collections import Counter, defaultdict


def word_counts(text: str) -> dict[str, int]:
    """Count lower-cased, whitespace-separated words."""
    return dict(Counter(text.lower().split()))


def invert(mapping: dict[str, int]) -> dict[int, str]:
    """Swap keys and values. Values are unique."""
    return {value: key for key, value in mapping.items()}


def group_by_length(words: list[str]) -> dict[int, list[str]]:
    """Group words by length, preserving input order within each group."""
    groups: defaultdict[int, list[str]] = defaultdict(list)
    for word in words:
        groups[len(word)].append(word)
    return dict(groups)


def top_words(text: str, n: int) -> list[tuple[str, int]]:
    """Return the n most common lower-cased words as (word, count), most common first.

    Ties keep first-seen order.
    """
    return Counter(text.lower().split()).most_common(n)


def merge_counts(*counts: dict[str, int]) -> dict[str, int]:
    """Add up several count dicts key by key, without modifying the inputs."""
    total: dict[str, int] = {}
    for d in counts:
        for key, value in d.items():
            total[key] = total.get(key, 0) + value
    return total


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group words that are anagrams of each other.

    Groups appear in order of first member; words keep input order within a group.
    """
    groups: dict[str, list[str]] = {}
    for word in words:
        groups.setdefault("".join(sorted(word)), []).append(word)
    return list(groups.values())
