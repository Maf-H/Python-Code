str_1 = input("Enter the first string: ")
str_2 = input("Enter the second string: ")

#  Copyright (c) 2024-06/04/2024, 16:48.
#  @author Mesfin Haftu

# This is what we're going to do with both strings:
str_1 = "".join(sorted(str_1.replace(' ', '').upper()))
str_2 = "".join(sorted(str_2.replace(' ', '').upper()))


def is_anagram(string_1, string_2):
    if string_1 == string_2:
        print("Anagram.")
    else:
        print("Not Anagram.")


is_anagram(str_1, str_2)
#  Listen, Silent
