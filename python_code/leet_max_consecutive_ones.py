def longest_ones(nums: list[int], k: int) -> int:
    """
    Given a binary array nums and an integer k, return the maximum number of consecutive 1's 
    in the array if you can flip at most k 0's.
    
    # Time: 0(n)
    # Space: O(1)
    Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
    Output: 6
    Explanation: [1,1,1,0,0,1,1,1,1,1,1]
    """
    left = 0
    window_size = 0
    zeros = 0
    result = 0
    # print(f'left:{left} window_size:{window_size} result:{result}')

    for right in range(len(nums)):
        zeros += 1 if nums[right] == 0 else 0
        # print(f'1. left  {left}:{[nums[left-1]]} right {right}:{[nums[right]]} window_size:{window_size} zeros:{zeros}--> {nums[left:right + 1]}')
        while zeros > k:
            zeros -= 1 if nums[left] == 0 else 0
            left += 1
        # [1,1,1,0,0,0,1,1,1,1,0]
            #          ∆         ∆
        # print(f'3. left  {left}:{[nums[left-1]]} right {right}:{[nums[right]]} window_size:{window_size} zeros:{zeros}--> {nums[left:right + 1]}')
        window_size = right - left + 1
        result = max(result, window_size)
    print(nums[left:right+1])
    return result
inp = [[1,1,1,0,0,0,1,1,1,1,0], 2, [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3]
print(longest_ones(inp[2], 3))


def longestOnes(nums: list[int], k: int) -> int:
    """
    Given a binary array nums and an integer k, return the maximum number of consecutive 1's 
    in the array if you can flip at most k 0's.
    
    # Time: 0(n)
    # Space: O(1)
    """
    # Initialize max_w (max window size) and num_zeros (number of zeros in the current window)
    # Initialize left and right pointers
    # Iterate through the array from left to right
    # If the current element is 0, increment num_zeros
    # If num_zeros exceeds k, move the left pointer to the right until num_zeros becomes less than or equal to k
    # Calculate the window size (right - left + 1) and update max_w if necessary
    # Return max_w as the result
    left = 0 
    for right in range(len(nums)):
        if nums[right] == 0:
            k -= 1
        if k < 0:
            if nums[left] == 0:
                k += 1
            left += 1

    return right - left + 1

inp = [[1,1,1,0,0,0,1,1,1,1,0], 2, [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3]
print(longestOnes(inp[2], 3))
