import sqlite3
from contextlib import closing

import pytest
from sqlite_store import (
    add_book,
    add_books,
    books_per_author,
    create_schema,
    find_by_author,
    update_year,
)


@pytest.fixture
def conn():
    connection = sqlite3.connect(":memory:")
    create_schema(connection)
    yield connection
    connection.close()


def count(conn):
    return conn.execute("SELECT COUNT(*) FROM books").fetchone()[0]


def test_schema_columns(conn):
    cols = [row[1] for row in conn.execute("PRAGMA table_info(books)")]
    assert cols == ["id", "title", "author", "year"]


def test_add_book_returns_ids(conn):
    first = add_book(conn, "Dune", "Herbert", 1965)
    second = add_book(conn, "Emma", "Austen", 1815)
    assert second == first + 1


def test_add_book_duplicate(conn):
    add_book(conn, "Dune", "Herbert", 1965)
    with pytest.raises(sqlite3.IntegrityError):
        add_book(conn, "Dune", "Herbert", 1966)
    assert count(conn) == 1


def test_add_book_is_committed(conn, tmp_path):
    db = tmp_path / "x.db"
    with closing(sqlite3.connect(db)) as c1, closing(sqlite3.connect(db)) as c2:
        create_schema(c1)
        add_book(c1, "Dune", "Herbert", 1965)
        assert c2.execute("SELECT COUNT(*) FROM books").fetchone()[0] == 1


@pytest.mark.parametrize("title, author", [(None, "Herbert"), ("Dune", None)])
def test_title_and_author_required(conn, title, author):
    with pytest.raises(sqlite3.IntegrityError):
        add_book(conn, title, author, 1965)
    assert count(conn) == 0


def test_find_by_author_sorted(conn):
    add_book(conn, "Emma", "Austen", 1815)
    add_book(conn, "Persuasion", "Austen", 1817)
    add_book(conn, "Sense", "Austen", 1811)
    add_book(conn, "Dune", "Herbert", 1965)
    assert find_by_author(conn, "Austen") == [
        ("Sense", 1811),
        ("Emma", 1815),
        ("Persuasion", 1817),
    ]
    assert find_by_author(conn, "Nobody") == []


def test_find_by_author_injection_is_inert(conn):
    add_book(conn, "Dune", "Herbert", 1965)
    assert find_by_author(conn, "x' OR '1'='1") == []
    assert find_by_author(conn, "'; DROP TABLE books; --") == []
    assert count(conn) == 1


def test_add_books_all_or_nothing(conn):
    add_book(conn, "Dune", "Herbert", 1965)
    batch = [("Emma", "Austen", 1815), ("Dune", "Herbert", 1965), ("X", "Y", 1)]
    with pytest.raises(sqlite3.IntegrityError):
        add_books(conn, batch)
    assert count(conn) == 1


def test_add_books_success(conn):
    add_books(conn, [("Emma", "Austen", 1815), ("Dune", "Herbert", None)])
    assert count(conn) == 2


def test_books_per_author(conn):
    add_books(conn, [("A", "x", 1), ("B", "x", 2), ("C", "y", 3)])
    assert books_per_author(conn) == {"x": 2, "y": 1}


def test_update_year(conn):
    add_book(conn, "Dune", "Herbert", 1900)
    assert update_year(conn, "Dune", 1965) is True
    assert find_by_author(conn, "Herbert") == [("Dune", 1965)]
    assert update_year(conn, "Missing", 1) is False
