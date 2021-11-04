from replit import clear
from art import logo

print(logo)

# Create an empty dictionary where we are going to store name/bid 
auction = {}
should_continue = True

# Populate auction dictionary
while should_continue:
    name = input("Tell me your name: ")
    bid = int(input("How much you would like to pay: $"))
    auction[name] = bid
    answer = input("Are there any users who want to bid? Type 'yes' or 'no' ")
    if answer == "no":
        should_continue = False
        #print("Goodbye! ")
    elif answer == "yes":
        clear()
# Check how Auction dictionary is looking
print(auction)

# Finding highest value in auction dictionary
highest_bid = 0
winner = ""
for name in auction:
    bid_amount = auction[name]
    #print(type(bid_amount))
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = name
print(f"The winner is {winner} with a bid of ${highest_bid}")

