#  Date & Time 27/04/2024, 16:26.
#  @author Mesfin Haftu
def recursive_sum(nums):
    if type(nums) == list:
        if len(nums) == 1:
            return nums[0]
        return nums[0] + recursive_sum(nums[1:])
    else:
        if nums == 1:
            return nums
        return nums + recursive_sum(nums - 1)  # you can check your answers by: (n^2 + n)/2


nums = [x for x in range(3, 16, 3)]
# nums = 4
print(nums)
print(recursive_sum(nums))
