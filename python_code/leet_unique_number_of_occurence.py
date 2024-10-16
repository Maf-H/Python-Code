"""Given an array of integers arr, return true if the number of occurrences of each value 
in the array is unique or false otherwise.
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. 
No two values have the same number of occurrences.
Input: arr = [1,2]
Output: false"""
from collections import Counter
def unique_occurrences(arr: list[int]) -> bool:
    cnt = Counter(arr)
    # unique_num = dict()
    # for i in list(cnt.values()):
    #     if i in unique_num:
    #         return False
    #     unique_num[i] = 1
    # return True
    return len(cnt) == len(set(cnt.values()))

arr = [[1,2,2,1,1,3], [1,2],[-3,0,1,-3,1,1,1,-3,10,0]] # true, false, true
for arr in arr:
    print(unique_occurrences(arr))