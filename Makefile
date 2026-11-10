.PHONY: setup test lint fmt types check verify-solutions
setup:
	uv sync
test:
	uv run pytest
lint:
	uv run ruff check .
fmt:
	uv run ruff format . && uv run ruff check --fix .
types:
	uv run ty check src tests solutions
check: lint types test

verify-solutions:
	uv run python scripts/verify_solutions.py
