# prettytable-pr78-demo

Minimal demo project focused on maintenance tasks: drop Python 2 claims, disable universal wheels, include Python 3.9 in CI targets, configure isort with the Black profile, and ensure business behavior stays the same.

## Setup

### 1) Create and activate virtual environment (Windows PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2) Install dependencies
```powershell
pip install -r requirements.txt
```

## Self-check commands

Run pytest (includes configuration self-checks and business logic tests):
```powershell
pytest
```

> Notes:
> - Configuration tests verify: no Python 2 classifiers, wheel not universal, CI includes Python 3.9, isort uses Black profile.
> - Business logic tests verify `format_table` behavior for typical and edge cases.
