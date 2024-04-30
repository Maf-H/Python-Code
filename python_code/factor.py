#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 15:49:30 2023

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

#Factor of a number

def factor(number):
    count = 0
    for i in range(1,number//2 + 1):
        if ((number % i) == 0):
            count += i
            print(i)
            
factor(25)