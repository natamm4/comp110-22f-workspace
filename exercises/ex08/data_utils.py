"""Dictionary related utility functions."""

__author__ = "730557757"

from csv import DictReader


# Define your functions below
def read_csv_rows(path: str) -> list[dict[str, str]]:
    """Read an entire CSV of data into a list of rows, each row represented as a dict[str, str]."""
    result: list[dict[str, str]] = []
    file_handle = open(path, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column whose name is the second parameter."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table represented as a list of rows (e.g. list[dict[str, str]]) into one represented as a dictionary of columns (e.g. dict[str, list[str]])."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = table[0]
    for column in first_row:
        list_cols: list[str] = column_values(table, column)
        result[column] = list_cols
    return result


def head(no_mutate: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with only the first `N` (a parameter) rows of data for each column."""
    result: dict[str, list[str]] = {}
    if n >= len(no_mutate):
        return no_mutate
    for column in no_mutate:
        items: list[str] = []
        for i in range(n):
            item: str = no_mutate[column][i]
            items.append(item)
        result[column] = items
    return result


def select(no_mutate: dict[str, list[str]], cols: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in cols:
        result[column] = no_mutate[column]
    return result


def concat(first: dict[str, list[str]], second: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in first:
        result[column] = first[column]
    for column in second:
        if column in result:
            result[column] += second[column]
        else:
            result[column] = second[column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Given a `list[str]`, this function will produce a `dict[str, int]` where each key is a unique value in the given list and each value associated is the _count_ of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for value in values:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result