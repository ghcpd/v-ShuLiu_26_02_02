import pathlib

import pytest

from prettytable_pr78_demo import format_table

try:  # Python 3.11+ has tomllib in the stdlib
    import tomllib  # type: ignore[attr-defined]
except ModuleNotFoundError:  # pragma: no cover - fallback for 3.10
    import tomli as tomllib  # type: ignore[no-redef]


PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
PYPROJECT = PROJECT_ROOT / "pyproject.toml"


def load_pyproject():
    return tomllib.loads(PYPROJECT.read_text(encoding="utf8"))


def test_business_format_table_typical_case():
    out = format_table(headers=["a", "b"], rows=[[1, 2], ["x", None]])
    assert out == ["a, b", "1, 2", "x, None"]


def test_business_format_table_rejects_empty_headers():
    with pytest.raises(ValueError, match="headers must not be empty"):
        format_table(headers=[], rows=[[1]])


def test_self_check_pyproject_invariants():
    data = load_pyproject()

    classifiers = data.get("project", {}).get("classifiers", [])
    assert all("Programming Language :: Python :: 2" not in c for c in classifiers)

    universal = data.get("tool", {}).get("wheel", {}).get("universal", False)
    assert universal is False

    versions = data.get("tool", {}).get("ci", {}).get("python-versions", [])
    assert "3.9" in versions

    profile = data.get("tool", {}).get("isort", {}).get("profile")
    assert profile == "black"
