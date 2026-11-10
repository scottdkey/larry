# Lesson 8: Generators and Iterators / Lección 8: Generadores e iteradores

Goals: write functions with `yield`, build lazy pipelines, and understand the
iterator protocol that powers every `for` loop.

> **ES:** Objetivos: escribir funciones con `yield`, construir pipelines
> perezosos (lazy) y entender el protocolo de iteradores que impulsa cada
> bucle `for`.

## yield

A function containing `yield` is a *generator function*. Calling it runs
nothing yet; it returns a generator that runs on demand:

> **ES:** Una función que contiene `yield` es una *función generadora*. Al
> llamarla todavía no se ejecuta nada; devuelve un generador que corre bajo
> demanda:

```python
def countdown(n: int):
    while n > 0:
        yield n
        n -= 1


gen = countdown(3)
next(gen)  # 3  (runs until the first yield, then pauses)
next(gen)  # 2
list(gen)  # [1]  (the rest)
next(gen)  # raises StopIteration
```

Local variables survive between pauses, which makes generators a neat way to
keep state without writing a class.

> **ES:** Las variables locales se conservan entre pausas, lo que hace de los
> generadores una forma práctica de mantener estado sin escribir una clase.

## Laziness and memory / Pereza (laziness) y memoria

```python
def squares(nums):
    for n in nums:
        yield n * n
```

`squares(range(10**12))` is instant; values are produced one at a time as the
consumer asks. That is why generators can be *infinite*:

> **ES:** `squares(range(10**12))` es instantáneo; los valores se producen uno
> a la vez según los pide el consumidor. Por eso los generadores pueden ser
> *infinitos*:

```python
def naturals():
    n = 0
    while True:
        yield n
        n += 1
```

Take a slice of an endless stream with `itertools.islice`:

> **ES:** Toma una porción de un flujo interminable con `itertools.islice`:

```python
from itertools import islice

list(islice(naturals(), 5))  # [0, 1, 2, 3, 4]
```

## Pipelines

Chain generators so each item flows through every stage before the next one is
read. Nothing is ever fully loaded:

> **ES:** Encadena generadores para que cada elemento pase por todas las
> etapas antes de leer el siguiente. Nunca se carga todo por completo:

```python
def non_blank(lines):
    return (line.strip() for line in lines if line.strip())


def shout(lines):
    for line in lines:
        yield line.upper()


for line in shout(non_blank(open("big.log"))):
    print(line)
```

## The iterator protocol / El protocolo de iteradores

`for x in thing` does this behind the scenes:

1. call `iter(thing)` to get an *iterator*;
2. call `next()` on it repeatedly;
3. stop when it raises `StopIteration`.

> **ES:** `for x in thing` hace esto entre bambalinas:
>
> 1. llama a `iter(thing)` para obtener un *iterador*;
> 2. llama a `next()` repetidamente;
> 3. se detiene cuando lanza `StopIteration`.

An *iterable* has `__iter__`; an *iterator* also has `__next__`, and its
`__iter__` returns itself.

> **ES:** Un *iterable* tiene `__iter__`; un *iterador* además tiene
> `__next__`, y su `__iter__` se devuelve a sí mismo.

```python
class Countdown:
    def __init__(self, n: int) -> None:
        self.n = n

    def __iter__(self) -> "Countdown":
        return self

    def __next__(self) -> int:
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return self.n + 1
```

Generators implement all of that for you; write a class only when you need
extra behaviour.

> **ES:** Los generadores implementan todo eso por ti; escribe una clase solo
> cuando necesites comportamiento extra.

## yield from

Delegate to another iterable:

> **ES:** Delega en otro iterable:

```python
def both(a, b):
    yield from a
    yield from b
```

## Gotchas / Trampas comunes

- A generator is single-use. Iterating it a second time yields nothing.
- `return value` inside a generator ends it; it does not hand back a value to
  the loop.
- Errors inside a generator appear when it is *consumed*, not when you call
  the function.
- `len()` and indexing do not work on generators; convert with `list()` if
  you really need them (and the stream is finite!).
- `list(infinite_generator())` never finishes. Use `islice` first.

> **ES:**
> - Un generador es de un solo uso. Iterarlo por segunda vez no produce nada.
> - `return value` dentro de un generador lo termina; no le devuelve un valor
>   al bucle.
> - Los errores dentro de un generador aparecen cuando se *consume*, no cuando
>   llamas a la función.
> - `len()` y la indexación no funcionan con generadores; convierte con
>   `list()` si de verdad los necesitas (¡y el flujo es finito!).
> - `list(infinite_generator())` nunca termina. Usa `islice` primero.

## Exercises / Ejercicios

Stubs live in `exercises/08_generators/generators.py`; tests are in
`test_generators.py`. Several tests check that your code is lazy, so do not
build a list in the generator functions.

> **ES:** Los stubs están en `exercises/08_generators/generators.py`; las
> pruebas están en `test_generators.py`. Varias pruebas verifican que tu código
> sea perezoso (lazy), así que no construyas una lista en las funciones
> generadoras.

```
uv run pytest exercises/08_generators
```
