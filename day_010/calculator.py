from replit import clear
from art import logo
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1/n2

# Create of Operation dictionary where the value is '+-*/' and the keys are name of the functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide, 
}
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

# Loop through symbols
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        # Pick one symbol
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        # Save calculation symbol based on user choice
        calculation_symbol = operations[operation_symbol]
        answer = calculation_symbol(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        proceed = input(f"Type 'y' with calculating with {answer} or type 'n' to start a new calculation...")
        if proceed == "n":
            should_continue = False
            calculator()
        elif proceed == "y":
            num1 = answer
                
calculator()