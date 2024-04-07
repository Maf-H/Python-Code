#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

import calendar as cal

# print(cal.calendar(1993))
# cal.prcal(2024)
# sets first day of the week to your choice.
cal.prmonth(2024, 3)
cal.setfirstweekday(0)

cal.prmonth(2024, 3)
"""
weekday(year, month, day) returns day of the week from 0 - 6
weekheader() returns 'Mo Tu We Th Fr Sa Su'
isleap(year) returns True if leap else False
leapdays(year1-> year2) returns total leap days between year1 and year2-1

"""
