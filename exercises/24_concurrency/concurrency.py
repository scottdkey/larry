"""Exercise: threads, processes, concurrent.futures.

Run tests: uv run pytest exercises/24_concurrency

ES: Ejercicio: hilos, procesos y concurrent.futures. Ejecuta las pruebas con el
comando de arriba.
"""

from collections.abc import Callable, Iterable


def count_primes(limit: int) -> int:
    """Count primes below limit (CPU-bound; trial division is fine).

    ES: Cuenta los primos menores que limit (CPU-bound; la división de prueba basta).
    """
    raise NotImplementedError


def map_threads[T, R](
    func: Callable[[T], R], items: Iterable[T], workers: int
) -> list[R]:
    """Apply func to items on a ThreadPoolExecutor; results in input order.

    ES: Aplica func a items en un ThreadPoolExecutor; resultados en orden de entrada.
    """
    raise NotImplementedError


def map_processes[T, R](
    func: Callable[[T], R], items: Iterable[T], workers: int
) -> list[R]:
    """Apply func to items on a ProcessPoolExecutor; results in input order.

    func must be a top-level (picklable) function.

    ES: Aplica func a items en un ProcessPoolExecutor; resultados en orden de
    entrada. func debe ser una función de nivel superior (serializable con pickle).
    """
    raise NotImplementedError


def try_all[T, R](
    func: Callable[[T], R], items: list[T], workers: int
) -> tuple[list[R], list[tuple[T, Exception]]]:
    """Run func on every item in threads; one failure must not stop the others.

    Return (results of successes in input order, [(item, exception), ...]).
    Hint: pool.submit gives Futures; future.exception() is None on success.

    ES: Ejecuta func en cada item con hilos; un fallo no debe detener a los demás.
    Devuelve (resultados de los éxitos en orden, [(item, excepción), ...]).
    Pista: pool.submit da Futures; future.exception() es None si hubo éxito.
    """
    raise NotImplementedError


class SafeCounter:
    """A counter that stays correct when many threads call increment().

    ES: Un contador que sigue siendo correcto cuando muchos hilos llaman a increment().
    """

    def __init__(self) -> None:
        raise NotImplementedError

    @property
    def value(self) -> int:
        raise NotImplementedError

    def increment(self, by: int = 1) -> None:
        """Add `by` to the counter. Protect the update with a threading.Lock.

        ES: Suma `by` al contador. Protege la actualización con un threading.Lock.
        """
        raise NotImplementedError


def hammer(counter: SafeCounter, threads: int, times: int) -> None:
    """Start `threads` threads that each call counter.increment() `times` times.

    Wait for all of them to finish before returning.

    ES: Inicia `threads` hilos que llaman cada uno a counter.increment() `times`
    veces. Espera a que todos terminen antes de retornar.
    """
    raise NotImplementedError
