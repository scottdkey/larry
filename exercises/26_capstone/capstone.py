"""Capstone: a todo CLI with JSON storage. See lessons/26_capstone.md.

Run tests: uv run pytest exercises/26_capstone

ES: Proyecto final: una CLI de tareas con almacenamiento JSON. Ejecuta las pruebas
con el comando de arriba.
"""

from dataclasses import dataclass
from pathlib import Path

import typer


@dataclass
class Task:
    id: int
    title: str
    done: bool = False


class TodoStore:
    """Tasks persisted to a JSON file; the file is created on first save.

    ES: Tareas guardadas en un archivo JSON; el archivo se crea al primer guardado.
    """

    def __init__(self, path: Path) -> None:
        """Load tasks from path if it exists, else start empty.

        ES: Carga las tareas desde path si existe; si no, empieza vacío.
        """
        raise NotImplementedError

    def add(self, title: str) -> Task:
        """Strip title, reject empty (ValueError), assign id = max id + 1, save.

        ES: Recorta title, rechaza vacío (ValueError), asigna id = máx + 1, guarda.
        """
        raise NotImplementedError

    def list(self, include_done: bool = False) -> list[Task]:
        """Open tasks only, unless include_done.

        ES: Solo tareas abiertas, salvo que include_done.
        """
        raise NotImplementedError

    def complete(self, task_id: int) -> Task:
        """Mark done and save. Unknown id raises KeyError.

        ES: Marca como hecha y guarda. Un id desconocido lanza KeyError.
        """
        raise NotImplementedError

    def remove(self, task_id: int) -> None:
        """Delete and save. Unknown id raises KeyError.

        ES: Elimina y guarda. Un id desconocido lanza KeyError.
        """
        raise NotImplementedError


app = typer.Typer(help="A tiny todo list.")


@app.callback()
def main(ctx: typer.Context, file: Path = Path("todo.json")) -> None:
    """Global option --file/-f picks the JSON file; stash a TodoStore in ctx.obj.

    ES: La opción global --file/-f elige el JSON; guarda un TodoStore en ctx.obj.
    """
    raise NotImplementedError


@app.command()
def add(ctx: typer.Context, title: str) -> None:
    """Print 'Added #<id>: <title>'. Empty title: message to stderr, exit 1.

    ES: Imprime 'Added #<id>: <title>'. Título vacío: mensaje a stderr, salida 1.
    """
    raise NotImplementedError


@app.command("list")
def list_tasks(ctx: typer.Context, all_: bool = False) -> None:
    """Print '[ ] 1 title' / '[x] 1 title' lines (--all includes done).

    Print 'No tasks.' when there is nothing to show.

    ES: Imprime líneas '[ ] 1 title' / '[x] 1 title' (--all incluye las hechas).
    Imprime 'No tasks.' cuando no hay nada que mostrar.
    """
    raise NotImplementedError


@app.command()
def done(ctx: typer.Context, task_id: int) -> None:
    """Print 'Completed #<id>'. Unknown id: 'No task #<id>' to stderr, exit 1.

    ES: Imprime 'Completed #<id>'. Id desconocido: 'No task #<id>' a stderr, salida 1.
    """
    raise NotImplementedError


@app.command()
def rm(ctx: typer.Context, task_id: int) -> None:
    """Print 'Removed #<id>'. Unknown id: 'No task #<id>' to stderr, exit 1.

    ES: Imprime 'Removed #<id>'. Id desconocido: 'No task #<id>' a stderr, salida 1.
    """
    raise NotImplementedError


if __name__ == "__main__":
    app()
