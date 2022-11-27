"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730557757"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly-linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"

    
def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    else:
        if head.next is None:
            return head.data
        else:
            return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Returns the data of the Node stored at the given index, or raises an IndexError if the index doesn't exist."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return head.data
    else:
        return value_at(head.next, index - 1)


def max(head: Optional[Node]) -> int:
    """Returns the max data value in the linked list, or raises a ValueError if the linked list is empty."""
    if head is None:
        raise ValueError("max cannot be called with None")
    elif head.next is None:
        return head.data
    else:
        current: int = head.data
        m: int = max(head.next)
        if m > current:
            return m
        else:
            return current


def linkify(items: list[int]) -> Optional[Node]:
    """Returns a Linked List of Nodes with the same values in the same order as the input list."""
    if items == []:
        return None
    elif len(items) == 1:
        return Node(items[0], None)
    else:
        return Node(items[0], linkify(items[1:]))


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Returns a new linked list of Nodes where each value in the original list is multiplied by the scaling factor."""
    if head is None:
        return None
    elif head.next is None:
        return Node(head.data * factor, None)
    else:
        return Node(head.data * factor, scale(head.next, factor))