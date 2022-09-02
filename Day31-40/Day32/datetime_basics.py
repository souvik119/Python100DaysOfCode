import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(type(now))
print(type(year))
print(month)
print(day_of_week)


date_of_birth = dt.datetime(year=1992, month=9, day=11)
print(date_of_birth)

