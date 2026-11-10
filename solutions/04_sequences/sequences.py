"""Lesson 4 exercises: lists, tuples, sets, slicing, sorting."""


def dedupe(items: list[int]) -> list[int]:
    """Remove duplicates, keeping the first occurrence of each, in original order."""
    seen: set[int] = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def rotate(items: list[int], k: int) -> list[int]:
    """Return a new list rotated right by k; k may be negative or larger than len.

    rotate([1, 2, 3, 4], 1) -> [4, 1, 2, 3]
    """
    if not items:
        return []
    k %= len(items)
    return items[-k:] + items[:-k] if k else items[:]


def chunks(items: list[int], size: int) -> list[list[int]]:
    """Split into consecutive lists of `size`; the last one may be shorter."""
    return [items[i : i + size] for i in range(0, len(items), size)]


def min_max(numbers: list[int]) -> tuple[int, int]:
    """Return (smallest, largest). Raise ValueError on an empty list."""
    if not numbers:
        raise ValueError("min_max() of empty list")
    return min(numbers), max(numbers)


def shared_sorted(a: list[str], b: list[str]) -> list[str]:
    """Return the sorted list of distinct items present in both a and b (use sets)."""
    return sorted(set(a) & set(b))


def sort_words(words: list[str]) -> list[str]:
    """Sort by length (shortest first), ties broken alphabetically ignoring case.

    Return a new list; do not modify the input.
    """
    return sorted(words, key=lambda w: (len(w), w.lower()))
