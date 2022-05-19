import random
from art import hangman

TEXT = "\033[0m"
HIGHLIGHT = "\033[7m"
RESPONSE = "\033[92m"
ALERT = "\033[91m"


def choose_word(age):
    file = open("words.txt", "r")
    words = file.readlines()
    file.close()

    easy_words = []
    hard_words = []

    for word in words:
        if len(word) > 2 and len(word) < 7:
            easy_words.append(word)
        elif len(word) >= 7:
            hard_words.append(word)

    if int(age) < 12:
        return random.choice(easy_words)[:-1]
    else:
        return random.choice(hard_words)[:-1]


guesses = []


def play(username, age):
    word = choose_word(age)

    failed_attempts = 0

    playing = True

    while playing:
        print(f"\nFailed attempts: {HIGHLIGHT} {failed_attempts}/7 {TEXT}\n")

        for letter in word:
            if letter.lower() in guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("")

        guess = input("\nChoose a letter:\n")

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
        raise SystemExit(
            f"\n{RESPONSE}You found the word {TEXT}{username.upper()}{RESPONSE}!"
            f" It was: {TEXT}{word}\n"
            )

    else:
        raise SystemExit(
            f"\n{ALERT}Game over {TEXT}{username.upper()}"
            f" {ALERT}the word was: {TEXT}{word}\n"
            )


def info():
    while True:
        username = input("\nWhat's your name?\n")
        age = input("\nWhat's your age?\n")
        if len(username) > 1 and age.isnumeric():
            print(f"\n{RESPONSE}Ok {username.upper()} let's play.{TEXT}")
            play(username, age)
        else:
            print(
                f"\n{ALERT}That is not a valid option,"
                f" Please try again.{TEXT}"
                )


def game_rules():
    while True:
        rules = input(f"\nLike to read the rules? {HIGHLIGHT} y/n {TEXT}\n")
        if rules.lower() == "y":
            print(f"\n{RESPONSE}Rules of the game.{TEXT}")
            info()
        elif rules.lower() == "n":
            print(f"\n{RESPONSE}Ok, no rules.{TEXT}")
            info()
        else:
            print(
                f"\n{ALERT}That is not a valid option,"
                f" Please try again.{TEXT}"
                )


def main():
    print(f"\n\033[42m Welcome To My {TEXT}")
    print(f"\033[42m Hangman Game! {TEXT}")
    print(f"{RESPONSE}{hangman[6]}{TEXT}")

    while True:
        start_playing = input(f"\nLike to play? {HIGHLIGHT} y/n {TEXT}\n")
        if start_playing.lower() == "y":
            print(f"\n{RESPONSE}You have decided to play.{TEXT}")
            game_rules()
        elif start_playing.lower() == "n":
            raise SystemExit(f"\n{ALERT}Exiting Game!{TEXT}\n")
        else:
            print(
                f"\n{ALERT}That is not a valid option,"
                f" Please try again.{TEXT}"
                )


main()
