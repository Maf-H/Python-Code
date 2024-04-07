#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 12:47:21 2023

@author: mesfin_haftu
"""

count = 1
passed = 0
failed = 0

#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

# Using while loop
'''while count <= 10:
    result = int(input("Enter Result 1 -> pass: 2 -> fail: "))
    if result == 1:
        passed += 1
    elif result == 2:
        failed += 1
    count += 1
print("Total Passed =", passed)
print("Total Failed =", failed)
if passed >= 8:
    print("\nRaise Tuition")
'''    
# using for loops

for count in range (0,10,1):# Start from 0 end at 9
    result = int(input("Enter Result 1 -> pass: 2 -> fail: "))
    if result == 1:
        passed += 1
    elif result == 2:
        failed += 1
        
print("Total Passed =", passed)
print("Total Failed =", failed)
if passed >= 8:
    print("\nRaise Tuition")
