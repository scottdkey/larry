# Lesson 20: SQLite / Lección 20: SQLite

Goals: store and query data with the built-in `sqlite3` module, use
parameterized queries, and understand transactions.

> **ES:** Objetivos: guardar y consultar datos con el módulo `sqlite3` incluido, usar consultas parametrizadas y entender las transacciones.

SQLite is a full SQL database stored in a single file (or in memory). It ships
with Python, so there is nothing to install.

> **ES:** SQLite es una base de datos SQL completa guardada en un solo archivo (o en memoria). Viene con Python, así que no hay nada que instalar.

## Connect and create a table / Conectar y crear una tabla

```python
import sqlite3

conn = sqlite3.connect(":memory:")  # or "app.db" for a file
conn.execute(
    "CREATE TABLE people (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER)"
)
```

`":memory:"` creates a throwaway database that vanishes on close. It is ideal
for tests: fast, isolated, no cleanup.

> **ES:** `":memory:"` crea una base de datos desechable que desaparece al cerrarse. Es ideal para pruebas: rápida, aislada y sin limpieza.

## Insert and query / Insertar y consultar

```python
conn.execute("INSERT INTO people (name, age) VALUES (?, ?)", ("Ada", 36))
conn.commit()

rows = conn.execute("SELECT name, age FROM people WHERE age > ?", (30,))
for name, age in rows:
    print(name, age)

conn.execute("SELECT ...").fetchone()  # one row or None
conn.execute("SELECT ...").fetchall()  # list of tuples
```

Rows are plain tuples. For name access, set
`conn.row_factory = sqlite3.Row`.

> **ES:** Las filas son tuplas simples. Para acceder por nombre, configura `conn.row_factory = sqlite3.Row`.

`cursor.lastrowid` is the id of the last inserted row, and `cursor.rowcount`
is how many rows an `UPDATE` or `DELETE` changed.

> **ES:** `cursor.lastrowid` es el id de la última fila insertada, y `cursor.rowcount` es cuántas filas cambió un `UPDATE` o `DELETE`.

## Always use parameters / Usa siempre parámetros

**Never** build SQL with f-strings or `+`:

> **ES:** **Nunca** construyas SQL con f-strings ni `+`:

```python
# DANGEROUS: name = "x'; DROP TABLE people; --"
conn.execute(f"SELECT * FROM people WHERE name = '{name}'")

# Safe: the driver sends the value separately from the SQL text
conn.execute("SELECT * FROM people WHERE name = ?", (name,))
```

This is SQL injection, one of the most common security bugs. Parameters (`?`)
work for values only. Table and column names cannot be parameters; if you must
vary them, choose from a fixed allow-list.

> **ES:** Esto es inyección SQL, uno de los errores de seguridad más comunes. Los parámetros (`?`) sirven solo para valores. Los nombres de tablas y columnas no pueden ser parámetros; si necesitas variarlos, elige de una lista permitida fija.

The parameter argument is always a sequence, so a single value needs a
trailing comma: `(name,)`.

> **ES:** El argumento de parámetros siempre es una secuencia, así que un solo valor necesita una coma final: `(name,)`.

## Transactions / Transacciones

A transaction groups changes so they all happen or none do. Python's sqlite3
opens one automatically before an `INSERT`/`UPDATE`/`DELETE`; nothing is saved
until `commit()`. `rollback()` discards the pending changes.

> **ES:** Una transacción agrupa cambios para que ocurran todos o ninguno. El sqlite3 de Python abre una automáticamente antes de un `INSERT`/`UPDATE`/`DELETE`; nada se guarda hasta `commit()`. `rollback()` descarta los cambios pendientes.

The connection is a context manager for exactly this:

> **ES:** La conexión es un context manager justamente para esto:

```python
with conn:  # commit on success, rollback on exception
    conn.execute("UPDATE accounts SET bal = bal - 50 WHERE id = 1")
    conn.execute("UPDATE accounts SET bal = bal + 50 WHERE id = 2")
```

Note that `with conn` does **not** close the connection. Call `conn.close()`
(or use `contextlib.closing(conn)`) when finished.

> **ES:** Ten en cuenta que `with conn` **no** cierra la conexión. Llama a `conn.close()` (o usa `contextlib.closing(conn)`) al terminar.

`executemany` runs one statement over many parameter tuples:

> **ES:** `executemany` ejecuta una sentencia sobre muchas tuplas de parámetros:

```python
conn.executemany("INSERT INTO people (name, age) VALUES (?, ?)", rows)
```

## Constraints are your friends / Las restricciones son tus amigas

`NOT NULL`, `UNIQUE`, and `PRIMARY KEY` make the database reject bad data
with `sqlite3.IntegrityError`. Let the database enforce rules rather than
checking in Python alone: it is correct even with multiple programs.

> **ES:** `NOT NULL`, `UNIQUE` y `PRIMARY KEY` hacen que la base de datos rechace datos incorrectos con `sqlite3.IntegrityError`. Deja que la base de datos haga cumplir las reglas en lugar de verificar solo en Python: es correcto incluso con varios programas.

## Useful SQL / SQL útil

```sql
SELECT author, COUNT(*) FROM books GROUP BY author;
SELECT * FROM books ORDER BY year DESC LIMIT 5;
UPDATE books SET year = ? WHERE title = ?;
DELETE FROM books WHERE id = ?;
```

## Gotchas / Errores comunes

- Forgetting `commit()`: your data is visible on your connection but lost
  when it closes, and other connections cannot see it.
- SQLite is loosely typed: it will happily store text in an INTEGER column
  if it cannot convert it. Validate in Python too.
- `NULL` becomes `None`; compare with `IS NULL`, not `= NULL`.
- A connection should be used from the thread that created it.

> **ES:**
>
> - Olvidar `commit()`: tus datos son visibles en tu conexión pero se pierden al cerrarla, y otras conexiones no pueden verlos.
> - SQLite es de tipado flexible: guardará texto en una columna INTEGER si no puede convertirlo. Valida también en Python.
> - `NULL` se vuelve `None`; compara con `IS NULL`, no con `= NULL`.
> - Una conexión debe usarse desde el hilo que la creó.

## Exercises / Ejercicios

Files:

> **ES:** Archivos:

- `exercises/20_sqlite/sqlite_store.py` — implement the stubs
- `exercises/20_sqlite/test_sqlite_store.py` — the tests
- Reference: `solutions/20_sqlite/sqlite_store.py`

> **ES:**
>
> - `exercises/20_sqlite/sqlite_store.py` — implementa los stubs
> - `exercises/20_sqlite/test_sqlite_store.py` — las pruebas
> - Referencia: `solutions/20_sqlite/sqlite_store.py`

Run: `uv run pytest exercises/20_sqlite`

> **ES:** Ejecuta: `uv run pytest exercises/20_sqlite`
