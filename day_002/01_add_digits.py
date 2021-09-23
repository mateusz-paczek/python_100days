# This program adds the digits in a 2 digit number
# e.g. if the input was 35, then output should be 3 + 5 = 8

digit = input("Please specify your digit: ")

result = int(digit[0])+int(digit[-1])
print(result)