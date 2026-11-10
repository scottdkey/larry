# Lesson 17: Testing with pytest / Lección 17: Pruebas con pytest

Goals: write clear tests, remove repetition with `parametrize` and fixtures,
test files and environment safely, and learn to judge whether your tests are
any good.

> **ES:** Objetivos: escribir pruebas claras, eliminar la repetición con `parametrize` y fixtures, probar archivos y variables de entorno de forma segura, y aprender a juzgar si tus pruebas son buenas.

## The shape of a test / La forma de una prueba

A test is a function named `test_*` in a file named `test_*.py`. It passes if
it finishes without raising. `assert` is all you need:

> **ES:** Una prueba (test) es una función llamada `test_*` en un archivo llamado `test_*.py`. Pasa si termina sin lanzar una excepción. `assert` es todo lo que necesitas:

```python
def test_addition():
    assert 1 + 1 == 2
```

When an assert fails, pytest shows both sides of the comparison. Run
`uv run pytest -x` to stop at the first failure, `-k name` to select tests by
name, and `-v` for one line per test.

> **ES:** Cuando un assert falla, pytest muestra ambos lados de la comparación. Ejecuta `uv run pytest -x` para detenerte en el primer fallo, `-k nombre` para seleccionar pruebas por nombre y `-v` para una línea por prueba.

Good tests are small, have one reason to fail, and have names that say what
should happen: `test_mean_of_empty_list_raises`.

> **ES:** Las buenas pruebas son pequeñas, tienen una sola razón para fallar y tienen nombres que dicen qué debería ocurrir: `test_mean_of_empty_list_raises`.

## parametrize: one test, many cases / parametrize: una prueba, muchos casos

```python
import pytest


@pytest.mark.parametrize(
    ("text", "expected"),
    [("abc", "ABC"), ("", ""), ("a b", "A B")],
)
def test_upper(text, expected):
    assert text.upper() == expected
```

Each row becomes its own test, reported separately. Include edge cases:
empty input, one item, boundaries, negatives.

> **ES:** Cada fila se convierte en su propia prueba y se reporta por separado. Incluye casos límite: entrada vacía, un solo elemento, fronteras, negativos.

## Expecting errors: pytest.raises / Esperar errores: pytest.raises

```python
def test_int_rejects_text():
    with pytest.raises(ValueError, match="invalid literal"):
        int("abc")
```

`match` is a regex searched in the message. The test fails if no error is
raised, or if a different error type is raised.

> **ES:** `match` es una regex que se busca dentro del mensaje. La prueba falla si no se lanza ningún error, o si se lanza un tipo de error distinto.

## Floats: pytest.approx / Flotantes: pytest.approx

```python
assert 0.1 + 0.2 == pytest.approx(0.3)
```

Never compare floats with `==` unless the values are exact.

> **ES:** Nunca compares flotantes con `==` a menos que los valores sean exactos.

## Fixtures: shared setup / Fixtures: preparación compartida

A fixture is a function that builds something a test needs. Tests ask for it
by naming it as a parameter.

> **ES:** Un fixture es una función que construye algo que una prueba necesita. Las pruebas lo piden nombrándolo como parámetro.

```python
import pytest


@pytest.fixture
def numbers() -> list[int]:
    return [3, 1, 2]


def test_sorted(numbers):
    assert sorted(numbers) == [1, 2, 3]
```

Every test gets a fresh value. Use `yield` inside a fixture to run cleanup
after the test. Put fixtures shared across files in `conftest.py`.

> **ES:** Cada prueba recibe un valor nuevo. Usa `yield` dentro de un fixture para ejecutar la limpieza después de la prueba. Pon los fixtures compartidos entre archivos en `conftest.py`.

## Built-in fixtures you will use constantly / Fixtures incluidos que usarás constantemente

`tmp_path` is a fresh empty directory (a `pathlib.Path`) per test:

> **ES:** `tmp_path` es un directorio nuevo y vacío (un `pathlib.Path`) por cada prueba:

```python
def test_write(tmp_path):
    f = tmp_path / "out.txt"
    f.write_text("hi")
    assert f.read_text() == "hi"
```

`monkeypatch` changes things for one test, then undoes them automatically:

> **ES:** `monkeypatch` cambia cosas durante una prueba y luego las deshace automáticamente:

