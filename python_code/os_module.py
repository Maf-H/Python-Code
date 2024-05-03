#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

import os
import sys
import pwd
import time
import shutil

"""
os.uname() 
returns:
    systemname — stores the name of the operating system;
    nodename — stores the machine name on the network;
    release — OS release;
    version — OS version;
    machine — stores the hardware architecture identifier, e.g., x86_64.
"""
print(os.getlogin()) # returns user who is login
print(os.getuid())  # returns user id
print(pwd.getpwuid(os.getuid())) # returns more detail about user, id, pwd, bash
"""
result =os.umask(0b111111111) # returns current user mask of (read write execute)(root, group, universal user) 1; False, 0: True
bin(result)
os.umask(result)
"""
columns, lines = shutil.get_terminal_size()
print(columns, lines)  # 80x24 is recommended

print(os.uname())
print(os.name)  # returns posix for Unix, nt for windows
# os.makedirs("Test Directory/Inner Directory") # creates directory inside a directory
# os.chdir("Test Directory") # use to change directory
os.chdir("../../")
# os.removedirs("Test Directory/Inner Directory")
print(os.listdir())  # shows list of files and directories
print(os.getcwd())  # used to know the current working directory
# most useful of these are st_uid, st_size, and st_mtime stands for modification time
print(os.stat("/Volumes/Mesfin's Drive/Programming/Python Code/python_code/os_module.py"))
result = time.localtime(os.stat("/Volumes/Mesfin's Drive/Programming/Python Code/python_code/os_module.py").st_mtime)
print("Modified time @:", time.strftime("%Y-%m-%d %H:%M:%S", result))
access_permission = os.stat("/Volumes/Mesfin's Drive/Programming/Python Code/python_code/os_module.py").st_mode
# access permission of file owner(read, write, execute) group(read, write, execute) universal(read, write, execute) 1: True, 0: False binary representation is reverse of uname
print("access_permission:", bin(access_permission)[-9:])  
"""
you can give all the above one by one to the method 
os.system("...")
"""

# print(os.system("rmdir Python Code"))
# print(os.system("listdir"))
# print(os.getcwd())

print("Platform: ", sys.platform)
columns, lines = shutil.get_terminal_size()
print(columns, lines)  # 80x24 is recommended