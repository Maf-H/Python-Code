"""
Luhn Algorithm to verify card number
Here's how the Luhn algorithm works:

Double every second digit, starting from the rightmost digit.
If any of the doubled numbers are greater than 9, subtract 9 from them.
Add all the digits of the original numbers and the doubled numbers together.
If the total is divisible by 10, the card number is valid. Otherwise, it's invalid.
Example:

Let's verify the card number 49927398716.

Double every second digit, starting from the right:
49927398716 becomes 499273987162
Subtract 9 from any doubled numbers greater than 9:
499273987162 becomes 499273987162
Add all the digits together:
4 + 9 + 9 + 2 + 7 + 3 + 9 + 8 + 7 + 1 + 6 + 2 = 87
Check if the total is divisible by 10:
87 is not divisible by 10, so the card number is invalid.
"""

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    print(total)
    return 0 == total % 10


def main():
	card_number = '4111-1111-4555-1142'
	card_translation = str.maketrans({'-': '', ' ': ''})
	translated_card_number = card_number.translate(card_translation)

	# print(translated_card_number)

	if verify_card_number(translated_card_number):
	    print("VALID!")
	else:
		print("INVALID!")

main()
