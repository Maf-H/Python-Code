#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 16:25:02 2023

@author: mesfin haftu
"""

#  Copyright (c) 2024-06/04/2024, 16:48.
#  @author Mesfin Haftu

import random


def dice_roll():
    dice_1 = random.randrange(1,7)
    dice_2 = random.randrange(1,7)
    sum_of_spots = dice_1 + dice_2
    print("You rolled %d + %d = %d" %(dice_1, dice_2, sum_of_spots))
    return sum_of_spots


counter = 1
result = dice_roll()

if result == 7 or result == 11:
    game_status = "WIN"
elif result == 2 or result == 3 or result == 12:
    game_status = "LOST"
else:
    point = result
    print("Point is ", point)
    game_status = "CONTINUE"
    
while game_status == "CONTINUE":
    print()
    next_roll = dice_roll()
    
    if next_roll == 7:
        game_status = "LOST"
    elif next_roll == result:
        game_status = "WIN"

if game_status == "WIN":
    print("You WIN!")
else:
    print("You LOST!")

