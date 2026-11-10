# Lesson 4: Sequences / Lección 4: Secuencias

Goals: work with lists, tuples, and sets; slice; sort; and know which to pick.

> **ES:** Objetivos: trabajar con listas, tuplas y sets (conjuntos); hacer slicing; ordenar; y saber cuál elegir.

## Lists / Listas

An ordered, changeable collection.

> **ES:** Una colección ordenada y modificable.

```python
nums = [3, 1, 2]
nums.append(4)  # [3, 1, 2, 4]
nums.insert(0, 9)  # [9, 3, 1, 2, 4]
nums.extend([7, 8])
last = nums.pop()  # removes and returns 8
nums.remove(9)  # removes first 9
len(nums), 3 in nums
```

### Slicing / Slicing (cortes)

Same rules as strings (lesson 3), and a slice is always a **new list**:

> **ES:** Mismas reglas que con las cadenas (lección 3), y un slice siempre es una **lista nueva**:

```python
items = [10, 20, 30, 40, 50]
items[1:3]  # [20, 30]
items[-2:]  # [40, 50]
items[::-1]  # reversed copy
items[:]  # shallow copy
```

You can also assign to a slice: `items[1:3] = [0]`.

> **ES:** También puedes asignar a un slice: `items[1:3] = [0]`.

### Comprehensions / Comprensiones

```python
squares = [n * n for n in range(5)]  # [0, 1, 4, 9, 16]
evens = [n for n in range(10) if n % 2 == 0]
```

Keep them short. If it needs more than one `if` or nested loop, use a regular loop.

> **ES:** Mantenlas cortas. Si necesitas más de un `if` o un bucle anidado, usa un bucle normal.

## Tuples / Tuplas

Like lists, but immutable. Use them for small, fixed-shape records and for returning several values:

> **ES:** Como las listas, pero inmutables. Úsalas para registros pequeños de forma fija y para devolver varios valores:

```python
point = (3, 4)
x, y = point  # unpacking


def bounds(xs: list[int]) -> tuple[int, int]:
    return min(xs), max(xs)


lo, hi = bounds([5, 2, 9])
```

A one-element tuple needs a trailing comma: `(1,)`.

> **ES:** Una tupla de un solo elemento necesita una coma al final: `(1,)`.

Star-unpacking grabs the rest: `first, *rest = [1, 2, 3]` gives `rest == [2, 3]`.

> **ES:** El desempaquetado con asterisco toma el resto: `first, *rest = [1, 2, 3]` da `rest == [2, 3]`.

## Sets / Conjuntos (sets)

Unordered, no duplicates, very fast membership tests. Items must be hashable (numbers, strings, tuples; not lists).

> **ES:** Sin orden, sin duplicados y con pruebas de pertenencia muy rápidas. Los elementos deben ser hashables (números, cadenas, tuplas; no listas).

```python
a = {1, 2, 3}
b = {3, 4}
a | b  # union {1, 2, 3, 4}
a & b  # intersection {3}
a - b  # difference {1, 2}
a ^ b  # symmetric difference {1, 2, 4}
set()  # empty set; {} is an empty dict!
```

Removing duplicates with `set(items)` loses the original order. To keep it, track what you've `seen` while looping.

> **ES:** Eliminar duplicados con `set(items)` pierde el orden original. Para conservarlo, lleva registro de lo que ya viste (`seen`) mientras recorres.

## Sorting / Ordenamiento

- `sorted(iterable)` returns a **new** list.
- `list.sort()` sorts **in place** and returns `None`.

> **ES:**
> - `sorted(iterable)` devuelve una lista **nueva**.
> - `list.sort()` ordena **en su lugar** y devuelve `None`.

```python
words = ["pear", "Fig", "apple"]
sorted(words)  # ['Fig', 'apple', 'pear']  (uppercase first)
sorted(words, key=str.lower)  # ['apple', 'Fig', 'pear']
sorted(words, key=len, reverse=True)
```

`key` is a function applied to each item to get its sort value. To sort by several criteria, return a tuple:

> **ES:** `key` es una función que se aplica a cada elemento para obtener su valor de orden. Para ordenar por varios criterios, devuelve una tupla:

```python
sorted(words, key=lambda w: (len(w), w.lower()))
```

Python's sort is stable: items that compare equal keep their original order.

> **ES:** El ordenamiento de Python es estable: los elementos que comparan igual conservan su orden original.

## Which one? / ¿Cuál usar?

| Need | Use |
|---|---|
| ordered, changing collection | `list` |
| fixed record, dict keys | `tuple` |
| uniqueness, membership, set math | `set` |

> **ES:**
> | Necesidad | Usa |
> |---|---|
> | colección ordenada que cambia | `list` |
> | registro fijo, claves de dict | `tuple` |
> | unicidad, pertenencia, operaciones de conjuntos | `set` |

## Common gotchas / Errores comunes

- `b = a` does **not** copy a list; both names point to the same list. Use `a.copy()` or `a[:]`.
- `x = my_list.sort()` sets `x` to `None`.
- `[[0] * 3] * 3` makes three references to the *same* inner list. Use `[[0] * 3 for _ in range(3)]`.
- Sets have no index: `my_set[0]` fails, and iteration order isn't something to rely on.
- `list.remove` raises `ValueError` if the item is missing.
- Modifying a list while iterating it skips items.

> **ES:**
> - `b = a` **no** copia una lista; ambos nombres apuntan a la misma lista. Usa `a.copy()` o `a[:]`.
> - `x = my_list.sort()` deja `x` en `None`.
> - `[[0] * 3] * 3` crea tres referencias a la *misma* lista interna. Usa `[[0] * 3 for _ in range(3)]`.
> - Los sets no tienen índice: `my_set[0]` falla, y no conviene confiar en el orden de iteración.
> - `list.remove` lanza `ValueError` si el elemento no está.
> - Modificar una lista mientras la recorres hace que se salten elementos.

## Exercises / Ejercicios

Stubs are in `exercises/04_sequences/sequences.py`.

> **ES:** Los esqueletos (stubs) están en `exercises/04_sequences/sequences.py`.

1. `dedupe` (keep order)
2. `rotate` (slicing and `%`)
3. `chunks`
4. `min_max` (tuples, raising errors)
5. `shared_sorted` (set operations)
6. `sort_words` (sort keys)

> **ES:**
> 1. `dedupe` (conserva el orden)
> 2. `rotate` (slicing y `%`)
> 3. `chunks`
> 4. `min_max` (tuplas, lanzar errores)
> 5. `shared_sorted` (operaciones de conjuntos)
> 6. `sort_words` (claves de orden)

Run the tests:

> **ES:** Ejecuta las pruebas:

```sh
uv run pytest exercises/04_sequences
```

Reference solutions are in `solutions/04_sequences/`.

> **ES:** Las soluciones de referencia están en `solutions/04_sequences/`.
