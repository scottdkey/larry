"""Lesson 10 exercises: pathlib and reading/writing files."""

from pathlib import Path


def write_lines(path: Path, lines: list[str]) -> None:
    """Write each line followed by a newline, as UTF-8.

    Create missing parent directories first.

    ES: Escribe cada línea seguida de un salto de línea, en UTF-8. Crea primero
    los directorios padre que falten.
    """
    raise NotImplementedError


def read_lines(path: Path) -> list[str]:
    """Return the file's lines without trailing newlines (UTF-8).

    ES: Devuelve las líneas del archivo sin saltos de línea finales (UTF-8).
    """
    raise NotImplementedError


def append_line(path: Path, line: str) -> None:
    """Append `line` plus a newline, creating the file if needed.

    ES: Agrega `line` más un salto de línea, creando el archivo si hace falta.
    """
    raise NotImplementedError


def count_words(path: Path) -> int:
    """Count whitespace-separated words, reading the file line by line
    (do not load the whole file into memory).

    ES: Cuenta palabras separadas por espacios, leyendo el archivo línea por
    línea (no cargues todo el archivo en memoria).
    """
    raise NotImplementedError


def files_with_suffix(directory: Path, suffix: str) -> list[str]:
    """Sorted names (not full paths) of files under `directory`, searched
    recursively, whose name ends with `suffix` (e.g. ".txt"). Skip directories.

    ES: Nombres ordenados (no rutas completas) de archivos dentro de `directory`,
    buscando recursivamente, cuyo nombre termina en `suffix` (p. ej. ".txt").
    Omite los directorios.
    """
    raise NotImplementedError


def save_json(path: Path, data: dict[str, object]) -> None:
    """Write `data` to `path` as JSON (indent=2).

    ES: Escribe `data` en `path` como JSON (indent=2).
    """
    raise NotImplementedError


def load_json(
    path: Path, default: dict[str, object] | None = None
) -> dict[str, object]:
    """Load JSON from `path`. If the file does not exist return `default`,
    or an empty dict when default is None.

    ES: Carga JSON desde `path`. Si el archivo no existe devuelve `default`, o
    un dict vacío cuando default es None.
    """
    raise NotImplementedError
