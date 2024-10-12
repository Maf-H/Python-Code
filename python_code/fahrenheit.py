#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 19:07:00 2023

@author: mesfin haftu
"""

#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

# The function to change Celsius to Fahrenheit


def fahrenheit(celsius):
    for num in range(1, celsius + 1):
        fahrenheit = (9/5) * num + 32
        print("%3d %10.1f " % (num, fahrenheit))
    return fahrenheit


celsius = int(input("Enter Temperature in Celsius: "))
temp_in_fahrenheit = fahrenheit(celsius)
print("%3dC = %3.1fF" % (celsius, temp_in_fahrenheit))

