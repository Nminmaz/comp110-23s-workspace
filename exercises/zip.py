"""CQ04."""

__author__ = "730486147"


def zip(keys: list[str], values: list[int]) -> dict[str, int]:
    """Produces a dictionary from two lists."""
    if len(keys) != len(values):
        return {}
    if len(keys) == 0 or len(values) == 0:
        return {}
    combined: dict[str, int] = {}
    for i in range(len(keys)):
        combined[keys[i]] = values[i]
    return combined