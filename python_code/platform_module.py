#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

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
