"""Exercise: a small typer CLI. Run tests: uv run pytest exercises/22_cli"""

from enum import StrEnum

import typer

app = typer.Typer(help="Tiny toolbox.")


class Direction(StrEnum):
    c2f = "c2f"
    f2c = "f2c"


@app.command()
def greet(name: str, shout: bool = False) -> None:
    """Print 'Hello, <name>!'. With --shout, print it uppercased."""
    raise NotImplementedError


@app.command()
def add(a: int, b: int) -> None:
    """Print a + b."""
    raise NotImplementedError


@app.command()
def repeat(text: str, times: int = 2) -> None:
    """Print text on its own line `times` times.

    Make the option available as both --times and -n (see typer.Option).
    If times < 1, write a message to stderr and exit with code 2
    (typer.Exit).
    """
    raise NotImplementedError


@app.command()
def stats(numbers: list[float]) -> None:
    """Print three lines: min=..., max=..., mean=... (format values with :g)."""
    raise NotImplementedError


@app.command()
def convert(value: float, direction: Direction = Direction.c2f) -> None:
    """Convert Celsius->Fahrenheit (c2f) or back (f2c); print with 1 decimal."""
    raise NotImplementedError


if __name__ == "__main__":
    app()
