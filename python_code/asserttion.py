"""
Demonstration of assert

The program runs flawlessly
if you enter a valid numerical value greater than or equal to zero;
otherwise, it stops and emits 'assert x >= 0.0'.
"""
#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

import math

x = float(input("Enter x : "))
assert x >= 0.0

print(math.sqrt(x))
print("No 'Assertion error'.")  # This line will be executed if there is no AssertionError
