#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

from random import randint


def quick_sort(values):

    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]

    for number in values[1:]:
        if number <= pivot:
            less_than_pivot.append(number)
        else:
            greater_than_pivot.append(number)
    # print("Left:%25s %1s right:%-25s" % (less_than_pivot, pivot, greater_than_pivot))
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


numbers = [randint(1, 1000) for i in range(100000)]
# print(numbers)
print(quick_sort(numbers))
