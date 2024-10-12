#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

from sys import path

path.append('..∖∖packages')
""" from sys import path: This line imports the path variable from the sys module. The sys module provides access to various system-specific variables and functions in Python. The path variable specifically refers to a list of directories where Python looks for modules when using the import statement.
path.append('..∖∖packages'): This line modifies the path variable by adding a new directory to the search list. The directory specified here is ..∖∖packages, which could be interpreted as two different paths depending on your environment:
Relative path: If ..∖∖packages is a relative path from the current script's location, it means adding the directory one level above the current directory and then entering the packages directory inside it. For example, if your script is in project/scripts, and the packages directory is in project, this would add project to the search list. """

from extra.iota import funI

print(funI())
from module import addl, multl

lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(addl(lists))
print(multl(lists))