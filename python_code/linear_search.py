"""
Linear search with input parameters of list and target
returns index of the target else returns None
"""


def linear_search(input_list, target):
    """
    returns index of the target else returns None
    :param input_list:
    :param target:
    :return:
    """
    for i in input_list:
        if i == target:
            return i
    return None


#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu


#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu


#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu


#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

input_list = [x for x in range(50)]
try:
    target = input("Enter a Target: ")
    target_type = type(target)
    result = linear_search(input_list, int(target))
    print("Target found at index: % i" % result if result is not None else "Target not in list")

except ValueError as err:
    print(err, "\nYou entered a non integer.")
except:
    print("Wrong input.")
