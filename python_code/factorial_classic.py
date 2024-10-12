#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 16:59:56 2023

@author: mesfinhaftu
"""

#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

# Recursion by sequential

def factorial(number):
    number = int(number)
    loop = number+1
    fact = 1
    
    for num in range (1, loop):
        fact *= num
    return fact
    
number1 = input("Enter The Number: ")
print("Factorial of ",number1," = ",factorial(number1))