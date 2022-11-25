"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730557757"


class Simpy:
    """Simpler, single dimension implementation of NumPy."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initialize the values attribute of Simpy to the argument passed in."""
        self.values = values

    def __repr__(self) -> str:
        """Gives a string representation of a Simpy object."""
        return f"Simpy({self.values})"

    def fill(self, value: float, n: int) -> None:
        """Fill a Simpy's values with a specific number of repeating values."""
        if len(self.values) == n:
            for i in range(n):
                self.values[i] = value
        if len(self.values) > n:
            for i in range(n):
                self.values[i] = value
            for i in range(n, len(self.values)):
                self.values.pop()
        if len(self.values) < n:
            for i in range(len(self.values)):
                self.values[i] = value
            for i in range(len(self.values), n):
                self.values.append(value)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values attribute with range of values in terms of floats."""
        assert step != 0.0
        i: int = 0
        self.values.append(start)
        while self.values[i] != (stop - step):
            self.values.append(self.values[i] + step)
            i += 1

    def sum(self) -> float:
        """Compute and return the sum of all items in the values attribute."""
        result: float = 0.0
        for value in self.values:
            result += value
        return result

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add the ability to use the addition operator (+) in conjunction with Simpy objects and floats."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        else:
            for value in self.values:
                result.values.append(value + rhs)
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add the ability to use the power operator (**) in conjunction with Simpy objects and floats."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        else:
            for value in self.values:
                result.values.append(value ** rhs)
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Add the ability to produce a mask, or a list[bool], based on the equality of each item in the values attribute with some other Simpy or float."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        else:
            for value in self.values:
                if value == rhs:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Add the ability to produce a mask, or a list[bool], based on the greater than relationship between each item in the values attribute with some other Simpy or float."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        else:
            for value in self.values:
                if value > rhs:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Add the ability to use the subscription operator with Simpy objects and to filter with a mask."""
        if isinstance(rhs, int):
            for value in self.values:
                if value > rhs:
                    result: float = self.values[rhs]
        else:
            result: Simpy = Simpy([])
            for i in range(len(self.values)):
                if rhs[i] is True:
                    result.values.append(self.values[i])
        return result