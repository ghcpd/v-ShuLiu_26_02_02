"""Test business logic to ensure it still works correctly after configuration changes."""

from prettytable_pr78_demo import format_table


def test_format_table_basic():
    """Test basic table formatting functionality."""
    headers = ["Name", "Age", "City"]
    rows = [
        ["Alice", 30, "New York"],
        ["Bob", 25, "Los Angeles"],
    ]
    
    result = format_table(headers, rows)
    
    assert len(result) == 3, "Should have header + 2 data rows"
    assert result[0] == "Name, Age, City"
    assert result[1] == "Alice, 30, New York"
    assert result[2] == "Bob, 25, Los Angeles"


def test_format_table_single_row():
    """Test table formatting with a single row."""
    headers = ["ID", "Value"]
    rows = [
        [1, "test"],
    ]
    
    result = format_table(headers, rows)
    
    assert len(result) == 2, "Should have header + 1 data row"
    assert result[0] == "ID, Value"
    assert result[1] == "1, test"


def test_format_table_empty_rows():
    """Test table formatting with no data rows."""
    headers = ["Column1", "Column2"]
    rows = []
    
    result = format_table(headers, rows)
    
    assert len(result) == 1, "Should have only header"
    assert result[0] == "Column1, Column2"


def test_format_table_empty_headers_raises():
    """Test that empty headers raise a ValueError."""
    headers = []
    rows = []
    
    try:
        format_table(headers, rows)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "headers must not be empty" in str(e)


def test_format_table_with_various_types():
    """Test table formatting with different data types."""
    headers = ["String", "Number", "Float", "Bool"]
    rows = [
        ["test", 42, 3.14, True],
        ["data", 0, -1.5, False],
    ]
    
    result = format_table(headers, rows)
    
    assert len(result) == 3
    assert result[0] == "String, Number, Float, Bool"
    assert result[1] == "test, 42, 3.14, True"
    assert result[2] == "data, 0, -1.5, False"
