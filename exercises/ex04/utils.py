"""List utility functions."""

__author__ = "730306940"


def all(n: list[int], number: int) -> bool:
    """Testing if all integers in a list are the same as the input integer."""
    i: int = 0
    state: bool = True
    if len(n) == 0:
        state = False
    else:
        while i < len(n):
            if n[i] != number:
                state = False
            i = i + 1
    return(state)


def is_equal(origin: list[int], compare: list[int]) -> bool:
    """Testing to see if two lists are the exact same."""
    x: int = 0
    equality: bool = True
    if len(origin) != len(compare):
        equality = False
    else:
        if len(origin) != 0 and len(compare) != 0:
            while x < len(origin):
                if origin[x] != compare[x]:
                    equality = False
                x = x + 1
    return(equality)


def max(test: list[int]) -> int:
    """Finding the largest number in a list of integers."""
    x: int = 0
    current_max: int
    if len(test) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        current_max = test[x]
        x = x + 1
        while x < len(test):
            if current_max < test[x]:
                current_max = test[x]
            x = x + 1
    return(current_max)