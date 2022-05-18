import random
from art import hangman

guesses = []


def play():
    file = open("words.txt", "r")
    words = file.readlines()
    file.close()
    word = random.choice(words)[:-1]

    failed_attempts = 0

    playing = True

    while playing:
        print(f"Failed attempts: {failed_attempts}/7\n")

        for letter in word:
            if letter.lower() in guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("")

        guess = input("Choose a letter:\n")

        guesses.append(guess.lower())

        if guess.lower() not in word.lower():
            failed_attempts += 1
            print(hangman[failed_attempts - 1])
            if failed_attempts == 7:
                break

        playing = False

        for letter in word:
            if letter.lower() not in guesses:
                playing = True

    if not playing:
        raise SystemExit(f"You found the word! It was: {word}")

    else:
        raise SystemExit(f"Game over the word was: {word}")


def splash():
    print("Welcome To My")
    print("Hangman Game!")
    print(hangman[6])


def main():
    splash()
    while True:
        start_playing = input("Like to play? y/n \n")
        if start_playing.lower() == "y":
            print("You have decided to play.")
            play()
        elif start_playing.lower() == "n":
            raise SystemExit("Exiting Game!")
        else:
            print("That is not a valid option, Please try again.")


main()
