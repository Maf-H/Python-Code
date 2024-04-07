"""
The code below demonstrates military time
with 1 second ahead and back
methods:
    -__init__
    -__str__
    -next_second
    -prev_second

"""


#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

class Timer:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __str__(self):
        return "%.2d:%.2d:%.2d" % (self.__hour, self.__minute, self.__second)

    def next_second(self):
        self.__second += 1
        if self.__second == 60:
            self.__second = 0
            self.__minute += 1
            if self.__minute == 60:
                self.__minute = 0
                self.__hour += 1
                if self.__hour == 24:
                    self.__hour = 0

    def prev_second(self):
        self.__second -= 1
        if self.__second == -1:
            self.__second = 59
            self.__minute -= 1
            if self.__minute == -1:
                self.__minute = 59
                self.__hour -= 1
                if self.__hour == -1:
                    self.__hour = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
