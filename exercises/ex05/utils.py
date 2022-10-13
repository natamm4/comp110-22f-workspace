"""EX 05 - Continue building list utility functions."""

__author__ = "730557757"


def only_evens(numbers: list[int]) -> list[int]:
    """Return a new list with the even elements given a list of integers."""
    evens: list[int] = []
    where: int = 0
    while where < len(numbers):
        if numbers[where] % 2 == 0:
            evens.append(numbers[where])
            where += 1
        else:
            where += 1
    return evens


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Return a new list with all of the integers from the first list, followed by all of the integers from the second list."""
    third_list: list[int] = []
    third_list = first_list + second_list
    return third_list


def sub(sub_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Return a list of the integers in the list given that fall between the two indicies given."""
    new_list: list[int] = []
    where_index: int = 0
    if start_index < 0:
        start_index = 0
    if end_index > len(sub_list):
        end_index = len(sub_list)
    if len(sub_list) == 0 or start_index > len(sub_list) or end_index <= 0:
        return new_list
    while where_index < end_index:
        if where_index >= start_index and where_index < end_index:
            new_list.append(sub_list[where_index])
            where_index += 1
        else:
            where_index += 1
    return new_list
