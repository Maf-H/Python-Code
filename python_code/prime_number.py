#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 19:23:28 2023

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

# Prime Number up-to n


def prime_number(maximum):
    counter = 0
    primes = []
    for num in range(2, maximum):
        half = num//2 + 1
        is_prime = True
        
        for i in range (2, half):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            counter += 1
    return primes
    print("There are \'%d\' Prime Numbers." % counter)


n = int(input("\nEnter upper bound of number n: "))          
print(prime_number(n))
                
        