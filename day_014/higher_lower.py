from art import logo, vs
from game_data import data
import random
from replit import clear

def format_data(account):
    """Format account data into printable data"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description} from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if user is right"""
    if a_followers > b_followers:
        if guess == "a":
            return True
        else:
            return False
    else:
        if guess == "a":
            return False
        else:
            return True

score = 0
print(logo)
# Make a game repeatable
account_b = random.choice(data)
game_should_continue = True
while game_should_continue:

    # Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}. ")
    print(vs)
    print(f"Compare B: {format_data(account_b)}. ")
    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B'").lower()


    # Check if user is correct
    ## Get the follower count of each account

    a_follower_count  = account_a["follower_count"] 
    b_follower_count  = account_b["follower_count"]
    ## Use if statemet to check if user is correct

    is_correct = check_answer(guess,a_follower_count, b_follower_count)

    clear()
    print(logo)
    # Give a user feedback on their guess
    if is_correct:
        score += 1
        print(f"You are right. You score is now {score}")
    else:
        game_should_continue = False
        print(f"Sorry, you are wrong. Your final score is {score}")

# Score keeping

# Make the game repeatable

# Making account at position B become the next account at position A


# Clear the screen