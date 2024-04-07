#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 17:08:13 2023

@author: mesfin_haftu
"""

#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

# calculating e with power series

def factorial(number):
    number = int(number)
    loop = number+1
    fact = 1
    
    for num in range (1, loop):
        fact *= num
    return fact

number = int(input("Enter The Number: "))
euler_number = 0
print("%4s %15s" %("No", "euler_value"))
for e in range (number + 1):
    euler_number += (1/factorial(e))
    print("%4d %10.6s" %(e, euler_number))
#print("The Euler number of the first 10 series = ", euler_number)