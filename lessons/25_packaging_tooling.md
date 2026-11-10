# Lesson 25: Packaging and tooling / Lección 25: Empaquetado y herramientas

## Goals / Objetivos

- Work comfortably with `uv`, virtual environments and `pyproject.toml`.
- Know what `ruff`, `ty` and `pytest` each do, and run them as a habit.
- Read the config files in this very repository.

> **ES:**
> - Trabaja con soltura con `uv`, entornos virtuales y `pyproject.toml`.
> - Conoce qué hace cada una de `ruff`, `ty` y `pytest`, y ejecútalas por hábito.
> - Lee los archivos de configuración de este mismo repositorio.

## Virtual environments / Entornos virtuales

A **virtual environment** (venv) is a private folder of installed packages for
one project, so projects with different needs do not clash. Never `pip install`
into your system Python.

> **ES:** Un **entorno virtual** (venv) es una carpeta privada de paquetes instalados para un proyecto, de modo que proyectos con necesidades distintas no choquen. Nunca hagas `pip install` en el Python del sistema.

With `uv` you rarely touch venvs directly; it creates `.venv/` for you and
`uv run` uses it.

> **ES:** Con `uv` casi nunca tocas los venvs directamente; él crea `.venv/` por ti y `uv run` lo usa.

## The uv workflow / El flujo de trabajo con uv

```bash
uv init myproj           # new project with pyproject.toml
uv add httpx             # add a dependency (edits pyproject.toml + uv.lock)
uv add --dev pytest      # add to the dev dependency group
uv remove httpx
uv sync                  # make .venv match the lockfile
uv run pytest            # run any command inside the environment
uv run python script.py
uv python install 3.13   # manage Python versions
```

- `uv.lock` pins exact versions of everything. **Commit it**, so every machine
  gets identical packages.
- `.venv/` is local and disposable. Never commit it; delete and `uv sync` any
  time.
- Prefer `uv run ...` over activating the venv by hand.

> **ES:**
> - `uv.lock` fija las versiones exactas de todo. **Súbelo al repositorio (commit)**, para que cada máquina tenga paquetes idénticos.
> - `.venv/` es local y desechable. Nunca lo subas; bórralo y ejecuta `uv sync` cuando quieras.
> - Prefiere `uv run ...` en lugar de activar el venv a mano.

## pyproject.toml

One file describes the project. Open this repo's `pyproject.toml` and find:

> **ES:** Un solo archivo describe el proyecto. Abre el `pyproject.toml` de este repo y busca:

```toml
[project]
name = "larry"
version = "0.1.0"
requires-python = ">=3.13"
dependencies = ["httpx>=0.28.1", "typer>=0.29.0"]

[dependency-groups]
dev = ["pytest>=8", "ruff>=0.8", "ty>=0.0.1a1"]

[tool.ruff]
line-length = 88
```

- `[project]` is standard metadata. `dependencies` are what your code needs to
  run; each entry is a name plus a version specifier (`>=1.0`, `~=1.4`, `==2.0`).
- `[dependency-groups]` holds development-only tools.
- `[tool.X]` sections configure tool `X` (ruff, pytest, ...).
- `[build-system]` says how to build a distributable package.

> **ES:**
> - `[project]` son los metadatos estándar. `dependencies` es lo que tu código necesita para ejecutarse; cada entrada es un nombre más un especificador de versión (`>=1.0`, `~=1.4`, `==2.0`).
> - `[dependency-groups]` contiene herramientas solo para desarrollo.
> - Las secciones `[tool.X]` configuran la herramienta `X` (ruff, pytest, ...).
> - `[build-system]` indica cómo construir un paquete distribuible.

You can read it from Python with the stdlib `tomllib`; the exercise does.

> **ES:** Puedes leerlo desde Python con `tomllib` de la biblioteca estándar; el ejercicio lo hace.

### Versions / Versiones

Versions look like `MAJOR.MINOR.PATCH` (semantic versioning). Patch is a bug
fix, minor adds features compatibly, major may break things.

> **ES:** Las versiones tienen la forma `MAJOR.MINOR.PATCH` (versionado semántico). Patch es una corrección de errores, minor agrega funciones de forma compatible y major puede romper cosas.

## Project layout / Estructura del proyecto

```text
src/larry/        # your importable package (the "src layout")
tests/            # tests
pyproject.toml
uv.lock
```

Package names are normalized: `Friendly_Bard`, `friendly-bard` and
`friendly.bard` are the same project.

> **ES:** Los nombres de paquetes se normalizan: `Friendly_Bard`, `friendly-bard` y `friendly.bard` son el mismo proyecto.

## The quality tools / Las herramientas de calidad

