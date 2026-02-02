import pathlib
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from prettytable_pr78_demo import format_table


def test_format_table_basic():
    headers = ["Name", "Age"]
    rows = [["Alice", 30], ["Bob", 25]]
    result = format_table(headers, rows)
    assert result == ["Name, Age", "Alice, 30", "Bob, 25"]


def test_format_table_no_rows_returns_header_only():
    headers = ["H1", "H2"]
    rows = []
    result = format_table(headers, rows)
    assert result == ["H1, H2"]


def test_format_table_empty_headers_raises():
    with pytest.raises(ValueError):
        format_table([], [[1, 2]])
