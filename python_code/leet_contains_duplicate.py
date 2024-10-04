"""
Python code to check whether there is a duplicate number or not.
"""
def contains_duplicate(nums: list[int]) -> bool:
    """
    create a dictionary that contains each unique digit 
    as a key and the number of repetition as value.
    if any digit has a value > 1 return True else False
    Time Complexity O(n)
    Space Complexity O(n)
    """
    # nums_dict = Counter(nums)
    # for key in nums_dict:
    #     if nums_dict[key] > 1:
    #         return True

    # return False

    nums_dict = {}
    for num in nums:
        if num in nums_dict:
            return True
        nums_dict[num] = 1
    return False
if __name__ == '__main__':
    print(contains_duplicate([1,2,3,4,5,7,8,4]))
