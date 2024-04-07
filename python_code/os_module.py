#  Copyright (c) 2024-06/04/2024, 16:48.
#  @author Mesfin Haftu

import os
import sys

"""
os.uname() 
returns:
    systemname — stores the name of the operating system;
    nodename — stores the machine name on the network;
    release — OS release;
    version — OS version;
    machine — stores the hardware architecture identifier, e.g., x86_64.
"""
print(os.uname())
print(os.name)  # returns posix for Unix, nt for windows
# os.makedirs("Test Directory/Inner Directory") # creates directory inside a directory
# os.chdir("Test Directory") # use to change directory
os.chdir("../../")
# os.removedirs("Test Directory/Inner Directory")
print(os.listdir())  # shows list of files and directories
print(os.getcwd())  # used to know the current working directory
"""
you can give all the above one by one to the method 
os.system("...")
"""

# print(os.system("rmdir Python Code"))
# print(os.system("listdir"))
# print(os.getcwd())

print(sys.platform)
