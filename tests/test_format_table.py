import pytest

from prettytable_pr78_demo import format_table


def test_format_table_formats_headers_and_rows():
    headers = ["Name", "Age"]
    rows = [["Alice", 30], ["Bob", 25]]

    result = format_table(headers, rows)

    assert result == [
        "Name, Age",
        "Alice, 30",
        "Bob, 25",
    ]


def test_format_table_str_coercion_of_cells():
    headers = ["ID", "Active"]
    rows = [[123, True]]

    result = format_table(headers, rows)

    assert result == ["ID, Active", "123, True"]


def test_format_table_requires_headers():
    with pytest.raises(ValueError):
        format_table([], [])
