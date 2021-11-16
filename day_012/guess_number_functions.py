import random
from art import logo

EASY_TURNS = 10
HARD_TURNS = 5

def compare(guess,answer,turns):
    ''' Function that compares two given numbers, check answer against guess. Returns number of turns remaining.'''
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print("This is correct number!")

def set_difficulty():
    ''' Function that set difficulty for the game'''
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_TURNS
    elif level == "hard":
        return HARD_TURNS

def game():
    print(logo)
    print("Welcome to the Number Guessing game")
    print("I am thinking about number between 1 and 100")
    answer = random.randint(1,100)
    print(f"Pssst, the correct number is {answer}")
    turns = set_difficulty()
    
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")

        # Let the user guess the number
        guess = int(input("Guess a number: "))
        turns = compare(guess,answer,turns)
        if turns == 0:
            print("You have run out of guesses. You lose! ")
            # exit when turns = 0
            return
        elif guess != answer:
            print("Guess again")

game()