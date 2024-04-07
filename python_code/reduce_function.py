#  Copyright (c) 02-06/04/2024, 16:48.
#  @author Mesfin Haftu

import functools

factorial = [5, 4, 3, 2, 1]
name = ["H", "E", "L", "L", "O"]

# Reduce function uses to perform an operation on iterable elements to make a single element
result = functools.reduce(lambda x, y: x + y, name)
print(result)
