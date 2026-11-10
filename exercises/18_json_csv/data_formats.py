"""Lesson 18: JSON and CSV round trips.

ES: Lección 18: viajes de ida y vuelta con JSON y CSV.
"""

from dataclasses import dataclass
from datetime import date
from pathlib import Path


@dataclass
class Event:
    name: str
    when: date
    tags: list[str]


def to_json(data: dict) -> str:
    """Serialize to JSON with sorted keys and 2-space indent.

    ES: Serializa a JSON con claves ordenadas y sangría de 2 espacios.
    """
    raise NotImplementedError


def read_csv_rows(text: str) -> list[dict[str, str]]:
    """Parse CSV text (first line is the header) into a list of dicts.

    Quoted fields may contain commas and newlines.

    ES: Convierte texto CSV (la primera línea es el encabezado) en una lista de
    dicts. Los campos entre comillas pueden contener comas y saltos de línea.
    """
    raise NotImplementedError


def write_csv(rows: list[dict[str, str | int]], fieldnames: list[str]) -> str:
    """Render rows as CSV text: header first, '\\n' line endings, in
    `fieldnames` order. Fields with commas or quotes must be quoted.
    Hint: the csv module writes '\\r\\n' by default; pass lineterminator.

    ES: Genera texto CSV: encabezado primero, saltos '\\n', en el orden de
    `fieldnames`. Los campos con comas o comillas deben ir entre comillas.
    Pista: csv escribe '\\r\\n' por defecto; usa lineterminator.
    """
    raise NotImplementedError


def csv_to_json(csv_text: str, int_fields: list[str]) -> str:
    """Convert CSV text to a JSON array of objects (use to_json-style
    indent=2, sort_keys=True). Columns named in `int_fields` become ints.

    ES: Convierte texto CSV en un arreglo JSON de objetos (indent=2,
    sort_keys=True). Las columnas en `int_fields` se vuelven enteros.
    """
    raise NotImplementedError


def encode_event(event: Event) -> str:
    """Serialize an Event to JSON; the date is stored as an ISO string.

    ES: Serializa un Event a JSON; la fecha se guarda como cadena ISO.
    """
    raise NotImplementedError


def decode_event(text: str) -> Event:
    """Inverse of encode_event.

    ES: Inverso de encode_event.
    """
    raise NotImplementedError


def load_json(path: Path, default: dict) -> dict:
    """Load a JSON object from path, or return `default` if the file is
    missing. Invalid JSON should raise ValueError (json.JSONDecodeError is one).

    ES: Carga un objeto JSON desde path, o devuelve `default` si el archivo no
    existe. JSON inválido debe lanzar ValueError (json.JSONDecodeError lo es).
    """
    raise NotImplementedError
