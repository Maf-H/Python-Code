#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:51:57 2023

@author: mesfin_haftu
"""

#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

# Factors of a number
# There are only four perfect number up-to 10,000 === 6, 28, 496, 8_128


def perfect_number(number):

    count = 0
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            count += i
        else:
            continue
            #  print(i)
    if count == number:
        print("%d is perfect number." % number)


for i in range(1, 1_000_000_000):
    perfect_number(i)

"""

Perfect number 
when (2**p - 1) = prime_number
    perfect_number = (2**p - 1)*2**(p - 1)
p = [2, 3, 5, 7, 9, 11, 13, 17, 19, 23]
perfect_number = [6, 28, 496,8_128,130_816\
                  2_096_128, 33_550_336, 8_589_869_056\
                  137_438_691_328, 35_184_367_894_528
                  ]

"""