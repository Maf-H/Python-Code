#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 19:07:40 2023

@author: mesfinhaftu
"""

#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

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
