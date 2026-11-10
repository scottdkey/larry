"""Capstone: a todo CLI with JSON storage."""

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Annotated

import typer


@dataclass
class Task:
    id: int
    title: str
    done: bool = False


class TodoStore:
    """Tasks persisted to a JSON file; the file is created on first save."""

    def __init__(self, path: Path) -> None:
        self.path = Path(path)
        self.tasks: list[Task] = []
        if self.path.exists():
            data = json.loads(self.path.read_text())
            self.tasks = [Task(**item) for item in data]

    def _save(self) -> None:
        payload = [asdict(t) for t in self.tasks]
        self.path.write_text(json.dumps(payload, indent=2))

    def _get(self, task_id: int) -> Task:
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise KeyError(task_id)

    def add(self, title: str) -> Task:
        title = title.strip()
        if not title:
            raise ValueError("title must not be empty")
        next_id = max((t.id for t in self.tasks), default=0) + 1
        task = Task(next_id, title)
        self.tasks.append(task)
        self._save()
        return task

    def list(self, include_done: bool = False) -> list[Task]:
        return [t for t in self.tasks if include_done or not t.done]

    def complete(self, task_id: int) -> Task:
        task = self._get(task_id)
        task.done = True
        self._save()
        return task

    def remove(self, task_id: int) -> None:
        task = self._get(task_id)
        self.tasks.remove(task)
        self._save()


app = typer.Typer(help="A tiny todo list.")


@app.callback()
def main(
    ctx: typer.Context,
    file: Annotated[Path, typer.Option("--file", "-f")] = Path("todo.json"),
) -> None:
    ctx.obj = TodoStore(file)


def _fail(message: str) -> typer.Exit:
    typer.echo(message, err=True)
    return typer.Exit(code=1)


@app.command()
def add(ctx: typer.Context, title: str) -> None:
    """Add a task and print 'Added #<id>: <title>'."""
    try:
        task = ctx.obj.add(title)
    except ValueError as e:
        raise _fail(str(e)) from e
    typer.echo(f"Added #{task.id}: {task.title}")


@app.command("list")
def list_tasks(
    ctx: typer.Context, all_: Annotated[bool, typer.Option("--all")] = False
) -> None:
    """List open tasks (or all with --all) as '[ ] 1 title' / '[x] 1 title'."""
    tasks = ctx.obj.list(include_done=all_)
    if not tasks:
        typer.echo("No tasks.")
    for t in tasks:
        typer.echo(f"[{'x' if t.done else ' '}] {t.id} {t.title}")


@app.command()
def done(ctx: typer.Context, task_id: int) -> None:
    """Mark a task done."""
    try:
        task = ctx.obj.complete(task_id)
    except KeyError as e:
        raise _fail(f"No task #{task_id}") from e
    typer.echo(f"Completed #{task.id}")


@app.command()
def rm(ctx: typer.Context, task_id: int) -> None:
    """Delete a task."""
    try:
        ctx.obj.remove(task_id)
    except KeyError as e:
        raise _fail(f"No task #{task_id}") from e
    typer.echo(f"Removed #{task_id}")


if __name__ == "__main__":
    app()
