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

feedback = [["nice", "a good choice", "great", "perfect", "alright", "ok"],
            ["well played", "good job", "you did it", "great success"]]


def choose_word(age):
    """
    Choses random word from txt file.
    Based on age input from user.
    """
    easy_words_file = open("easy_words.txt", "r")
    easy_words = easy_words_file.readlines()
    easy_words_file.close()

    hard_words_file = open("hard_words.txt", "r")
    hard_words = hard_words_file.readlines()
    hard_words_file.close()

    # Random word based on age input.
    if int(age) < 16:
        return random.choice(easy_words)[:-1]
    else:
        return random.choice(hard_words)[:-1]


def calc_colour(fav_colour):
    """
    Function for displaying favourite colour.
    Choses random if not listed.
    """
    for key, value in colours.items():
        # Find a matching key in colours dict.
        if fav_colour.lower().find(key) != -1:
            print(
                f"\n{value}{key.capitalize()} {TEXT}is"
                f" {random.choice(feedback[0])}."
                )
            return value
    # Favourite colour not in dict.
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
    """
    Validate user guess.
    Only one alphabet letter is accepted.
    Check if letter already been guessed.
    """
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


def play_again(username, age, fav_colour):
    """
    Ask the user to play again
    without resetting user info.
    """
    while True:
        again = input(
            f"\n{TEXT}Do you want to play again? {HIGHLIGHT} y/n {TEXT}\n"
            )
        if again.lower() == "y":
            print(
                f"\n{RESPONSE}{random.choice(feedback[0]).capitalize()},"
                f" you have decided to play again.{TEXT}"
                )
            guesses.clear()
            play(username, age, fav_colour)
        elif again.lower() == "n":
            raise SystemExit(f"\n{ALERT}Exiting Game.{TEXT}\n")
        else:
            print(
                f"\n{ALERT}That is not a valid option,"
                f" Please try again.{TEXT}"
                )


def play(username, age, fav_colour):
    """
    Main game function.
    Game logic was inspired by NeuralNine:
    https://www.youtube.com/watch?v=5x6iAKdJB6U
    """
    word = choose_word(age)

    play_colour = calc_colour(fav_colour)

    failed_attempts = 0

    playing = True

    # Will loop until failed_attempts reaches 7 or secret word is guessed.
    while playing:
        print(
            f"\n{TEXT}Failed attempts:"
            f" {HIGHLIGHT} {failed_attempts}/7 {TEXT}\n"
            )

        # Display secret word as underscore if not correct letter guessed.
        for letter in word:
            if letter.lower() in guesses:
                print(play_colour, letter, end=" ")
            else:
                print(play_colour, "_", end=" ")
        print("")

        guess = ask_guess()

        guesses.append(guess.lower())

        # Code to increment failed_attempts.
        if guess.lower() not in word.lower():
            failed_attempts += 1
            print(f"{play_colour}{hangman[failed_attempts - 1]}")
            if failed_attempts == 7:
                break

        playing = False

        for letter in word:
            if letter.lower() not in guesses:
                playing = True

    # User found the secret word.
    if not playing:
        print(
            f"\n{RESPONSE}{random.choice(feedback[1]).capitalize()}"
            f" {TEXT}{username.capitalize()} {RESPONSE}you found the word!"
            f" It was: {play_colour}{word}\n"
            )
        time.sleep(1)
        play_again(username, age, fav_colour)

    # Failed_attempts reached 7.
    else:
        print(
            f"\n{ALERT}Game over {TEXT}{username.capitalize()}"
            f" {ALERT}the word was: {play_colour}{word}\n"
            )
        time.sleep(1)
        play_again(username, age, fav_colour)


def val_age(username):
    """
    Validate user age.
    Will only accept numbers.
    """
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
    """
    Validate name and favourite colour.
    Will only accept alphabet letters, 2 characters or more.
    """
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
    """
    The user will be able to read the rules
    before proceeding.
    """
    while True:
        rules = input(
            f"\nDo you want to read the rules? {HIGHLIGHT} y/n {TEXT}\n"
            )
        if rules.lower() == "y":
            print(
                f"\n{ALERT}h _ n g m _ n"
                f"\n{RESPONSE}Hangman is a simple word guessing game. \nYou"
                f" try to guess the secret word letter by letter. \nThe"
                f" number of incorrect guesses before the game ends is 7."
                f" \nGuess the word before your man gets hung. \nIf you"
                f" are younger than 16 years you are presented with easier"
                f" words. \n{ALERT}You must be older than 7 years to play this"
                f" game.{TEXT}"
                )
            time.sleep(5)
            break
        elif rules.lower() == "n":
            print(
                f"\n{RESPONSE}{random.choice(feedback[0]).capitalize()},"
                f" no rules.{TEXT}"
                )
            break
        else:
            print(
                f"\n{ALERT}That is not a valid option,"
                f" Please try again.{TEXT}"
                )


def main():
    """
    Provides a welcome message to the user.
    Initialize the game after user inputs.
    """
    print(f"\n\033[42m Welcome To My {TEXT}")
    print(f"\033[42m Hangman Game! {TEXT}")
    print(f"{RESPONSE}{hangman[6]}{TEXT}")

    while True:
        start_playing = input(
            f"\nDo you want to play? {HIGHLIGHT} y/n {TEXT}\n"
            )
        if start_playing.lower() == "y":
            print(
                f"\n{RESPONSE}{random.choice(feedback[0]).capitalize()},"
                f" you have decided to play.{TEXT}"
                )
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
