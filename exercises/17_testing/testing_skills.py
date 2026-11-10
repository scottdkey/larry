"""Lesson 17: functions to implement, plus checkers you write yourself.

ES: Lección 17: funciones por implementar, más verificadores que escribes tú.
"""

from collections.abc import Callable
from pathlib import Path


def clamp(value: float, low: float, high: float) -> float:
    """Return value limited to the range [low, high].

    Raise ValueError if low > high.

    ES: Devuelve value limitado al rango [low, high]. Lanza ValueError si
    low > high.
    """
    raise NotImplementedError


def mean(values: list[float]) -> float:
    """Return the arithmetic mean. Raise ValueError for an empty list.

    ES: Devuelve la media aritmética. Lanza ValueError si la lista está vacía.
    """
    raise NotImplementedError


def slugify(text: str) -> str:
    """Lowercase, trim, and join words with single hyphens.

    slugify("  Hello,   World! ") == "hello-world"
    Only letters and digits count as word characters.

    ES: Pasa a minúsculas, recorta y une las palabras con un solo guion. Solo las
    letras y los dígitos cuentan como caracteres de palabra.
    """
    raise NotImplementedError


def read_settings(path: Path) -> dict[str, str]:
    """Parse `key = value` lines from a text file.

    Blank lines and lines starting with '#' are skipped. Keys and values are
    stripped. A non-blank line without '=' raises ValueError.

    ES: Lee líneas `clave = valor` de un archivo de texto. Se omiten las líneas
    en blanco y las que empiezan con '#'. Claves y valores se recortan. Una
    línea no vacía sin '=' lanza ValueError.
    """
    raise NotImplementedError


def greeting() -> str:
    """Return 'Hello, <name>!' where name comes from the GREET_NAME
    environment variable, or 'stranger' if it is not set.

    ES: Devuelve 'Hello, <name>!' donde name viene de la variable de entorno
    GREET_NAME, o 'stranger' si no está definida.
    """
    raise NotImplementedError


def check_leap_year(is_leap_year: Callable[[int], bool]) -> None:
    """Write assertions that pass for a correct leap-year function and fail
    (raise AssertionError) for each broken variant the grader tries.

    Rules: divisible by 4, except centuries, except multiples of 400.

    ES: Escribe aserciones que pasen con una función de año bisiesto correcta y
    fallen (AssertionError) con cada variante rota. Reglas: divisible entre 4,
    excepto siglos, excepto múltiplos de 400.
    """
    raise NotImplementedError


def check_clamp(clamp_fn: Callable[[float, float, float], float]) -> None:
    """Write assertions that pass for a correct clamp and catch broken ones
    (wrong bound, swapped bounds, off-by-one at the edges).

    ES: Escribe aserciones que pasen con un clamp correcto y atrapen los rotos
    (límite equivocado, límites invertidos, error de uno en los bordes).
    """
    raise NotImplementedError
