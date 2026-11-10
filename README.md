# larry

A hands-on Python course. Tooling: [uv](https://docs.astral.sh/uv/) (Python + deps),
[ruff](https://docs.astral.sh/ruff/) (lint/format), [ty](https://docs.astral.sh/ty/) (types), pytest.

## Setup

### 1. Install uv

| OS | Command |
|---|---|
| macOS | `brew install uv` (or the curl script below) |
| Linux | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Windows (PowerShell) | `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 \| iex"` |

Restart your terminal afterwards, then check with `uv --version`.
You do not need to install Python yourself; uv downloads the right version.

### 2. Get the code and install

```sh
git clone <repo-url> larry && cd larry
uv sync            # installs Python 3.13 + dev tools into .venv
uv run pytest      # should show 1 passed
```

`make` is optional (macOS/Linux ship it; on Windows use the `uv run` commands
directly, or `winget install GnuWin32.Make`). Equivalent commands:

```sh
uv run ruff check .      # lint
uv run ruff format .     # format
uv run ty check          # types
uv run pytest            # tests
```

### 3. Editor

Install [VS Code](https://code.visualstudio.com/) with the Python and Ruff
extensions, and choose the `.venv` interpreter when prompted.

### Troubleshooting

- Windows `running scripts is disabled`: run PowerShell as your user and use the `-ExecutionPolicy ByPass` command above.
- `uv: command not found`: restart the terminal so PATH updates.

## Layout

- `lessons/` — numbered lessons and the syllabus
- `src/larry/` — code the learner writes and reads
- `tests/` — pytest tests; write the test first, then make it pass

## Daily commands

| Command | Does |
|---|---|
| `uv run python file.py` | run a script |
| `uv add <pkg>` | add a dependency |
| `make fmt` | format and autofix |
| `make check` | lint, type-check, test |
