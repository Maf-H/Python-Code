def pivot_index(nums: list[int]) -> int:
    if len(nums) < 2:
        return -1

    left = 0
    pivot = 0
    right = sum(nums[pivot + 1:])
    nums.extend([0])
    
    while pivot < len(nums) - 1:
        print((left, right), pivot,nums)
        if left == right:
            return pivot
        left += nums[pivot]
        pivot += 1
        right -= nums[pivot]
    return -1

nums = [[1,7,3,6,5,6], [1,2,3], [2,1,-1]]
for num in nums:
    print(pivot_index(num))