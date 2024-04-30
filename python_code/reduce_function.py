#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

import functools

factorial = [5, 4, 3, 2, 1]
name = ["H", "E", "L", "L", "O"]

# Reduce function uses to perform an operation on iterable elements to make a single element
result = functools.reduce(lambda x, y: x + y, name)
print(result)
