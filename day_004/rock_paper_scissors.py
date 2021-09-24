# Program that simulates Rock-Paper-Scissors game
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = [rock,paper,scissors]

print("Welcome to Rock-Paper-Scissors game! You play against computer. ")
your_choice = int(input("Choose Rock, Paper or Scissors. Rock - '1', Paper - '2', Scissors - '3' "))
if your_choice > 3 or your_choice < 1:
    print("You choose wrong number, you lose")
else:
    print(f"You choose: {choice[your_choice-1]} ")

    print("Computer chose")
    computer_choice = random.randint(1,3)
    print(choice[computer_choice-1])

    if your_choice == 1:
        if computer_choice == 1:
            print("Draw")
        elif computer_choice == 2:
            print("You lose")
        else:
            print("You won")

    if your_choice == 2:
        if computer_choice == 1:
            print("You won")
        elif computer_choice == 2:
            print("Draw")
        else:
            print("You lose")

    if your_choice == 3:
        if computer_choice == 1:
            print("You lose")
        elif computer_choice == 2:
            print("You won")
        else:
            print("Draw")

