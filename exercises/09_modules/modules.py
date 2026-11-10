"""Lesson 9 exercises: imports and a tour of the standard library."""

import sys  # noqa: F401  (used by the __main__ block you will write)
from collections.abc import Callable, Sequence


def days_between(start: str, end: str) -> int:
    """Days from `start` to `end`, both ISO dates like "2024-01-31".

    Negative if end is earlier. Hint: datetime.date.fromisoformat.

    ES: Días desde `start` hasta `end`, ambas fechas ISO como "2024-01-31".
    Negativo si end es anterior. Pista: datetime.date.fromisoformat.
    """
    raise NotImplementedError


def top_words(text: str, n: int) -> list[tuple[str, int]]:
    """Return the n most common words (lowercased) as (word, count) pairs.

    A word is a run of letters or apostrophes (re.findall(r"[a-z']+", ...)).
    Hint: collections.Counter.most_common.

    ES: Devuelve las n palabras más comunes (en minúsculas) como pares
    (palabra, cantidad). Una palabra es una secuencia de letras o apóstrofes.
    Pista: collections.Counter.most_common.
    """
    raise NotImplementedError


def slugify(title: str) -> str:
    """Lowercase, keep runs of a-z0-9, join them with single hyphens.

    slugify("  Hello, World! 2024 ") -> "hello-world-2024"

    ES: Pasa a minúsculas, conserva secuencias de a-z0-9 y las une con guiones
    simples.
    """
    raise NotImplementedError


def to_sorted_json(data: dict[str, object]) -> str:
    """Serialise to JSON with sorted keys and an indent of 2 spaces.

    ES: Serializa a JSON con claves ordenadas y sangría de 2 espacios.
    """
    raise NotImplementedError


def load_callable(path: str) -> Callable[..., object]:
    """Import and return an object from a "module:attribute" string.

    load_callable("math:sqrt")(9) -> 3.0
    Hint: importlib.import_module and getattr.

    ES: Importa y devuelve un objeto a partir de una cadena "módulo:atributo".
    Pista: importlib.import_module y getattr.
    """
    raise NotImplementedError


def main(argv: Sequence[str]) -> int:
    """Sum integer arguments and print "total: N"; return 0.

    If any argument is not an integer, print "error: arguments must be integers"
    and return 1. Then add an `if __name__ == "__main__":` block at the bottom
    that calls raise SystemExit(main(sys.argv[1:])).

    ES: Suma los argumentos enteros e imprime "total: N"; devuelve 0. Si algún
    argumento no es entero, imprime "error: arguments must be integers" y
    devuelve 1. Luego agrega al final un bloque `if __name__ == "__main__":`
    que llame a raise SystemExit(main(sys.argv[1:])).
    """
    raise NotImplementedError
