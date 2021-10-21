alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def ceasar(text, shift_amount, direction):
    new_text = ""
    if direction=="encode":
        for letter in text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_text += alphabet[new_position]
        print(f"The encoded text is {new_text}")
    elif direction == "decode":
        for letter in text:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            new_text += alphabet[new_position]
        print(f"The decoded text is {new_text}")

ceasar(text=text, shift_amount=shift, direction=direction)