#  Copyright (c) 02-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

import functools

factorial = [5, 4, 3, 2, 1]
name = ["H", "E", "L", "L", "O"]

# Reduce function uses to perform an operation on iterable elements to make a single element
result = functools.reduce(lambda x, y: x + y, name)
print(result)
