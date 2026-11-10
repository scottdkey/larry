"""Lesson 11 exercises: exceptions."""

from collections.abc import Callable, Mapping


def parse_int(text: str, default: int = 0) -> int:
    """Return int(text), or `default` if text is not a valid integer.

    ES: Devuelve int(text), o `default` si text no es un entero válido.
    """
    raise NotImplementedError


def safe_divide(a: float, b: float) -> float | None:
    """Return a / b, or None when b is zero. Use try/except, not an `if`.

    ES: Devuelve a / b, o None cuando b es cero. Usa try/except, no un `if`.
    """
    raise NotImplementedError


def get_nested(data: Mapping[str, object], keys: list[str]) -> object | None:
    """Follow `keys` through nested dicts (EAFP style); None if any step is missing.

    get_nested({"a": {"b": 1}}, ["a", "b"]) -> 1
    get_nested({"a": 1}, ["a", "b"]) -> None   (1 is not subscriptable)

    ES: Sigue `keys` a través de dicts anidados (estilo EAFP); None si falta
    algún paso.
    """
    raise NotImplementedError


class InsufficientFundsError(Exception):
    """Raised when withdrawing more than the balance.

    Store `balance` and `amount` as attributes; the message should be
    "cannot withdraw {amount}; balance is {balance}".

    ES: Se lanza al retirar más que el saldo. Guarda `balance` y `amount` como
    atributos; el mensaje debe ser "cannot withdraw {amount}; balance is
    {balance}".
    """

    def __init__(self, balance: int, amount: int) -> None:
        raise NotImplementedError


class Account:
    """A bank account holding an integer balance.

    ES: Una cuenta bancaria con un saldo entero.
    """

    def __init__(self, balance: int = 0) -> None:
        raise NotImplementedError

    def withdraw(self, amount: int) -> int:
        """Subtract `amount` and return the new balance.

            Raise ValueError if amount <= 0, InsufficientFundsError if it exceeds
            the balance (leaving the balance unchanged).

        ES: Resta `amount` y devuelve el nuevo saldo. Lanza ValueError si
        amount <= 0, InsufficientFundsError si excede el saldo (dejándolo sin
        cambios).
        """
        raise NotImplementedError


class ConfigError(Exception):
    """Raised for unusable configuration text.

    ES: Se lanza para texto de configuración inutilizable.
    """


def load_config(text: str) -> dict[str, object]:
    """Parse JSON text that must be an object.

    Invalid JSON -> raise ConfigError chained with `raise ... from` so the
    original JSONDecodeError is the __cause__. A non-object (e.g. a list)
    -> ConfigError too.

    ES: Analiza texto JSON que debe ser un objeto. JSON inválido -> lanza
    ConfigError encadenado con `raise ... from` para que el JSONDecodeError
    original sea el __cause__. Un valor que no sea objeto (p. ej. una lista)
    -> también ConfigError.
    """
    raise NotImplementedError


def run_all(tasks: list[Callable[[], object]], log: list[str]) -> int:
    """Run each task, returning how many raised an Exception.

    For every task append "start" to `log`; then "ok" if it succeeded or
    "failed" if it raised (swallow the error and keep going); and always
    "end" afterwards. Use try/except/else/finally.

    ES: Ejecuta cada tarea y devuelve cuántas lanzaron una Exception. Por cada
    tarea agrega "start" a `log`; luego "ok" si tuvo éxito o "failed" si
    lanzó (traga el error y continúa); y siempre "end" al final. Usa
    try/except/else/finally.
    """
    raise NotImplementedError
