def start():
    play_game = True

    while play_game:
        continue_playing = input("Like to play? y/n \n")
        if continue_playing.lower() == "y":
            print("You have decided to play.")
        elif continue_playing.lower() == "n":
            print("Closing game.")
            play_game = False
        else:
            print("That is not a valid option, Please try again.")


start()
