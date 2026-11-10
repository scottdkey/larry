"""Exercise: read and manipulate pyproject.toml data.

Run tests: uv run pytest exercises/25_packaging_tooling
"""

import re  # noqa: F401  (handy for the dependency and name helpers)
import tomllib  # noqa: F401


def project_name(text: str) -> str:
    """Return [project].name from pyproject TOML text."""
    raise NotImplementedError


def dependency_names(text: str) -> list[str]:
    """Return bare, lowercased dependency names from [project].dependencies.

    'httpx>=0.28' -> 'httpx'; 'Typer[all]>=0.9' -> 'typer';
    'foo; python_version<"3.13"' -> 'foo'. Keep file order; [] if none.
    """
    raise NotImplementedError


def normalize_name(name: str) -> str:
    """PEP 503 normalization: lowercase, runs of '-', '_', '.' become one '-'."""
    raise NotImplementedError


def bump_version(version: str, part: str) -> str:
    """Bump 'MAJOR.MINOR.PATCH'; part is 'major', 'minor' or 'patch'.

    Lower parts reset to 0. An unknown part raises ValueError.
    """
    raise NotImplementedError


def ruff_rules(text: str) -> list[str]:
    """Return [tool.ruff.lint].select, or [] if it is not configured."""
    raise NotImplementedError
