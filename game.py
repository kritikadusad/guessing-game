"""A number-guessing game."""

# Put your code here
import random
first_name = input("Howdy, what's your name?")
print("{}, I'm thinking of a number between 1 and 100\nTry to guess my number".format(first_name))

random_number = random.randint(1,100)
print(random_number)
guess_count = 0

while True:
	guess_count += 1
	guess = int(input("What is your guess?"))
	if guess > random_number:
		print("Your guess is too high, try again")
	elif guess < random_number:
		print("Your guess is too low, try again")
	else:
		print("Well done, {}! You found my number in {} tries!".format(first_name, guess_count))
		break
	

