# prettytable-pr78-demo

A minimal demo project showcasing maintenance tasks around packaging metadata, CI Python versions, and tooling alignment. The core library (`prettytable_pr78_demo`) provides a tiny `format_table` helper; the emphasis here is on cleaning configuration without changing business behavior.

## Maintenance goals addressed

- Remove Python 2 claims from packaging classifiers; project is Python 3-only.
- Stop publishing a universal (Py2+Py3) wheel; configure wheel as non-universal.
- Update CI target matrix to include Python 3.9 (and other Python 3 versions).
- Configure `isort` to use the Black profile for consistent imports.
- Add self-check tests verifying the above plus core business behavior.

## Setup

From the project root on Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

On POSIX shells:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Self-check commands

Run tests:

```bash
pytest
```

These tests verify:

- `pyproject.toml` no longer lists Python 2 classifiers.
- The wheel config is not marked `universal`.
- `tool.ci.python-versions` includes Python 3.9.
- `tool.isort.profile` is set to `black`.
- `format_table` still behaves correctly for typical and edge cases.

Optional (not required but aligned with configuration):

```bash
# Format imports according to the configured Black profile
isort .
```

No additional structured reports are produced by the self-checks.
