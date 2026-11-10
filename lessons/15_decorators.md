# Lesson 15: Decorators

> **ES:** Lección 15: Decoradores (decorators)

Goals: treat functions as values, write decorators, preserve metadata with
`functools.wraps`, and write decorators that take arguments.

> **ES:** Objetivos: tratar las funciones como valores, escribir decoradores,
> conservar los metadatos con `functools.wraps`, y escribir decoradores que
> reciben argumentos.

## Functions are values

> **ES:** ## Las funciones son valores

You can pass functions around like any other object.

> **ES:** Puedes pasar funciones de un lado a otro como cualquier otro objeto.

```python
def apply_twice(func, value):
    return func(func(value))


apply_twice(lambda x: x * 2, 3)  # 12
```

Functions can also be defined inside functions and returned. The inner one
remembers the outer variables (a closure).

> **ES:** Las funciones también se pueden definir dentro de otras funciones y
> devolverse. La función interna recuerda las variables de la externa (un
> closure).

```python
def make_adder(n: int):
    def add(x: int) -> int:
        return x + n

    return add


add5 = make_adder(5)
add5(1)  # 6
```

## A decorator

> **ES:** ## Un decorador

A decorator takes a function and returns a replacement.

> **ES:** Un decorador recibe una función y devuelve un reemplazo.

```python
from functools import wraps


def shout(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper


@shout
def greet(name: str) -> str:
    """Say hi."""
    return f"hi {name}"


greet("bo")  # 'HI BO'
```

`@shout` above `def greet` is shorthand for `greet = shout(greet)`.

> **ES:** `@shout` encima de `def greet` es una forma abreviada de
> `greet = shout(greet)`.

`*args, **kwargs` lets the wrapper accept whatever the original accepts.

> **ES:** `*args, **kwargs` permite que el wrapper acepte lo mismo que acepta la
> función original.

## Why `@wraps`?

> **ES:** ## ¿Por qué `@wraps`?

Without it `greet.__name__` would be `"wrapper"` and the docstring lost, which
hurts debugging and tools. `@wraps(func)` copies the metadata over.

> **ES:** Sin él, `greet.__name__` sería `"wrapper"` y se perdería el docstring,
> lo que dificulta la depuración y perjudica a las herramientas.
> `@wraps(func)` copia los metadatos.

## Keeping state

> **ES:** ## Mantener estado

Because the wrapper is a function object, it can carry attributes, or you can
use a variable in the enclosing scope.

> **ES:** Como el wrapper es un objeto función, puede llevar atributos, o puedes
> usar una variable del ámbito externo.

```python
def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper
```

A `cache` dict in the outer function gives you memoization the same way.
(In real code use `functools.cache`.)

> **ES:** Un dict `cache` en la función externa te da memoización de la misma
> manera. (En código real usa `functools.cache`.)

## Decorators with arguments

> **ES:** ## Decoradores con argumentos

`@repeat(3)` means "call `repeat(3)`, and use what it returns as the
decorator". So you need one more layer: a factory returning the decorator.

> **ES:** `@repeat(3)` significa "llama a `repeat(3)` y usa lo que devuelva como
> decorador". Por eso necesitas una capa más: una fábrica que devuelve el
> decorador.

```python
def repeat(times: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(3)
def ping() -> None:
    print("ping")
```

## Typing decorators

> **ES:** ## Tipado de decoradores

With PEP 695 syntax a decorator that preserves the signature looks like:

> **ES:** Con la sintaxis de PEP 695, un decorador que conserva la firma se ve
> así:

```python
from collections.abc import Callable


def shout[**P](func: Callable[P, str]) -> Callable[P, str]: ...
```

`**P` captures the parameter list, and `P.args`/`P.kwargs` annotate
`*args`/`**kwargs` in the wrapper. Don't worry about the typing until the
untyped version makes sense.

> **ES:** `**P` captura la lista de parámetros, y `P.args`/`P.kwargs` anotan
> `*args`/`**kwargs` en el wrapper. No te preocupes por el tipado hasta que la
> versión sin tipos tenga sentido.

## Gotchas

> **ES:** ## Trampas comunes

- Forgetting `return wrapper` makes the decorated name `None`.
- Forgetting to return `func(...)`'s result swallows the return value.
- `@repeat` without parentheses passes the function as `times`; use `@repeat(3)`.
- Stacked decorators apply bottom-up: the one closest to `def` wraps first.
- Decorators run at definition time; the wrapper runs at call time.

> **ES:**
> - Olvidar `return wrapper` hace que el nombre decorado sea `None`.
> - Olvidar devolver el resultado de `func(...)` descarta el valor de retorno.
> - `@repeat` sin paréntesis pasa la función como `times`; usa `@repeat(3)`.
> - Los decoradores apilados se aplican de abajo hacia arriba: el más cercano a
>   `def` envuelve primero.
> - Los decoradores se ejecutan al momento de la definición; el wrapper se
>   ejecuta al momento de la llamada.

## Exercises

> **ES:** ## Ejercicios

Files:

- Stubs: `exercises/15_decorators/decorators.py`
- Tests: `exercises/15_decorators/test_decorators.py`

> **ES:** Archivos: los stubs y los tests indicados arriba.

Implement `apply_twice`, `shout`, `count_calls`, `repeat`, `memoize` and
`retry`. Run:

> **ES:** Implementa `apply_twice`, `shout`, `count_calls`, `repeat`, `memoize`
> y `retry`. Ejecuta:

```
uv run pytest exercises/15_decorators
```
