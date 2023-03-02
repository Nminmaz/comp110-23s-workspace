"""EX05 pt. 2 - Testing Functions."""

__author__ = "730486147"


from exercises.ex05.utils import only_evens, sub, concat


def test_all_even() -> None:
    """Tests the case where all are even."""
    test_list: list[int] = [2, 4, 8]
    assert(only_evens(test_list)) == test_list


def test_some_even() -> None:
    """Tests the case where some are even."""
    test_list: list[int] = [2, 4, 3]
    assert(only_evens(test_list)) == [2, 4]


def test_all_odd() -> None:
    """Tests the case where all are odd."""
    test_list: list[int] = [2, 4, 3]
    assert(only_evens(test_list)) == [2, 4]


def test_full_lists() -> None:
    """Tests when the lists are both full."""
    test_list1: list[int] = [1, 2]
    test_list2: list[int] = [3, 4]
    assert concat(test_list1, test_list2) == [1, 2, 3, 4]


def test_one_full() -> None:
    """Tests when one list is empty and the other is full."""
    test_list1: list[int] = [1, 2]
    test_list2: list[int] = []
    assert concat(test_list1, test_list2) == [1, 2]


def test_empty_lists() -> None:
    """Tests when both lists are empty."""
    test_list1: list[int] = []
    test_list2: list[int] = []
    assert concat(test_list1, test_list2) == []


def test_in_domain() -> None:
    """Tests when the interval is in the set."""
    test_list = [10, 20, 30, 40]
    assert sub(test_list, 1, 3) == [20, 30]

def test_negative() -> None:
    """Tests when the start is negative."""
    test_list = [10, 20, 30, 40]
    assert sub(test_list, -1, 3) == [10, 20, 30]

def test_wrong_end() -> None:
    """Tests when the start is greater than the length."""
    test_list = [10, 20, 30, 40]
    assert sub(test_list, 4, 5) == []
