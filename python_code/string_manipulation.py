""" String Manipulation. """

alpha = "መስፍን ሃፍቱ"
print(ord('a'))  # ascii / utf-8 character value
print(chr(4640))  # code value to ascii / utf-8

#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

# Slices

print(alpha[::2])
print(alpha[1:4:2])  # alpha(start:end:jump-1)
# del alpha[0]  # String is immutable " raises Error"
# del alpha # This deletes the string
name_as_char = list(alpha)
print(name_as_char)
print(alpha.count('ፍ'))
alpha.split() # returns a  list from the input which are separated by space

ls_1 = ["መስፍን", "ሃፍቱ", "ተሾመ", "ረታ"]
str1 = "መስፍን"
print(ls_1)
#  print(sorted(ls_1))
ls_1.sort()
print(ls_1)