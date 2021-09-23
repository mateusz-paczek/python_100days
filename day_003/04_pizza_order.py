# Program that calculates how much you should pay for Pizza
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: +$1

print("Welcome in Pizza ordering system")
pizza_size = input("What size of pizza do you want? Small - press 'S', Medium - press 'M', Large - press 'L' ")
if pizza_size == "S":
    bill = 15
elif pizza_size == "M":
    bill = 20
elif pizza_size == "L":
    bill = 20
add_pepperoni = input("Do you want to have pepperoni on your pizza? Yes - press 'Y', No - press 'N' ")
if add_pepperoni =="Y":
    if size == "S":
        bill += 2
    else:
        bill += 3 
extra_cheese = input("Do you want to have extra cheese on your pizza? Yes - press 'Y', No - press 'N' ")
if extra_cheese == "Y":
    bill +=1

print(f"Your pizza costs ${bill}. Thank you for your order! ")
