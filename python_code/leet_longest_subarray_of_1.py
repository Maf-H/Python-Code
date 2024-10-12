""" 
Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's 
in the resulting array. Return 0 if there is no such subarray.
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] 
longest subarray with value of 1's is [1,1,1,1,1].
variable sliding window
"""
def longest_subarray(nums: list[int]) -> int:
    length = len(nums)
    result = 0
    left = 0
    zero = 1
    if length < 2:
        return 0

    for right in range(length):
        #  if current array value is 0 we pretend like we use the last weapon
        zero -= 1 if nums[right] == 0 else 0
        #  move the left pointer to the right until we have found 1
        while zero < 0:
            zero += 1 if nums[left] == 0 else 0
            left += 1

        result = max(result, right - left + 1)
    return result - 1
nums = [[1,1,0,1], [0,1,1,1,0,1,1,0,1], [1,1,1], [1]]
for num in nums:
    print(longest_subarray(num))