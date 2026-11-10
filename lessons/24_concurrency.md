# Lesson 24: Threads, processes, and async / Lección 24: Hilos, procesos y async

## Goals / Objetivos

- Choose between threads, processes and async for a given problem.
- Understand the GIL in plain terms.
- Use `concurrent.futures` and protect shared state with a lock.

> **ES:**
> - Elige entre hilos (threads), procesos y async para un problema dado.
> - Entiende el GIL en términos sencillos.
> - Usa `concurrent.futures` y protege el estado compartido con un lock.

## Two kinds of slow / Dos tipos de lentitud

1. **I/O-bound**: mostly waiting (network, disk, database).
2. **CPU-bound**: mostly computing (math, image processing, parsing big data).

> **ES:**
> 1. **Limitado por I/O** (I/O-bound): casi todo es espera (red, disco, base de datos).
> 2. **Limitado por CPU** (CPU-bound): casi todo es cómputo (matemáticas, procesamiento de imágenes, análisis de datos grandes).

The right tool depends on which one you have. Measure first: if adding CPU
makes it faster, it is CPU-bound.

> **ES:** La herramienta correcta depende de cuál tengas. Mide primero: si agregar CPU lo hace más rápido, es CPU-bound.

## The GIL, plainly / El GIL, en palabras simples

CPython has a **Global Interpreter Lock**: only one thread runs Python bytecode
at a time. Think of one kitchen with one stove and many cooks; only one cook can
use the stove at once.

> **ES:** CPython tiene un **Global Interpreter Lock** (GIL): solo un hilo ejecuta bytecode de Python a la vez. Piensa en una cocina con una sola estufa y muchos cocineros; solo un cocinero puede usar la estufa a la vez.

- But a thread that is *waiting* (on a socket, a file, `time.sleep`) lets go of
  the stove. So threads overlap waiting just fine.
- Threads doing pure-Python computation take turns, so they gain nothing.
- Separate **processes** each have their own interpreter and their own GIL, so
  they truly run in parallel (on separate cores).

> **ES:**
> - Pero un hilo que está *esperando* (un socket, un archivo, `time.sleep`) suelta la estufa. Por eso los hilos superponen bien las esperas.
> - Los hilos que hacen cómputo en Python puro se turnan, así que no ganan nada.
> - Los **procesos** separados tienen cada uno su propio intérprete y su propio GIL, por lo que corren de verdad en paralelo (en núcleos distintos).

(Python 3.13 has an experimental free-threaded build without the GIL. The
standard build you are using has it.)

> **ES:** (Python 3.13 tiene una compilación experimental free-threaded sin GIL. La compilación estándar que estás usando sí lo tiene.)

## Cheat sheet / Hoja de referencia rápida

| Tool | Best for | Cost |
| --- | --- | --- |
| `asyncio` | thousands of waiting tasks | needs async libraries |
| threads | tens of blocking I/O calls | shared memory, needs locks |
| processes | CPU-bound work | startup, data is pickled between processes |

> **ES:**
>
> | Herramienta | Ideal para | Costo |
> | --- | --- | --- |
> | `asyncio` | miles de tareas en espera | requiere librerías async |
> | threads | decenas de llamadas de I/O bloqueantes | memoria compartida, requiere locks |
> | processes | trabajo CPU-bound | arranque, los datos se serializan con pickle entre procesos |

## concurrent.futures

One interface, two backends.

> **ES:** Una interfaz, dos backends.

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

with ThreadPoolExecutor(max_workers=8) as pool:
    pages = list(pool.map(fetch, urls))  # results in input order
```

Swap in `ProcessPoolExecutor` for CPU work:

> **ES:** Cambia a `ProcessPoolExecutor` para trabajo de CPU:

```python
if __name__ == "__main__":
    with ProcessPoolExecutor() as pool:
        totals = list(pool.map(count_primes, [10**5, 2 * 10**5]))
