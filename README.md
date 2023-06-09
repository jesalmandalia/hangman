# Hangman

Hangman is a classic game in which a player thinks of a word, and the other player tries to guess that word within a certain amount of attempts. It is a popular game that tests your vocabulary and deductive skills.

In the implementation of the Hangman game, the computer thinks of a word, and the user tries to guess it. The game progresses as the user enters letters one by one, attempting to uncover the word. If the user guesses a correct letter, it is revealed in the word. However, if the user guesses an incorrect letter, a part of the hangman is drawn. The goal is to guess the word before the hangman is completely drawn.

## Milestone 2
In milestone 2 of the game, the "milestone_2.py" file sets up some of the necessary variables for constructing the Hangman game. These variables include the word to be guessed and a list to keep track of the guessed letters. The file also includes a check to ensure that the user's input is alphabetical and a single letter.

## Milestone 3
Building upon milestone 2, milestone 3 introduces two functions. 

-The first function, "check_guess()", converts the user's input, referred to as 'guess', to lowercase and then checks if the guess is included in the word. This function determines whether the guess is correct or not.

-The second function, "ask_for_input()", prompts the user to input a letter. It performs the necessary checks to ensure that the user's input is alphabetical and a single letter. If the input passes all the tests, the "check_guess()" function is called to evaluate the guess.

These milestones provide the foundation for a basic Hangman game, allowing players to guess letters and uncover the hidden word. 
