# Treasure hunt based on the following diagram
# #https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

turn = input("Where do you want to turn? Right - 'R' or Left - 'L' ")
if turn == 'L':
    swim_or_wait = input("Would you like to swim or wait? Swim - 'S' or Wait - 'W' ")
    if swim_or_wait == "W":
        door = input("Which door you would like to choose? Blue - 'B', Red - 'R' or Yellow - 'Y' ")
        if door == "Y":
            print("You win !!!")
        elif (door == "R"):
            print("Burned by fire. Game Over")
        elif (door == "B"):
            print("Eaten by beast. Game Over")
        else:
            print("Game Over")

    else:
        print("Attacked by trout. Game Over")
else: 
    print("Fall into the hole. Game Over")