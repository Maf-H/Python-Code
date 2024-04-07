#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 03:26:25 2023

@author: mesfinhaftu
"""

#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

# Two dimentional sequence
list_1 = [[1,2,3],[4,5,6],[7,8,9]]
tuple_1 = ((1,2,3) ,(3,), (4,5))

for row in list_1:
    for i in row:
        print(i, end = ' ')
    print()
print()

for row in tuple_1:
    for i in row:
        print(i, end = ' ')
    print()
print("       ",)
print(list_1[1])
    
