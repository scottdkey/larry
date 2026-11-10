# Lesson 6: Functions / Lección 6: Funciones

Goals: write flexible functions with defaults, `*args`, `**kwargs`, and keyword-only parameters; understand closures; use `lambda`.

> **ES:** Objetivos: escribir funciones flexibles con valores por defecto, `*args`, `**kwargs` y parámetros solo por nombre (keyword-only); entender los closures (clausuras); usar `lambda`.

## Anatomy / Anatomía

```python
def greet(name: str, punctuation: str = "!") -> str:
    """Return a greeting."""
    return f"Hello, {name}{punctuation}"


greet("Ada")  # 'Hello, Ada!'
greet("Ada", punctuation="?")  # keyword argument
```

A function without `return` returns `None`. Type hints document intent and are checked by `uv run ty check`.

> **ES:** Una función sin `return` devuelve `None`. Las anotaciones de tipo (type hints) documentan la intención y las verifica `uv run ty check`.

## Default values, and the big gotcha / Valores por defecto y el gran error común

Defaults are evaluated **once**, when the function is defined, not on each call. A mutable default is shared between calls:

> **ES:** Los valores por defecto se evalúan **una sola vez**, cuando se define la función, no en cada llamada. Un valor por defecto mutable se comparte entre llamadas:

```python
def add(item, items=[]):  # BUG
    items.append(item)
    return items


add(1)  # [1]
add(2)  # [1, 2]  surprise!
```

The fix is `None` as a sentinel:

> **ES:** La solución es usar `None` como valor centinela:

```python
def add(item: int, items: list[int] | None = None) -> list[int]:
    if items is None:
        items = []
    items.append(item)
    return items
```

## `*args` and `**kwargs` / `*args` y `**kwargs`

`*args` collects extra positional arguments into a tuple; `**kwargs` collects extra keyword arguments into a dict.

> **ES:** `*args` reúne los argumentos posicionales extra en una tupla; `**kwargs` reúne los argumentos por nombre extra en un dict.

```python
def total(*numbers: int) -> int:
    return sum(numbers)


def show(**options: str) -> None:
    for key, value in options.items():
        print(f"{key}={value}")


total(1, 2, 3)
show(color="red", size="L")
```

The same symbols unpack at call time:

> **ES:** Los mismos símbolos desempaquetan al momento de llamar:

```python
nums = [1, 2, 3]
total(*nums)
show(**{"color": "red"})
```

## Keyword-only and positional-only / Solo por nombre y solo posicional

Parameters after `*` (or after `*args`) can only be passed by keyword. Parameters before `/` can only be passed by position.

> **ES:** Los parámetros después de `*` (o después de `*args`) solo se pueden pasar por nombre. Los parámetros antes de `/` solo se pueden pasar por posición.

```python
def join(*words: str, sep: str = " ") -> str:
    return sep.join(words)


join("a", "b", sep="-")  # fine
join("a", "b", "-")  # "-" is just another word


def describe(name, /, **attrs): ...  # attrs may contain a key called "name"
```

Keyword-only is a good habit for flags such as `reverse=True`; call sites read clearly.

> **ES:** Usar parámetros solo por nombre es un buen hábito para banderas como `reverse=True`; así las llamadas se leen con claridad.

## Functions are values / Las funciones son valores

You can pass functions around, store them, and return them:

> **ES:** Puedes pasar funciones como argumentos, guardarlas y devolverlas:

```python
from collections.abc import Callable


def apply_twice(f: Callable[[int], int], x: int) -> int:
    return f(f(x))


apply_twice(abs, -3)
```

## Closures / Closures (clausuras)

A function defined inside another can use the outer function's variables, even after the outer function has returned:

> **ES:** Una función definida dentro de otra puede usar las variables de la función exterior, incluso después de que esta haya terminado:

```python
def make_multiplier(factor: int):
    def multiply(x: int) -> int:
        return x * factor

    return multiply


triple = make_multiplier(3)
triple(5)  # 15
```

To *rebind* an outer variable (not just read it), declare it `nonlocal`:

> **ES:** Para *reasignar* una variable exterior (no solo leerla), decláralo `nonlocal`:

```python
def make_counter():
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter
```

Each call to `make_counter()` gets its own `count`.

> **ES:** Cada llamada a `make_counter()` obtiene su propio `count`.

## `lambda`

A tiny anonymous function limited to one expression:

> **ES:** Una pequeña función anónima limitada a una sola expresión:

```python
double = lambda x: x * 2  # works, but prefer def for named functions
sorted(words, key=lambda w: len(w))
```

Use lambda for short throwaway callbacks like sort keys. If you give it a name, use `def`.

> **ES:** Usa lambda para callbacks cortos y desechables, como las claves de orden. Si le vas a poner un nombre, usa `def`.

## Docstrings

The first string in a function is its docstring; `help(func)` shows it. One clear sentence is usually enough.

> **ES:** La primera cadena de una función es su docstring; `help(func)` la muestra. Normalmente basta con una frase clara.

## Common gotchas / Errores comunes

- Mutable default arguments (above).
- Forgetting `return` yields `None`.
- Assigning to a variable inside a function makes it local; reading an outer one is fine, rebinding needs `nonlocal` (or `global`, which you should avoid).
- Closures capture variables, not values: `[lambda: i for i in range(3)]` all return `2`. Bind with a default: `lambda i=i: i`.
- Mutating an argument (like `list.sort()`) changes the caller's data. Say so in the docstring, or copy.
- `list.sort()` returns `None`; don't `return items.sort()`.

> **ES:**
> - Argumentos por defecto mutables (arriba).
> - Olvidar `return` produce `None`.
> - Asignar a una variable dentro de una función la vuelve local; leer una exterior está bien, reasignarla requiere `nonlocal` (o `global`, que conviene evitar).
> - Los closures capturan variables, no valores: `[lambda: i for i in range(3)]` devuelve `2` en todos. Enlaza con un valor por defecto: `lambda i=i: i`.
> - Mutar un argumento (como con `list.sort()`) cambia los datos de quien llama. Indícalo en el docstring, o haz una copia.
> - `list.sort()` devuelve `None`; no escribas `return items.sort()`.

## Exercises / Ejercicios

Stubs are in `exercises/06_functions/functions.py`.

> **ES:** Los esqueletos (stubs) están en `exercises/06_functions/functions.py`.

1. `add_item` (the defaults gotcha)
2. `join_words` (`*args`, keyword-only)
3. `describe` (positional-only, `**kwargs`)
4. `make_multiplier` (closure)
5. `make_counter` (`nonlocal`)
6. `compose` (functions as values)
7. `sort_people` (lambda as sort key)

> **ES:**
> 1. `add_item` (el error de los valores por defecto)
> 2. `join_words` (`*args`, solo por nombre)
> 3. `describe` (solo posicional, `**kwargs`)
> 4. `make_multiplier` (closure)
> 5. `make_counter` (`nonlocal`)
> 6. `compose` (funciones como valores)
> 7. `sort_people` (lambda como clave de orden)

Run the tests:

> **ES:** Ejecuta las pruebas:

```sh
uv run pytest exercises/06_functions
```

Reference solutions are in `solutions/06_functions/`.

> **ES:** Las soluciones de referencia están en `solutions/06_functions/`.
