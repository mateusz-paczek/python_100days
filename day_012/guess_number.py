import random
from art import logo
print(logo)
print("Welcome to the Number Guessing game")
print("I am thinking about number between 1 and 100")

guess = random.randint(1,100)
print(type(guess))
print(f"Pssst, the correct number is {guess}")
print(guess)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
if difficulty == "easy":
    no_of_guesses = 5
elif difficulty == "hard":
    no_of_guesses = 10

while no_of_guesses:
    user_guess = int(input("Make a guess: "))
    if user_guess > guess:
        print("Too high")
        no_of_guesses -= 1
        print(f"You have {no_of_guesses} attempts remaining to guess the number")
    elif user_guess < guess:
        print("Too low")
        no_of_guesses -= 1
        print(f"You have {no_of_guesses} attempts remaining to guess the number")
    else: 
        print("You won!")
        no_of_guesses = 0

