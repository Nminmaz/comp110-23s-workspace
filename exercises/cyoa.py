"""EX06 Choose Your Own Adventure."""


__author__ = "730486147"


from random import randint
EXHALE: str = "\U0001F624"
SMILE: str = "\U0001F600"
UPSET: str = "\U0001F610"
SHOCKED: str = "\U0001F92F"
OOF: str = "\U0001F62C"
points: int = 0
player: str = ""


def main() -> None:
    """The main function for the adventure."""
    global player
    global points
    greet()
    major: str = ""
    i: int = 0
    while major != "Quit":
        major = ""
        idx: int = 0
        print(f"Total points: {points}")
        if i > 0:
            print("Keep going if you would like.")
        print(f"Now, {player}, declare your major!")
        while len(major) == 0 and idx < 5:
            major = input("Please type Business, Communications, Math, or Quit: ")
            if major != "Business" and major != "Communications" and major != "Math" and major != "Quit":
                major = ""
                print("That's not an option.")
            idx += 1
        if idx == 5: 
            print("I don't have time for your nonsense... Try again!")
            return
        if major == "Quit":
            print(f"It seems that you're not built for this... {OOF}")
            print(f"{player} finished with {points} points.")
        elif major == "Business":
            points += business()
        elif major == "Communications":
            points += communications()
        elif major == "Math":
            print("You and your competitor, a business major named Soham will be judged on one criteria")
            number: int = int(input("What is your favorite number? "))
            points += math(number)
        i += 1


def greet() -> None:
    """Greeting function that explains the game."""
    global player
    print(f"Hello, bright student. Allow me to introduce myself: My name is Kevin G. {SMILE}")
    print("My last name is actually Johnson, but people around here know I'm a real G.")
    print("Anyway, I'm sorry to inform you that you have been selected for a special admission program.")
    print("If you want to get into UNC, you're gonna need to prove your intellectual skills against our other applicants.")
    print(f"In a truly EPIC competition... {EXHALE} {EXHALE}")
    print("The more you outsmart our other applicants, the more adventure points you will earn.")
    print("So try your best, because we will choose the student with the most points.")
    name: str = input("First, tell me your name: ")
    player = name
    return


def business() -> int:
    """The story for business majors."""
    global player
    print(f"Ah, excellent choice! Alright, {player}, your opponent is a math major named Bana.")
    print(f"You will be challenged to answer several math questions and then engage in mental combat {SMILE}")
    points: int = 0
    for i in range(0, 3):
        print(f"Round {i+1}:")
        x: int = randint(-10, 10)
        y: int = randint(-10, 10)
        correct: int = x + y
        answer: int = int(input(f"What is the sum of {x} and {y}? "))
        if answer == correct:
            print(f"Bana answered {correct-1}.")
            print(f"{answer} is correct, {player}! You earned 1 point.")
            points += 1
            if i == 0:
                print("Bana: I'll get it right next time!")
            if i == 1:
                print("Bana: Aw frick on a stick.")
            if i == 2:
                print("Bana: no no No NO NOOOO!")
        else:
            print(f"Bana answered, {correct}, which is correct.")
            print(f"{answer} is wrong! Don't give up")
    print("Wow. What an amazing display of intelligence. Now fight! (mentally)")
    print("Use the materials in front of you to compete with your opponent.")
    choice: str = input("Choose one of the following: Pencil, Coloring Book, Eraser: ")
    while choice != "Pencil" and choice != "Coloring Book" and choice != "Eraser":
        print("Invalid Choice.")
        choice = input("Choose one of the following: Pencil, Coloring Book, Eraser: ")
    if choice == "Pencil":
        print(f"Terrible mistake. Bana proceeds to write down the CPT theorem, demonstrating his intellect {OOF}")
        print("You lost 1 point")
        if points > 1:
            points -= 1
        else:
            points = 0
    elif choice == "Coloring Book":
        print("You open the coloring book, the official textbook required for BUSI 590...")
        print("While you have memorized the material, it is far too complex for Bana.")
        print(f"You earned 10 points {SMILE}")
        points += 10
    elif choice == "Eraser":
        print("You erase Bana's real analysis homework, ruining his day.")
        print(f"That's just messed up. You didn't gain or lose any points, but I hope you feel bad {UPSET}")
    print(f"Excellent work, both of you, but {player} has won this competition and earned {points} points {SHOCKED}")
    return (points)


def communications() -> int:
    """Adventure for communications majors."""
    global player
    print(f"By your choice alone, I can tell that you are an outstanding student {SMILE}")
    print("Only the most advanced humans in UNC can hope to make it through our communications major.")
    print("Thus, I will require that you face another communications major named Kandala.")
    print("You will both have the same task.")
    sentence: str = input("Please type a phrase in any language: ")
    points: int = 0
    if len(sentence) > 0:
        print(f"Wow, {player}, truly amazing. Your communication skills... they're remarkable.")
        print("I'm afraid we can't teach you communication more advanced than that!")
        print(f"You earned 10 points! {SMILE}")
        points += 10
    else:
        print("You failed the test, but we value your effort.")
        print("You earned one point.")
        points += 1
    return points


def math(number: int) -> int:
    """The math major route."""
    global player
    points: int = 0
    if number > 10:
        print(f"Wow, {player} that's a big number... you earned 1 point")
        print("Soham chose the lucky number 7, a much better option. Unfortunately, you have lost this test")
        print("Thank you for your time and effort.")
        points += 1
    elif number % 2 == 0:
        print(f"Really, {player}? An even number? You earned ZERO points! {UPSET}")
        print("Soham chose the lucky number 7, a much better option. Unfortunately, you have lost this test")
        print("Thank you for your time and effort.")
    else:
        print(f"What a great choice, {player}. You earned 3 points {SMILE}")
        if number != 7:
            print("While you did not pick the best number, you made a very respectable decision.")
        print("You have passed this test and tied against Soham in the competition.")
        points += 3
        if number == 7:
            print("And for choosing the magic number 7, you have earned an additional 7 points!")
            points += 7
    return (points)


if __name__ == "__main__":
    main()