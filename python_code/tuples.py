#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 12:23:34 2023

@author: mesfinhaftu
"""

#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

# Tuple:- Their value is immutable and length of the tuple can't be changed
hour = int(input("Enter Hour: "))
minute = int(input("Enter Minute: "))
second = int(input("Enter Second: "))

clock = (hour, minute, second)
print(clock)
#clock[2] = 59   This line raises error because of tuples are immutable

print(clock[0:2])
