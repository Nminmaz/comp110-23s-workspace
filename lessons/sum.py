"""Example function for unit tests."""

__author__ = "730486147"


def sum(xs: list[float]) -> float:
    """return sum of all elements in xs."""
    sum_total: float = 0.0
    for i in range(len(xs)):
        sum_total += xs[i]
    return sum_total