def increasing_triplet(nums):
    """
    checks 
        if current element is less than first,
            then: update value of first
        else current element is less than second:
            then: update value of irst
        else:
            we found the third element,
            return true.
        if it is not fullfill the above conditions,
            return false
    :type nums: List[int]
    :rtype: bool
    """
    length = len(nums)
    if length < 3:
        return False

    first = second = float('inf')
    for i in range(length):
        if nums[i] <= first:
            first = nums[i]
        elif nums[i] <= second:
            second = nums[i]
        else:
            return True
    return False

nums = [[1,2], [1,1,1,1,1,1,1,1,1,1,1,1,1,1], [1,2,3,4,5], [5,4,3,2,1], [2,1,5,0,4,6], [20,100,10,12,5,13]]
print(increasing_triplet(nums[5]))
