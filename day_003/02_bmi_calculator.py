# Program that calculates your BMI and interprets result

height = float(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))

bmi = (weight) / (height ** 2)

if bmi < 18.5:
    print(f"Your BMI is: {round(bmi,2)}. You are underweight")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your BMI is: {round(bmi,2)}. Your weight is normal")
elif bmi >= 25 and bmi < 30:
    print(f"Your BMI is: {round(bmi,2)}. You are slightly overweight")
elif bmi >= 30 and bmi < 35:
    print(f"Your BMI is: {round(bmi,2)}. You are obese")
elif bmi >= 35:
    print(f"Your BMI is: {round(bmi,2)}. You are clinically obese")
    