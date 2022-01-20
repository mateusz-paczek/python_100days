import smtplib
import random
import datetime as dt

# Open file with quotes
with open("quotes.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

# Choosing random quote from file
qoute = random.choice(lines)

# Starting with sending email
my_email = "<your_email>"
password = "<password>"

now = dt.datetime.now()
# Store actual day of the week in variable (0 - Monday, 1 - Tuesday etc.)
day_of_week = now.weekday()

# Send email if this is Tuesday
if day_of_week == 1:

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        
        connection.sendmail(
            from_addr=my_email,
            to_addrs="<recipient_email>",
            msg=f"Subject:MOTIVATION QOUTE\n\n{qoute}"
        )