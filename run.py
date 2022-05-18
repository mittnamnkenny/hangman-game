import random

guesses = []
wrong_guesses = []

def play():
    file = open("words.txt", "r")
    words = file.readlines()
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
            wrong_guesses.append(guess)
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


def start():
    play_game = True

    while play_game:
        continue_playing = input("Like to play? y/n \n")
        if continue_playing.lower() == "y":
            print("You have decided to play.")
            play()
        elif continue_playing.lower() == "n":
            print("Closing game.")
            play_game = False
        else:
            print("That is not a valid option, Please try again.")


start()
