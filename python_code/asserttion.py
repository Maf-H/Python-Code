"""
Demonstration of assert

The program runs flawlessly
if you enter a valid numerical value greater than or equal to zero;
otherwise, it stops and emits 'assert x >= 0.0'.
"""
#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

import math

x = float(input("Enter x : "))
assert x >= 0.0

print(math.sqrt(x))
print("No 'Assertion error'.")  # This line will be executed if there is no AssertionError
