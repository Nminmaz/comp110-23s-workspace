def lockedin(number: int) -> int:
    if number > 10:
        number = number % 10
    while number % 7 == 0:
        
        number = number + 1