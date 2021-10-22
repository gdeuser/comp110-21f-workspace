"""Practice with dictionaries."""

__author__ = "730306940"


def invert(og: dict[str, str]) -> dict[str, str]:
    """Inverting the keys and values of a dictionary."""
    result: dict[str, str] = dict()
    for key in og:
        if og[key] in result:
            raise KeyError("Cannot have a repeating key value.")
        result[og[key]] = key
    return result


def favorite_color(color: dict[str, str]) -> str:
    """Finding the most favorite color in a dictionary."""
    counting: dict[str, int] = dict()
    for key in color:
        if color[key] in counting:
            counting[color[key]] += 1
        else:
            counting[color[key]] = 1
    current_max: int = 0
    current_max_color: str = ""
    for key in counting:
        if counting[key] > current_max:
            current_max = counting[key]
            current_max_color = key
    return current_max_color


def count(start: list[str]) -> dict[str, int]:
    """Putting items in a list into a dictionary."""
    counter: dict[str, int] = dict()
    for item in start:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    return counter