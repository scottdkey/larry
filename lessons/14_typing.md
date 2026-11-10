# Lesson 14: Typing

> **ES:** Lección 14: Tipado (typing)

Goals: annotate code usefully, write generics with Python 3.12+ syntax,
describe structural interfaces with `Protocol`, and type dicts and fixed
choices with `TypedDict` and `Literal`.

> **ES:** Objetivos: anotar el código de forma útil, escribir genéricos con la
> sintaxis de Python 3.12+, describir interfaces estructurales con `Protocol`,
> y tipar dicts y opciones fijas con `TypedDict` y `Literal`.

Type hints do not change how code runs. They are checked by tools:

> **ES:** Las anotaciones de tipo no cambian cómo se ejecuta el código. Las
> verifican herramientas externas:

```
uv run ty check path/to/file.py
```

## Basics

> **ES:** ## Conceptos básicos

```python
def greet(name: str, times: int = 1) -> str:
    return (f"hi {name} " * times).strip()


ids: list[int] = [1, 2]
lookup: dict[str, float] = {}
maybe: str | None = None  # "a str or None"
pair: tuple[int, str] = (1, "a")
```

Use built-in generics (`list[int]`) and `X | None`, not `typing.List` or
`Optional`. For callables use `collections.abc.Callable`:

> **ES:** Usa los genéricos integrados (`list[int]`) y `X | None`, no
> `typing.List` ni `Optional`. Para callables usa `collections.abc.Callable`:

```python
from collections.abc import Callable


def apply(f: Callable[[int], str], x: int) -> str:
    return f(x)
```

Checkers force you to handle `None`:

> **ES:** Los type checkers te obligan a manejar `None`:

```python
def first_or_none[T](items: list[T]) -> T | None:
    return items[0] if items else None


x = first_or_none([1, 2])
x + 1  # error: x may be None
if x is not None:
    x + 1  # fine, the type is narrowed to int
```

## Generics (PEP 695)

> **ES:** ## Genéricos (PEP 695)

`[T]` after a function or class name declares a type variable.

> **ES:** `[T]` después del nombre de una función o clase declara una variable
> de tipo.

```python
def first[T](items: list[T]) -> T:
    return items[0]


class Stack[T]:
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()


s: Stack[int] = Stack()
s.push(1)
s.push("a")  # checker error
```

Several variables work too: `def group_by[K, V](...)`. The `type` statement
makes aliases: `type Pair[T] = tuple[T, T]`.

> **ES:** También puedes usar varias variables: `def group_by[K, V](...)`. La
> sentencia `type` crea alias: `type Pair[T] = tuple[T, T]`.

## Protocol: structural typing

> **ES:** ## Protocol: tipado estructural

A `Protocol` describes what an object can do. Any class with matching methods
qualifies, with no inheritance needed ("duck typing", checked).

> **ES:** Un `Protocol` describe lo que un objeto puede hacer. Cualquier clase
> con métodos compatibles califica, sin necesidad de herencia ("duck typing",
> pero verificado).

```python
from typing import Protocol


class Speaker(Protocol):
    def speak(self) -> str: ...


class Cat:
    def speak(self) -> str:
        return "meow"


def chorus(speakers: list[Speaker]) -> str:
    return " & ".join(s.speak() for s in speakers)


chorus([Cat()])  # fine
```

## TypedDict

> **ES:** ## TypedDict

Describes the keys and value types of a plain `dict`, common for JSON data.

> **ES:** Describe las claves y los tipos de valor de un `dict` normal; es común
> para datos JSON.

```python
from typing import TypedDict


class User(TypedDict):
    name: str
    age: int


u: User = {"name": "Ada", "age": 36}
u["nmae"]  # checker error: unknown key
```

At runtime it is still just a `dict`.

> **ES:** En tiempo de ejecución sigue siendo simplemente un `dict`.

## Literal

> **ES:** ## Literal

Restrict a value to specific constants.

> **ES:** Restringe un valor a constantes específicas.

```python
from typing import Literal

type Direction = Literal["left", "right"]


def turn(d: Direction) -> None: ...


turn("up")  # checker error
```

## Gotchas

> **ES:** ## Trampas comunes

- Hints are not enforced at runtime. `greet(5)` still runs.
- `list[int]` is not accepted where `list[float]` is expected, since lists are
  mutable. Use `Sequence[float]` for read-only parameters.
- Don't reach for `Any`; it switches checking off.
- Use quotes (`"Vector"`) for a class referring to itself inside its own body,
  unless the name is already defined.

> **ES:**
> - Las anotaciones no se verifican en tiempo de ejecución. `greet(5)` igual se
>   ejecuta.
> - `list[int]` no se acepta donde se espera `list[float]`, porque las lists son
>   mutables. Usa `Sequence[float]` para parámetros de solo lectura.
> - No recurras a `Any`; desactiva la verificación.
> - Usa comillas (`"Vector"`) cuando una clase se refiere a sí misma dentro de
>   su propio cuerpo, a menos que el nombre ya esté definido.

## Exercises

> **ES:** ## Ejercicios

Files:

- Stubs: `exercises/14_typing/typing_lesson.py`
- Tests: `exercises/14_typing/test_typing_lesson.py`

> **ES:** Archivos: los stubs y los tests indicados arriba.

Your solution must also satisfy the type checker:

> **ES:** Tu solución también debe satisfacer al type checker:

```
uv run pytest exercises/14_typing
uv run ty check exercises/14_typing/typing_lesson.py
```
