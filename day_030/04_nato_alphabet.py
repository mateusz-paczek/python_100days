import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(data)
print("=====================================================================")
phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}
print(phonetic_dict)

print ("====================================================================")
#should_continue = True
#while should_continue:
#    try:
#        word = input("Enter a word: ").upper()
#        output_list = [phonetic_dict[letter] for letter in word]
#        should_continue = False
#    except KeyError:
#        print("Only letters are allowed")

### Alternative
def generate_phonetic():
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)
    except KeyError:
        print("Only letters are allowed")
        generate_phonetic() 

generate_phonetic()


