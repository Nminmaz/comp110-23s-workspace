"""EX02 - One Shot Wordle - you only have one shot."""

__author__ = "730486147"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
word: str = "python"
guess: str = input(f"What is your {len(word)}-letter guess? ")
index: int = 0
# rather than a blank string I started with a string of white boxes
result: str = (WHITE_BOX * len(word))


# the loop to determine if the guess is the right length
while len(guess) != len(word):
    guess = str(input(f"That was not {len(word)} letters! Try again: "))

# a quick end in case the guess is right
if guess == word:
    print(GREEN_BOX * len(word))
    print("Woo! You got it!")
else:
    while index < len(word):
        counter: int = 0
        # a nested loop to check for matching letters across all indices
        while counter < len(word):
            if guess[index] == word[counter]:
                # checking if letters at the same index match
                if index == counter:
                    result = f"{result[0:index]}{GREEN_BOX}{result[index+1:]}"
                # checking if letters at different indices match
                elif result[index] != GREEN_BOX:
                    result = f"{result[0:index]}{YELLOW_BOX}{result[index+1:]}"
                # these conditionals can replace the white box at a given index
            counter += 1
        index += 1
    print(result)
    # since the guess is certainly wrong
    print("Not quite. Play again soon!")
            