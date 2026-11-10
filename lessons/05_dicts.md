# Lesson 5: Dictionaries / Lección 5: Diccionarios

Goals: store and look up data by key, count and group things, and use `Counter` and `defaultdict`.

> **ES:** Objetivos: guardar y consultar datos por clave, contar y agrupar cosas, y usar `Counter` y `defaultdict`.

## Dict basics / Fundamentos de dict

A dict maps keys to values. Keys must be hashable (strings, numbers, tuples of those). Since Python 3.7 dicts remember insertion order.

> **ES:** Un dict asocia claves con valores. Las claves deben ser hashables (cadenas, números, tuplas de esos). Desde Python 3.7 los dicts recuerdan el orden de inserción.

```python
ages = {"ann": 31, "bo": 27}
ages["cy"] = 40  # add or overwrite
ages["ann"]  # 31
ages["zed"]  # KeyError
ages.get("zed")  # None
ages.get("zed", 0)  # 0
"bo" in ages  # True (checks keys)
del ages["bo"]
len(ages)
```

### Looping / Recorrer

```python
for name in ages:  # keys
    ...
for name, age in ages.items():  # key/value pairs
    print(f"{name} is {age}")
ages.keys(), ages.values()
```

### Comprehensions and merging / Comprensiones y combinación

```python
{n: n * n for n in range(4)}  # {0: 0, 1: 1, 2: 4, 3: 9}
{v: k for k, v in ages.items()}  # inverted
defaults = {"color": "red", "size": 1}
merged = defaults | {"size": 3}  # right side wins
```

## The counting pattern / El patrón de conteo

```python
counts: dict[str, int] = {}
for word in "a b a".split():
    counts[word] = counts.get(word, 0) + 1
```

This works, but the standard library does it for you.

> **ES:** Esto funciona, pero la biblioteca estándar lo hace por ti.

## `Counter`

```python
from collections import Counter

c = Counter("mississippi")
c["s"]  # 4
c["z"]  # 0 (missing keys count as zero, no KeyError)
c.most_common(2)  # [('i', 4), ('s', 4)]
c.update("ss")
c + Counter("m")  # add counts
```

`Counter` is a dict subclass. Wrap with `dict(c)` if you need a plain dict.

> **ES:** `Counter` es una subclase de dict. Envuélvelo con `dict(c)` si necesitas un dict normal.

## `defaultdict`

A dict that creates a missing value on first access, using the factory you give it:

> **ES:** Un dict que crea un valor faltante en el primer acceso, usando la fábrica (factory) que le indiques:

```python
from collections import defaultdict

by_first: defaultdict[str, list[str]] = defaultdict(list)
for word in ["apple", "avocado", "banana"]:
    by_first[word[0]].append(word)
# {'a': ['apple', 'avocado'], 'b': ['banana']}
```

Without it you'd write `by_first.setdefault(word[0], []).append(word)`, which also works on plain dicts.

> **ES:** Sin él escribirías `by_first.setdefault(word[0], []).append(word)`, que también funciona con dicts normales.

## Grouping / Agrupar

Grouping is "pick a key for each item, collect items under that key". Anagrams, for instance, share the same sorted letters:

> **ES:** Agrupar es "elegir una clave para cada elemento y reunir los elementos bajo esa clave". Los anagramas, por ejemplo, comparten las mismas letras ordenadas:

```python
"".join(sorted("listen")) == "".join(sorted("silent"))  # True
```

That sorted string makes a good dict key.

> **ES:** Esa cadena ordenada sirve como una buena clave de dict.

## Dicts as records / Dicts como registros

Small dicts often model records, e.g. `{"name": "Ada", "age": 36}`. Later lessons introduce dataclasses, which give you named, typed fields; for now just know that a dict is the flexible, quick option.

> **ES:** Los dicts pequeños suelen modelar registros, por ejemplo `{"name": "Ada", "age": 36}`. Lecciones posteriores presentan las dataclasses, que ofrecen campos con nombre y tipo; por ahora basta saber que un dict es la opción flexible y rápida.

## Common gotchas / Errores comunes

- `d[key]` raises `KeyError` for missing keys; use `.get()` when absence is normal.
- Don't change a dict's size while looping over it. Loop over `list(d)` if you must delete.
- Lists can't be keys (unhashable). Use a tuple.
- `{}` is an empty dict, not an empty set.
- `.get(key, [])` returns a throwaway list that is *not* stored in the dict; appending to it loses data. Use `setdefault` or `defaultdict`.
- Printing a `defaultdict` or `Counter` shows the class name; convert with `dict(...)` if you want plain output.

> **ES:**
> - `d[key]` lanza `KeyError` si la clave no existe; usa `.get()` cuando la ausencia es normal.
> - No cambies el tamaño de un dict mientras lo recorres. Recorre `list(d)` si necesitas borrar.
> - Las listas no pueden ser claves (no son hashables). Usa una tupla.
> - `{}` es un dict vacío, no un set vacío.
> - `.get(key, [])` devuelve una lista temporal que *no* se guarda en el dict; si le agregas elementos, pierdes datos. Usa `setdefault` o `defaultdict`.
> - Al imprimir un `defaultdict` o `Counter` se muestra el nombre de la clase; conviértelo con `dict(...)` si quieres una salida simple.

## Exercises / Ejercicios

Stubs are in `exercises/05_dicts/dicts.py`.

> **ES:** Los esqueletos (stubs) están en `exercises/05_dicts/dicts.py`.

1. `word_counts`
2. `invert`
3. `group_by_length`
4. `top_words` (`Counter.most_common`)
5. `merge_counts` (varargs of dicts)
6. `group_anagrams`

> **ES:**
> 1. `word_counts`
> 2. `invert`
> 3. `group_by_length`
> 4. `top_words` (`Counter.most_common`)
> 5. `merge_counts` (varargs de dicts)
> 6. `group_anagrams`

Run the tests:

> **ES:** Ejecuta las pruebas:

```sh
uv run pytest exercises/05_dicts
```

Reference solutions are in `solutions/05_dicts/`.

> **ES:** Las soluciones de referencia están en `solutions/05_dicts/`.
