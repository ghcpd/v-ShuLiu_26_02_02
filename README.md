# prettytable-pr78-demo

Small Python demo library plus configuration-focused tests.

This workspace is a maintenance exercise to:

- Remove Python 2-related packaging metadata and stop claiming a universal wheel.
- Ensure the (simplified) CI target versions include Python 3.9.
- Configure `isort` to use the Black profile.
- Add self-check tests that confirm the configuration is correct and that core business behavior still works.

## Setup (Windows / PowerShell)

Create and activate a virtual environment in the project root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Self-checks

Run the test suite (includes configuration self-check tests):

```powershell
pytest
```
