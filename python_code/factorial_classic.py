#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 16:59:56 2023

@author: mesfinhaftu
"""

#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

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