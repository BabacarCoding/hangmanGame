
import random
from operator import mod


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
    fails = 0
    print("Welcome to hangman! You will have 10 tries to guess a letter of a word.")
    print("If you fail to guess the word by the tenth try, you will fail!")
    print("However, if you guess all the letters of the word before the tenth try, you will succeed and become the hangman master!")
    print("")
    print("------------------")
    print("")
    print("Your word has been chosen. It is :")
    print(blank)

    while fails < 10:
        print(
            f"You have {10 - fails} fails left. Would you like to: Guess word or Guess letter.")
        move = input("Type your answer choice as shown: 'letter' or 'word' : ")
        index = []
        if move == "letter":  # If you have chosen to guess a letter

            print(f"The word has {blank} letters")
            choice = ((input("Type your letter guess!")).lower()).strip()
            count = -1

            if choice in word:  # If your guess was a letter in the word

                print(f"{choice} appears {word.count(choice)} times.")
                word = list(word)

                if word.count(choice) > 1:  # If the letter appear more than once in the word

                    for i in range(len(word)):
                        if word[i] == choice:
                            index.append(i)
                    print(index)

                    for i in index:
                        blank = list(blank)
                        blank[i] = choice
                        blank = "".join(blank)

                else:
                    index = word.index(choice)
                    blank = list(blank)
                    blank[index] = choice
                    blank = "".join(blank)

            else:  # If your guess was not a letter in the word
                fails += 1
                if fails == 1:
                    print(
                        f"{choice} is not included in the word. Your pal Bob, looks like this: ")
                    print("")
                    print("--------")
                    print("")

                    print("0")
                    print("")
                    print("")
                elif fails == 2:
                    print(
                        f"{choice} is not included in the word. Your pal Bob, looks like this: ")
                    print("")
                    print("--------")
                    print("")

                    print("0")
                    print("|")
                    print("")
                elif fails == 3:
                    print(
                        f"{choice} is not included in the word. Your pal Bob, looks like this: ")
                    print("")
                    print("--------")
                    print("")

                    print(" 0")
                    print(" |")
                    print("/ ")
                elif fails == 4:
                    print(
                        f"{choice} is not included in the word. Your pal Bob, looks like this: ")
                    print("")
                    print("--------")
                    print("")

                    print(" 0")
                    print(" |")
                    print('/ \\')
                elif fails == 5:
                    print(
                        f"{choice} is not included in the word. Your pal Bob, looks like this: ")
                    print("")
                    print("--------")
                    print("")

                    print(" 0 /")
                    print(" |")
                    print("/ \\")
                elif fails == 6:
                    print(
                        f"{choice} is not included in the word. Your pal Bob, looks like this: ")
                    print("")
                    print("--------")
                    print("")

                    print("\ 0 /")
                    print("  |")
                    print(" / \\")
                elif fails == 7:
                    print(
                        f"{choice} is not included in the word. Your pal Bob, looks like this: ")
                    print("")
                    print("--------")
                    print("")

                    print("\ 0 /")
                    print("  |")
                    print("_/ \\")

                elif fails == 8:
                    print(
                        f"{choice} is not included in the word. Your pal Bob, looks like this: ")
                    print("")
                    print("--------")
                    print("")

                    print("\ 0 /")
                    print("  |")
                    print("_/ \_")
                elif fails == 9:
                    print(
                        f"{choice} is not included in the word. Your pal Bob, looks like this: ")
                    print("")
                    print("--------")
                    print("")

                    print("  |")
                    print("\ 0 /")
                    print("  |")
                    print("_/ \_")
                elif fails == 10:
                    print(
                        f"{choice} is not included in the word. Your pal Bob, looks like this: ")
                    print("")
                    print("--------")
                    print("")

                    print("   ___")
                    print("  |")
                    print("\ 0 /")
                    print("  |")
                    print("_/ \_")

                    print("Bob is dead.")
        if str(blank) == str(word):
            fails = 10
            print("worked")

        print(blank)

    if blank != word:
        print("Since Bob is dead, you failed hangman. Better luck next time!")
    else:
        print("You successfully guessed the word within 10 tries. Good job!")


hangman()
