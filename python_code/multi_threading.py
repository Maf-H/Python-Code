#  Copyright (c) 02-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

# Multithreading is recommended for io bound tasks GIL (global interpreter Lock) allows 1 thread execution at a time,
# when one of the threads become idle the next will continue
# thread = a flow of execution. Like a separate order
# of instructions.However, each thread takes a turn running to achieve concurrency GIL = (global interpreter lock) ,
# allows only one thread to hold the control of the Pytahon interpreter
import threading
import time


def eat():
    time.sleep(3)
    print('You ate your breakfast')


def coffee():
    time.sleep(4)
    print('You drank your coffee.')


def study():
    time.sleep(5)
    print('You finish studying.')


# The following code creates additional threads
# and use each for every function
# executing these 3 functions takes 5 seconds only

x = threading.Thread(target=eat, args=())
x.start()
y = threading.Thread(target=coffee, args=())
y.start()
z = threading.Thread(target=study, args=())
z.start()

# executing these 3 functions takes 3 + 4 + 5 = 12 seconds
# eat()
# coffee()
# study()

# if you join a thread the main function will wait to finish that thread
x.join()
y.join()
z.join()

print('Total number of active threads: ', threading.active_count())
print(threading.enumerate())
print('Main thread process time: ', time.process_time())

