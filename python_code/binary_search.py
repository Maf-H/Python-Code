#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu
def binary_search(input_list, target):
    first = 0
    last = len(input_list) - 1
    while first <= last:
        mid = (first + last) // 2
        if target == input_list[mid]:
            return mid
        elif input_list[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return None


in_list = [x for x in range(1, 51)]
print(binary_search(in_list, 1))
