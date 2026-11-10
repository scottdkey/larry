"""Lesson 20: a small book store on sqlite3."""

import sqlite3


def create_schema(conn: sqlite3.Connection) -> None:
    with conn:
        conn.execute(
            """
            CREATE TABLE books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER,
                UNIQUE (title, author)
            )
            """
        )


def add_book(
    conn: sqlite3.Connection, title: str, author: str, year: int | None
) -> int:
    with conn:
        cur = conn.execute(
            "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
            (title, author, year),
        )
    assert cur.lastrowid is not None
    return cur.lastrowid


def find_by_author(conn: sqlite3.Connection, author: str) -> list[tuple[str, int]]:
    rows = conn.execute(
        "SELECT title, year FROM books WHERE author = ? ORDER BY year", (author,)
    )
    return [(title, year) for title, year in rows]


def add_books(
    conn: sqlite3.Connection, books: list[tuple[str, str, int | None]]
) -> None:
    # `with conn` commits on success and rolls back if the block raises
    with conn:
        conn.executemany(
            "INSERT INTO books (title, author, year) VALUES (?, ?, ?)", books
        )


def books_per_author(conn: sqlite3.Connection) -> dict[str, int]:
    rows = conn.execute("SELECT author, COUNT(*) FROM books GROUP BY author")
    return dict(rows.fetchall())


def update_year(conn: sqlite3.Connection, title: str, year: int) -> bool:
    with conn:
        cur = conn.execute("UPDATE books SET year = ? WHERE title = ?", (year, title))
    return cur.rowcount > 0
