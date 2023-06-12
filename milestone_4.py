import random


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['' for _ in range(len(self.word))]
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        index_word = enumerate(self.word)
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letter in self.word:
                for i, letter in index_word:
                    if letter == guess:
                        self.word_guessed[i] = guess
                self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            
    def ask_for_input(self):
        while True:
            guess = input("Enter a letter: ")  # user input to get a letter

            # check user input is a single alphabetical letter
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


# Example usage:
words = ["apple", "banana", "cherry"]
hangman_game = Hangman(words)
hangman_game.ask_for_input()
print(hangman_game.word_guessed)
