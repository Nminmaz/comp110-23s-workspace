"""EX02 - One Shot Wordle - you only have one shot."""

__author__ = "730486147"

word: str = "knoll"
guess: str = input(f"What is your {len(word)}-letter guess? ")
index: int = 0
result: str = ("\U00002B1C"*len(word))

while len(guess) != len(word):
    guess = str(input(f"That was not {len(word)} letters! Try again: "))
if guess == word:
    print("\U0001F7E9"*len(word))
    print("Woo! You got it!")
    quit()
else:
    while index < len(word):
        counter: int = 0
        while counter < len(word):
            if guess[index] == word[counter]:
                if index == counter:
                    result = f"{result[0:index]}\U0001F7E9{result[index+1:]}"
                elif result[index] != "\U0001F7E9":
                    result = f"{result[0:index]}\U0001F7E8{result[index+1:]}"
            counter += 1
        index += 1
    print(result)
    print("Not quite. Play again soon!")
            