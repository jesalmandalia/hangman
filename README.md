# Hangman

Hangman is a classic game in which a player thinks of a word, and the other player tries to guess that word within a certain amount of attempts. It is a popular game that tests your vocabulary and deductive skills.

In the implementation of the Hangman game, the computer thinks of a word, and the user tries to guess it. The game progresses as the user enters letters one by one, attempting to uncover the word. If the user guesses a correct letter, it is revealed in the word. However, if the user guesses an incorrect letter, a part of the hangman is drawn. The goal is to guess the word before the hangman is completely drawn.

## Milestone 2
In milestone 2 of the game, the "milestone_2.py" file sets up some of the necessary variables for constructing the Hangman game. These variables include the word to be guessed. The file also includes a check to ensure that the user's input is alphabetical and a single letter.

## Milestone 3
Building upon milestone 2, milestone 3 introduces two functions:

### check_guess()
The `check_guess()` function converts the user's input, referred to as 'guess', to lowercase and then checks if the guess is included in the word. This function determines whether the guess is correct or not. If the guess is correct, it updates the word_guessed list to reveal the correctly guessed letters.

### ask_for_input()
The `ask_for_input()` function prompts the user to input a letter. It performs the necessary checks to ensure that the user's input is alphabetical and a single letter. If the input passes all the tests, the `check_guess()` function is called to evaluate the guess. Additionally, it keeps track of the list of guesses made by the user.

## Milestone 4
In milestone 4, the Hangman class is defined, encapsulating the game's functionality. Here is an overview of the class:

### Hangman Class
The Hangman class represents the Hangman game.

#### Attributes
- `word`: The word to be guessed, picked randomly from a word_list.
- `word_guessed`: A list representing the current state of the word being guessed, with underscores for unguessed letters and revealed letters for correctly guessed ones.
- `num_letters`: The number of unique letters in the word that have not been guessed yet.
- `num_lives`: The number of lives (attempts) the player has remaining.
- `word_list`: A list of words from which the word to be guessed is selected.
- `list_of_guesses`: A list of the guesses that have already been tried.

#### Methods
- `__init__(self, word_list, num_lives=5)`: The initializer method that sets up the Hangman object. It randomly selects a word from the word_list, initializes the word_guessed list, and sets the number of letters, number of lives, word list, and list of guesses.

- `check_guess(self, guess)`: This method checks if the guess is in the word. It converts the guess to lowercase and updates the word_guessed list if the guess is correct. If the guess is incorrect, it reduces the number of lives and provides feedback to the player.

- `ask_for_input(self)`: This method prompts the user to input a letter. It performs input validation to ensure the input is a single alphabetical character. If the input is valid, it calls the `check_guess()` method to evaluate the guess and updates the list of guesses.

These milestones provide the foundation for a basic Hangman game, allowing players to guess letters and uncover
