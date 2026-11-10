# Lesson 26: Capstone - a todo CLI / Lección 26: Proyecto final - una CLI de tareas

You will build `todo`, a command-line task list that saves to a JSON file. It
combines earlier lessons: dataclasses, classes, file I/O with `pathlib`, JSON,
exceptions, type hints, comprehensions, a typer CLI (lesson 22) and tests.

> **ES:** Construirás `todo`, una lista de tareas de línea de comandos que se guarda en un archivo JSON. Combina lecciones anteriores: dataclasses, clases, E/S de archivos con `pathlib`, JSON, excepciones, anotaciones de tipo, comprehensions, una CLI con typer (lección 22) y pruebas.

## What it does / Qué hace

```text
$ todo add "buy milk"
Added #1: buy milk
$ todo add "write lesson"
Added #2: write lesson
$ todo done 1
Completed #1
$ todo list
[ ] 2 write lesson
$ todo list --all
[x] 1 buy milk
[ ] 2 write lesson
$ todo rm 2
Removed #2
$ todo --file work.json list      # pick a different file
No tasks.
```

## Your starting point / Tu punto de partida

Edit `exercises/26_capstone/capstone.py`. It has the shape and docstrings.
The tests in `exercises/26_capstone/test_capstone.py` are the spec; read them
first. Run:

> **ES:** Edita `exercises/26_capstone/capstone.py`. Tiene la estructura y los docstrings. Las pruebas en `exercises/26_capstone/test_capstone.py` son la especificación; léelas primero. Ejecuta:

```bash
uv run pytest exercises/26_capstone
uv run python exercises/26_capstone/capstone.py --help
```

## Step by step / Paso a paso

Work in this order and run the tests after each step.

> **ES:** Trabaja en este orden y ejecuta las pruebas después de cada paso.

### Step 1: the data / Paso 1: los datos

`Task` is a dataclass with `id`, `title`, and `done` (default `False`). It is
given. `dataclasses.asdict(task)` turns one into a dict, and `Task(**d)` turns
a dict back.

> **ES:** `Task` es una dataclass con `id`, `title` y `done` (por defecto `False`). Ya viene dada. `dataclasses.asdict(task)` convierte una en un dict, y `Task(**d)` convierte un dict de vuelta en una `Task`.

### Step 2: TodoStore, in memory / Paso 2: TodoStore, en memoria

Implement `__init__` (start with an empty list for now), `add`, `list`,
`complete` and `remove`.

> **ES:** Implementa `__init__` (por ahora empieza con una lista vacía), `add`, `list`, `complete` y `remove`.

- `add` strips the title and raises `ValueError` if it is empty. The new id is
  one more than the largest existing id (use `max(..., default=0)`), so ids do
  not get reused after deleting the last one... and never collide.
- `list` returns open tasks, or all of them when `include_done=True`.
  A list comprehension fits.
- `complete` and `remove` raise `KeyError` for unknown ids. A small private
  helper `_get(task_id)` avoids repeating the search.

> **ES:**
> - `add` recorta (strip) el título y lanza `ValueError` si queda vacío. El nuevo id es uno más que el id más grande existente (usa `max(..., default=0)`), así los ids no se reutilizan tras borrar el último... y nunca colisionan.
> - `list` devuelve las tareas abiertas, o todas cuando `include_done=True`. Una list comprehension encaja bien.
> - `complete` y `remove` lanzan `KeyError` para ids desconocidos. Una pequeña función auxiliar privada `_get(task_id)` evita repetir la búsqueda.

### Step 3: persistence / Paso 3: persistencia

- On every change, write the full list to `self.path` as JSON
  (`path.write_text(json.dumps(payload, indent=2))`).
- In `__init__`, if the file exists, read it with `json.loads` and rebuild the
  tasks. A missing file simply means "no tasks yet".

> **ES:**
> - En cada cambio, escribe la lista completa en `self.path` como JSON (`path.write_text(json.dumps(payload, indent=2))`).
> - En `__init__`, si el archivo existe, léelo con `json.loads` y reconstruye las tareas. Un archivo inexistente simplemente significa "aún no hay tareas".

