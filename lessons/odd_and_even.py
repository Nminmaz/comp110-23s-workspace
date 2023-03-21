"""Odd and even practice problem."""


__author__ = "730486147"


def odd_and_even(l1: list[int]) -> list[int]:
    """Returns a new list with only odd elements."""
    l2: list[int] = []
    for i in range(len(l1)):
        if ((i) % 2 == 0) and (l1[i] % 2 != 0):
            l2.append(l1[i])
    return (l2)