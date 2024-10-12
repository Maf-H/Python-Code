#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

from os import strerror

try:
    new_file = open("file_2.txt", 'wt')
    for i in range(10):
        new_file.write("Line #" + str(i + 1) + "\n")
    new_file.close()
except IOError as err:
    print(strerror(err))

