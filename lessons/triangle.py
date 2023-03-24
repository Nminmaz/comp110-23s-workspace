def triangle(number: int) -> None:
    numbers: str = ""
    for i in range(number):
        numbers += f" {i + 1}"
        print(numbers)

def sumrange(number: int) -> int:
    total: int = 0
    for i in range(number + 1):
        total += i
    return total

def multiple(number: int) -> None:
    for i in range(10):
        print((i + 1)* number)

def l_to_d(l1: list[str], l2: list[int]) -> dict[str,int]:
    if len(l1) == len(l2):
        d: dict[str,int] = {}
        for i in range(len(l1)):
            d[l1[i]] = l2[i]
        return (d)
    else:
        return {}

def combine(d1: dict[str,int], d2: dict[str,int]) -> dict[str,int]:
    d: dict[str,int] = {}
    for i in d1:
        d[i] = d1[i]
    for i in d2:
        d[i] = d2[i]
    return(d)

