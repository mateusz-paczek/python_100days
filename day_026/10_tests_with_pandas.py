import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

for (key,value) in student_dict.items():
    print(value)

data_frame = pandas.DataFrame(student_dict)

print(data_frame)

for (index,row) in data_frame.iterrows():
    print(row.score)

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
print(nato_df)

for (index,row) in nato_df.iterrows():
    print(row.code)
nato_dict = {row.code:row.letter for (index,row) in nato_df.iterrows()}
print(nato_dict)
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}