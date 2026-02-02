import pathlib
import sys

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

try:  # Python 3.11+ has tomllib in the stdlib
    import tomllib  # type: ignore[attr-defined]
except ModuleNotFoundError:  # pragma: no cover - fallback for 3.10
    import tomli as tomllib  # type: ignore[no-redef]

from prettytable_pr78_demo import format_table

PYPROJECT = PROJECT_ROOT / "pyproject.toml"


def load_pyproject():
    return tomllib.loads(PYPROJECT.read_text(encoding="utf8"))


def test_classifiers_python3_only():
    data = load_pyproject()
    classifiers = data.get("project", {}).get("classifiers", [])
    assert classifiers, "project classifiers should be declared"
    assert any(
        c.endswith("Python :: 3 :: Only") for c in classifiers
    ), "project classifiers should clearly state Python 3 only"
    assert all(
        "Programming Language :: Python :: 2" not in c for c in classifiers
    ), "project classifiers must not claim Python 2 support"


def test_wheel_universal_explicitly_false():
    data = load_pyproject()
    universal = data.get("tool", {}).get("wheel", {}).get("universal")
    # Explicit False is clearer than omitting the setting; baseline was True.
    assert universal is False, "wheel.universal should be explicitly false"


def test_ci_matrix_includes_python39():
    data = load_pyproject()
    versions = data.get("tool", {}).get("ci", {}).get("python-versions", [])
    assert "3.9" in versions, "CI configuration should include Python 3.9"


def test_isort_black_profile():
    data = load_pyproject()
    profile = data.get("tool", {}).get("isort", {}).get("profile")
    assert profile == "black", "isort should be configured with the Black profile"


def test_format_table_happy_path():
    headers = ["A", "B"]
    rows = [[1, 2], [3, "x"]]
    assert format_table(headers, rows) == ["A, B", "1, 2", "3, x"]


def test_format_table_requires_headers():
    with pytest.raises(ValueError):
        format_table([], [])


# Local import to avoid hard dependency on pytest in library code
import pytest  # noqa: E402, isort:skip
