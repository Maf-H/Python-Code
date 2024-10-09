"""
a function counts how many ways can k be generated from input number  
"""
from collections import Counter
def max_operations_nlogn(nums: list[int], k: int) -> int:
    """
    Time complexity O(nlogn)
    Space complexity O(1)
    """
    if len(nums) < 2:
        return 0
    count = 0
    left = 0
    right = len(nums) - 1
    nums.sort()
    
    while left < right:
        curr = k - nums[left]
        temp = nums[left] + nums[right]
        if temp == k:
            count += 1
            left += 1
            right -= 1
        elif temp < k:
            left += 1
        else:
            right -= 1 
    return count

def max_operations_n(nums, k):
    """
    Time complexity O(n)
    Space complexity O(n)
    """
    operations = 0
    pairs = Counter(nums)
    if (k % 2 == 0) and ((k // 2) in pairs):
        print('half', k % 2 == 0, (k // 2) in pairs)
        operations += (pairs[k // 2] // 2)
        del pairs[k // 2]
    print(pairs, operations)
    print("key k-key ops")
    for key in pairs:
        temp = k - key
        if temp in pairs:
            operations += min(pairs[key], pairs[temp])
            pairs[temp] = 0
        print(key, temp, operations)
    return operations

num = [[1,2,3,4], [1,2,2,3,4,5], [3,1,3,4,3], [2,2,2,3,1,1,4,1], [3,5,1,5]]
print(max_operations_n(num[3], 4))
