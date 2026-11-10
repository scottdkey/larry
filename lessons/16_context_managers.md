# Lesson 16: Context Managers

> **ES:** Lección 16: Administradores de contexto (context managers)

Goals: use `with` to guarantee cleanup, write context managers as generators
with `contextlib.contextmanager`, and as classes with `__enter__`/`__exit__`.

> **ES:** Objetivos: usar `with` para garantizar la limpieza, escribir context
> managers como generadores con `contextlib.contextmanager`, y como clases con
> `__enter__`/`__exit__`.

## The `with` statement

> **ES:** ## La sentencia `with`

You have seen this already:

> **ES:** Ya has visto esto:

```python
from pathlib import Path

with Path("notes.txt").open() as f:
    text = f.read()
# f is closed here, even if read() raised
```

`with` runs setup, runs your block, then always runs cleanup. It replaces
`try`/`finally` for resources: files, locks, database connections, temporary
state.

> **ES:** `with` ejecuta la preparación, ejecuta tu bloque y luego siempre
> ejecuta la limpieza. Reemplaza a `try`/`finally` para recursos: archivos,
> locks, conexiones a bases de datos, estado temporal.

## The generator way

> **ES:** ## La forma con generadores

`@contextmanager` turns a generator with a single `yield` into a context
manager. Code before `yield` is setup, code after is cleanup.

> **ES:** `@contextmanager` convierte un generador con un solo `yield` en un
> context manager. El código antes de `yield` es la preparación; el código
> después es la limpieza.

```python
from contextlib import contextmanager
from collections.abc import Iterator


@contextmanager
def announce(label: str) -> Iterator[None]:
    print(f"start {label}")
    try:
        yield
    finally:
        print(f"end {label}")


with announce("job"):
    print("working")
```

Wrap the `yield` in `try`/`finally`: if the block raises, the exception is
re-raised at the `yield`, and without `finally` your cleanup would be skipped.

> **ES:** Envuelve el `yield` en `try`/`finally`: si el bloque lanza una
> excepción, esta se vuelve a lanzar en el `yield`, y sin `finally` tu limpieza
> se omitiría.

You can yield a value, which `as` receives:

> **ES:** Puedes hacer yield de un valor, que `as` recibe:

```python
@contextmanager
def opened(path: str) -> Iterator[int]:
    ...
    yield 42


with opened("x") as value:
    ...
```

## The class way

> **ES:** ## La forma con clases

Implement two methods.

> **ES:** Implementa dos métodos.

```python
from types import TracebackType


class Tracker:
    def __init__(self) -> None:
        self.events: list[str] = []

    def __enter__(self) -> "Tracker":
        self.events.append("enter")
        return self  # bound by `as`

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> bool:
        self.events.append("exit")
        return False
```

`__exit__` receives the exception details (all `None` if the block succeeded).
Its return value decides what happens to an exception:

> **ES:** `__exit__` recibe los detalles de la excepción (todos `None` si el
> bloque terminó bien). Su valor de retorno decide qué pasa con la excepción:

- falsy: the exception propagates (the usual choice)
- truthy: the exception is swallowed

> **ES:**
> - falsy: la excepción se propaga (lo habitual)
> - truthy: la excepción se suprime

```python
class Suppress:
    def __init__(self, exc_type: type[BaseException]) -> None:
        self.exc_type = exc_type

    def __enter__(self) -> None: ...
    def __exit__(self, exc_type, exc, tb) -> bool:
        return exc_type is not None and issubclass(exc_type, self.exc_type)
```

The standard library ships this as `contextlib.suppress`.

> **ES:** La biblioteca estándar incluye esto como `contextlib.suppress`.

## Choosing

> **ES:** ## Cómo elegir

- Generator style: short, linear setup/cleanup. Usually the best default.
- Class style: when the manager carries state, is reusable, or needs to
  inspect the exception.

> **ES:**
> - Estilo generador: preparación y limpieza cortas y lineales. Normalmente es
>   la mejor opción por defecto.
> - Estilo clase: cuando el manager mantiene estado, es reutilizable o necesita
>   inspeccionar la excepción.

## Generators and `with`

> **ES:** ## Generadores y `with`

A `with` inside a generator keeps the resource open while the generator is
suspended, and closes it when the generator finishes or is closed.

> **ES:** Un `with` dentro de un generador mantiene el recurso abierto mientras
> el generador está suspendido, y lo cierra cuando el generador termina o se
> cierra.

```python
def read_lines(path: Path) -> Iterator[str]:
    with path.open() as f:
        for line in f:
            yield line.strip()
```

## Gotchas

> **ES:** ## Trampas comunes

- Swallowing exceptions by accident: returning `True` from `__exit__` hides
  bugs. Return `False`/`None` unless that is the point.
- A `@contextmanager` generator must `yield` exactly once.
- `with a, b:` enters both and exits in reverse order.
- Tests that touch files should use pytest's `tmp_path`, never real paths.

> **ES:**
> - Suprimir excepciones por accidente: devolver `True` desde `__exit__` oculta
>   errores. Devuelve `False`/`None` a menos que ese sea el objetivo.
> - Un generador con `@contextmanager` debe hacer `yield` exactamente una vez.
> - `with a, b:` entra a ambos y sale en orden inverso.
> - Los tests que tocan archivos deben usar `tmp_path` de pytest, nunca rutas
>   reales.

## Exercises

> **ES:** ## Ejercicios

Files:

- Stubs: `exercises/16_context_managers/context_managers.py`
- Tests: `exercises/16_context_managers/test_context_managers.py`

> **ES:** Archivos: los stubs y los tests indicados arriba.

Implement `Tracker`, `temporary_value`, `Suppress`, `read_lines` and
`timer_log`. Note that `temporary_value` and `timer_log` need the
`@contextmanager` decorator. Run:

> **ES:** Implementa `Tracker`, `temporary_value`, `Suppress`, `read_lines` y
> `timer_log`. Ten en cuenta que `temporary_value` y `timer_log` necesitan el
> decorador `@contextmanager`. Ejecuta:

```
uv run pytest exercises/16_context_managers
```
