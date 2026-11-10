"""Lesson 20: a small book store on sqlite3.

ES: Lección 20: una pequeña tienda de libros con sqlite3.
"""

import sqlite3


def create_schema(conn: sqlite3.Connection) -> None:
    """Create table `books`: id INTEGER PRIMARY KEY, title TEXT NOT NULL,
    author TEXT NOT NULL, year INTEGER, with UNIQUE(title, author).

    ES: Crea la tabla `books` con esas columnas y UNIQUE(title, author).
    """
    raise NotImplementedError


def add_book(
    conn: sqlite3.Connection, title: str, author: str, year: int | None
) -> int:
    """Insert one book (parameterized query), commit, and return its new id.
    Duplicate title+author raises sqlite3.IntegrityError.

    ES: Inserta un libro (consulta parametrizada), haz commit y devuelve su id
    nuevo. Un title+author duplicado lanza sqlite3.IntegrityError.
    """
    raise NotImplementedError


def find_by_author(conn: sqlite3.Connection, author: str) -> list[tuple[str, int]]:
    """Return (title, year) pairs for the author, oldest first.
    Must be safe against SQL injection in `author`.

    ES: Devuelve pares (title, year) del autor, del más antiguo al más nuevo.
    Debe ser seguro contra inyección SQL en `author`.
    """
    raise NotImplementedError


def add_books(
    conn: sqlite3.Connection, books: list[tuple[str, str, int | None]]
) -> None:
    """Insert (title, author, year) rows all-or-nothing: if any row fails,
    none are stored and the error propagates.

    ES: Inserta filas (title, author, year) todo o nada: si alguna falla, no se
    guarda ninguna y el error se propaga.
    """
    raise NotImplementedError


def books_per_author(conn: sqlite3.Connection) -> dict[str, int]:
    """Map each author to their number of books.

    ES: Asocia cada autor con su número de libros.
    """
    raise NotImplementedError


def update_year(conn: sqlite3.Connection, title: str, year: int) -> bool:
    """Set the year for every book with this title; commit.
    Return True if at least one row changed.

    ES: Asigna el año a todos los libros con este título; haz commit. Devuelve
    True si al menos una fila cambió.
    """
    raise NotImplementedError
