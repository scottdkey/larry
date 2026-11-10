# Lesson 2: Control Flow / Lección 2: Control de flujo

Goals: make decisions with `if` and `match`, repeat work with `for` and `while`, and generate numbers with `range`.

> **ES:** Objetivos: tomar decisiones con `if` y `match`, repetir trabajo con `for` y `while`, y generar números con `range`.

## Making decisions with `if` / Tomar decisiones con `if`

```python
temperature = 31

if temperature > 30:
    print("hot")
elif temperature > 15:
    print("nice")
else:
    print("cold")
```

Python uses indentation (4 spaces) instead of braces. The colon `:` starts a block.

> **ES:** Python usa indentación (4 espacios) en lugar de llaves. Los dos puntos `:` inician un bloque.

Conditions don't have to be booleans. These are "falsy": `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `None`, `False`. Almost everything else is truthy:

> **ES:** Las condiciones no tienen que ser booleanos. Estos valores son "falsy" (se evalúan como falso): `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `None`, `False`. Casi todo lo demás es "truthy" (se evalúa como verdadero):

```python
name = ""
if not name:
    print("no name given")
```

Combine conditions with `and`, `or`, `not`, and chain comparisons: `0 <= x < 10`.

> **ES:** Combina condiciones con `and`, `or`, `not`, y encadena comparaciones: `0 <= x < 10`.

A one-line conditional expression:

> **ES:** Una expresión condicional en una sola línea:

```python
label = "even" if n % 2 == 0 else "odd"
```

## Pattern matching with `match` / Coincidencia de patrones con `match`

`match` compares a value against several patterns. It is more than a switch statement: it can take apart tuples, lists, and more.

> **ES:** `match` compara un valor contra varios patrones. Es más que un `switch`: puede descomponer tuplas, listas y más.

```python
def describe(command: str) -> str:
    match command.split():
        case ["quit"]:
            return "bye"
        case ["go", direction]:
            return f"going {direction}"
        case ["take", *items]:
            return f"taking {len(items)} item(s)"
        case _:
            return "huh?"
```

- `_` is the catch-all.
- A name in a pattern (like `direction`) *captures* that part.
- Add a guard with `if`: `case n if n < 0:`.
- Combine alternatives with `|`: `case "y" | "yes":`.

> **ES:**
> - `_` es el comodín que captura todo lo demás.
> - Un nombre dentro de un patrón (como `direction`) *captura* esa parte.
> - Agrega una guarda con `if`: `case n if n < 0:`.
> - Combina alternativas con `|`: `case "y" | "yes":`.

Use plain `if`/`elif` for simple comparisons; use `match` when the *shape* of the data matters.

> **ES:** Usa `if`/`elif` simples para comparaciones sencillas; usa `match` cuando importa la *forma* de los datos.

## `for` loops / Bucles `for`

A `for` loop walks over anything iterable (lists, strings, dicts, files...):

> **ES:** Un bucle `for` recorre cualquier iterable (listas, cadenas, dicts, archivos...):

```python
for letter in "abc":
    print(letter)
```

Need the position too? Use `enumerate`:

> **ES:** ¿Necesitas también la posición? Usa `enumerate`:

```python
for i, letter in enumerate("abc"):
    print(i, letter)  # 0 a, 1 b, 2 c
```

Walk two sequences together with `zip`:

> **ES:** Recorre dos secuencias a la vez con `zip`:

```python
for name, score in zip(["Ann", "Bo"], [90, 85]):
    print(f"{name}: {score}")
```

## `range`

`range(stop)`, `range(start, stop)`, `range(start, stop, step)`. The stop value is **excluded**.

> **ES:** `range(stop)`, `range(start, stop)`, `range(start, stop, step)`. El valor `stop` está **excluido**.

```python
list(range(5))  # [0, 1, 2, 3, 4]
list(range(2, 6))  # [2, 3, 4, 5]
list(range(10, 0, -3))  # [10, 7, 4, 1]
```

## `while` loops / Bucles `while`

Use `while` when you don't know in advance how many times to loop:

> **ES:** Usa `while` cuando no sabes de antemano cuántas veces vas a repetir:

```python
n = 27
steps = 0
while n != 1:
    n = n // 2 if n % 2 == 0 else 3 * n + 1
    steps += 1
