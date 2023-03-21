"""Short words."""


__author__ = "730486147"


def short_words(l1:list[str]) -> list[str]:
    l2: list[str] = []
    for i in l1:
        if len(i) < 5:
            l2.append(i)
        else:
            print(f"{i} is too long!")
    return (l2)