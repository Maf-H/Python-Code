#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

import random
from time_class_with_setter_and_getter import Time

hour = int(random.randrange(0,24))
minute = int(random.randrange(0,60))
second = int(random.randrange(0,60))

time_1 = Time()
time_1.set_time(hour, minute, second)
print()
time_1.military_watch()
#print(time_1.__dict__) # tells variables and values of the class
time_1.standard_watch()
print()
print(time_1)
#print(time_1.__private) # we cant access attribute name starts with double underscore (__) that means they are private attributes
#print(time_1._Time__private) # we can access private attributes using _ClassName__attributeName


"""
print(Time.__bases__) # tells it's anccestors, if it is inherited.
print(Time.__dict__) # tells names of methods and variables.
print(Time.__doc__) # tells comments written under class.
print(Time.__module__) # tells names of modules.
print(Time.__name__) # tells name of the class.
print(time_1.__dict__) # tells variables and values of the class
"""
"""
These can be call by class_name.__method__
__bases__
__dict__
__doc__
__module__
__name__
 _hour, _minute, _second
"""
