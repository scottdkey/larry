"""Lesson 5 exercises: dicts, Counter, defaultdict, grouping."""


def word_counts(text: str) -> dict[str, int]:
    """Count lower-cased, whitespace-separated words.

    ES: Cuenta palabras en minúscula separadas por espacios.
    """
    raise NotImplementedError


def invert(mapping: dict[str, int]) -> dict[int, str]:
    """Swap keys and values. Values are unique.

    ES: Intercambia claves y valores. Los valores son únicos.
    """
    raise NotImplementedError


def group_by_length(words: list[str]) -> dict[int, list[str]]:
    """Group words by length, preserving input order within each group.

    ES: Agrupa palabras por longitud, conservando el orden de entrada en cada grupo.
    """
    raise NotImplementedError


def top_words(text: str, n: int) -> list[tuple[str, int]]:
    """Return the n most common lower-cased words as (word, count), most common first.

    Ties keep first-seen order.

    ES: Devuelve las n palabras más comunes en minúscula como (palabra, conteo).
    Los empates conservan el orden de primera aparición.
    """
    raise NotImplementedError


def merge_counts(*counts: dict[str, int]) -> dict[str, int]:
    """Add up several count dicts key by key, without modifying the inputs.

    ES: Suma varios dicts de conteo clave por clave, sin modificar las entradas.
    """
    raise NotImplementedError


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group words that are anagrams of each other.

    Groups appear in order of first member; words keep input order within a group.

    ES: Agrupa palabras que son anagramas entre sí. Los grupos van en orden de su
    primer miembro; las palabras conservan el orden de entrada dentro del grupo.
    """
    raise NotImplementedError
