
import random


def hangman():
    word_list = ["baby", "door", "banana", "finger", "fence", "big",
                 "swimming", "pool", "sun", "church", "yoyo", "boy", "bag"]
    word = random.choice(word_list)
    length_word = len(word)
    count = 0
    blank = ""
    while count < length_word:
        blank += "_"
        count += 1

    global fails
    fails = 0
    print("")
    print("")
    print("")
    print("-------------")
    print("")
    print("")
    print("")
    print("Welcome to hangman! You will have to guess a word without failing more than 10 times")
    print("If you fail to guess the word by the tenth mistake, you will fail!")
    print("However, if you guess all the letters of the word before the tenth mistake, you will succeed and become the hangman master! \n")
    print("------------------ \n")
    print("Your word has been chosen.")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    while fails < 10:
        penalty = 0
        guess = ""
        print(
            f"{blank} is what you have guessed so far. You have {10 - fails} fails left. Would you like to: Guess word or Guess letter.")
        move = input(
            "Type your answer choice as shown: 'l' for letter or 'w' for word : \n")
        print("-------------")
        print("")
        print("")
        print("")

        index = []
        if move == "l":  # If you have chosen to guess a letter

            print(f"The word has {blank} letters")
            print("Type your letter guess! \n")
            choice = input("")
            print("")
            count = -1

            if choice in word:  # If your guess was a letter in the word

                print(
                    f"The letter {choice} appears {word.count(choice)} times.")
                word = list(word)

                if word.count(choice) > 1:  # If the letter appear more than once in the word

                    for i in range(len(word)):
                        if word[i] == choice:
                            index.append(i)

                    for i in index:
                        blank = list(blank)
                        blank[i] = choice
                        blank = "".join(map(str, blank))

                else:
                    index = word.index(choice)
                    blank = list(blank)
                    blank[index] = choice
                    blank = "".join(map(str, blank))

                word = "".join(map(str, word))

            else:  # If your guess was not a letter in the word
                fails += 1
                if fails == 1:
                    print(
                        f"The letter {choice} is not included in the word. Your pal Bob, looks like this: ")
                    print("")
                    print("")

                    print("0")
                    print("")
                    print("")
                    print("")
                    print("")

                elif fails == 2:
                    print(
                        f"The letter {choice} is not included in the word. Your pal Bob, looks like this: ")
                    print("")
                    print("")

                    print("0")
                    print("|")
                    print("")
                    print("")
                    print("")

                elif fails == 3:
                    print(
                        f"The letter {choice} is not included in the word. Your pal Bob, looks like this: ")
                    print("")
                    print("")

                    print(" 0")
                    print(" |")
                    print("/ ")
                    print("")
                    print("")

                elif fails == 4:
                    print(
                        f"The letter {choice} is not included in the word. Your pal Bob, looks like this: ")
                    print("")
                    print("")

                    print(" 0")
                    print(" |")
                    print('/ \\')
                    print("")
                    print("")

                elif fails == 5:
                    print(
                        f"The letter {choice} is not included in the word. Your pal Bob, looks like this: ")
                    print("")
                    print("")

                    print(" 0 /")
                    print(" |")
                    print("/ \\")
                    print("")
                    print("")

                elif fails == 6:
                    print(
                        f"The letter {choice} is not included in the word. Your pal Bob, looks like this: ")
                    print("")
                    print("")

                    print("\ 0 /")
                    print("  |")
                    print(" / \\")
                    print("")
                    print("")

                elif fails == 7:
                    print(
                        f"The letter {choice} is not included in the word. Your pal Bob, looks like this: ")
                    print("")
                    print("")

                    print("\ 0 /")
                    print("  |")
                    print("_/ \\")
                    print("")
                    print("")

                elif fails == 8:
                    print(
                        f"The letter {choice} is not included in the word. Your pal Bob, looks like this: ")
                    print("")
                    print("")

                    print("\ 0 /")
                    print("  |")
                    print("_/ \_")
                    print("")
                    print("")

                elif fails == 9:
                    print(
                        f"The letter {choice} is not included in the word. Your pal Bob, looks like this: ")
                    print("")
                    print("")

                    print("  |")
                    print("\ 0 /")
                    print("  |")
                    print("_/ \_")
                    print("")
                    print("")

                elif fails == 10:
                    print(
                        f"The letter {choice} is not included in the word. Your pal Bob, looks like this: ")
                    print("")
                    print("")

                    print("   ___")
                    print("  |")
                    print("\ 0 /")
                    print("  |")
                    print("_/ \_")
                    print("")
                    print("")

                    print("Bob is dead.")

        elif move == "w":
            guess = input(
                "You have a chance to guess the word. What do you think the word is? Note: If you guess incorrectly, Bob dies. \n")
        else:
            pass

        if blank == word:
            fails = 10
        elif guess != "":
            if guess == word:
                fails = 10
            else:
                print(
                    "Your guess is incorrect. Like stated before, the penalty of an incorrect word guess is death to Bob")
                fails = 10
                penalty = 1
        else:
            pass
    print("Exited while loop.")

    if blank != word:
        print("Since Bob is dead, you failed hangman. Better luck next time!")
    elif penalty == 1:
        print(
            "You wagered Bob's life and failed. Now, you will never play hangman again...")
    else:
        print(
            "You succeeded in guessing the word. Good job, now you are the hangman master.")


hangman()
