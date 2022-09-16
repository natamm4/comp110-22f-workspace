"""EX 04 - Utils."""

__author__ = "730557757"


def all(multiple: list[int], single: int) -> bool: 
    """Returns True if the single integer entered is equal to all elements in the list, and False if it does not."""
    if len(multiple) == 0:
        return False
    index: int = 0
    while index < len(multiple):
        if multiple[index] == single:
            index += 1
        else:
            return False
    return True


def max(max_list: list[int]) -> int:
    """Returns the largest number in the list."""
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty List")
    the_max: int = max_list[0]
    where: int = 1
    while where < len(max_list):
        if max_list[where] > the_max:
            the_max = max_list[where]
        else:
            where += 1
    return the_max


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Returns True if the lists are deeply equal, and False if they are not."""
    if len(first_list) == 0 and len(second_list) != 0 or len(second_list) == 0 and len(first_list) != 0:
        return False
    if len(first_list) != len(second_list):
        return False
    this_index: int = 0
    while this_index < len(first_list) and this_index < len(second_list):
        if first_list[this_index] == second_list[this_index]:
            this_index += 1
        else: 
            return False
    return True