#  Copyright (c) 2024-06/04/2024, 16:48.
#  @author Mesfin Haftu

from datetime import datetime as dt, timedelta as td, time as t

"""
November 4, 2020 , 14:53:00
===========================
2020/11/04 14:53:00
20/November/04 14:53:00 PM
Wed, 2020 Nov 04
Wednesday, 2020 November 04
Weekday: 3
Day of the year: 309

Week number of the year: 44
"""

date_in = dt(2020, 11, 4, 14, 53, 0)
print(date_in.strftime('%Y/%m/%d %H:%M:%S'))
print(date_in.strftime('%y/%B/%d %H:%M:%S %p'))
print(date_in.strftime('%a, %Y %b %d'))
print(date_in.strftime('%A, %Y %B %d'))
print(date_in.strftime('Weekday:'), date_in.isoweekday())
print(date_in.strftime("Day of The Year: %j"))
print(date_in.strftime('Week number of the year: %W'))

