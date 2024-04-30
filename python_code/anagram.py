str_1 = input("Enter the first string: ")
str_2 = input("Enter the second string: ")

#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
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
