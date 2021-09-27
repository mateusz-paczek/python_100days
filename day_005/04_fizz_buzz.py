# Program that implements FizzBuzz game
# Rules: Program should print each number from 1 to 100
#        If the number is divisible by 3 than instead of the number it should print "Fizz"
#        If the number is divisible by 5 than instead of the number it should print "Buzz" 
#        If the number is divisible by 3 and 5 than instead of the number it should print "FizzBuzz"

for n in range(1,101):
    if (n % 3 == 0) and (n % 5 == 0):
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)