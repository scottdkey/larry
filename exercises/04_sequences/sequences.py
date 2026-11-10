"""Lesson 4 exercises: lists, tuples, sets, slicing, sorting."""


def dedupe(items: list[int]) -> list[int]:
    """Remove duplicates, keeping the first occurrence of each, in original order.

    ES: Quita duplicados conservando la primera aparición y el orden original.
    """
    raise NotImplementedError


def rotate(items: list[int], k: int) -> list[int]:
    """Return a new list rotated right by k; k may be negative or larger than len.

    rotate([1, 2, 3, 4], 1) -> [4, 1, 2, 3]

    ES: Devuelve una lista nueva rotada a la derecha k posiciones (k puede ser
    negativo).
    """
    raise NotImplementedError


def chunks(items: list[int], size: int) -> list[list[int]]:
    """Split into consecutive lists of `size`; the last one may be shorter.

    ES: Divide en listas consecutivas de `size`; la última puede ser más corta.
    """
    raise NotImplementedError


def min_max(numbers: list[int]) -> tuple[int, int]:
    """Return (smallest, largest). Raise ValueError on an empty list.

    ES: Devuelve (menor, mayor). Lanza ValueError con una lista vacía.
    """
    raise NotImplementedError


def shared_sorted(a: list[str], b: list[str]) -> list[str]:
    """Return the sorted list of distinct items present in both a and b (use sets).

    ES: Devuelve la lista ordenada de elementos distintos presentes en a y b (usa sets).
    """
    raise NotImplementedError


def sort_words(words: list[str]) -> list[str]:
    """Sort by length (shortest first), ties broken alphabetically ignoring case.

    Return a new list; do not modify the input.

    ES: Ordena por longitud (menor primero), desempate alfabético sin distinguir
    mayúsculas. Devuelve una lista nueva; no modifiques la entrada.
    """
    raise NotImplementedError
