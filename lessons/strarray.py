"""Examples of "vectorized" operations via magic methods."""

from __future__ import annotations
from typing import Union


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items

    def __repr__(self) -> str:
        """Gives a str representation of a StrArray object."""
        return f"StrArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        result: StrArray = StrArray([])
        if isinstance(rhs, str):
            for item in self.items:
                result.items.append(item + rhs)
                # or:
                # item += rhs
                # result.items.append(item)
        else:
            assert len(self.items) == len(rhs.items)
            for i in range(len(self.items)):
                self.items[i] += rhs.items[i]
                result.items.append(self.items[i])
                # or:
                # result.items.append(self.items[i] + rhs.items[i])
        return result


a: StrArray = StrArray(["Armando", "Pete", "Leaky"])
b: StrArray = StrArray(["Bacot", "Nance", "Black"])
print(a)
print(a + "!")
print(a + " " + b)
print(b + ", " + a + "!")