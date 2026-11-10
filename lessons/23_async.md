# Lesson 23: Async with asyncio / Lección 23: Async con asyncio

## Goals / Objetivos

- Understand what `async` / `await` do and when they help.
- Run many waits at once with `gather`, `TaskGroup` and timeouts.
- Limit concurrency and handle failures.

> **ES:**
> - Entiende qué hacen `async` / `await` y cuándo ayudan.
> - Ejecuta muchas esperas a la vez con `gather`, `TaskGroup` y timeouts.
> - Limita la concurrencia y maneja los fallos.

## The idea / La idea

Much slow code is just *waiting*: for a network reply, a database, a timer.
While one task waits, the CPU could do something else. `asyncio` runs many
tasks on **one thread**, switching between them whenever one hits an `await`.

> **ES:** Gran parte del código lento solo está *esperando*: una respuesta de red, una base de datos, un temporizador. Mientras una tarea espera, la CPU podría hacer otra cosa. `asyncio` ejecuta muchas tareas en **un solo hilo**, cambiando entre ellas cada vez que una llega a un `await`.

```python
import asyncio


async def greet(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"hi {name}"


print(asyncio.run(greet("Ada", 0.1)))
```

- `async def` makes a **coroutine function**. Calling it does not run it; it
  returns a coroutine object.
- `await` runs another coroutine and pauses this one until it finishes. Only
  inside `async def`.
- `asyncio.run(coro)` starts the event loop, runs `coro`, and shuts down. Call
  it once at the top level of your program.

> **ES:**
> - `async def` crea una **función corrutina** (coroutine function). Llamarla no la ejecuta; devuelve un objeto corrutina.
> - `await` ejecuta otra corrutina y pausa la actual hasta que termine. Solo funciona dentro de `async def`.
> - `asyncio.run(coro)` inicia el event loop, ejecuta `coro` y lo cierra. Llámalo una sola vez en el nivel superior de tu programa.

## Running things concurrently / Ejecutar cosas de forma concurrente

Awaiting one after another is still sequential:

> **ES:** Hacer `await` de una tras otra sigue siendo secuencial:

```python
await greet("a", 1)
await greet("b", 1)  # total 2 seconds
```

`asyncio.gather` runs them together and returns results in input order:

> **ES:** `asyncio.gather` las ejecuta juntas y devuelve los resultados en el orden de entrada:

```python
results = await asyncio.gather(greet("a", 1), greet("b", 1))  # about 1 second
```

## TaskGroup (preferred in 3.11+) / TaskGroup (preferido en 3.11+)

```python
async with asyncio.TaskGroup() as tg:
    t1 = tg.create_task(greet("a", 1))
    t2 = tg.create_task(greet("b", 1))
print(t1.result(), t2.result())
```

The `async with` block waits for every task. If one task raises, the others are
cancelled and the errors arrive together as an `ExceptionGroup`:

> **ES:** El bloque `async with` espera a todas las tareas. Si una lanza una excepción, las demás se cancelan y los errores llegan juntos como un `ExceptionGroup`:

```python
try:
    async with asyncio.TaskGroup() as tg:
        tg.create_task(boom())
except* ValueError as eg:
    print(eg.exceptions)
```

`except*` handles the matching errors inside the group.

> **ES:** `except*` maneja los errores que coinciden dentro del grupo.

## Timeouts

```python
try:
    result = await asyncio.wait_for(slow(), timeout=2)
except TimeoutError:
    result = "gave up"
```

There is also the block form, `async with asyncio.timeout(2): ...`.
The slow task is cancelled when the timeout hits.

> **ES:** También existe la forma de bloque, `async with asyncio.timeout(2): ...`. La tarea lenta se cancela cuando se cumple el timeout.

## Limiting concurrency / Limitar la concurrencia

Launching 1000 requests at once is rude. Use a `Semaphore`:

> **ES:** Lanzar 1000 solicitudes a la vez es de mala educación. Usa un `Semaphore`:

```python
sem = asyncio.Semaphore(10)


async def limited(job):
    async with sem:
        return await job()
```

At most 10 jobs are inside the `async with` at a time.

> **ES:** Como máximo 10 trabajos están dentro del `async with` al mismo tiempo.

## Failures in gather / Fallos en gather

By default the first exception from `gather` propagates to you (the other tasks
keep running). To collect everything:

> **ES:** Por defecto, la primera excepción de `gather` se propaga hacia ti (las demás tareas siguen ejecutándose). Para recolectarlo todo:

```python
outcomes = await asyncio.gather(*jobs, return_exceptions=True)
failures = [o for o in outcomes if isinstance(o, Exception)]
```

## Real code uses async libraries / El código real usa librerías async

`httpx.AsyncClient` is the async twin of the client from lesson 21:

> **ES:** `httpx.AsyncClient` es el gemelo async del cliente de la lección 21:

```python
async with httpx.AsyncClient() as client:
    responses = await asyncio.gather(*(client.get(u) for u in urls))
```

## Gotchas / Errores comunes

- **Blocking calls freeze everything.** `time.sleep(5)` inside a coroutine
  stops the whole loop. Use `await asyncio.sleep(5)`, or run blocking code in
  a thread with `await asyncio.to_thread(func, arg)`.
- **Forgetting `await`** gives you a coroutine object and a "never awaited"
  warning, not the result.
- **Async is not parallel.** CPU-heavy work in a coroutine still blocks the
  loop; see the next lesson.
- Do not call `asyncio.run` from inside a running loop.
- Keep a reference to tasks from `create_task`, or they may be garbage
  collected. A `TaskGroup` does this for you.

> **ES:**
> - **Las llamadas bloqueantes congelan todo.** `time.sleep(5)` dentro de una corrutina detiene todo el loop. Usa `await asyncio.sleep(5)`, o ejecuta el código bloqueante en un hilo con `await asyncio.to_thread(func, arg)`.
> - **Olvidar `await`** te da un objeto corrutina y una advertencia de "never awaited", no el resultado.
> - **Async no es paralelo.** El trabajo pesado de CPU dentro de una corrutina igual bloquea el loop; mira la siguiente lección.
> - No llames a `asyncio.run` desde dentro de un loop que ya está en ejecución.
> - Guarda una referencia a las tareas de `create_task`, o podrían ser eliminadas por el garbage collector. Un `TaskGroup` lo hace por ti.

## Testing / Pruebas

You do not need a plugin. Wrap the coroutine in `asyncio.run` in a normal test:

> **ES:** No necesitas ningún plugin. Envuelve la corrutina en `asyncio.run` dentro de una prueba normal:

```python
def test_double():
    assert asyncio.run(double(4)) == 8
```

Use tiny sleeps (0 to 0.05s) so tests stay fast and deterministic.

> **ES:** Usa esperas muy pequeñas (0 a 0.05 s) para que las pruebas sean rápidas y deterministas.

## Exercises / Ejercicios

Edit `exercises/23_async/async_io.py`: `double`, `double_all`, `with_default`,
`run_limited`, `collect_successes`, `squares_in_group`.

> **ES:** Edita `exercises/23_async/async_io.py`: `double`, `double_all`, `with_default`, `run_limited`, `collect_successes`, `squares_in_group`.

```bash
uv run pytest exercises/23_async
```
