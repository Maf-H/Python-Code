# -*- coding: utf-8 -*-
"""
Spyder Editor

@ author Mesfin Haftu"""
#  Copyright (c) 2024-06/04/2024, 16:48.
#  @author Mesfin Haftu

# Continue and Break
print("Year %28s"%"Quib of The Number")
print("=======      =====================")

for i in range (10):
    if i == 5:
        continue
    print("%4d%21d" %(i, i**3))
print()
    
for i in range (10):
    if i == 5:
        break
    print("%4d%21d" %(i, i**3))