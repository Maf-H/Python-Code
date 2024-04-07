"""  Importing modules with addition and multiplication functions. """

#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

__counter = 0


def addl(lists):
    global __counter
    __counter += 1
    suml = 0

    for i in lists:
        suml += i
    return suml


def multl(lists):
    global __counter
    __counter += 1
    prodl = 1

    for i in lists:
        prodl *= i
    return prodl


if __name__ == "__main__":
    lists = [1, 2, 3, 4, 5]
    print(addl(lists))
    print(multl(lists))
