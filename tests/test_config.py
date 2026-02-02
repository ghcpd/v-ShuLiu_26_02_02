import pathlib

try:  # Python 3.11+ has tomllib in the stdlib
    import tomllib  # type: ignore[attr-defined]
except ModuleNotFoundError:  # pragma: no cover - fallback for 3.10
    import tomli as tomllib  # type: ignore[no-redef]


PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
PYPROJECT = PROJECT_ROOT / "pyproject.toml"


def load_pyproject():
    text = PYPROJECT.read_text(encoding="utf8")
    return tomllib.loads(text)


def test_pyproject_exists():
    assert PYPROJECT.is_file(), "pyproject.toml should exist at project root"


def test_project_is_python3_only():
    """Project metadata should no longer claim Python 2 support."""
    data = load_pyproject()
    classifiers = data.get("project", {}).get("classifiers", [])
    assert all(
        "Programming Language :: Python :: 2" not in c for c in classifiers
    ), "project classifiers must not claim Python 2 support"


def test_wheel_not_universal():
    """Wheel configuration should not be universal (Python 2 + 3)."""
    data = load_pyproject()
    universal = data.get("tool", {}).get("wheel", {}).get("universal", False)
    assert not universal, "wheel should not be configured as universal"


def test_ci_includes_python39():
    """The CI matrix should include Python 3.9."""
    data = load_pyproject()
    versions = data.get("tool", {}).get("ci", {}).get("python-versions", [])
    assert "3.9" in versions, "CI configuration should include Python 3.9"


def test_isort_uses_black_profile():
    """isort should use the Black profile to simplify config."""
    data = load_pyproject()
    profile = data.get("tool", {}).get("isort", {}).get("profile")
    assert profile == "black", "isort should use the Black profile"
