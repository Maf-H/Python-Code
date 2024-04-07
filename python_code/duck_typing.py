#  Copyright (c) 02-06/04/2024, 16:48.
#  @author Mesfin Haftu

# duck typing is a concept where the class of an object is less important than the methods/attr class type is not
# checked if minimum methods/attributes are present
# "If it walks like a duck, and it quacks like a duck, then it must be a duck."

class Duck:

    def walking(self):
        print("This duck is walking.")

    def talking(self):
        print("This duck is quaking.")


class Chicken:

    def walking(self):
        print("This Chicken is walking.")

    def talking(self):
        print("This Chicken is clucking.")


class Person:
    def catching(self, duck):
        duck.walking()
        duck.talking()
        print("You catch a critter.")


person = Person()
# The program doesn't care about the class of the object
# if it's methods/attr are the same
person.catching(Chicken())
person.catching(Duck())
