import pandas

data = pandas.read_csv("birthdays.csv")
print(data)

# Loop through DataFrame in Pandas
for (index,row) in data.iterrows():
    print(row["name"]) 