"""A number-guessing game."""

# Put your code here
import random
first_name = input("Howdy, what's your name?")

guess_list = []

def guessing_number(): 
	global guess_list
	print("{}, I'm thinking of a number between 1 and 100\nTry to guess my number".format(first_name))
	random_number = random.randint(1,100)
	print(random_number)
	guess_count = 0
	
	while True:
		guess_count += 1
		try:
			guess = int(input("What is your guess?"))
		except ValueError: 
			print("this is not a number! Try again ")
			continue

		if  guess < 1 or guess >100 : 
			print("wow! you don't know your numbers! enter a VALID number!")
		else: 
			if guess > random_number:
				print("Your guess is too high, try again")
			elif guess < random_number:
				print("Your guess is too low, try again")
			else:
				print("Well done, {}! You found my number in {} tries! ".format(first_name, guess_count))
				restart = input("Would you like to play again? ")
				guess_list.append(guess_count)
				break
	best_score = min(guess_list)
	print("Your lowest number of guesses has been {}!".format(best_score))
	return restart
	


while True: 
	game = guessing_number()
	if game == 'yes':
		guessing_number()
		break
	else:
		break
	
		
		


