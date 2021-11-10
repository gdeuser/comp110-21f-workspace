"""Utility functions."""

__author__ = "730306940"

from csv import DictReader


def read_csv_rows(file: str) -> list[dict[str, str]]:
    """Reading data from a file."""
    result: list[dict[str, str]] = []
    file_handle = open(file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce list of strings of all values in a column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table of list of rows into dictionary of columns."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(original: dict[str, list[str]], included_rows: int) -> dict[str, list[str]]:
    """Choose certain rows to include in a dictionary table."""
    result: dict[str, list[str]] = {}
    for title in original:
        if included_rows >= len(original[title]):
            return original
        else:
            values: list[str] = []
            i: int = 0
            while i < included_rows:
                item: str = original[title][i]
                values.append(item)
                i += 1
            result[title] = values
    return result


def select(unchanged_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Selecting certain columns out of a dictionary."""
    result: dict[str, list[str]] = {}
    for item in column_names:
        result[item] = unchanged_table[item]
    return result


def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Add two existing tables into a new dictionary."""
    result: dict[str, list[str]] = {}
    for key in table_one:
        result[key] = table_one[key]
    for key in table_two:
        existence: bool = key in result
        if existence is True:
            result[key] = table_one[key] + table_two[key]
        else:
            result[key] = table_two[key]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Counting the number of times a value appears."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def in_person_recommendation(start: dict[str, list[str]]) -> list[int]:
    """Taking all of the recommendation values for the Remote section."""
    section: list[str] = start["section"]
    would_recommend: list[str] = start["would_recommend"]
    recommend_in_person: list[int] = []
    i: int = 0
    y: int = 0
    while i < len(section):
        if section[i] == "In-Person":
            recommend_in_person.append(int(would_recommend[i]))
            y += 1
        i += 1
    return recommend_in_person


def remote_recommendation(start: dict[str, list[str]]) -> list[int]:
    """Taking all of the recommendation values for the Remote section."""
    section: list[str] = start["section"]
    would_recommend: list[str] = start["would_recommend"]
    recommend_remote: list[int] = []
    i: int = 0
    y: int = 0
    while i < len(section):
        if section[i] == "Remote":
            recommend_remote.append(int(would_recommend[i]))
            y += 1
        i += 1
    return recommend_remote


def average(n: list[int]) -> float:
    """Averaging all of the values in a list."""
    how_many: int = len(n)
    i = 0
    for item in n:
        i += item
    avg: float = i / how_many
    return avg