```

Notes on processes:

- The function and its arguments are pickled, so it must be a top-level
  function (no lambdas, no nested functions).
- Guard script entry points with `if __name__ == "__main__":`; macOS and
  Windows start workers by re-importing your module.

> **ES:**
> Notas sobre procesos:
>
> - La función y sus argumentos se serializan con pickle, así que debe ser una función de nivel superior (sin lambdas ni funciones anidadas).
> - Protege los puntos de entrada de los scripts con `if __name__ == "__main__":`; macOS y Windows inician los workers volviendo a importar tu módulo.

## Futures

`pool.submit` returns a `Future`, a promise of a result.

> **ES:** `pool.submit` devuelve un `Future`, una promesa de un resultado.

```python
from concurrent.futures import as_completed

with ThreadPoolExecutor() as pool:
    futures = {pool.submit(fetch, u): u for u in urls}
    for fut in as_completed(futures):  # as each finishes
        try:
            print(futures[fut], fut.result())
        except Exception as e:
            print(futures[fut], "failed:", e)
```

- `fut.result()` returns the value or re-raises the worker's exception.
- `fut.exception()` returns the exception (or `None`) without raising.
- `pool.map` raises the first error when you reach that item in the results.

> **ES:**
> - `fut.result()` devuelve el valor o vuelve a lanzar la excepción del worker.
> - `fut.exception()` devuelve la excepción (o `None`) sin lanzarla.
> - `pool.map` lanza el primer error cuando llegas a ese elemento en los resultados.

## Shared state and locks / Estado compartido y locks

Threads share memory. `counter += 1` is really read, add, write; two threads can
interleave and lose an update (a **race condition**).

> **ES:** Los hilos comparten memoria. `counter += 1` en realidad es leer, sumar y escribir; dos hilos pueden intercalarse y perder una actualización (una **condición de carrera**, race condition).

```python
import threading

lock = threading.Lock()


def increment():
    global counter
    with lock:
        counter += 1
```

Only one thread at a time holds the lock. Keep the locked section small.
Better still: avoid shared state. Have workers return values and combine them
in the main thread.

> **ES:** Solo un hilo a la vez tiene el lock. Mantén pequeña la sección bloqueada. Mejor aún: evita el estado compartido. Haz que los workers devuelvan valores y combínalos en el hilo principal.

## Gotchas / Errores comunes

- More threads is not always faster; pools of 5 to 32 are typical.
- Races are timing-dependent, so a missing lock may pass most test runs.
  Stress tests (many threads, many iterations) expose them.
- Forgetting to `join` threads (or leave the `with` block) means you read
  results too early.
- Process pools copy data. Passing huge objects costs more than the work.
- Do not mix: calling blocking code from async code needs
  `await asyncio.to_thread(...)`.

> **ES:**
> - Más hilos no siempre es más rápido; lo típico son pools de 5 a 32.
> - Las condiciones de carrera dependen del momento exacto, así que un lock faltante puede pasar la mayoría de las ejecuciones de pruebas. Las pruebas de estrés (muchos hilos, muchas iteraciones) las exponen.
> - Olvidar hacer `join` de los hilos (o salir del bloque `with`) significa que lees los resultados demasiado pronto.
> - Los pools de procesos copian datos. Pasar objetos enormes cuesta más que el trabajo mismo.
> - No mezcles: llamar código bloqueante desde código async requiere `await asyncio.to_thread(...)`.

## Exercises / Ejercicios

Edit `exercises/24_concurrency/concurrency.py`: `count_primes`, `map_threads`,
`map_processes`, `try_all`, `SafeCounter`, `hammer`.

> **ES:** Edita `exercises/24_concurrency/concurrency.py`: `count_primes`, `map_threads`, `map_processes`, `try_all`, `SafeCounter`, `hammer`.

```bash
uv run pytest exercises/24_concurrency
```

Optional experiment: time `map_threads(count_primes, [200_000] * 4, 4)` against
`map_processes(...)` to see the GIL at work.

> **ES:** Experimento opcional: mide el tiempo de `map_threads(count_primes, [200_000] * 4, 4)` frente a `map_processes(...)` para ver el GIL en acción.
