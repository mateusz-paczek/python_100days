# Program that tells you how many weeks you have left considering you will live till 90y
# Assumptions: 365 days in a year, 52 weeks in a year and 12 months in a year

age = int(input("What is your age? "))

years_remaining = 90 - age

print(f"You have {years_remaining * 365} days, {years_remaining * 52} weeks and {years_remaining * 12 } months left. Enjoy every minute! ")