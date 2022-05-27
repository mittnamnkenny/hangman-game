# My Hangman Game

This is my third milestone assignment with Code Institute. Hangman game is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.
This is a classic hangman game, where the user tries to guess the secret word letter by letter.
The number of incorrect guesses before the game ends is 7.

This site is targeted toward people who have an interest in simple word guessing games and Python.

[View the live project here.](https://hangman-game-mittnamnkenny.herokuapp.com/)

![Responsice Mockup](documentation/design.png)

##  User Experience (UX)

- ### User stories

    -   #### As a User, I want to be able to:

        1. Clearly understand how to navigate and start the game.
        2. Easily find instructions on how to play the game.
        3. Understand what input is required to proceed and that any exception is returned with a message to the user without causing the game to crash.
        4. Clearly see the number of incorrect guesses before the game ends.
        5. Clearly see what the secret word was if the user fails to guess it before the game ends.
        6. Continue playing the game once the game has finished without having to reenter the initial inputs from when the game started.
        7. Have a fun time playing the game and that it functions as expected.

## Flow chart
  - To explain the game logic, I created a flow chart using Lucidchart:

    ![Flow Chart](documentation/flow.png)

## Features

### Existing Features

#### 1. Welcome message

  - This is displayed when the game starts.
  - It will provide a welcome message to the user together with the ASCII hangman.
  - Then the user will then be prompted to start the game.

  - The user can choose: 
      - (y) - for yes - continue.
      - (n) - for no - closing the game.

    An error message informs the user if their entry is not in the correct format: ”That is not a valid option, Please try again.” The user must enter (y) to continue with the game.

    ![Welcome](documentation/welcome.png)

#### 2. Rules

  - After the user has decided to play the game, the user will be asked if they wish to read the rules before proceeding:

  - The user can choose: 
      - (y) - for yes - read the rules. 
      - (n) - for no - continue without reading the rules.

    An error message informs the user if their entry is not in the correct format: ”That is not a valid option, Please try again.” The user must enter (y) or (n) to continue.

    ![Navigation](documentation/rules.png)

#### 3. Setup

  - In the setup process the user will be asked for: name, age and favourite colour.
  ##### Name
  - The name input is used to interact with the user in various print statements.
  - The user must enter a name before proceeding, only alphabet letters, 2 characters or more is accepted.
  ##### Age
  - The age input is used to determine which random word is chosen for the game.
  - If the user's age is under 16, a word from the easier words list is presented.
  - The user must be 5 years or older to play the game.
  - The user will have to enter a number here to proceed.
  ##### Favourite colour
  - Lastly, the user will be asked for their favourite colour.
  - This is used to change the colour of the ASCII hangman.
  - If the user input matches with any key in the colours dictionary, otherwise a random colour is chosen.

  If the user enters an incorrect value in the setup process, an error message is displayed: ”That is not a valid option, Please try again.”

##### Matching Favourite colour:
![Setup](documentation/setup.png)

##### Random Favourite colour:
![Colours](documentation/colours.png)

#### 4. Game area

  - Once the user has finished the setup process, the game will begin. 
  - Depending on the age of the user, a random word is chosen.
  - The word to guess is represented by a row of dashes representing each letter of the word. The user will then try to guess the secret word letter by letter.
  - When the user enters a letter that is not in the secret word, the failed attempts count will increment by 1 and the terminal will print one element of the ASCII hangman.
  - The number of tries before the game ends is 7.

Only one alphabet letter is accepted or an error message is displayed: ”That is not a valid option, Please try again.”

When the user enters an already guessed letter again, the following message appears: You already tried: (letter). This will not increment the failed attempts count.
 
![Game Area](documentation/game.png)

#### 5. Result

  - The game will end when the user guessed the secret word or failed attempts reaches 7.
  - The user will be presented with a short message and then asked to play again: Do you want to play again? y/n

  - The user can choose: 
      - (y) - for yes - this will start a new game, with initial inputs.
      - (n) - for no - closing the game.

    An error message informs the user if their entry is not in the correct format: ”That is not a valid option, Please try again.” The user must enter (y) or (n) to continue.

##### User found the word:
![Win](documentation/win.png)

##### Failed attempts reached 7:
![Lose](documentation/lose.png)

#### Additional features

  - A feedback list was created to generate random text messages; this was implemented in various print statements to make the game more interesting and improve the overall experience.

### Features Left to Implement

- This game is popular in Sweden and in the future I would like to do a translated version of this game: Hänga gubbe.

## Design

- To make this game more attractive to the user, I have used the following code to print coloured text:

  - `<TEXT = "\033[0m">`
  - `<HIGHLIGHT = "\033[7m">`
  - `<RESPONSE = "\033[92m">`
  - `<ALERT = "\033[91m">`

- The favourite colours that are listed in the game:

  -  `<"red": "\033[31m",>`
  -  `<"green": "\033[32m",>`
  -  `<"yellow": "\033[33m",>`
  -  `<"blue": "\033[34m",>`
  -  `<"pink": "\033[95m",>`
  -  `<"cyan": "\033[36m",>`
  -  `<"purple": "\033[35m">`

## Technologies Used

- Python.
- [Am I Responsive:](http://ami.responsivedesign.is) Checking the responsive.
- [PEP8:](http://pep8online.com/) Check your code for PEP8 requirements.
- [Lucidchart:](https://www.lucidchart.com/pages/) Was used to create the flow chart.
- [Writer:](https://writer.com/grammar-checker/) Free Grammar Check.
- [Git](https://git-scm.com/) Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- [GitHub:](https://github.com/) GitHub is used to store the projects code after being pushed from Git.
- [Heroku:](https://dashboard.heroku.com/) for deployment of the application.