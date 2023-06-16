import random

#list of fruit
word_list = ["mango","coconut","strawberry","avocado","peach"]
print(word_list)

#print a randon word from the word_list
word = random.choice(word_list)
print(word)


def check_guess(guess):
	#converts guess into lowercase
	guess = guess.lower()

	if guess in word:
		print(f"Good guess! {guess} is in the word.")
	else:
	        print(f"Sorry, {guess} is not in the word. Try again.")
        
def ask_for_input():
	while True:
		guess = input("Enter a letter: ") #user input to get a letter

		# check user input is a single alphabetical letter
		if len(guess) == 1 and guess.isalpha():
			check_guess(guess)
			break
		else:
			print("Invalid letter. Please, enter a single alphabetical character.")
	
  
ask_for_input()


 
