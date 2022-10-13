"""EX 05 Tests - Test the list utility functions."""

__author__ = "730557757"


from utils import only_evens
from utils import sub
from utils import concat


"""Tests for the only_evens function."""


def test_only_evens_empty() -> None:
    """Tests an empty list in only_evens."""
    numbers: list[int] = []
    assert only_evens(numbers) == []


def test_only_evens_one() -> None:
    """Tests a list with just one even integer in only_evens."""
    numbers: list[int] = [1, 2, 3, 5]
    assert only_evens(numbers) == [2]


def test_only_evens_multiple() -> None:
    """Tests a list of multiple integers in only_evens."""
    numbers: list[int] = [6, 2, 4, 10, 8, 14]
    assert only_evens(numbers) == [6, 2, 4, 10, 8, 14]


"""Tests for the concat function."""


def test_concat_empty() -> None:
    """Tests an empty list in concat."""
    first_list: list[int] = []
    second_list: list[int] = []
    assert concat(first_list, second_list) == []


def test_concat_single() -> None:
    """Tests a list with just one integer and another empty list in concat."""
    first_list: list[int] = [10]
    second_list: list[int] = []
    assert concat(first_list, second_list) == [10]


def test_concat_multiple() -> None:
    """Tests two lists of multiple integers in concat."""
    first_list: list[int] = [1, 2, 3, 6, 8, 9]
    second_list: list[int] = [3, 7, 10, 8]
    assert concat(first_list, second_list) == [1, 2, 3, 6, 8, 9, 3, 7, 10, 8]


"""Tests for the sub function."""


def test_sub_empty() -> None:
    """Tests an empty list in sub."""
    sub_list: list[int] = []
    start_index: int = 0
    end_index: int = 9
    assert sub(sub_list, start_index, end_index) == []


def test_sub_all() -> None:
    """Tests a list with all integers contained in the range in sub."""
    sub_list: list[int] = [1, 2, 3, 6, 8, 9]
    start_index: int = 0
    end_index: int = 9
    assert sub(sub_list, start_index, end_index) == [1, 2, 3, 6, 8, 9]


def test_sub_shortened() -> None:
    """Tests a list of integers with only some within the range in sub."""
    sub_list: list[int] = [1, 2, 3, 6, 8, 9]
    start_index: int = 0
    end_index: int = 3
    assert sub(sub_list, start_index, end_index) == [1, 2, 3]
