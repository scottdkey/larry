# Lesson 22: Command-line apps with typer / Lección 22: Aplicaciones de línea de comandos con typer

## Goals / Objetivos

- Turn plain functions into CLI commands with `typer`.
- Use arguments, options, flags, enums and multiple values.
- Signal errors with exit codes and `stderr`.
- Test a CLI without a terminal using `CliRunner`.

> **ES:**
> - Convierte funciones simples en comandos de CLI con `typer`.
> - Usa argumentos, opciones, flags, enums y valores múltiples.
> - Señala errores con códigos de salida y `stderr`.
> - Prueba una CLI sin terminal usando `CliRunner`.

## From function to command / De función a comando

`typer` reads your type hints and builds the command line for you.

> **ES:** `typer` lee tus anotaciones de tipo y construye la línea de comandos por ti.

```python
import typer


def main(name: str, shout: bool = False) -> None:
    message = f"Hello, {name}!"
    typer.echo(message.upper() if shout else message)


if __name__ == "__main__":
    typer.run(main)
```

```text
$ uv run python hello.py Ada --shout
HELLO, ADA!
```

- A parameter with no default (`name`) is a positional **argument**.
- A parameter with a default (`shout`) is an **option**; a `bool` becomes a
  `--shout` / `--no-shout` flag.
- The docstring becomes the `--help` text. Try `--help` on everything.

> **ES:**
> - Un parámetro sin valor por defecto (`name`) es un **argumento** posicional.
> - Un parámetro con valor por defecto (`shout`) es una **opción**; un `bool` se convierte en un flag `--shout` / `--no-shout`.
> - El docstring se convierte en el texto de `--help`. Prueba `--help` en todo.

## Several commands / Varios comandos

Use a `Typer` app and decorate each function.

> **ES:** Usa una app `Typer` y decora cada función.

```python
app = typer.Typer()


@app.command()
def add(a: int, b: int) -> None:
    typer.echo(a + b)


@app.command()
def hello(name: str) -> None:
    typer.echo(f"Hi {name}")


if __name__ == "__main__":
    app()
```

`python tool.py add 2 3` prints `5`. Passing `x` instead of `3` makes typer
print a usage error and exit with code 2. You wrote no validation; the type
hint did it.

> **ES:** `python tool.py add 2 3` imprime `5`. Si pasas `x` en lugar de `3`, typer imprime un error de uso y termina con código 2. No escribiste ninguna validación; la hizo la anotación de tipo.

Note: with exactly one command, typer treats the app as that command. With two
or more, the command name becomes required.

> **ES:** Nota: con exactamente un comando, typer trata la app como ese comando. Con dos o más, el nombre del comando es obligatorio.

## Options with short names / Opciones con nombres cortos

Use `Annotated` to add details to a parameter:

> **ES:** Usa `Annotated` para agregar detalles a un parámetro:

```python
from typing import Annotated


@app.command()
def repeat(
    text: str,
    times: Annotated[int, typer.Option("--times", "-n")] = 2,
) -> None:
    for _ in range(times):
        typer.echo(text)
```

Now `repeat hi -n 3` and `repeat hi --times 3` both work.

> **ES:** Ahora tanto `repeat hi -n 3` como `repeat hi --times 3` funcionan.

## Many values and enums / Varios valores y enums

```python
from enum import StrEnum


class Mode(StrEnum):
    fast = "fast"
    slow = "slow"


@app.command()
def total(numbers: list[float], mode: Mode = Mode.fast) -> None:
    typer.echo(sum(numbers))
```

- `list[float]` as an argument accepts one or more values.
- An `Enum` option is restricted to its members; anything else is a usage error,
  and `--help` lists the choices.

> **ES:**
> - `list[float]` como argumento acepta uno o más valores.
> - Una opción `Enum` está restringida a sus miembros; cualquier otro valor es un error de uso, y `--help` muestra las opciones disponibles.

## Output and exit codes / Salida y códigos de salida

- `typer.echo(msg)` writes to stdout; `typer.echo(msg, err=True)` to stderr.
- `raise typer.Exit(code=1)` stops the program quietly with that code.
- By convention, 0 is success, 1 is "your request failed", 2 is "bad usage".

> **ES:**
> - `typer.echo(msg)` escribe en stdout; `typer.echo(msg, err=True)` escribe en stderr.
> - `raise typer.Exit(code=1)` detiene el programa sin ruido con ese código.
> - Por convención, 0 es éxito, 1 es "tu solicitud falló" y 2 es "uso incorrecto".

```python
if times < 1:
    typer.echo("times must be at least 1", err=True)
    raise typer.Exit(code=2)
```

## Shared options and state / Opciones compartidas y estado

A `@app.callback()` runs before every command. It is the place for global
options, and it can pass state to commands through `ctx.obj`:

> **ES:** Un `@app.callback()` se ejecuta antes de cada comando. Es el lugar para las opciones globales, y puede pasar estado a los comandos mediante `ctx.obj`:

```python
@app.callback()
def main(ctx: typer.Context, verbose: bool = False) -> None:
    ctx.obj = {"verbose": verbose}


@app.command()
def run(ctx: typer.Context) -> None:
    if ctx.obj["verbose"]:
        typer.echo("verbose mode")
```

Usage: `tool.py --verbose run`. You will use this in the capstone.

> **ES:** Uso: `tool.py --verbose run`. Lo usarás en el proyecto final (capstone).

## Testing a CLI / Probar una CLI

`CliRunner` calls your app in-process and captures the output.

> **ES:** `CliRunner` llama a tu app dentro del mismo proceso y captura la salida.

```python
from typer.testing import CliRunner

runner = CliRunner()
result = runner.invoke(app, ["add", "2", "3"])
assert result.exit_code == 0
assert result.stdout.strip() == "5"  # stdout only; use result.output for everything
```

Test the exit code and the output. Test the failure paths too.

> **ES:** Prueba el código de salida y la salida. Prueba también los caminos de error.

## Gotchas / Errores comunes

- Forgetting `if __name__ == "__main__": app()` means nothing happens when you
  run the file.
- Uncaught exceptions in a command give exit code 1 and a traceback, so
  raise `typer.Exit` for expected failures.
- `print` works, but `typer.echo` handles encodings and `err=True` for you.
- A function named `list` or `all` shadows builtins. Give the function another
  name and pass it to the decorator: `@app.command("list")`.
- Mutable defaults are as bad here as anywhere; use `None`.

> **ES:**
> - Olvidar `if __name__ == "__main__": app()` significa que no pasa nada al ejecutar el archivo.
> - Las excepciones no capturadas en un comando dan código de salida 1 y un traceback, así que lanza `typer.Exit` para los fallos esperados.
> - `print` funciona, pero `typer.echo` maneja las codificaciones y `err=True` por ti.
> - Una función llamada `list` o `all` oculta los builtins. Dale otro nombre a la función y pásalo al decorador: `@app.command("list")`.
> - Los valores por defecto mutables son igual de malos aquí que en cualquier lugar; usa `None`.

## Exercises / Ejercicios

Edit `exercises/22_cli/cli.py`. Implement `greet`, `add`, `repeat`, `stats` and
`convert`; each docstring says exactly what to print. Then run:

> **ES:** Edita `exercises/22_cli/cli.py`. Implementa `greet`, `add`, `repeat`, `stats` y `convert`; cada docstring dice exactamente qué imprimir. Luego ejecuta:

```bash
uv run pytest exercises/22_cli
```

Try the app by hand too: `uv run python exercises/22_cli/cli.py --help`.

> **ES:** Prueba también la app a mano: `uv run python exercises/22_cli/cli.py --help`.
