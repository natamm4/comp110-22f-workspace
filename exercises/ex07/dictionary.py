"""EX 07 - Continue practicing with dictionary functions."""

__author__ = "730557757"


def invert(original: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of strings associated with other strings, switch the keys and the values."""
    inverted: dict[str, str] = {}
    for key in original:
        if original[key] in inverted:
            raise KeyError("Replicate key not allowed!")
        inverted[original[key]] = key
    return inverted


def favorite_color(preferences: dict[str, str]) -> str:
    """Given a dictionary of people and their favorite colors, return the most popular color."""
    color: str = ""
    amount: dict[str, int] = {}
    most_popular: int = 0
    for person in preferences:
        if preferences[person] in amount:
            amount[preferences[person]] += 1
        else:
            amount[preferences[person]] = 1
    for key in amount:
        if amount[key] == most_popular:
            color = list(amount)[0]
        if amount[key] > most_popular:
            color = key
            most_popular = amount[key]
    return color


def count(words: list[str]) -> dict[str, int]:
    """Given a list of strings, produce a dictionary where each key is a value from the list and each value counts the number of appearances that its associated value made in the list."""
    result: dict[str, int] = {}
    for word in words:
        if word in result:
            result[word] += 1
        else: 
            result[word] = 1
    return result