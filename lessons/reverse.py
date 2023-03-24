"""Reverses a list."""

def reverse(l1: list[int]) -> list[int]:
    l2: list[int] = []
    if len(l1) > 0:
        idx: int = len(l1) - 1
    else:
        return []
    while idx >= 0:
        l2.append(l1[idx])
        idx -= 1
    return l2

print(reverse([]))
print(reverse([3, 2, 1]))