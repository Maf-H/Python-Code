#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 8 07:34:00 2024

@author: mesfin_haftu
There are only 10 up-to 2.7e155
these are:

    [6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008139952128, 10889035741470030830754200461521744560128, 14474011154664524427946373126085988481573677491474835889066354349131199152128, 26815615859885194199148049996411692254958731641184786755447122887443528060146978161514511280138383284395055028465118831722842125059853682308859384882528256]
"""


def is_prime_number(number) -> int:
    """
    Checks if the number is a prime number
    """

    is_prime = True
    half = (number // 2) + 1

    for i in range(2, half):
        if number % i == 0:
            is_prime = False
            break

    return number


def perfect_numbers():

    perfect_number = []
    perfect_powers = [2, 3, 5, 7, 13, 17, 19, 31, 127, 257]
    #   prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,\
    #                41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, \
    #                89, 97, 101, 103, 107, 109, 113, 127, 131, \
    #                137, 139, 149, 151, 157, 163, 167, 173, 179, \
    #                181, 191, 193, 197, 199, 211, 223, 227, 229, \
    #                233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293
    #                ]

    for p in perfect_powers:

        euclid_fun = (2 ** p - 1) * 2 ** (p - 1)
        perfect_number.append(euclid_fun)
    return perfect_number


"""
    for p in perfect_powers:
        if is_prime_number((2 ** p - 1)):
            euclid_fun = (2 ** p - 1) * 2 ** (p - 1)
            perfect_number.append(euclid_fun)
    return perfect_number
"""


#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved


#  num = int(input(" Enter a number: "))
result = perfect_numbers()
print(result)
