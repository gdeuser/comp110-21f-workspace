"""List utility functions part 2."""

__author__ = "730306940"


def only_evens(n: list[int]) -> list[int]:
    """Finding only the evens in a given list."""
    start: int = 0
    even_list: list[int] = []
    while start < len(n):
        if n[start] % 2 == 0:
            even_list.append(int(n[start]))
        start += 1
    return(even_list)


def sub(origin: list[int], start: int, end: int) -> list[int]:
    """Creating a sublist from an orginal input list."""
    sublist: list[int] = []
    if origin == []:
        return origin
    if end > len(origin):
        end = len(origin)
    if start < origin[0]:
        start = 0
    while start < end:
        sublist.append(int(origin[start]))
        start += 1
    return sublist


def concat(first: list[int], second: list[int]) -> list[int]:
    """Concatenating two lists into a new list."""
    result: list[int]
    result = first + second
    return result


print(sub([], 1, 3))