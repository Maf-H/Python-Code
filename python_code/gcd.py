
#  Copyright (c) 2024-06/04/2024, 16:48.
#  @author Mesfin Haftu

def gcd(x, y):
    while y:
        z = x
        x = y
        y = z % y
    return x

print(gcd(36,8))
print(2-4)