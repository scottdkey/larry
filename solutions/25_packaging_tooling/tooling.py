"""Exercise: read and manipulate pyproject.toml data."""

import re
import tomllib


def project_name(text: str) -> str:
    """Return [project].name from pyproject TOML text."""
    return tomllib.loads(text)["project"]["name"]


def dependency_names(text: str) -> list[str]:
    """Return bare, lowercased dependency names (no versions, extras or markers).

    Covers [project].dependencies only, in file order.
    """
    deps = tomllib.loads(text).get("project", {}).get("dependencies", [])
    names = []
    for dep in deps:
        match = re.match(r"[A-Za-z0-9][A-Za-z0-9._-]*", dep)
        if match:
            names.append(match.group().lower())
    return names


def normalize_name(name: str) -> str:
    """PEP 503 normalization: lowercase, runs of -_. become a single '-'."""
    return re.sub(r"[-_.]+", "-", name).lower()


def bump_version(version: str, part: str) -> str:
    """Bump 'MAJOR.MINOR.PATCH'; part is 'major', 'minor' or 'patch'.

    Lower parts reset to 0. Unknown part raises ValueError.
    """
    major, minor, patch = (int(p) for p in version.split("."))
    match part:
        case "major":
            return f"{major + 1}.0.0"
        case "minor":
            return f"{major}.{minor + 1}.0"
        case "patch":
            return f"{major}.{minor}.{patch + 1}"
        case _:
            raise ValueError(f"unknown part: {part!r}")


def ruff_rules(text: str) -> list[str]:
    """Return [tool.ruff.lint].select, or [] if it is not configured."""
    tool = tomllib.loads(text).get("tool", {})
    return tool.get("ruff", {}).get("lint", {}).get("select", [])
