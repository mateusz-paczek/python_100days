# Program that calculates sum of the even numbers from 1 to 100

sum = 0
for number in range(1,101):
    if number % 2 == 0:
        sum += number

print(f"Total sum of even numbers from 1 to 100 is: {sum}. ")