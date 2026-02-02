# prettytable-pr78-demo

A minimal Python project demonstrating maintenance tasks related to packaging configuration, CI/CD setup, and code style tooling.

## Project Description

This project serves as a maintenance task demonstration focused on:
- Removing Python 2 support declarations from packaging configuration
- Updating CI target Python versions to include Python 3.9
- Configuring isort to use the Black profile
- Ensuring all self-check tests pass to verify configuration changes

The project includes a simple `format_table` function for CSV-like table formatting, along with comprehensive tests to validate both business logic and configuration settings.

## Maintenance Changes Applied

The following maintenance tasks have been completed:

1. **Packaging Configuration**: Removed Python 2.7 classifier and set `universal = false` in wheel configuration
2. **CI Configuration**: Added Python 3.9 to the list of target Python versions
3. **Code Style**: Configured isort to use the `black` profile
4. **Test Coverage**: Added business logic tests to ensure core functionality remains intact

## Prerequisites

- Windows 10 or later
- Python 3.10 or later

## Setup Instructions

### 1. Create Virtual Environment

Create a virtual environment in the project root directory:

```powershell
python -m venv .venv
```

### 2. Activate Virtual Environment

Activate the virtual environment using PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

Install the required development dependencies:

```powershell
pip install -r requirements.txt
```

### 4. Install the Package

Install the project in editable mode:

```powershell
pip install -e .
```

## Running Tests

To run all self-check tests:

```powershell
pytest
```

For verbose output:

```powershell
pytest -v
```

## Test Coverage

The test suite includes:

### Configuration Tests ([tests/test_config.py](tests/test_config.py))
- Verifies `pyproject.toml` exists
- Ensures no Python 2 classifiers are present
- Confirms wheel is not configured as universal
- Validates CI includes Python 3.9
- Checks isort uses the Black profile

### Business Logic Tests ([tests/test_business_logic.py](tests/test_business_logic.py))
- Tests basic table formatting functionality
- Tests single row formatting
- Tests empty rows handling
- Tests error handling for empty headers
- Tests formatting with various data types

## Expected Test Results

All tests should pass with output similar to:

```
================= 10 passed in 0.04s =================
```

## Project Structure

```
Claude-sonnet-4.5/
├── src/
│   └── prettytable_pr78_demo/
│       └── __init__.py          # Core business logic
├── tests/
│   ├── test_config.py           # Configuration self-checks
│   └── test_business_logic.py   # Business logic tests
├── pyproject.toml               # Project metadata and configuration
├── requirements.txt             # Development dependencies
├── prompt.txt                   # Task description
└── README.md                    # This file
```

## Success Criteria

✅ All tests pass successfully  
✅ No Python 2 support declared in packaging  
✅ Wheel is not configured as universal  
✅ CI configuration includes Python 3.9  
✅ isort configured to use Black profile  
✅ Business logic remains functionally correct
