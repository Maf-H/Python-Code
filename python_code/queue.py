"""
The following code demonstrates Queue with
    -enqueue
    -dequeue
    -is_empty
    -queue_size
"""


#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

class Queue:

    def __init__(self):
        self.__queue = []
        self.__size = 0

    def enqueue(self, val):
        self.__queue.append(val)
        self.__size += 1

    def dequeue(self):
        if not self.is_empty():
            self.__size -= 1
            val = self.__queue[0]
            del self.__queue[0]
            return val
        else:
            return "\nQueue is empty!"

    def is_empty(self):
        if self.__size == 0:
            return True
        else:
            return False

    def queue_size(self):
        return "Queue size = %d" % self.__size


queue_ob = Queue()
for i in range(1, 10):
    queue_ob.enqueue(i)
    print(queue_ob.queue_size())

for i in range(10):
    print(queue_ob.dequeue(), end = ",")

