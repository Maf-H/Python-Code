#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 15:49:30 2023

@author: mesfinhaftu
"""
#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

#Factor of a number

def factor(number):
    count = 0
    for i in range(1,number//2 + 1):
        if ((number % i) == 0):
            count += i
            print(i)
            
factor(25)