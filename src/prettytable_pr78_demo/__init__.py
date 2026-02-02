def format_table(headers, rows):
    """Return a very small CSV-like representation of a table.

    This is just to have some "real" code in the project; it is
    not the main focus of the maintenance task.
    """
    if not headers:
        raise ValueError("headers must not be empty")

    formatted_rows = []
    formatted_rows.append(", ".join(str(cell) for cell in headers))
    for row in rows:
        formatted_rows.append(", ".join(str(cell) for cell in row))
    return formatted_rows
