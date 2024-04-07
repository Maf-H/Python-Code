#  Copyright (c) 02-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

# Using walrus operator you can assign value to variables as part of larger expression.

foods = list()
# while True:
#     food = input("What food do you like? ")
#     if food == 'quite':
#         break
#     foods.append(food)

while food := input("What food do you like? ") != 'quite':
    foods.append(food)