# With dir or help built-in commands it is possible to know the available functions in a certain
# module. As you can see, in the datetime module there are many functions, but we will focus on date,
# datetime, time and timedelta. Let se see them one by one.

from datetime import datetime, date, time, timedelta

print(dir(datetime))
# ['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__', '__doc__',
# '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI',
# 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

now = datetime.now()
print(now)

day = now.day
month = now.month
year = now.year

hour = now.hour
minute = now.minute
second = now.second

timestamp = now.timestamp()

print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38

# Formatting Datetime

formatted_date = datetime(2022, 12, 30)  # 2022-12-30 00:00:00
print(formatted_date)

# https://strftime.org/

new_formatted_datetime = now.strftime('%H:%M:%S')
new_formatted_datetime2 = now.strftime("%d/%m/%Y, %H:%M:%S")
print('new date:', new_formatted_datetime)
print('new date2:', new_formatted_datetime2)

# String to date
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")

# Date

dt = date(2022, 9, 22)  # 2022-09-22
print('dt: ', dt)

# Time

t = time(12, 46, 7)
t2 = time(12, 46, 7, 3123)
print('t:', t)  # 12:46:07

# Time & Datetime difference finding

t1 = date(2022, 4, 13)
t2 = date(2023, 1, 1)

time_left_to_new_year = t2 - t1
print(time_left_to_new_year)  # 263 days, 0:00:00

# Difference Between Two Points in Time Using timedelata

t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)  # 94 days, 4:00:20
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)  # 7 days, 5:03:30
t3 = t1 - t2
print("t3 =", t3)  # 86 days, 22:56:50
