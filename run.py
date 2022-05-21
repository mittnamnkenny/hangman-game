import random
import time
from art import hangman

TEXT = "\033[0m"
HIGHLIGHT = "\033[7m"
RESPONSE = "\033[92m"
ALERT = "\033[91m"

colours = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "pink": "\033[95m",
    "cyan": "\033[36m",
    "purple": "\033[35m"
}


def choose_word(age):
    easy_words_file = open("easy_words.txt", "r")
    easy_words = easy_words_file.readlines()
    easy_words_file.close()

    hard_words_file = open("hard_words.txt", "r")
    hard_words = hard_words_file.readlines()
    hard_words_file.close()

    if int(age) < 16:
        return random.choice(easy_words)[:-1]
    else:
        return random.choice(hard_words)[:-1]


def calc_colour(fav_colour):
    for key, value in colours.items():
        if fav_colour.lower().find(key) != -1:
            print(f"\n{value}{key.capitalize()} {TEXT}is a good choice.")
            return value
    print(
        f'\n{RESPONSE}Favourite colour'
        f' "{TEXT}{fav_colour}{RESPONSE}" not listed.\n'
        )
    time.sleep(1)
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
            if guess.lower() not in guesses:
                return guess
            else:
                print(f"\n{ALERT}You already tried: {TEXT}{guess}")
                time.sleep(1)
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


def val_age(username):
    while True:
        result = input(f"\nHow old are you {username.capitalize()}?\n")
        if result.isnumeric():
            if int(result) < 7:
                print(f"\n{ALERT}You are too young to play this game!")
                time.sleep(1)
                raise SystemExit(f"\nExiting Game.{TEXT}\n")
            else:
                return result
        else:
            print(
                f"\n{ALERT}That is not a valid option,"
                f" Please try again.{TEXT}"
                )


def val_text(val):
    while True:
        result = input(f"\nWhat's your {val}?\n")
        if len(result) > 1 and result.isalpha():
            return result
        else:
            print(
                f"\n{ALERT}That is not a valid option,"
                f" Please try again.{TEXT}"
                )


def game_rules():
    while True:
        rules = input(
            f"\nDo you want to read the rules? {HIGHLIGHT} y/n {TEXT}\n"
            )
        if rules.lower() == "y":
            print(f"\n{RESPONSE}Rules of the game.{TEXT}")
            time.sleep(5)
            break
        elif rules.lower() == "n":
            print(f"\n{RESPONSE}Ok, no rules.{TEXT}")
            break
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
        start_playing = input(
            f"\nDo you want to play? {HIGHLIGHT} y/n {TEXT}\n"
            )
        if start_playing.lower() == "y":
            print(f"\n{RESPONSE}You have decided to play.{TEXT}")
            game_rules()
            username = val_text("name")
            age = val_age(username)
            fav_colour = val_text("favourite colour")
            play(username, age, fav_colour)
        elif start_playing.lower() == "n":
            raise SystemExit(f"\n{ALERT}Exiting Game.{TEXT}\n")
        else:
            print(
                f"\n{ALERT}That is not a valid option,"
                f" Please try again.{TEXT}"
                )


main()
