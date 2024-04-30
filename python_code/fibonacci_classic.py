#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 2024:01:58
@author: mesfin_haftu
"""


#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu


#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu


#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu


#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu


# Fibonacci Series using recursive function


def fib(num):
    if num < 0:
        return None
    if num == 0:
        return 0
    if num < 3:
        return 1
    else:
        fib_1 = 1
        fib_2 = 1
        fib_3 = 0

        for x in range(3, num + 1):
            fib_3 = fib_1 + fib_2
            fib_1, fib_2 = fib_2, fib_3

        return fib_3


bound = int(input("How many series do you need? "))

for i in range(bound):
    print(fib(i))
