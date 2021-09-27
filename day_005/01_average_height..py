# Program that calculates average height of students (rounded to Integer)

student_heights = input("Input a list of student height, seperated by space. ").split()

# converting string into integers
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

#print(student_heights)

# Calculating average height (sum of all entries / no. of entries)
sum = 0
for student_height in student_heights:
    sum += student_height

average_height = int(sum / len(student_heights))
print(f"Average height is: {average_height} cm. ")