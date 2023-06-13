import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initialises the Hangman game with the a word list and number of lives.

        Args:
            word_list (list): List of words to choose from. 
            num_lives (int, optional): Number of lives the player has, default is 5. This can be customised before running.
        """
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in range(len(self.word))]
        self.num_letters = len(set(self.word)) 
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Checks if the guessed letter is correct and follows game logic accordingly.

        Args:
            guess (str): User input guessed letter.
        """
        guess = guess.lower()
        index_word = enumerate(self.word)
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letter in self.word:
                for i, letter in index_word:
                    if letter == guess:
                        self.word_guessed[i] = guess
            self.num_letters -= 1
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        Asks the player for a single alphabetical letter input and performs checks to the input.
        """
        while self.num_lives > 0 and self.num_letters > 0:
            guess = input("Enter a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


def play_game(word_list):
    """
    Plays the Hangman game using the provided word list.

    Args:
        word_list (list): List of words to choose from.
    """
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            print(f"The word being guessed was {game.word}")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives > 0 and game.num_letters <= 0:
            print("Congratulations. You won the game!")
            break


"""
Example of running the Hangman game by calling the play_game function. 
The  num_lives (int) and word_list (list) can be customised before running.
"""
num_lives = 5 
word_list = ["mango", "coconut", "strawberry", "avocado", "peach"] 

play_game(word_list)
