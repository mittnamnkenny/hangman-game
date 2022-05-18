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
        raise SystemExit(f"You found the word {username}! It was: {word}")

    else:
        raise SystemExit(f"Game over {username} the word was: {word}")


def info():
    while True:
        username = input("What's your name? \n")
        age = input("What's your age? \n")
        if len(username) > 1 and age.isnumeric():
            print(f"Ok {username} let's play.")
            play(username, age)
        else:
            print("That is not a valid option, Please try again.")


def game_rules():
    while True:
        rules = input("Like to read the rules? y/n \n")
        if rules.lower() == "y":
            print("Rules of the game.")
            info()
        elif rules.lower() == "n":
            print("Ok, no rules.")
            info()
        else:
            print("That is not a valid option, Please try again.")


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
            game_rules()
        elif start_playing.lower() == "n":
            raise SystemExit("Exiting Game!")
        else:
            print("That is not a valid option, Please try again.")


main()
