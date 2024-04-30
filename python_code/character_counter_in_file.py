#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

from os import strerror


def character_counter():
    # create a dictionary using comprehension with latin alphabets
    histogram = {chr(alpha): 0 for alpha in range(ord("a"), ord("z") + 1)}
    user_chosen_file = input("Enter full path of a file with it's name? ")

    try:
        opened_file = open(user_chosen_file, "rt")
        to_process = opened_file.read()
        print(to_process, "\n")

        for line in to_process.lower():
            for character in line:
                counter = 0
                # If it is a letter...
                if character.isalpha():
                    counter += 1
                    if counter > 0:
                        # we'll treat it as lower-case and update the appropriate counter.
                        histogram[character.lower()] += counter

                else:
                    continue
            opened_file.close()
        # If you want to sort the output in descending order
        # for i in dict(sorted(histogram.items(), key=lambda item: item[1], reverse=True)):
        for i in histogram.keys():
            if histogram[i] > 0:
                print(i.lower(), "->", histogram[i], end=",")

    except IOError as err:
        print(strerror(err.errno))
    except IndexError as err:
        print(err)


character_counter()
