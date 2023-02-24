"""EX04 - 'list' Utility Functions - A bunch of random functions."""

__author__ = "730486147"


def all(numbers: list[int], value: int) -> bool:
    """Checks if all numbers in a list are the same"""
    idx: int = 0
    while idx < len(numbers):
        if numbers[idx] != value:
            return (False)
        idx += 1
    return (True)


def max(input: list[int]) -> int:
    """Finds the maximum value in a list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    idx2: int = 0
    highest: int = input[0]
    while idx2 < (len(input)-1):
        if highest < input[idx2 + 1]:
            highest = input[idx2 + 1]
        idx2 += 1
    return (highest)


def is_equal(lst1: list[int], lst2: list[int]) -> bool:
    """Checks if two lists are the same"""
    if len(lst1) != len(lst2):
        return (False)
    idx3: int = 0
    while idx3 < len(lst1):
        if lst1[idx3] != lst2[idx3]:
            return (False)
        idx3 += 1
    return True