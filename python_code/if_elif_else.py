#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 16:49:42 2023

@author: mesfinhaftu
"""

#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

# Grading System of AAiT
grade = float(input("Enter Course Grade: "))
if (grade >= 91):
    print('A+')
elif(grade >= 83):
    print('A')
elif(grade >= 80):
    print('A-')
elif(grade >= 75):
    print('B+')
elif(grade >= 70):
    print('B')
elif(grade >= 65):
    print('B-')
elif(grade >= 60):
    print('C+')
elif(grade >= 55):
    print('C')
elif(grade >= 50):
    print('C-')
elif(grade >= 45):
    print('D')
elif(grade >= 40):
    print('F')
else:
    print("NG")

    
