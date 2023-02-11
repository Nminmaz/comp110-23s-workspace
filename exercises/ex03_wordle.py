"""EX03 - Wordle - The real deal."""

__author__ = "730486147"


def contains_char(word: str, character: str) -> bool:
    """Determines whether a character is in a given word."""
    assert len(character) == 1
    idx1: int = 0
    while idx1 < len(word):
        if character == word[idx1]:
            return (True)
        idx1 += 1
    return (False)


def emojified(guess: str, answer: str) -> str:
    """Determines which emoji to place based on guesses."""
    assert len(guess) == len(answer)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    idx2: int = 0
    result: str = ""

    while idx2 < len(answer):
        if contains_char(answer, guess[idx2]):
            if answer[idx2] == guess[idx2]:
                result += GREEN_BOX
            else:
                result += YELLOW_BOX
        else:
            result += WHITE_BOX
        idx2 += 1
    return (result)


def input_guess(expect_len: int) -> str:
    """Makes sure that a guess is the correct length."""
    attempt: str = input(f"Enter a {expect_len} character word: ")
    while len(attempt) != expect_len:
        attempt = input(f"That wasn't {expect_len} chars! Try again: ")
    return (attempt)


def main() -> None:
    """The entrypoint of the program and main game loop."""
    GREEN_BOX: str = "\U0001F7E9"
    SECRET: str = "codes"
    LENGTH = len(SECRET)
    turn: int = 1
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        realguess = input_guess(LENGTH)
        emojis: str = emojified(realguess, SECRET)
        print(emojis)
        if emojis == (GREEN_BOX * LENGTH):
            print(f"You won in {turn}/6 turns!")
            return
        turn += 1
    print("X/6 - Sorry, try again tomorrow!")
    return


if __name__ == "__main__":
    main()