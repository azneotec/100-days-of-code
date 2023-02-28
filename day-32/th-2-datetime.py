import datetime as dt

now = dt.datetime.now()
print(now)
print(type(now))

year = now.year
print(year)
print(type(year))

month = now.month
print(month)  # 0 - Jan, 1 - Feb
print(type(month))

day_of_week = now.weekday()
print(day_of_week)  # 0 - Monday, 1 - Tuesday

date_of_birth = dt.datetime(year=2012, month=12, day=20)
print(date_of_birth)
