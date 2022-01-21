from datetime import datetime
import smtplib
from sqlite3 import connect
import requests
import smtplip

MY_LAT = 50.049683
MY_LONG = 19.944544
MY_EMAIL = "<MY_EMAIL>"
MY_PASSWORD = "<MY_PASSWORD>"

def is_iss_overhead():
    # Check ISS position at the moment
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    # Extract ISS Latitude and Longitude
    iss_latitude = int(data["iss_position"]["latitude"])
    iss_longitude = int(data["iss_position"]["longitude"])

    # Your position is withing +5 or -5 degrees of the ISS position
    if MY_LAT-5 <= iss_latitude <= MY_LAT + 5 and MY_LONG <= iss_longiture <= MY_LONG + 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    # Extract sunrise and sunset 
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    # Check if its a night
    if time_now >= sunset or time_now <= sunrise:
        return True

if is_iss_overhead() and is_night():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject:Look up\n\nThe ISS is above you now!"
    )
#print(data)