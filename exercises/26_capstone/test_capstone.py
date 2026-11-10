import json

import pytest
from capstone import Task, TodoStore, app
from typer.testing import CliRunner

runner = CliRunner()


def test_store_add_assigns_ids_and_persists(tmp_path):
    path = tmp_path / "t.json"
    store = TodoStore(path)
    assert store.add("  milk ") == Task(1, "milk")
    assert store.add("eggs").id == 2
    reloaded = TodoStore(path)
    assert [t.title for t in reloaded.list()] == ["milk", "eggs"]
    assert json.loads(path.read_text())[0]["title"] == "milk"


def test_store_rejects_empty_title(tmp_path):
    with pytest.raises(ValueError):
        TodoStore(tmp_path / "t.json").add("   ")


def test_store_complete_and_list(tmp_path):
    store = TodoStore(tmp_path / "t.json")
    store.add("a")
    store.add("b")
    assert store.complete(1).done is True
    assert [t.id for t in store.list()] == [2]
    assert [t.id for t in store.list(include_done=True)] == [1, 2]
    assert TodoStore(tmp_path / "t.json").list(include_done=True)[0].done


def test_store_remove_next_id_follows_max_and_unknown_ids_raise(tmp_path):
    store = TodoStore(tmp_path / "t.json")
    store.add("a")
    store.add("b")
    store.remove(1)
    assert [t.id for t in store.list()] == [2]
    assert store.add("c").id == 3
    with pytest.raises(KeyError):
        store.remove(99)
    with pytest.raises(KeyError):
        store.complete(99)


def run(tmp_path, *args):
    return runner.invoke(app, ["--file", str(tmp_path / "t.json"), *args])


def test_cli_full_flow(tmp_path):
    assert run(tmp_path, "list").stdout.strip() == "No tasks."
    assert run(tmp_path, "add", "milk").stdout.strip() == "Added #1: milk"
    run(tmp_path, "add", "eggs")
    assert run(tmp_path, "done", "1").stdout.strip() == "Completed #1"
    assert run(tmp_path, "list").stdout.splitlines() == ["[ ] 2 eggs"]
    assert run(tmp_path, "list", "--all").stdout.splitlines() == [
        "[x] 1 milk",
        "[ ] 2 eggs",
    ]
    assert run(tmp_path, "rm", "2").stdout.strip() == "Removed #2"
    assert run(tmp_path, "list", "--all").stdout.splitlines() == ["[x] 1 milk"]


def test_cli_errors(tmp_path):
    path = tmp_path / "t.json"
    runner.invoke(app, ["--file", str(path), "add", "milk"])
    before = path.read_text()
    for args, message in (
        (["done", "9"], "No task #9"),
        (["rm", "9"], "No task #9"),
    ):
        result = run(tmp_path, *args)
        assert result.exit_code == 1
        assert isinstance(result.exception, SystemExit)
        assert message in result.output
        assert path.read_text() == before

    result = run(tmp_path, "add", "  ")
    assert result.exit_code == 1
    assert isinstance(result.exception, SystemExit)
    assert result.output.strip()
    assert path.read_text() == before


def test_cli_short_file_option(tmp_path):
    path = tmp_path / "short.json"
    result = runner.invoke(app, ["-f", str(path), "add", "milk"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "Added #1: milk"
    assert json.loads(path.read_text())[0]["title"] == "milk"
