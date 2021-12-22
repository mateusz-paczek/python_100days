#file = open("my_file.txt")
#content = file.read()
#print(content)
#file.close()

with open("my_file.txt", mode="a") as file:
    print(file.write("\nNew text\n"))