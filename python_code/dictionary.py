#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 16:19:47 2023

@author: mesfin haftu
"""


# Dictionary can be created or updated from existing using dictionary comprehension.
# dictionary = {key: expression  for (key, value) in iterable}
# dictionary = {key: expression  for (key, value) in iterable if condition}
# dictionary = {key: if/else  for (key, value) in iterable}
# kiremt = {key: value for (key, value) in months.items() if 1 <= key < 4}
# print('ክረምት፡', kiremt)
books = {1: "ዴርቶጋዳ", 2: "ዝጎራ", 3: "ኅያሉ ሽብርተኛ"}
months = {1: "መስከረም", 2: "ጥቅምት", 3: "ሕዳ", 4: "ታሕሳስ", 5: "ጥር", 6: "የካቲት", 7: "መጋቢት", 8: "ሚያዝያ", 9: "ግንቦት", 10: "ሰኔ",
          11: "ሐምሌ", 12: "ነሃሴ", 13: "ጳጉሜ"}

print(books[3])
books[4] = "መርበብት"
books[5] = "ሐሽማል"
#  print(books)
del books[5]  # deleting dictionary value with key
# print(months)
# print(books)
# 6months.clear()
# print(books)
books.update(months)
print(months.get(19))

"""
 clear()
 copy()
 get( key [, returnValue] )
 has_key( key )
 items()
 keys()
 popitem()
 setdefault( key [, dummyValue] )
 update( newDictionary )
 values()
 iterkeys()
 iteritems()
 itervalues()
"""
werat = months.copy()
print(werat)
months[14] = "Shallow Copy"
print(months.items())
# print(werat)
