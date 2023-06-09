import random

#list of fruit
word_list = ["mango","coconut","strawberry","avocado","peach"]
print(word_list)

#print a randon word from the word_list
word = random.choice(word_list)
print(word)

#user input to get a letter
guess = input("Enter a letter: ")

#check user input is a single alphabetical letter
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
