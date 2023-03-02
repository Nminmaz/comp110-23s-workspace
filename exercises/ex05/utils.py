"""EX05 - More Utility Functions."""

__author__ = "730486147"


def only_evens(numbers: list[int]) -> list[int]:
    """Puts the even numbers of a list into a new list."""
    evens: list[int] = []
    for i in numbers:
        if i % 2 == 0:
            evens.append(i)
    return (evens)


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Combines two lists."""
    combined: list[int] = []
    for i in list1:
        combined.append(i)
    for i in list2:
        combined.append(i)
    return (combined)


def sub(ints: list[int], start: int, end: int) -> list[int]:
    """Selects a segment of the list."""
    if start < 0:
        start = 0
    if end > len(ints):
        end = len(ints)
    if len(ints) == 0 or start >= len(ints) or end < 0:
        return ([])
    segment: list[int] = []
    for i in range(start, end):
        segment.append(ints[i])
    return (segment)