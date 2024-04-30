#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

from datetime import date
from datetime import timedelta
import datetime
import time

#  date.today() returns current year, month, day
today = date.today()
print("Today: ", date.today())
print("Year: ", today.year)
print("Month: ", today.month)
print("Day: ", today.day)
#  To create date object just pass the parameter
my_date = date(1993, 1, 29)
# replace(yyyy, mm, dd) you can pass 1 or 2 or 3 parameters to be replaced.
replaced = my_date.replace(year=1993)
# print(replaced)  # You can replace passed year, month, day value.
# print(my_date.weekday())  # return day of the week: monday - sunday 0 - 6
# print("DoB Week day", my_date.isoweekday())  # return day of the week: monday - sunday, 1 - 7

#  time stamp is the time in seconds starting from\
#  the Unix Os launched (1970, January 1, 00:00:00)
time_stamp = time.time()
# print("Time Stamp:", time_stamp, "Seconds since Jan 1, 1970, 00:00:00")
date_from_stamp = date.fromtimestamp(time_stamp)
# print(date_from_stamp)
# print(date.fromisoformat("2000-01-01"))
#  datetime module has time
t = datetime.time(5, 19, 55)
# print(t, "\nHour:", t.hour, "\nMinute:", t.minute, "\nSecond:", t.second)
#  sleep(second) waits second, and do what you order after that.
# print("I need to take a nap.")
# time.sleep(3)
# print("Take a good nap.")
# ctime() returns current week, date, month, year and time
# print(time.ctime())
# ctime(seconds) takes total seconds from the Epoch and returns date and time string from the second.
# print(time.ctime(time_stamp))
# print(time.gmtime(time.time()), "\n", time.localtime(time.time()))
# print(time.asctime(time.gmtime(time.time())))
# print(time.mktime())
print(datetime.datetime.today())
print(datetime.datetime.now())
dt = datetime.datetime(1993, 1, 29, 12, 0)
print(dt)
print("Timestamp: ", dt.timestamp())
d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))

dt = datetime.datetime(2022, 1, 31, 23, 59)
"""
%a stands for week day
%b Month as locale’s abbreviated name.
%I Hour (12-hour clock) as a zero-padded decimal number.
%M Minute as a zero-padded decimal number.
%p Locale’s equivalent of either AM or PM.
"""

print(dt.strftime('%a %d %b %Y, %I:%M%p'))
print(datetime.datetime.strptime("2022/1/31 11:59:00", "%Y/%m/%d %H:%M:%S"))

# changes to days, hours, minutes, seconds, micro-seconds
delta = timedelta(weeks=200, days=2, hours=30)
print(delta)
print("Days:", delta.days)
print("Seconds:", delta.seconds)


