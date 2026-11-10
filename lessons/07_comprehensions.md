# Lesson 7: Comprehensions / Lección 7: Comprensiones

Goals: build lists, dicts and sets in one readable expression; use generator
expressions for lazy work; meet `itertools`.

> **ES:** Objetivos: construir listas, dicts y sets en una sola expresión
> legible; usar expresiones generadoras para trabajo perezoso (lazy); conocer
> `itertools`.

## List comprehensions / Comprensiones de listas

A loop that builds a list:

> **ES:** Un bucle que construye una lista:

```python
squares = []
for n in range(5):
    squares.append(n * n)
```

The same thing as a comprehension:

> **ES:** Lo mismo como comprensión:

```python
squares = [n * n for n in range(5)]  # [0, 1, 4, 9, 16]
```

Read it as: "give me `n * n` for each `n` in `range(5)`".

> **ES:** Léela así: "dame `n * n` por cada `n` en `range(5)`".

Add a filter with `if` at the end:

> **ES:** Agrega un filtro con `if` al final:

```python
evens = [n for n in range(10) if n % 2 == 0]  # [0, 2, 4, 6, 8]
```

Use a conditional *expression* (`a if cond else b`) at the front to transform
instead of filter:

> **ES:** Usa una *expresión* condicional (`a if cond else b`) al principio
> para transformar en lugar de filtrar:

```python
labels = ["even" if n % 2 == 0 else "odd" for n in range(3)]
```

## Nested loops / Bucles anidados

Loops read left to right, in the same order you would write them as statements:

> **ES:** Los bucles se leen de izquierda a derecha, en el mismo orden en que
> los escribirías como sentencias:

```python
matrix = [[1, 2], [3, 4]]
flat = [x for row in matrix for x in row]  # [1, 2, 3, 4]
```

## Dict and set comprehensions / Comprensiones de dict y set

```python
words = ["apple", "fig", "kiwi"]
lengths = {w: len(w) for w in words}  # {"apple": 5, "fig": 3, "kiwi": 4}
initials = {w[0] for w in words}  # {"a", "f", "k"}
swapped = {v: k for k, v in lengths.items()}
```

A set comprehension uses `{x for ...}`; a dict one has `key: value`. An empty
`{}` is a dict, so use `set()` for an empty set.

> **ES:** Una comprensión de set usa `{x for ...}`; la de dict lleva
> `key: value`. Un `{}` vacío es un dict, así que usa `set()` para un set
> vacío.

## Generator expressions / Expresiones generadoras

Swap the square brackets for parentheses and nothing is computed until you ask:

> **ES:** Cambia los corchetes por paréntesis y nada se calcula hasta que lo
> pidas:

```python
total = sum(n * n for n in range(1_000_000))  # no million-item list in memory
```

When a generator expression is the only argument, the extra parentheses can go.
Use it with `sum`, `max`, `any`, `all`, `"".join(...)` and friends.

> **ES:** Cuando una expresión generadora es el único argumento, se pueden
> omitir los paréntesis extra. Úsala con `sum`, `max`, `any`, `all`,
> `"".join(...)` y similares.

```python
any(w.startswith("k") for w in words)  # stops at the first match
```

A generator can only be consumed once:

> **ES:** Un generador solo se puede consumir una vez:

```python
gen = (n for n in range(3))
list(gen)  # [0, 1, 2]
list(gen)  # []  (already used up)
```

## itertools basics / Fundamentos de itertools

The standard `itertools` module has fast building blocks:

> **ES:** El módulo estándar `itertools` ofrece bloques de construcción
> rápidos:

```python
from itertools import batched, chain, combinations, count, islice

list(combinations("abc", 2))  # [("a","b"), ("a","c"), ("b","c")]
list(batched(range(5), 2))  # [(0, 1), (2, 3), (4,)]   (3.12+)
list(chain([1, 2], [3]))  # [1, 2, 3]
list(islice(count(10), 3))  # [10, 11, 12]  count() never ends
```

## Gotchas / Trampas comunes

- Keep them short. If a comprehension needs two `if`s and a nested loop, a
  plain `for` loop is kinder to the next reader.
- Do not use a comprehension just for side effects (`[print(x) for x in xs]`);
  write a loop.
- The loop variable does not leak out of a comprehension (unlike a `for` loop).
- A list in `[...]` is built fully and immediately; use `(...)` when you only
  need to iterate once.
- Avoid `[[0] * 3] * 3`; the rows are the same list. Use
  `[[0] * 3 for _ in range(3)]`.

> **ES:**
> - Mantenlas cortas. Si una comprensión necesita dos `if` y un bucle
>   anidado, un `for` normal es más amable con el próximo lector.
> - No uses una comprensión solo por sus efectos secundarios
>   (`[print(x) for x in xs]`); escribe un bucle.
> - La variable del bucle no se "escapa" de la comprensión (a diferencia de un
>   bucle `for`).
> - Una lista en `[...]` se construye completa e inmediatamente; usa `(...)`
>   cuando solo necesites iterar una vez.
> - Evita `[[0] * 3] * 3`; las filas son la misma lista. Usa
>   `[[0] * 3 for _ in range(3)]`.

## Exercises / Ejercicios

Stubs live in `exercises/07_comprehensions/comprehensions.py`. Replace each
`raise NotImplementedError` and read the docstrings for the exact behaviour.
Tests are in `test_comprehensions.py`.

> **ES:** Los stubs están en `exercises/07_comprehensions/comprehensions.py`.
> Reemplaza cada `raise NotImplementedError` y lee los docstrings para ver el
> comportamiento exacto. Las pruebas están en `test_comprehensions.py`.

```
uv run pytest exercises/07_comprehensions
```

Stuck? A finished version is in `solutions/07_comprehensions/`; try first.

> **ES:** ¿Atascado? Hay una versión terminada en
> `solutions/07_comprehensions/`; intenta primero por tu cuenta.
