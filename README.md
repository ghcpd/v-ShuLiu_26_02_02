# prettytable-pr78-demo

Minimal demo project focused on maintenance tasks:
- Drop Python 2 metadata (no universal wheel).
- Ensure CI targets include Python 3.9+.
- Align isort with the Black profile.
- Keep the tiny business function (`format_table`) unchanged and covered by tests.

## ✅ What changed in this maintenance round
- **Packaging metadata**: removed Python 2 classifiers; added Python 3-only classifiers (`Programming Language :: Python :: 3 :: Only`).
- **Wheel config**: `tool.wheel.universal = false` (project is Python 3 only).
- **CI targets**: `tool.ci.python-versions` now includes **"3.9"** (plus 3.8, 3.10).
- **isort**: configured with `profile = "black"`.
- **Self-check tests**: added config assertions and business-function coverage in `tests/`.

## 🐍 Environment setup (Windows PowerShell)
```powershell
# from the project root
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

> 💡 Deactivate later with `deactivate`.

## 📦 Install dependencies
```powershell
pip install -r requirements.txt
```

## ✅ Run self-checks
```powershell
pytest
```

These tests verify:
- No Python 2 classifiers remain.
- Wheel is not marked universal.
- CI matrix includes Python 3.9.
- isort uses the Black profile.
- `format_table` behaves correctly (happy path + error on empty headers).

## 📁 Project layout
```
pyproject.toml       # metadata, wheel, ci, isort config
requirements.txt     # test + tomli/tomllib dependency
src/prettytable_pr78_demo/__init__.py  # format_table business logic
tests/               # configuration and behavior self-checks
```

## 🔧 Optional tooling
- `isort .` (will use the Black profile per `pyproject.toml`).
- `black .` (not a required dependency here, but config is compatible).

No structured report files (e.g., JSON reports) are produced by default.
