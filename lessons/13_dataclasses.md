# Lesson 13: Dataclasses, Enums and NamedTuple

> **ES:** Lección 13: Dataclasses, Enums y NamedTuple

Goals: write data-holding classes without boilerplate, freeze them, give
fields safe defaults, model fixed choices with `Enum`, and know when a
`NamedTuple` fits.

> **ES:** Objetivos: escribir clases que guardan datos sin código repetitivo,
> congelarlas, darles a los campos valores por defecto seguros, modelar
> opciones fijas con `Enum`, y saber cuándo conviene un `NamedTuple`.

## `@dataclass`

> **ES:** ## `@dataclass`

In lesson 12 you wrote `__init__`, `__repr__` and `__eq__` by hand. A dataclass
generates them from annotated fields.

> **ES:** En la lección 12 escribiste `__init__`, `__repr__` y `__eq__` a mano.
> Una dataclass los genera a partir de los campos anotados.

```python
from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int = 100  # fields with defaults come last


b = Book("Dune", "Herbert")
print(b)  # Book(title='Dune', author='Herbert', pages=100)
print(b == Book("Dune", "Herbert"))  # True
```

## Mutable defaults need `field`

> **ES:** ## Los valores por defecto mutables necesitan `field`

```python
from dataclasses import dataclass, field


@dataclass
class Playlist:
    name: str
    songs: list[str] = field(default_factory=list)
```

Writing `songs: list[str] = []` raises an error, because one list would be
shared by every instance. `default_factory` calls `list()` per instance.

> **ES:** Escribir `songs: list[str] = []` lanza un error, porque una sola list
> sería compartida por todas las instancias. `default_factory` llama a `list()`
> por cada instancia.

## Frozen (immutable) dataclasses

> **ES:** ## Dataclasses frozen (inmutables)

```python
@dataclass(frozen=True)
class Point:
    x: float
    y: float


p = Point(1, 2)
p.x = 5  # FrozenInstanceError
```

Frozen instances are hashable, so they work in sets and as dict keys. To
"change" one use `dataclasses.replace(p, x=5)`.

> **ES:** Las instancias frozen son hashables, así que funcionan en sets y como
> claves de dict. Para "cambiar" una usa `dataclasses.replace(p, x=5)`.

## Validation with `__post_init__`

> **ES:** ## Validación con `__post_init__`

```python
@dataclass
class Rating:
    stars: int

    def __post_init__(self) -> None:
        if not 1 <= self.stars <= 5:
            raise ValueError(f"stars must be 1-5, got {self.stars}")
```

It runs right after the generated `__init__`.

> **ES:** Se ejecuta justo después del `__init__` generado.

## Enums

> **ES:** ## Enums

An `Enum` is a fixed set of named values.

> **ES:** Un `Enum` es un conjunto fijo de valores con nombre.

```python
from enum import Enum


class Color(Enum):
    RED = "red"
    GREEN = "green"


Color.RED  # <Color.RED: 'red'>
Color.RED.value  # 'red'
Color("green")  # lookup by value -> Color.GREEN
Color("pink")  # ValueError
```

Compare members with `is` (`color is Color.RED`). They also work well with
`match`:

> **ES:** Compara los miembros con `is` (`color is Color.RED`). También
> funcionan muy bien con `match`:

```python
match color:
    case Color.RED:
        print("stop")
    case Color.GREEN:
        print("go")
```

## NamedTuple

> **ES:** ## NamedTuple

A tuple whose positions have names. It is immutable and unpackable.

> **ES:** Una tuple cuyas posiciones tienen nombre. Es inmutable y se puede
> desempaquetar.

```python
from typing import NamedTuple


class Rect(NamedTuple):
    width: float
    height: float


r = Rect(2, 3)
w, h = r
print(r.width)
```

Choosing between them:

> **ES:** Cómo elegir entre ellos:

| Need                                  | Use                      |
|---------------------------------------|--------------------------|
| Mutable record, methods, validation   | `@dataclass`             |
| Immutable, hashable record            | `@dataclass(frozen=True)`|
| Lightweight, tuple-compatible record  | `NamedTuple`             |
| One of a fixed set of choices         | `Enum`                   |

> **ES:** Tabla: registro mutable, con métodos y validación: `@dataclass`;
> registro inmutable y hashable: `@dataclass(frozen=True)`; registro ligero y
> compatible con tuple: `NamedTuple`; una opción de un conjunto fijo: `Enum`.

## Gotchas

> **ES:** ## Trampas comunes

- Non-default fields cannot follow default fields.
- Dataclass annotations are not enforced at runtime; `Book(1, 2)` works. Use a
  type checker (`uv run ty check`) or `__post_init__`.
- `frozen=True` is shallow: a frozen dataclass holding a list can still have
  that list mutated.

> **ES:**
> - Los campos sin valor por defecto no pueden ir después de los que sí lo
>   tienen.
> - Las anotaciones de una dataclass no se verifican en tiempo de ejecución;
>   `Book(1, 2)` funciona. Usa un type checker (`uv run ty check`) o
>   `__post_init__`.
> - `frozen=True` es superficial: una dataclass frozen que contiene una list
>   todavía permite modificar esa list.

## Exercises

> **ES:** ## Ejercicios

Files:

- Stubs: `exercises/13_dataclasses/dataclasses_lesson.py`
- Tests: `exercises/13_dataclasses/test_dataclasses_lesson.py`

> **ES:** Archivos: los stubs y los tests indicados arriba.

The stubs are empty class shells: you add the fields. Run:

> **ES:** Los stubs son cascarones de clase vacíos: tú agregas los campos.
> Ejecuta:

```
uv run pytest exercises/13_dataclasses
```
