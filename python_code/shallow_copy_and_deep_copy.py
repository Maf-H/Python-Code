#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 19:07:40 2023

@author: mesfinhaftu
"""

#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

from copy import deepcopy

dictionary = { "first" : [ 1, 2, 3 ], "second" : [4, 5, 6] }
shallow_copy = dictionary.copy() # copy by reference
deep_copy = deepcopy(dictionary) # copy by value
print(dictionary)
print(shallow_copy)
dictionary["second"].append(4)
print(dictionary)
print(shallow_copy)
print(deep_copy)
