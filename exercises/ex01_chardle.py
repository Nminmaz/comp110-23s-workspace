"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730486147"

word: str = input("Enter a 5-character word: ")
count: int = 0
instances: int = 0

if len(word) == 5:
    character: str = input("Enter a single character: ")
else: 
    character = ""
    print("Error: Word must contain 5 characters")
    quit()

if len(character) != 1:
    print("Error: Character must be a single character.")
    quit()

print(f"Searching for {character} in {word}")

while count < 5:
    if character == word[count]:
        print(f"{character} found at index {count}")
        instances += 1
    count += 1

if instances > 0:
    if instances == 1:
        print(f"1 instance of {character} found in {word}")
    else:
        print(f"{instances} instances of {character} found in {word}")
else:
    print(f"No instances of {character} found in {word}")
