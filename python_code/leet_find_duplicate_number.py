class Solution:
    def find_duplicate(self, nums: list[int]) -> int:
        # Let's use 
        # ->Floyds cycle detection and 
        # ->cycle begining algorithm
        slow = 0
        fast = 0
        # checks the existing of cycle and takes its value/node/index
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        # find the duplicate by following the cycle
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast: 
                return slow
nums = [[1,3,4,2,2], [3,1,3,4,2], [3,3,3,3,3]]
for num in nums:
    print(Solution().find_duplicate(num))