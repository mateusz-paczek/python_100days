# Program that calculates a highest score 

scores = input("Input a list of student scores. ").split()

# Convert elements of the list to integers

for n in range(0, len(scores)):
    scores[n] = int(scores[n])

print(scores)

max_score = 0
for score in scores:
    if score > max_score:
        max_score = score

print(f"Max score if {max_score}. ")