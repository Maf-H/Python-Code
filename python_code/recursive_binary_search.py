def recursive_binary_search(input_list, target):
    """_summary_ returns True if target is in the list
    else returns False.

    Args:
        input_list (_type_): _description_
        target (_type_): _description_

    Returns:
        _type_: _description_
    """
    if len(input_list) == 0:
        return False
    else:
        mid = len(input_list)//2
        if input_list[mid] == target:
            return True
        elif input_list[mid] < target:
            return recursive_binary_search(input_list[mid + 1:], target)
        else:
            return recursive_binary_search(input_list[:mid], target)
        

#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu


#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu


#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu


#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

lst = [x for x in range(50)]
target = int(input("Target: "))
print(recursive_binary_search(lst, target))
    

