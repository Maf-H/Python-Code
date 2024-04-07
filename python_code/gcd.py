
#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

def gcd(x, y):
    while y:
        z = x
        x = y
        y = z % y
    return x

print(gcd(36,8))
print(2-4)