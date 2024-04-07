#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 00:31:21 2023

@author: mesfinhaftu
"""


def modify_list(a_list):          
    for i in range(len(a_list)):
        a_list[i] *= 2
        
def modify_element(element):
        element *= 2

#  Copyright (c) 2024-06/04/2024, 16:48.
#  @author Mesfin Haftu

a_list = [1,2,3,4,5]
print(a_list)
print()

modify_element(a_list[4]) #Passing element of a list can't be  change original values ...called passing by value

print(a_list[4])
print()


modify_list(a_list)   #Passing the entire list gives you the ability to change values ...called passing by reference
print(a_list)
print()

modify_element(a_list[4])
print(a_list[4])
print()

modify_element(a_list[4])
print(a_list[4])
print()


modify_list(a_list)
print(a_list)
print()

modify_element(a_list[4])
print(a_list[4])