### Step 4: the CLI / Paso 4: la CLI

- The `@app.callback()` takes `--file/-f` (default `todo.json`), builds a
  `TodoStore`, and saves it on `ctx.obj`. Use the `Annotated` +
  `typer.Option("--file", "-f")` form from lesson 22.
- Each command reads the store from `ctx.obj`.
- Print exactly what the spec shows; tests compare the text.
- Turn `ValueError` / `KeyError` into a stderr message and `typer.Exit(code=1)`
  rather than a traceback.
- The command called `list` needs `@app.command("list")` and a different
  Python name. `--all` collides with the builtin `all` too, so name the
  parameter `all_` and give the option its real name:
  `Annotated[bool, typer.Option("--all")]`.

> **ES:**
> - El `@app.callback()` recibe `--file/-f` (por defecto `todo.json`), construye un `TodoStore` y lo guarda en `ctx.obj`. Usa la forma `Annotated` + `typer.Option("--file", "-f")` de la lección 22.
> - Cada comando lee el store desde `ctx.obj`.
> - Imprime exactamente lo que muestra la especificación; las pruebas comparan el texto.
> - Convierte `ValueError` / `KeyError` en un mensaje a stderr y `typer.Exit(code=1)` en lugar de un traceback.
> - El comando llamado `list` necesita `@app.command("list")` y un nombre de Python distinto. `--all` también choca con el builtin `all`, así que nombra el parámetro `all_` y dale a la opción su nombre real: `Annotated[bool, typer.Option("--all")]`.

### Step 5: use it for real / Paso 5: úsalo de verdad

Add a few tasks by hand, open the JSON file, and notice it is human-readable.

> **ES:** Agrega algunas tareas a mano, abre el archivo JSON y observa que es legible para personas.

## Design notes / Notas de diseño

- The store knows nothing about the CLI; the CLI knows nothing about JSON. That
  separation is why the store is easy to test without any terminal.
- Tests use pytest's `tmp_path` fixture, so they never touch your real file.

> **ES:**
> - El store no sabe nada de la CLI; la CLI no sabe nada de JSON. Esa separación es la razón por la que el store es fácil de probar sin ninguna terminal.
> - Las pruebas usan el fixture `tmp_path` de pytest, así que nunca tocan tu archivo real.

## Stretch goals (no tests) / Retos extra (sin pruebas)

1. Add `todo edit ID "new title"`.
2. Store a `created` timestamp (`datetime`) on each task and show it with
   `--verbose`.
3. Swap JSON for `sqlite3` (lesson 20) behind the same `TodoStore` methods.
   The tests should still pass.
4. Write the file atomically: write to a temp file, then `Path.replace`.
5. Package it with a `[project.scripts]` entry so `uv run todo` works.
   Lesson 25 shows where that goes.
6. Run `uv run ruff check`, `ruff format` and `ty check` on your solution.

> **ES:**
> 1. Agrega `todo edit ID "new title"`.
> 2. Guarda un timestamp `created` (`datetime`) en cada tarea y muéstralo con `--verbose`.
> 3. Cambia JSON por `sqlite3` (lección 20) detrás de los mismos métodos de `TodoStore`. Las pruebas deberían seguir pasando.
> 4. Escribe el archivo de forma atómica: escribe en un archivo temporal y luego usa `Path.replace`.
> 5. Empaquétalo con una entrada `[project.scripts]` para que `uv run todo` funcione. La lección 25 muestra dónde va eso.
> 6. Ejecuta `uv run ruff check`, `ruff format` y `ty check` sobre tu solución.

## Done? / ¿Terminaste?

All tests in `uv run pytest exercises/26_capstone` pass, and you can explain
each function to a friend. Compare with `solutions/26_capstone/capstone.py`
only after trying on your own.

> **ES:** Todas las pruebas de `uv run pytest exercises/26_capstone` pasan, y puedes explicarle cada función a un amigo. Compara con `solutions/26_capstone/capstone.py` solo después de intentarlo por tu cuenta.
