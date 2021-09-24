# Program that picks random person to pay for the bill

import random
names_string = input("Give me everybody's names, seperated by comma and space. ")
names = names_string.split(", ")

index = random.randint(0,len(names)-1)

print(f"Today {names[index]} will pay for the bill! ")

# Alternative method 
# person_to_pay = random.choice(names)