#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

import pprint
import random

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] += 1

print(count)
pprint.pprint(count)

name = "mesfin Haftu"
degree = "Computer Engineering"
print("My name is {}. I graduated in {}.".format(name, degree))

cards = [x for x in range(2, 10)] + ['J', 'Q', 'K', 'A']
print(cards)
random.shuffle(cards)
print(cards)


def summer(*args):
    result = 0
    for i in args:
        result += i
    return result


print(summer(1, 2, 3, 4, 5))
