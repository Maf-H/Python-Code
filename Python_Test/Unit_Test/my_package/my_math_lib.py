#  Copyright (c) 02-06/04/2024, 16:48.
#  @author Mesfin Haftu

class my_math_lib:
    def __init__(self):
        """Constructor of this class."""
        print("Creating object:", self.__class__.__name__)

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def __del__(self):
        """Destructor for this class."""
        print("Destroying object: " + self.__class__.__name__)
