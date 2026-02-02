import pathlib
import sys

import pytest

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_ROOT))

from prettytable_pr78_demo import format_table


def test_format_table_typical():
    headers = ["a", "b"]
    rows = [[1, 2], [3, 4]]
    assert format_table(headers, rows) == ["a, b", "1, 2", "3, 4"]


def test_format_table_empty_headers_raises():
    with pytest.raises(ValueError, match="headers must not be empty"):
        format_table([], [[1]])
