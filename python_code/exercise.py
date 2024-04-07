#  Copyright (c) 2024-06/04/2024, 16:48.
#  @author Mesfin Haftu

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

name = 'Mesfin'
print(name, '\n', name.encode('utf-8'))
for i in name.encode('utf-8'):
    print(i)


