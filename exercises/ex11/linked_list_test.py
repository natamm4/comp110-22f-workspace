"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last
from exercises.ex11.linked_list import Node, value_at
from exercises.ex11.linked_list import Node, max
from exercises.ex11.linked_list import Node, linkify
from exercises.ex11.linked_list import Node, scale

__author__ = "730557757"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Value_at of an empty list should raise an IndexError."""
    with pytest.raises(IndexError):
        value_at(None, 0)


def test_value_at_index_zero() -> None:
    """Value_at should return the data of the current Node if index is 0."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 0) == 1


def test_max_empty() -> None:
    """Max of an empty list should raise a ValueError."""
    with pytest.raises(ValueError):
        max(None)


def test_max_reg() -> None:
    """Max should return the maximum data value in the linked list."""
    linked_list = Node(100, Node(42, Node(3, None)))
    assert max(linked_list) == 100


def test_linkify_empty() -> None:
    """Linkify should return a linked list of these nodes."""
    items = []
    assert linkify(items) == None

def test_linkify_end() -> None:
    """Linkify should return a linked list of these nodes."""
    items = [10, 20, 30, 40]
    assert str(linkify(items)) == "10 -> 20 -> 30 -> 40 -> None"


def test_scale_empty() -> None:
    """Scale should return None if head is None."""
    linked_list = None
    assert scale(linked_list, 2) == None


def test_scale_reg() -> None:
    """Scale should return a linked list of each node multiplied by the factor."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert str(scale(linked_list, 3)) == "30 -> 60 -> 90 -> None"