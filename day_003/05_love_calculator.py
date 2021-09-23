# This program will count given names agains T R U E   L O V E 

print ("Welcome to Love Calculator")

name1 = input("What is your name? ")
name2 = input("What is their name? ")

combined_string = (name1 + name2).lower()

t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")

l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")

first_digit = t + r + u + e
second_digit = l + o + v + e
score = str(first_digit) + str(second_digit)

if (int(score) < 10) or (int(score) > 90):
    print(f"Your Love Score is: {score}. You go together like coke and mentos")
elif (int(score) >=40) and (int(score) <=50):
    print(f"Your Love Score is {score}. You are all right together")
else:
    print(f"Your score is {score}")

#print(score)
