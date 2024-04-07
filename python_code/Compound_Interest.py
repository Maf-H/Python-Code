#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 13:35:04 2023

@author: mesfin_haftu
"""

#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

# compound interest

principal = float(input("Enter Principal: "))
rate = float(input("Enter Rate: "))/100
year = int(input("Enter Year: "))

amount = 0.0
for current_month in range(1, (year*12 + 1)):
    # noinspection PyPep8
    amount = principal*(1+rate/12)**current_month
#    print(current_month, "month Amount = ", amount)

# noinspection PyUnboundLocalVariable
print("\nAmount =", amount)


