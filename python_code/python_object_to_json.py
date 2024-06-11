"""#! /usr/bin/python3"""
# Date Created: May 24 2024 05:46
# @author mesfin haftu

import json

class Who():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
def encode_who(w):
    try:
        return w.__dict__
    except TypeError as t_err:
        print(__class__.__name__, 'is not JSON serializable')
        
some_one = Who("Jean Doe", 31)
# print(json.dumps(some_one))
print(json.dumps(some_one, default=encode_who))
