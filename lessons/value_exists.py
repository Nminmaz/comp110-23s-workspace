"""Some function."""


__author__ = "730486147"


def value_exists(dictionary: dict[str, int], number: int) -> bool:
    for i in dictionary:
        if dictionary[i] == number:
            return True
    return False