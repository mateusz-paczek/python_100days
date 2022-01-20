import smtplib

my_email = "<your_email>"
password = "<your_password>"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="<dest_email>",
        msg="Subject:ELOELO\n\nThis is content of the mail"
    )