```python
def test_env(monkeypatch):
    monkeypatch.setenv("HOME_DIR", "/x")
    monkeypatch.delenv("DEBUG", raising=False)
    monkeypatch.setattr("os.getcwd", lambda: "/fake")
```

`capsys` captures printed output (`capsys.readouterr().out`).

> **ES:** `capsys` captura lo que se imprime (`capsys.readouterr().out`).

## Tests should be independent and deterministic / Las pruebas deben ser independientes y deterministas

- Never depend on test order or on files left by another test.
- Do not use the network, the real clock, or random numbers without control.
  Replace them with `monkeypatch` or pass them in as arguments.
- Do not touch your real home directory; use `tmp_path`.

> **ES:**
>
> - Nunca dependas del orden de las pruebas ni de archivos que dejó otra prueba.
> - No uses la red, el reloj real ni números aleatorios sin control. Reemplázalos con `monkeypatch` o pásalos como argumentos.
> - No toques tu directorio home real; usa `tmp_path`.

## Are my tests any good? Mutation thinking / ¿Son buenas mis pruebas? Pensar en mutaciones

Passing tests prove little if they would also pass on broken code. A
*mutant* is a deliberately broken copy of your function (change `<` to `<=`,
drop a condition). Good tests fail on every mutant. When you write a test,
ask: "what bug would this catch?"

> **ES:** Las pruebas que pasan demuestran poco si también pasarían con código roto. Un *mutante* es una copia deliberadamente rota de tu función (cambiar `<` por `<=`, quitar una condición). Las buenas pruebas fallan con cada mutante. Cuando escribas una prueba, pregúntate: "¿qué error atraparía esto?"

Boundaries are where mutants hide. For a range check, test the value just
inside, exactly on, and just outside each edge.

> **ES:** Las fronteras son donde se esconden los mutantes. Para una verificación de rango, prueba el valor justo dentro, exactamente en el borde y justo fuera de cada extremo.

## Gotchas / Errores comunes

- A test with no `assert` always passes. Check that yours can fail.
- `assert x == y, "message"` is fine, but pytest's own output is usually
  enough.
- `pytest.raises` without `match` accepts any message; be specific when it
  matters.
- Do not test too much in one function; the first failure hides the rest.
- Loops over cases inside a single test hide which case failed; use
  `parametrize`.

> **ES:**
>
> - Una prueba sin `assert` siempre pasa. Verifica que la tuya pueda fallar.
> - `assert x == y, "message"` está bien, pero la salida propia de pytest suele ser suficiente.
> - `pytest.raises` sin `match` acepta cualquier mensaje; sé específico cuando importe.
> - No pruebes demasiado en una sola función; el primer fallo oculta los demás.
> - Los bucles sobre casos dentro de una sola prueba ocultan cuál caso falló; usa `parametrize`.

## Exercises / Ejercicios

Files:

> **ES:** Archivos:

- `exercises/17_testing/testing_skills.py` — implement the stubs
- `exercises/17_testing/test_testing_skills.py` — the tests (read them!)
- Reference: `solutions/17_testing/testing_skills.py`

> **ES:**
>
> - `exercises/17_testing/testing_skills.py` — implementa los stubs
> - `exercises/17_testing/test_testing_skills.py` — las pruebas (¡léelas!)
> - Referencia: `solutions/17_testing/testing_skills.py`

Tasks:

> **ES:** Tareas:

1. `clamp`, `mean`, `slugify`: plain functions with parametrized tests.
2. `read_settings`: reads a file; tests use `tmp_path`.
3. `greeting`: reads an environment variable; tests use `monkeypatch`.
4. `check_leap_year` and `check_clamp`: here *you* write the tests. The grader
   runs your checker against a correct function (must pass) and several buggy
   ones (each must raise `AssertionError`). Think like a mutant hunter.

> **ES:**
>
> 1. `clamp`, `mean`, `slugify`: funciones simples con pruebas parametrizadas.
> 2. `read_settings`: lee un archivo; las pruebas usan `tmp_path`.
> 3. `greeting`: lee una variable de entorno; las pruebas usan `monkeypatch`.
> 4. `check_leap_year` y `check_clamp`: aquí *tú* escribes las pruebas. El evaluador ejecuta tu verificador contra una función correcta (debe pasar) y varias con errores (cada una debe lanzar `AssertionError`). Piensa como un cazador de mutantes.

Run: `uv run pytest exercises/17_testing`

> **ES:** Ejecuta: `uv run pytest exercises/17_testing`
