#with open("weather_data.csv") as file:
#    content = file.readlines()
#    print(content)

import csv
with open("weather_data.csv") as file:
    content = csv.reader(file)   
    temperature = []
    print(content)
    for row in content:
        print(row)
        if row[1] != "temp":
            temperature.append(int(row[1]))
print(temperature)