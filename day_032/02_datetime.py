import datetime as dt

now = dt.datetime.now()
print(now)

year = now.year
print(year)

day_of_week = now.weekday()
print(day_of_week)
date_of_birth = dt.datetime(year=1981 , month=10 , day=15 , hour=6)
print(date_of_birth)