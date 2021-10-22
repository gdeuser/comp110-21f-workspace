"""Unit tests for dictionary functions."""


from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730306940"


def test_invert_empty() -> None:
    """Testing for empty dictionary."""
    og: dict[str, str] = dict()
    assert invert(og) == dict()


def test_invert_three_key() -> None:
    """Testing with three keys."""
    og: dict[str, str] = {"grace": "elizabeth", "mark": "deuser", "kathy": "reilly"}
    assert invert(og) == {"elizabeth": "grace", "deuser": "mark", "reilly": "kathy"}


def test_invert_two_key() -> None:
    """Testing with two keys."""
    og: dict[str, str] = {"grace": "deuser", "kathy": "reilly"}
    assert invert(og) == {"deuser": "grace", "reilly": "kathy"}


def test_favorite_color_empty() -> None:
    """Testing with an empty dictionary."""
    color: dict[str, str] = dict()
    assert favorite_color(color) == ""


def test_favorite_color_tie() -> None:
    """Testing for a tie with the colors."""
    color: dict[str, str] = {"grace": "green", "blake": "yellow", "mark": "red"}
    assert favorite_color(color) == "green"


def test_favorite_color_winner() -> None:
    """Testing with a winning color."""
    color: dict[str, str] = {"grace": "green", "blake": "blue", "mark": "red", "kathy": "blue"}
    assert favorite_color(color) == "blue"


def test_count_empty() -> None:
    """Testing for this program with an empty list."""
    start: list[str] = []
    assert count(start) == dict()


def test_count_not_repeating() -> None:
    """Testing for nonrepeating list items."""
    start: list[str] = ["red", "orange", "yellow"]
    assert count(start) == {"red": 1, "orange": 1, "yellow": 1}


def test_count_repeating() -> None:
    """Testing for a list with repeated items."""
    start: list[str] = ["red", "orange", "red", "yellow", "red"]
    assert count(start) == {"red": 3, "orange": 1, "yellow": 1}