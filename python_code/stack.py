#  Copyright (c) 2024-06/04/2024, 16:48.
#  @author Mesfin Haftu

class Stack:
    def __init__(self):
        self.__stack = []
        self.__count = 0

    def is_empty(self):
        if len(self.__stack) == 0:
            return True
        else:
            return False

    def push(self, val):
        self.__count += 1
        self.__stack.append(val)

    def pop(self):
        if not self.is_empty():
            self.__count -= 1
            val = self.__stack[-1]
            del self.__stack[-1]
            return val
        else:
            return "The stack is empty! "

    def stack_size(self):
        return "Stack size = %d" % self.__count


stack_object = Stack()

for i in range(1, 10):
    stack_object.push(i)
    print(stack_object.stack_size())
print()
print(stack_object.stack_size())

for i in range(10):
    print(stack_object.pop(), end=",")

print("\n", stack_object.stack_size())
