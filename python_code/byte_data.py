#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    byte_data = open("byte_file.txt", "wb")
    byte_data.write(data)
    byte_data = open("byte_file.txt", "rb")
    byte_data.readinto(data)
    byte_data.close()
except IOError as err:
    print(strerror(err))


for b in data:
    print(hex(b), end=' ')