```

Make sure something inside the loop eventually makes the condition false, or it runs forever (Ctrl+C stops it).

> **ES:** Asegúrate de que algo dentro del bucle haga falsa la condición en algún momento, o se ejecutará para siempre (Ctrl+C lo detiene).

## `break`, `continue`, and loop `else` / `break`, `continue` y el `else` de un bucle

- `break` leaves the loop immediately.
- `continue` skips to the next iteration.
- `else` on a loop runs only if the loop finished *without* `break`.

> **ES:**
> - `break` sale del bucle de inmediato.
> - `continue` salta a la siguiente iteración.
> - `else` en un bucle se ejecuta solo si el bucle terminó *sin* `break`.

```python
for n in range(2, 10):
    if n % 7 == 0:
        print("found a multiple of 7")
        break
else:
    print("none found")
```

The loop `else` is handy for "search, and do something if not found", like testing for primes.

> **ES:** El `else` de un bucle es útil para "buscar, y hacer algo si no se encuentra", como al comprobar números primos.

## Early returns / Retornos anticipados

Inside a function, `return` exits straight away, even from inside nested loops. That is often cleaner than a flag variable:

> **ES:** Dentro de una función, `return` sale de inmediato, incluso desde bucles anidados. Esto suele ser más limpio que usar una variable bandera:

```python
def first_negative(numbers: list[int]) -> int | None:
    for n in numbers:
        if n < 0:
            return n
    return None
```

## Common gotchas / Errores comunes

- `=` assigns, `==` compares. `if x = 3:` is a syntax error.
- `range(5)` stops at 4, not 5.
- Don't add to or remove from a list while looping over it; build a new list instead.
- Compare with `None` using `is None`, not `== None`.
- `elif` chains stop at the first match, so order matters: check `n % 15` before `n % 3` in FizzBuzz.

> **ES:**
> - `=` asigna, `==` compara. `if x = 3:` es un error de sintaxis.
> - `range(5)` se detiene en 4, no en 5.
> - No agregues ni quites elementos de una lista mientras la recorres; construye una lista nueva.
> - Compara con `None` usando `is None`, no `== None`.
> - Las secuencias de `elif` se detienen en la primera coincidencia, así que el orden importa: revisa `n % 15` antes que `n % 3` en FizzBuzz.

## Exercises / Ejercicios

Stubs are in `exercises/02_control_flow/control_flow.py`. Replace each `raise NotImplementedError` with a real body.

> **ES:** Los esqueletos (stubs) están en `exercises/02_control_flow/control_flow.py`. Reemplaza cada `raise NotImplementedError` por un cuerpo real.

1. `fizzbuzz`
2. `http_class` (practice `match`)
3. `sum_of_evens` (practice `range` with a step)
4. `primes_below` (loop `else` or early exit)
5. `collatz_steps` (a `while` loop)
6. `find_pair` (nested loops, early return)

> **ES:**
> 1. `fizzbuzz`
> 2. `http_class` (practica `match`)
> 3. `sum_of_evens` (practica `range` con un paso)
> 4. `primes_below` (`else` de bucle o salida anticipada)
> 5. `collatz_steps` (un bucle `while`)
> 6. `find_pair` (bucles anidados, retorno anticipado)

Run the tests:

> **ES:** Ejecuta las pruebas:

```sh
uv run pytest exercises/02_control_flow
```

They fail at first, because the stubs raise `NotImplementedError`. Your goal is green. A reference solution lives in `solutions/02_control_flow/`; peek only after trying.

> **ES:** Al principio fallan, porque los stubs lanzan `NotImplementedError`. Tu meta es que pasen (verde). Hay una solución de referencia en `solutions/02_control_flow/`; mírala solo después de intentarlo.