| Tool | Command | Job |
| --- | --- | --- |
| ruff | `uv run ruff check` | linter: finds bugs and bad style |
| ruff | `uv run ruff format` | formatter: one consistent layout |
| ty | `uv run ty check` | type checker: verifies your hints |
| pytest | `uv run pytest` | runs your tests |

> **ES:**
>
> | Herramienta | Comando | Función |
> | --- | --- | --- |
> | ruff | `uv run ruff check` | linter: encuentra errores y mal estilo |
> | ruff | `uv run ruff format` | formateador: un diseño consistente |
> | ty | `uv run ty check` | verificador de tipos: comprueba tus anotaciones |
> | pytest | `uv run pytest` | ejecuta tus pruebas |

Useful flags: `ruff check --fix` applies safe fixes; `pytest -x` stops at the
first failure; `pytest -k name` selects tests by name; `pytest -q` is quiet.

> **ES:** Flags útiles: `ruff check --fix` aplica correcciones seguras; `pytest -x` se detiene en el primer fallo; `pytest -k name` selecciona pruebas por nombre; `pytest -q` es silencioso.

Enable more ruff rules in `[tool.ruff.lint]`, e.g.
`select = ["E", "F", "I", "UP", "B", "SIM"]` (errors, pyflakes, import order,
modernizing syntax, likely bugs, simplifications).

> **ES:** Activa más reglas de ruff en `[tool.ruff.lint]`, por ejemplo `select = ["E", "F", "I", "UP", "B", "SIM"]` (errores, pyflakes, orden de imports, modernización de sintaxis, probables bugs, simplificaciones).

## Habits worth building / Hábitos que vale la pena crear

1. Run format, lint, type check and tests before every commit:

   ```bash
   uv run ruff format && uv run ruff check && uv run ty check && uv run pytest
   ```

2. Automate it. A `Makefile` target, a `pre-commit` hook or CI job running that
   same line means nobody has to remember it.
3. Small commits with clear messages.
4. Keep secrets (tokens, passwords) out of the repo; read them from environment
   variables.
5. Add a dependency only when it saves real effort, and note why.
6. Fix the lockfile, not the symptom: if it works on your machine but not a
   teammate's, check `uv.lock` was committed.

> **ES:**
> 1. Ejecuta format, lint, verificación de tipos y pruebas antes de cada commit (ver el comando arriba).
> 2. Automatízalo. Un target de `Makefile`, un hook de `pre-commit` o un job de CI que ejecute esa misma línea hace que nadie tenga que acordarse.
> 3. Commits pequeños con mensajes claros.
> 4. Mantén los secretos (tokens, contraseñas) fuera del repo; léelos desde variables de entorno.
> 5. Agrega una dependencia solo cuando ahorre esfuerzo real, y anota por qué.
> 6. Arregla el lockfile, no el síntoma: si funciona en tu máquina pero no en la de un compañero, verifica que `uv.lock` se haya subido.

## Gotchas / Errores comunes

- Editing `pyproject.toml` dependencies by hand needs `uv sync` / `uv lock`
  afterward; `uv add` does both.
- `pytest` cannot import your code? Check `pythonpath` / the package layout.
- Running `python` instead of `uv run python` uses the wrong interpreter.
- A formatter changes files. Commit before the first run on old code so the
  diff is easy to review.

> **ES:**
> - Si editas a mano las dependencias de `pyproject.toml`, necesitas `uv sync` / `uv lock` después; `uv add` hace ambas.
> - ¿`pytest` no puede importar tu código? Revisa `pythonpath` / la estructura del paquete.
> - Ejecutar `python` en lugar de `uv run python` usa el intérprete equivocado.
> - Un formateador modifica archivos. Haz commit antes de la primera ejecución sobre código antiguo para que el diff sea fácil de revisar.

## Exercises / Ejercicios

Edit `exercises/25_packaging_tooling/tooling.py`. You will parse TOML text with
`tomllib`, extract dependency names from specifier strings, normalize project
names, bump versions, and read ruff's rules.

> **ES:** Edita `exercises/25_packaging_tooling/tooling.py`. Analizarás texto TOML con `tomllib`, extraerás nombres de dependencias a partir de cadenas de especificadores, normalizarás nombres de proyecto, incrementarás versiones y leerás las reglas de ruff.

```bash
uv run pytest exercises/25_packaging_tooling
```

Then, no tests needed: in a scratch folder run `uv init demo`, `uv add httpx`,
and `uv run python -c "import httpx; print(httpx.__version__)"`. Look at what
changed in `pyproject.toml`.

> **ES:** Luego, sin necesidad de pruebas: en una carpeta temporal ejecuta `uv init demo`, `uv add httpx` y `uv run python -c "import httpx; print(httpx.__version__)"`. Mira qué cambió en `pyproject.toml`.
