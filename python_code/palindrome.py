def is_palindrome(sample):
    sample = sample.replace(' ', '').lower()
    if sample == sample[::-1]:
        print("It's a palindrome.")
    else:
        print("It's not a palindrome.")


sample_input = input("Enter a word, phrase or sentence: ")
is_palindrome(sample_input)
#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

#  Ten animals I slam in a net.
