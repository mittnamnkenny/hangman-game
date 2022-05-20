import random
from art import hangman

TEXT = "\033[0m"
HIGHLIGHT = "\033[7m"
RESPONSE = "\033[92m"
ALERT = "\033[91m"

colours = {
    "red": "\033[91m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m"
}


def choose_word(age):
    easy_words_file = open("easy_words.txt", "r")
    easy_words = easy_words_file.readlines()
    easy_words_file.close()

    hard_words_file = open("hard_words.txt", "r")
    hard_words = hard_words_file.readlines()
    hard_words_file.close()

    if int(age) < 7:
        print(f"\n{ALERT}You are too young to play this game!")
        raise SystemExit(f"\nExiting Game.{TEXT}\n")
    elif int(age) < 15:
        return random.choice(easy_words)[:-1]
    else:
        return random.choice(hard_words)[:-1]


def calc_colour(fav_colour):
    for key, value in colours.items():
        if fav_colour.lower().find(key) != -1:
            return value
    print(
        f'\n{RESPONSE}Favourite colour'
        f' "{TEXT}{fav_colour}{RESPONSE}" not listed.\n'
        )
    random_colour_items = random.choice(list(colours.items()))
    print(
        f"{random_colour_items[1]}{random_colour_items[0].capitalize()}"
        f" {TEXT}was chosen instead."
        )
    return random_colour_items[1]


guesses = []


def ask_guess():
    while True:
        guess = input(f"\n{TEXT}Choose a letter:\n")
        if guess.isalpha() and len(guess) == 1:
            return guess
        else:
            print(
                f"\n{ALERT}That is not a valid option,"
                f" Please try again.{TEXT}"
                )


def play(username, age, fav_colour):
    word = choose_word(age)

    play_colour = calc_colour(fav_colour)

    failed_attempts = 0

    playing = True

    while playing:
        print(
            f"\n{TEXT}Failed attempts:"
            f" {HIGHLIGHT} {failed_attempts}/7 {TEXT}\n"
            )

        for letter in word:
            if letter.lower() in guesses:
                print(play_colour, letter, end=" ")
            else:
                print(play_colour, "_", end=" ")
        print("")

        guess = ask_guess()

        guesses.append(guess.lower())

        if guess.lower() not in word.lower():
            failed_attempts += 1
            print(f"{play_colour}{hangman[failed_attempts - 1]}")
            if failed_attempts == 7:
                break

        playing = False

        for letter in word:
            if letter.lower() not in guesses:
                playing = True

    if not playing:
        raise SystemExit(
            f"\n{RESPONSE}You found the word {TEXT}{username.capitalize()}"
            f"{RESPONSE}! It was: {TEXT}{word}\n"
            )

    else:
        raise SystemExit(
            f"\n{ALERT}Game over {TEXT}{username.capitalize()}"
            f" {ALERT}the word was: {TEXT}{word}\n"
            )


def info():
    while True:
        username = input("\nWhat's your name?\n")
        age = input("\nWhat's your age?\n")
        fav_colour = input("\nWhat's your favourite colour?\n")
        if len(username) > 1 and age.isnumeric() and len(fav_colour) > 1:
            print(f"\n{RESPONSE}Ok {username.capitalize()} let's play.{TEXT}")
            play(username, age, fav_colour)
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
            raise SystemExit(f"\n{ALERT}Exiting Game.{TEXT}\n")
        else:
            print(
                f"\n{ALERT}That is not a valid option,"
                f" Please try again.{TEXT}"
                )


main()
