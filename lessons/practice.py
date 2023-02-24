def stars(word: str):
    idx: int = 0
    while idx < (len(word) - 1):
        if word[idx] != "a":
            print("I don't like this letter")
        else:
            print("Aaaaaa")
        idx = idx + 1
    print("Your word has been censored")
    print(word[0] + "*"*(len(word)-2) + word[(len(word)-1):])

stars("rats")