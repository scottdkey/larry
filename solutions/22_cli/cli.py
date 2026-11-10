"""Exercise: a small typer CLI."""

from enum import StrEnum
from statistics import mean
from typing import Annotated

import typer

app = typer.Typer(help="Tiny toolbox.")


class Direction(StrEnum):
    c2f = "c2f"
    f2c = "f2c"


@app.command()
def greet(name: str, shout: bool = False) -> None:
    """Print a greeting; with --shout, uppercase it."""
    message = f"Hello, {name}!"
    typer.echo(message.upper() if shout else message)


@app.command()
def add(a: int, b: int) -> None:
    """Print a + b."""
    typer.echo(a + b)


@app.command()
def repeat(
    text: str,
    times: Annotated[int, typer.Option("--times", "-n")] = 2,
) -> None:
    """Print text once per line, `times` times."""
    if times < 1:
        typer.echo("times must be at least 1", err=True)
        raise typer.Exit(code=2)
    for _ in range(times):
        typer.echo(text)


@app.command()
def stats(numbers: list[float]) -> None:
    """Print min, max and mean of the numbers, one per line."""
    typer.echo(f"min={min(numbers):g}")
    typer.echo(f"max={max(numbers):g}")
    typer.echo(f"mean={mean(numbers):g}")


@app.command()
def convert(value: float, direction: Direction = Direction.c2f) -> None:
    """Convert a temperature, printed with one decimal."""
    result = value * 9 / 5 + 32 if direction is Direction.c2f else (value - 32) * 5 / 9
    typer.echo(f"{result:.1f}")


if __name__ == "__main__":
    app()
