#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 10:56:01 2023

@author: mesfinhaftu
"""
#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

#factorial classic
# factorial = 1
# limit = int(input("Enter Factorial of The Number: "))
# for fact in range(1,limit + 1):
#     factorial *= fact
#     print(factorial)

#Factorial Recursion

def factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        return number * factorial(number - 1)

upper_number = int(input("\nEnter Number: "))
for num in range(1, upper_number + 1):
    print("%3d! = %15d" %(num, factorial(num))) #prints intermediate results