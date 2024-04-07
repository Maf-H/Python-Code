#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 18:17:10 2023

@author: mesfinhaftu
"""

#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

count = 0
total = 0
grade = int(input("Enter Grade: -1 to END = "))

while grade != -1:
    total += grade
    count += 1
    grade = float(input("Enter Grade: -1 to END = "))

if count != 0:
    print("\nAverage = ", total/count)
else:
    print("\nNo grade is entered.")
