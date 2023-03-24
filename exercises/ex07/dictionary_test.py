"""Testing dictionary functions."""


__author__ = "730486147"


from exercises.ex07.dictionary import invert, favorite_color, count


def test_long() -> None:
    """Tests the invert function on a long list."""
    test_dict: dict[str, str] = {'a': 'z', 'b' : 'y', 'c': 'x'}
    assert (invert(test_dict)) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_short() -> None:
    """Tests the invert function on a short list."""
    test_dict: dict[str, str] = {'apple': 'cat'}
    assert(invert(test_dict)) == {'cat': 'apple'}


def test_empty() -> None:
    """Tests when a list will have duplicate keys."""
    test_dict: dict[str, str] = {}
    assert(invert(test_dict)) == {}


def test_max() -> None:
    """Tests the favorite_colors functions when there is a clear maximum."""
    test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert (favorite_color(test_dict)) == "blue"


def test_equal() -> None:
    """Tests when there are multiple colors with the same count."""
    test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue"}
    assert (favorite_color(test_dict)) == "yellow"


def test_one() -> None:
    """Tests when there is only one key-value pair."""
    test_dict: dict[str, str] = {"Marc": "yellow"}
    assert (favorite_color(test_dict)) == "yellow"


def test_ones() -> None:
    """Tests when there is one of each string."""
    test_dict: list[str] = ['Bana', 'Kandala', 'Ranesh']
    assert (count(test_dict)) == {'Bana': 1, 'Kandala': 1, 'Ranesh': 1}


def test_oneword() -> None:
    """Tests when there is only one word in the list that is repeated."""
    test_dict: list[str] = ['Bana', 'Bana', 'Bana']
    assert (count(test_dict)) == {'Bana': 3}


def test_nowords() -> None:
    """Tests when there are no words in the list."""
    test_dict: list[str] = []
    assert (count(test_dict)) == {}