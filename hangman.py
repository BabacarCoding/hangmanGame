import csv
import random

file = open("words.csv", "r")
csv_reader = csv.reader(file)

word_list = []
for row in csv_reader:
    word_list.append(row)


def hangman():
    # word_list = ["baby", "door", "banana", "finger", "fence", "big",
    #              "swimming", "pool", "sun", "church", "yoyo", "boy", "bag"]
    word = random.choice(word_list)
    word = "".join(map(str, word))
    length_word = len(word)
    print(f"{word} is the chosen word.")
    count = 0
    blank = ""
    for character in word:
        if character == " ":
            blank += " "
            count += 1
        else:
            blank += "_"
            count += 1

    global fails
    fails = 0
    print("\n \n \n \n ")
    print("------------- \n \n \n")
    print("Welcome to hangman! You will have to guess a word without failing more than 10 times")
    print("If you fail to guess the word by the tenth mistake, you will fail!")
    print("However, if you guess all the letters of the word, or the word itself, before the tenth mistake, you will succeed and become the hangman master! \n")
    print("------------------ \n")
    print("Your word has been chosen.   \n \n \n \n \n \n \n ")

    incorrect_guesses = []
    while fails < 10:
        penalty = 0
        guess = ""
        print(
            f"{blank} is what you have guessed so far. You have {10 - fails} fails left. Would you like to: Guess word or Guess letter.")
        move = input(
            "Type your answer choice as shown: 'l' for letter or 'w' for word : \n")
        print("------------- \n \n \n ")

        index = []
        if move == "l":  # If you have chosen to guess a letter

            if fails > 0:
                print(
                    f"The word has {blank} letters. The incorrect letters you have guessed so far are: {set(incorrect_guesses)}.")

            else:
                print(
                    f"The word has {blank} letters. The incorrect letters you have guessed so far are: none.")

            print("Type your letter guess! \n")

            choice = (input("")).strip()
            print("")
            count = -1

            if choice in word:  # If your guess was a letter in the word
                if choice == "":
                    print("Please enter a letter, not whitespace \n \n")
                elif choice.isdigit() == True:
                    print("Please enter a letter, not a number")
                else:
                    print(
                        f"The letter {choice} appears {word.count(choice)} times.")
                    word = list(word)

                    # If the letter appear more than once in the word
                    if word.count(choice) > 1:

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
                incorrect_guesses.append(choice)
                fails += 1
                if fails == 1:
                    print(
                        f"The letter {choice} is not included in the word. Your pal Bob, looks like this: \n \n")

                    print("0 \n \n \n \n")

                elif fails == 2:
                    print(
                        f"The letter {choice} is not included in the word. Your pal Bob, looks like this: \n \n")

                    print("0")
                    print("| \n \n \n")

                elif fails == 3:
                    print(
                        f"The letter {choice} is not included in the word. Your pal Bob, looks like this: \n \n")

                    print(" 0")
                    print(" |")
                    print("/ \n \n")
                elif fails == 4:
                    print(
                        f"The letter {choice} is not included in the word. Your pal Bob, looks like this: \n \n")

                    print(" 0")
                    print(" |")
                    print('/ \\ \n \n')

                elif fails == 5:
                    print(
                        f"The letter {choice} is not included in the word. Your pal Bob, looks like this: \n \n")

                    print(" 0 /")
                    print(" |")
                    print("/ \\ \n \n")

                elif fails == 6:
                    print(
                        f"The letter {choice} is not included in the word. Your pal Bob, looks like this: \n \n")

                    print("\ 0 /")
                    print("  |")
                    print(" / \\ \n \n")

                elif fails == 7:
                    print(
                        f"The letter {choice} is not included in the word. Your pal Bob, looks like this: \n \n")

                    print("\ 0 /")
                    print("  |")
                    print("_/ \\ \n \n")

                elif fails == 8:
                    print(
                        f"The letter {choice} is not included in the word. Your pal Bob, looks like this: \n \n")

                    print("\ 0 /")
                    print("  |")
                    print("_/ \_ \n \n")

                elif fails == 9:
                    print(
                        f"The letter {choice} is not included in the word. Your pal Bob, looks like this: \n \n")

                    print("  |")
                    print("\ 0 /")
                    print("  |")
                    print("_/ \_ \n \n")

                elif fails == 10:
                    print(
                        f"The letter {choice} is not included in the word. Your pal Bob, looks like this: ")
                    print("")
                    print("")

                    print("   ___")
                    print("  |")
                    print("\ 0 /")
                    print("  |")
                    print("_/ \_ \n \n")

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
                print(word)
                fails = 10
                penalty = 1
        else:
            pass

    if penalty == 1:
        print(
            "You wagered Bob's life and failed. Now, you will never play hangman again...")
    elif guess == word or blank == word:
        print(
            f"You succeeded in guessing the word {word}. Good job, now you are the hangman master.")
    elif blank != word:
        print(
            f"Since Bob is dead, you failed hangman. The word was {word} Better luck next time!")
    else:
        pass


hangman()
