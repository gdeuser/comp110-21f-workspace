"""Unit tests for list utility functions."""


from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730306940"


def test_only_evens_empty() -> None:
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_no_evens() -> None:
    xs: list[int] = [1, 3, 5]
    assert only_evens(xs) == []


def test_only_evens_all_evens() -> None:
    xs: list[int] = [2, 4, 6, 8]
    assert only_evens(xs) == [2, 4, 6, 8]


def test_sub_negative_start() -> None:
    origin: list[int] = [1, 2, 3, 4, 5]
    assert sub(origin, -2, 3) == [1, 2, 3]


def test_sub_sinlge() -> None:
    origin: list[int] = [1, 2, 3, 4]
    assert sub(origin, 0, 1) == [1]


def test_sub_whole_list() -> None:
    origin: list[int] = [1, 2, 3, 4]
    assert sub(origin, 0, 5) == [1, 2, 3, 4]


def test_concat_empty_arguments() -> None:
    first: list[int] = []
    second: list[int] = []
    assert concat(first, second) == []


def test_concat_empty_second() -> None:
    first: list[int] = [1, 2, 3]
    second: list[int] = []
    assert concat(first, second) == [1, 2, 3]


def test_concat_full_lists() -> None:
    first: list[int] = [1, 3, 5]
    second: list[int] = [2, 4, 6]
    assert concat(first, second) == [1, 3, 5, 2, 4, 6]