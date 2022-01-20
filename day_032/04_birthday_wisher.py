##################### Normal Starting Project ######################

import random
import datetime as dt
import smtplib

MY_EMAIL = "MY_EMAIL@GMAIL.COM"
MY_PASSWORD = "<MY_PASSWORD>"

now = dt.datetime.now()
# Create tuple with month and day
today = (now.month,now.day)
#print(today)


# HINT 2: Use pandas to read the birthdays.csv
import pandas
data = pandas.read_csv("birthdays.csv")

#for index,row in data.iterrows():
#   print(index,row)
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

print(birthdays_dict)

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        new_content = contents.replace("[NAME]", birthday_person["name"])


import smtplib

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"], msg=f"Subject: Happy Birthday\n\n{new_content}")


