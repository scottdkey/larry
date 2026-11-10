# Lesson 11: Errors and Exceptions / Lección 11: Errores y excepciones

Goals: catch and raise exceptions well, define your own, chain them, and
choose between EAFP and LBYL.

> **ES:** Objetivos: capturar y lanzar excepciones correctamente, definir las
> tuyas, encadenarlas y elegir entre EAFP y LBYL.

## try / except / else / finally

```python
def read_number(text: str) -> int | None:
    try:
        value = int(text)
    except ValueError:
        print("not a number")
        return None
    else:
        print("parsed fine")  # runs only if no exception occurred
        return value
    finally:
        print("always runs")  # cleanup, even after return or raise
```

Rules of thumb:

> **ES:** Reglas generales:

- Keep the `try` body tiny: only the line that can fail.
- Catch specific exceptions. Bare `except:` or `except Exception:` hides bugs;
  reserve the latter for boundaries like a task runner that must keep going.
- Catch several at once with a tuple: `except (KeyError, TypeError):`.
- Name the exception with `as exc` when you need it.

> **ES:**
> - Mantén el cuerpo del `try` mínimo: solo la línea que puede fallar.
> - Captura excepciones específicas. Un `except:` a secas o `except Exception:`
>   oculta errores; reserva este último para fronteras como un ejecutor de
>   tareas que debe seguir funcionando.
> - Captura varias a la vez con una tupla: `except (KeyError, TypeError):`.
> - Dale nombre a la excepción con `as exc` cuando la necesites.

## Raising / Lanzar excepciones

```python
def withdraw(balance: int, amount: int) -> int:
    if amount <= 0:
        raise ValueError("amount must be positive")
    return balance - amount
```

Use built-ins (`ValueError`, `TypeError`, `KeyError`) where they fit. Bare
`raise` inside `except` re-raises the current error unchanged.

> **ES:** Usa las excepciones incorporadas (`ValueError`, `TypeError`,
> `KeyError`) donde encajen. Un `raise` a secas dentro de `except` vuelve a
> lanzar el error actual sin cambios.

## Custom exceptions / Excepciones personalizadas

Subclass `Exception` (never `BaseException`):

> **ES:** Hereda de `Exception` (nunca de `BaseException`):

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance: int, amount: int) -> None:
        super().__init__(f"cannot withdraw {amount}; balance is {balance}")
        self.balance = balance
        self.amount = amount
```

Attributes let callers react programmatically instead of parsing messages.
Give a library one base error (`class ShopError(Exception)`) so users can
catch everything from it.

> **ES:** Los atributos permiten que quien llama reaccione por código en lugar
> de analizar mensajes. Dale a una biblioteca un error base
> (`class ShopError(Exception)`) para que los usuarios puedan capturar todo lo
> que venga de ella.

## Chaining with `raise ... from` / Encadenar con `raise ... from`

Translate low-level errors into your own while keeping the original:

> **ES:** Traduce errores de bajo nivel a los tuyos conservando el original:

```python
try:
    config = json.loads(text)
except json.JSONDecodeError as exc:
    raise ConfigError("config is not valid JSON") from exc
```

The original is stored as `__cause__` and shown in the traceback. Raising a
new error inside `except` without `from` still links it implicitly, but
`from` states the intent. `from None` hides the original.

> **ES:** El original se guarda como `__cause__` y aparece en el traceback.
> Lanzar un error nuevo dentro de `except` sin `from` también lo enlaza de
> forma implícita, pero `from` deja clara la intención. `from None` oculta el
> original.

## EAFP vs LBYL

- LBYL, "look before you leap": check first.
- EAFP, "easier to ask forgiveness than permission": just try.

> **ES:**
> - LBYL, "mira antes de saltar" (look before you leap): verifica primero.
> - EAFP, "es más fácil pedir perdón que permiso" (easier to ask forgiveness
>   than permission): simplemente intenta.

```python
# LBYL
if "name" in data and isinstance(data["name"], str):
    name = data["name"]

# EAFP
try:
    name = data["name"]
except KeyError:
    name = "anonymous"
```

Python favours EAFP: it avoids race conditions (a file can vanish between
`exists()` and `open()`) and often reads better. Use LBYL when the check is
cheap and the failure is not exceptional.

> **ES:** Python favorece EAFP: evita condiciones de carrera (un archivo puede
> desaparecer entre `exists()` y `open()`) y a menudo se lee mejor. Usa LBYL
> cuando la verificación es barata y el fallo no es excepcional.

## Gotchas / Trampas comunes

- Exceptions are for exceptional cases; do not use them for ordinary
  control flow in hot loops.
- Never `except: pass`. At minimum, log it.
- Order matters: put specific `except` clauses before general ones.
- `finally` runs even on `return`; a `return` inside `finally` swallows errors.
- Test failures with `pytest.raises`:

> **ES:**
> - Las excepciones son para casos excepcionales; no las uses para el flujo de
>   control normal en bucles críticos.
> - Nunca `except: pass`. Como mínimo, regístralo en un log.
> - El orden importa: pon las cláusulas `except` específicas antes de las
>   generales.
> - `finally` se ejecuta incluso con `return`; un `return` dentro de `finally`
>   se traga los errores.
> - Prueba los fallos con `pytest.raises`:

```python
import pytest


def test_bad_amount():
    with pytest.raises(ValueError, match="positive"):
        withdraw(10, 0)
```

## Exercises / Ejercicios

Stubs are in `exercises/11_errors/errors.py`; tests in `test_errors.py`.

> **ES:** Los stubs están en `exercises/11_errors/errors.py`; las pruebas en
> `test_errors.py`.

```
uv run pytest exercises/11_errors
```
