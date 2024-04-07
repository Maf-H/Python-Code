#  Copyright (c) 2024-06/04/2024, 16:48.
#  @author Mesfin Haftu

from os import strerror


try:
    stream = open("/python_code/file.txt", 'rt', encoding='utf-8')
    char = stream.read(1)
    char_counter = 1
    while char != '':
        if char != '\n':
            print(char, end='')
            char_counter += 1
        else:
            print(': %d characters.\n' % char_counter if char_counter != 0 else '')
            char_counter = 0
        char = stream.read(1)

    stream.close()
except IOError as err:
    print(strerror(err.errno))


stream = open("file.txt")
print(stream.readlines(20))
print(stream.readlines(20))
print(stream.readlines(20))
#
stream.close()


