"""EX 07 Tests - Test the list dictionary functions."""

__author__ = "730557757"


from dictionary import invert
from dictionary import favorite_color
from dictionary import count
import pytest


"""Tests for the invert function."""


def test_invert_empty() -> None:
    """Tests an empty dictionary in invert."""
    original: dict[str, str] = {}
    assert invert(original) == {}


def test_invert_multiple() -> None:
    """Tests a dictionary in invert."""
    original: dict[str, str] = {'pineapple': 'fruit', 'labrador': 'dog', 'daisy': 'flower'}
    assert invert(original) == {'fruit': 'pineapple', 'dog': 'labrador', 'flower': 'daisy'}


def test_invert_singular() -> None:
    """Tests a dictionary in invert."""
    original: dict[str, str] = {'yard': 'grass'}
    assert invert(original) == {'grass': 'yard'}


def test_invert_keyerror() -> None:
    """Tests if the KeyError is being raised in invert."""
    with pytest.raises(KeyError):
        original = {'natalie': 'ammerman', 'christina': 'ammerman'}
        invert(original)


"""Tests for the favorite_color function."""


def test_favorite_color_empty() -> None:
    """Tests an empty dictionary in favorite_color."""
    preferences: dict[str, str] = {}
    assert favorite_color(preferences) == ""


def test_favorite_color_second() -> None:
    """Tests a dictionary in favorite_color."""
    preferences: dict[str, str] = {'Fred': 'purple', 'Christina': 'green', 'Cole': 'orange', 'William': 'orange'}
    assert favorite_color(preferences) == "orange"


def test_favorite_color_third() -> None:
    """Tests a dictionary in favorite_color."""
    preferences: dict[str, str] = {'Teddy': 'teal', 'Francesca': 'teal', 'Ruby': 'teal'}
    assert favorite_color(preferences) == "teal"


"""Tests for the count function."""


def test_count_empty() -> None:
    """Tests an empty list in count."""
    words: list[str] = ()
    assert count(words) == {}


def test_count_second() -> None:
    """Tests a list in count."""
    words: list[str] = ('fruit', 'pebbles', 'pebbles')
    assert count(words) == {'fruit': 1, 'pebbles': 2}


def test_count_third() -> None:
    """Tests a list in count."""
    words: list[str] = ('fruit', 'pebbles', 'pebbles', 'fruit', 'orange', 'grass')
    assert count(words) == {'fruit': 2, 'pebbles': 2, 'orange': 1, 'grass': 1}