#  Copyright (c) 2024-06/04/2024, 16:48.
#  @author Mesfin Haftu

from platform import platform, machine, processor, system, version
from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)

platform(aliased = False, terse = False)
print(platform())
print(platform( 1 ))
print(platform(False, True))
print(machine())
print(processor())
print(system())
print(version())
