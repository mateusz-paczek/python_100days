import pandas
data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])

temp_list = data["temp"].to_list()
print(temp_list)

sum_temp = 0
for temp in temp_list:
     sum_temp += temp
     
average_temp = sum_temp/len(temp_list)
print(average_temp)