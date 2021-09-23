# Program that calculate how much each person should pay for the meal if tip is specified.
# Format result to 2 decimal places = 25.20


print("Welcome to tip calculator")

bill = float(input("How much is the bill? "))
persons = int(input("For how many persons? "))
tip = int(input("How much tip you would like to give? "))

tip_as_percent = tip / 100

payment = (bill * (1+ tip_as_percent)) / persons
print(f"Each person should pay {round(payment,2)} dollars! ")
