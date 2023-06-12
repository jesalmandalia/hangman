Hangman is a classic game in which a player thinks of a word, and the other player tries to guess that word within a certain amount of attempts. It is a popular game that tests your vocabulary and deductive skills.

In the implementation of the Hangman game, the computer thinks of a word, and the user tries to guess it. The game progresses as the user enters letters one by one, attempting to uncover the word. If the user guesses a correct letter, it is revealed in the word. In the Hangman game, if the user guesses an incorrect letter, instead of drawing a visual representation of the hangman, the number of lives is reduced by 1. The goal of the game remains the same: to guess the word before the number of lives reaches 0, indicating a lost game.

- [Milestone 2](#milestone-2)
- [Milestone 3](#milestone-3)
	- [check\_guess()](#check_guess)
	- [ask\_for\_input()](#ask_for_input)
- [Milestone 4](#milestone-4)
	- [Hangman Class](#hangman-class)
		- [Attributes](#attributes)
		- [Methods](#methods)
- [Milestone 5](#milestone-5)
	- [play\_game()](#play_game)
- [How To Run](#how-to-run)


# Milestone 2
In milestone 2 of the game, the "milestone_2.py" file sets up some of the necessary variables for constructing the Hangman game. These variables include the word to be guessed. The file also includes a check to ensure that the user's input is alphabetical and a single letter.

# Milestone 3
Building upon milestone 2, milestone 3 introduces two functions:

## check_guess()
The `check_guess()` function converts the user's input, referred to as 'guess', to lowercase and then checks if the guess is included in the word. This function determines whether the guess is correct or not. If the guess is correct, it updates the word_guessed list to reveal the correctly guessed letters.

## ask_for_input()
The `ask_for_input()` function prompts the user to input a letter. It performs the necessary checks to ensure that the user's input is alphabetical and a single letter. If the input passes all the tests, the `check_guess()` function is called to evaluate the guess. Additionally, it keeps track of the list of guesses made by the user.

# Milestone 4
In milestone 4, the Hangman class is defined, encapsulating the game's functionality. Here is an overview of the class:

## Hangman Class
The Hangman class represents the Hangman game.

### Attributes
- `word`: The word to be guessed, picked randomly from a word_list.
- `word_guessed`: A list representing the current state of the word being guessed, with underscores for unguessed letters and revealed letters for correctly guessed ones.
- `num_letters`: The number of unique letters in the word that have not been guessed yet.
- `num_lives`: The number of lives (attempts) the player has remaining.
- `word_list`: A list of words from which the word to be guessed is selected.
- `list_of_guesses`: A list of the guesses that have already been tried.

### Methods
- `__init__(self, word_list, num_lives=5)`: The initialiser method that sets up the Hangman object. It randomly selects a word from the word_list, initialises the word_guessed list, and sets the number of letters, number of lives, word list, and list of guesses.

- `check_guess(self, guess)`: This method checks if the guess is in the word. It converts the guess to lowercase and updates the word_guessed list if the guess is correct. If the guess is incorrect, it reduces the number of lives and provides feedback to the player.

- `ask_for_input(self)`: This method prompts the user to input a letter. It performs input validation to ensure the input is a single alphabetical character. If the input is valid, it calls the `check_guess()` method to evaluate the guess and updates the list of guesses.

These milestones provide the foundation for a basic Hangman game, allowing players to guess letters and uncover the hidden word.

# Milestone 5
In milestone 5, further improvements are made to the Hangman game. The following changes are implemented:

## play_game()
- Create a function called `play_game` that takes `word_list` as a parameter.
- Inside the `play_game` function:
  - Create a variable called `num_lives` and assign it the value 5.
  - Create an instance of the Hangman class by calling `Hangman(word_list, num_lives)` and assign it to a variable called `game`.
  - Use a while loop with the condition `True` to control the game flow. Inside the loop, do the following:
    - Check if `num_lives` is 0. If it is, the game has ended and the user lost. Print a message saying 'You lost!' along with the word which failed to be guessed.
    - Next, check if `num_letters` is greater than 0. If it is, the game is not over, so call the `ask_for_input` method of the `game` object to continue the game. It's worth noting that in the `ask_for_input` method, the condition for the while loop has been updated compared to Milestone 4. The new condition checks if `num_lives` is greater than 0 and `num_letters` is greater than 0, which aligns with the game logic.
    - If `num_lives` is not 0 and `num_letters` is not greater than 0, that means the user has won the game. Print a message saying 'Congratulations. You won the game!'.

 Outside the function:
  - Call the `play_game` function to play the game. Don't forget to pass in your list of words as an argument to the function.

# How To Run

To run the game:
1. Ensure you have Python installed on your machine.
2. Download or clone this repository.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the following command to execute the game:

   ```bash
   python milestone_5.py

You should see the game prompt you to enter a letter. Follow the instructions to play the game. The filename `milestone_5.py` can be substituted with any of the other milestones documented above to run the code according to each stage of development. 

Please note that you can customise the word list by modifying the `word_list` variable in the code.

Feel free to explore the code and have fun playing Hangman!

