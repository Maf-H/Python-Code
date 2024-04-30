#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 15:51:21 2023

@author: mesfin haftu
"""
#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

# Lists:- Their value and length of the list can be mutable or changed
# list = [expression for item in iterable]
# list = [expression for item in iterable if condition]
# list = [expression  if/else for item in iterable]
a_list = []

for i in range(1, 11):
    a_list += [i]    # Increases and assigns the list value
    # a_list[i] = i  #:===== we cant assign values this way
# The above for loop can be written shortly using list comprehension
# a_list = [i for i in range(1,11)]
# list_greater_than_5 = [i for i in a_list if i > 5]
# print(list_greater_than_5)
print(a_list)

for items in a_list:
    print(items)
    
a_list[9] = 99
print(a_list)
a_list[-10] = -111
a_list += ["Added"]     # Uses to increase list size
print(a_list)
del a_list[-11]         # Delete list value at index -11
print(a_list)

a_list.append("append")
print(a_list)
print("%6s  %-10s" % ("No", "Frequency"))
for i in range(1, len(a_list)):
    print("%6d  %-10d" % (i, a_list.count(i)))
    
"""
append( item ) 
count( element ) 
extend( newList ) 
index( element )
insert( index, item ) 
pop( [index] )
remove( element ) 
reverse()
sort( [compare-function] )
"""
