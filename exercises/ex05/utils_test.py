"""Unit tests for list utility functions."""


from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730306940"


def test_only_evens_empty() -> None:
    """Testing for empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_no_evens() -> None:
    """Testing for a list with no even numbers."""
    xs: list[int] = [1, 3, 5]
    assert only_evens(xs) == []


def test_only_evens_all_evens() -> None:
    """Testing for a list with only even numbers."""
    xs: list[int] = [2, 4, 6, 8]
    assert only_evens(xs) == [2, 4, 6, 8]


def test_sub_negative_start() -> None:
    """Testing for a negative starting number."""
    origin: list[int] = [1, 2, 3, 4, 5]
    assert sub(origin, -2, 3) == [1, 2, 3]


def test_sub_sinlge() -> None:
    """Testing for a returned list with a single int."""
    origin: list[int] = [1, 2, 3, 4]
    assert sub(origin, 0, 1) == [1]


def test_sub_whole_list() -> None:
    """Testing for a returned list of the full original list."""
    origin: list[int] = [1, 2, 3, 4]
    assert sub(origin, 0, 5) == [1, 2, 3, 4]


def test_concat_empty_arguments() -> None:
    """Testing for empty lists."""
    first: list[int] = []
    second: list[int] = []
    assert concat(first, second) == []


def test_concat_empty_second() -> None:
    """Testing for one empty list."""
    first: list[int] = [1, 2, 3]
    second: list[int] = []
    assert concat(first, second) == [1, 2, 3]


def test_concat_full_lists() -> None:
    """Testing for two full lists."""
    first: list[int] = [1, 3, 5]
    second: list[int] = [2, 4, 6]
    assert concat(first, second) == [1, 3, 5, 2, 4, 6]