"""
# r- read,
w- write, Creates a new file or overwrites the existing file.
a- append, appends a file at the end of the file "use \n to append in the new line
r+ - read/write
"""

#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

names_profession = open("file.txt", "r") # r- read, w- write, a- append, r+ - read/write
print(names_profession.readable()) # Prints Boolean True if the file is readable.
print(names_profession.read()) # Print all the contents of the file.
print(names_profession.readline()) # Reads the first line and change the cursor position to the next line.
print("******")

for name_prof in names_profession.readlines():
    print(name_prof)

names_profession.close()
