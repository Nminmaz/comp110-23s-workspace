"""Dictionary utility functions."""


__author__ = "730486147"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Switches the keys and values in a dictionary."""
    output_dict: dict[str, str] = {}
    for i in d:
        if d[i] in output_dict:
            raise KeyError("You cannot have two of the same keys.")
        output_dict[d[i]] = i
    return (output_dict)


def favorite_color(d: dict[str, str]) -> str:
    """Determines the most common favorite color."""
    count: dict[str, int] = {}
    for i in d:
        if d[i] in count:
            count[d[i]] += 1
        else:
            count[d[i]] = 1
    highest: int = 0
    favorite: str = ""
    for i in count:
        if count[i] > highest:
            highest = count[i]
            favorite = i
    return (favorite)


def count(values: list[str]) -> dict[str, int]:
    """Counts the frequency of a numbers in a list."""
    frequency: dict[str, int] = {}
    for i in values:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return (frequency)
