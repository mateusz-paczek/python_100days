import requests
import datetime as dt
MY_LAT = 51.507
MY_LONG = -0.1234

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,

}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
time_now = dt.datetime.now()

print(data)
print(time_now)
print(sunrise.split("T")[1].split(":")[0])
print(sunset)