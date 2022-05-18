import random
from art import hangman


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
        print(f"Failed attempts: \033[7m {failed_attempts}/7 \033[0m\n")

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
        raise SystemExit(
            f"\033[92mYou found the word \033[0m{username}\033[92m!"
            f" It was: \033[0m{word}"
            )

    else:
        raise SystemExit(
            f"\033[91mGame over \033[0m{username}"
            f" \033[91mthe word was: \033[0m{word}"
            )


def info():
    while True:
        username = input("What's your name? \n")
        age = input("What's your age? \n")
        if len(username) > 1 and age.isnumeric():
            print(f"\033[92mOk {username} let's play.\033[0m")
            play(username, age)
        else:
            print(
                "\033[91mThat is not a valid option, Please try again.\033[0m"
                )


def game_rules():
    while True:
        rules = input("Like to read the rules? \033[7m y/n \033[0m\n")
        if rules.lower() == "y":
            print("\033[92mRules of the game.\033[0m")
            info()
        elif rules.lower() == "n":
            print("\033[92mOk, no rules.\033[0m")
            info()
        else:
            print(
                "\033[91mThat is not a valid option, Please try again.\033[0m"
                )


def main():
    print("\033[42mWelcome To My\033[0m")
    print("\033[42mHangman Game!\033[0m")
    print(f"\033[92m{hangman[6]}\033[0m")

    while True:
        start_playing = input("Like to play? \033[7m y/n \033[0m\n")
        if start_playing.lower() == "y":
            print("\033[92mYou have decided to play.\033[0m")
            game_rules()
        elif start_playing.lower() == "n":
            raise SystemExit("\033[91mExiting Game!\033[0m")
        else:
            print(
                "\033[91mThat is not a valid option, Please try again.\033[0m"
                )


main()
