"""List utility functions."""

__author__ = "730306940"


def all(n: list[int], number: int) -> bool:
    """Testing if all integers in a list are the same as the input integer."""
    i: int = 0
    state: bool = True
    while i < len(n):
        if n[i] != number:
            state = not True
        i = i + 1
    return(state)


def is_equal(origin: list[int], compare: list[int]) -> bool:
    """Testing to see if two lists are the exact same."""


def max(input: list[int]) -> int:
    """Finding the largest number in a list of integers."""
    x: int = 0
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        if input[x]