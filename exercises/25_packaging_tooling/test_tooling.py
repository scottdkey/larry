import pytest
from tooling import (
    bump_version,
    dependency_names,
    normalize_name,
    project_name,
    ruff_rules,
)

PYPROJECT = """
[project]
name = "larry"
version = "0.1.0"
dependencies = [
    "httpx>=0.28.1",
    "Typer[all]>=0.9",
    'tomli; python_version < "3.11"',
]

[tool.ruff.lint]
select = ["E", "F", "I"]
"""


def test_project_name():
    assert project_name(PYPROJECT) == "larry"


def test_dependency_names():
    assert dependency_names(PYPROJECT) == ["httpx", "typer", "tomli"]
    assert dependency_names('[project]\nname = "x"\n') == []


def test_normalize_name():
    assert normalize_name("Friendly_Bard") == "friendly-bard"
    assert normalize_name("a.b__c--d") == "a-b-c-d"


def test_bump_version():
    assert bump_version("1.2.3", "patch") == "1.2.4"
    assert bump_version("1.2.3", "minor") == "1.3.0"
    assert bump_version("1.2.3", "major") == "2.0.0"
    with pytest.raises(ValueError):
        bump_version("1.2.3", "huge")


def test_ruff_rules():
    assert ruff_rules(PYPROJECT) == ["E", "F", "I"]
    assert ruff_rules('[project]\nname = "x"\n') == []
