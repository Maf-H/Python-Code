#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 21:01:22 2023

@author: mesfin_haftu
"""
#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

num = int(input(" Enter a number: "))
is_prime = True
half = (num//2)+1

for i in range(2, half):
    if num % i == 0:
        is_prime = False
        break
       
if is_prime:
    print(num, ": is a 'Prime'.")
else:
    print("Not a Prime!")
