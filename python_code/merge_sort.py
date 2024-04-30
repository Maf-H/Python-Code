#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

from random import randint


def merge_sort(items):
    """
    Sort the list in ascending order
    divide: find the middle element index and divide the list in to equal or near equal two lists.
    conquer: sort the divided lists.
    merge: merge the sorted sub lists in to one and return the list.

    :param items:
    :return merge(left, right):
    time complexity O(nlog(n))
    """

    if len(items) <= 1:
        return items

    else:
        left_half, right_half = split(items)
        left = merge_sort(left_half)
        right = merge_sort(right_half)

    return merge(left, right)


def split(items):
    """
    Splits the list in two equal parts if it is list length is even or
    the left half list greater than by 1 to the right half list
    :param items:
    :return left_half, right_half:
    time complexity O(log(n))
    """
    mid = len(items) // 2
    left_half = items[: mid]
    right_half = items[mid:]
    # print("sssssssssssssssssssssss")
    # print(left_half, right_half)
    # print("sssssssssssssssssssssss")
    return left_half, right_half


def merge(left_half, right_half):
    """
    Sorts the sub lists and return the sorted list.
    :param left_half:
    :param right_half:
    :return sorted_list:
    time complexity O(n)
    """
    sorted_list = []
    i = 0
    j = 0

    while i < len(left_half) and j < len(right_half):

        if left_half[i] < right_half[j]:
            sorted_list.append(left_half[i])
            i += 1
        else:
            sorted_list.append(right_half[j])
            j += 1
    # print("____________________")
    # print(sorted_list)
    # print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
    if i < len(left_half):
        sorted_list += left_half[i:]
    else:
        sorted_list += right_half[j:]
    # print(sorted_list)
    # print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
    return sorted_list


input_list = [randint(1, 100) for i in range(11)]
print(input_list)
print(merge_sort(input_list))


def merge_sort(values):
    if len(values) <= 1:
        return values
    middle_index = len(values) // 2
    left_values = merge_sort(values[:middle_index])
    right_values = merge_sort(values[middle_index:])
    print("%15s %-15s " % (left_values, right_values))
    sorted_values = []
    left_index = 0
    right_index = 0
    while left_index < len(left_values) and right_index < len(right_values):
        if left_values[left_index] < right_values[right_index]:
            sorted_values.append(left_values[left_index])
            left_index += 1
        else:
            sorted_values.append(right_values[right_index])
            right_index += 1
    sorted_values += left_values[left_index:] if left_index < len(left_values) else right_values[right_index:]
    return sorted_values


numbers = [7, 10, 1, 5, 8, 33, 26, 6]
print(numbers)
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)

