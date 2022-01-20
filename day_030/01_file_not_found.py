try:
    file = open("file.txt")
    a_dict = {"key":"value"}
    print(a_dict["key"])
except FileNotFoundError:
    file = open("file.txt", "w")
    file.write("EloElo")
except KeyError as error_message:
    print(f"The key {error_message} does not exist. ")

else: 
    content = file.read()
    print(content)

finally:
    file.close()
    print("File was closed")