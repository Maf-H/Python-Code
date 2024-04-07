#  Copyright (c) 2024-06/04/2024, 16:48.
#  @author Mesfin Haftu

from os import strerror

try:
    new_file = open("file_2.txt", 'wt')
    for i in range(10):
        new_file.write("Line #" + str(i + 1) + "\n")
    new_file.close()
except IOError as err:
    print(strerror(err))

