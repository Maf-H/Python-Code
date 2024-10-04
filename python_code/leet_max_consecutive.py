consecutive = {}
def findLHS(nums: list[int]) -> int:
    for i in set(nums):
        consecutive[i] = nums.count(i)
    max_con = 0    
    for i in consecutive:
        if i + 1 in consecutive:
            max_con = max(max_con, consecutive[i] + consecutive[i + 1])
    return max_con
         
        
        
    #     max_con = 0
    #     if (i + 1) in nums:
    #         max_con = nums.count(i) + nums.count(i + 1)
    #     if max_con > len(nums)//2:
    #         return max_con
    #     else:
    #         consecutive.append(max)
    # return max(consecutive) 

nums = [1,3,2,2,5,2,3,7]
# nums = [1,1,1,1]
nums = [1,2,3,4]
print(findLHS(nums))