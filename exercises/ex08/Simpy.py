"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730306940"


class Simpy:
    """Models Numpy object."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initialize a new Simpy object."""
        self.values = values

    def __str__(self) -> str:
        """Making a string representation of a Simpy."""
        return f"Simpy({self.values})"

    def fill(self, value: float, repeat: int) -> None:
        """Modifying object to repeat a float a certain amount of times."""
        self.values = []
        i: int = 0
        while i < repeat:
            self.values.append(value)
            i += 1
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in a range of values."""
        self.values = []
        assert step != 0.0
        if step > 0.0:
            next_value: float = start
            while next_value < stop:
                self.values.append(next_value)
                next_value += step
        else:
            next_value: float = start
            while next_value > stop:
                self.values.append(next_value)
                next_value += step

    def sum(self) -> float:
        """Calls the built-in sum function."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adding together a float or Simpy to create a new Simpy object."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Raising a Simpy to either a float or another Simpy to create new Simpy object."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Checking to see if values in a Simpy are equal to a float or values in another Simpy."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                result.append(value == rhs)
        else:
            assert len(self.values) == len(rhs.values)                
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] == rhs.values[i])
                i += 1
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Seeing if a Simpy is greater than obejcts in another Simpy or a float."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                result.append(value > rhs)
        else:
            assert len(self.values) == len(rhs.values)                
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] > rhs.values[i])
                i += 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Using subscription notation with Simpy."""
        result: Simpy = Simpy([])
        if isinstance(rhs, int):
            assert rhs < len(self.values) and rhs >= 0
            return self.values[rhs]
        else:
            assert len(self.values) == len(rhs)
            i: int = 0
            while i < len(self.values):
                if rhs[i] is True:
                    result.values.append(self.values[i])
                i += 1
            return result