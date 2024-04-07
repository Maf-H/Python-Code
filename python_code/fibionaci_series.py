#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 12:10:55 2023

@author: mesfin_haftu
"""


#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved


#  Fibonacci Series using recursive function
def fibonacci_series(number):
    if number < 0:
        return None
    elif number == 0:
        return 0
    elif number < 3:
        return 1
    else:
        return fibonacci_series(number - 1) + fibonacci_series(number - 2)


upper_number = int(input("\nEnter Number: "))

for num in range(upper_number + 1):
    print("%3d = %15d" % (num, fibonacci_series(num)))  # prints intermediate results

golden_ratio = fibonacci_series(upper_number) / fibonacci_series(upper_number - 1)  # Golden_ratio = 1.618
print("golden_ratio = %.4f" % golden_ratio)
