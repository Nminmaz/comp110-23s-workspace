"""Some function."""


__author__ = "730486147"


def value_exists(numbas: dict[str, int], numba: int) -> bool:
    for i in numbas:
        if numbas[i] == numba:
            return True
    return False