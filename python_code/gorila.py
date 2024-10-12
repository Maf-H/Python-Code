def sumRange(nums: list, left: int, right: int):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    print(nums)
    if left != 0:
        return nums[right] - nums[left - 1]
    else:
        return nums[right]

# a = [-2,0,3,-5,2,-1]
# print(sumRange(a, 2, 5))

def threeSum(nums: list[int]) ->list[list[int]]:
    length = len(nums)
    i = 0
    j = i + 1
    k = length - 1
    nums = sorted(nums)
    answer = []
    while i != j and i != k and j != k:
        current_sum = nums[i] + nums[j] + nums[k]
        if current_sum == 0:
            output = [nums[i] , nums[j] , nums[k]]
            if output not in answer:
                answer.insert(0, output)
                print("-----True:",i,j,k, answer)
            j += 1
        elif current_sum > 0:
            if k-1 == j and j-i > k-j:
                j -= 1
            k -= 1

        else:
            if i+1 == j and j-i < k-j:
                j += 1
            i += 1
        print(i,j,k, nums[i:k+1])
    print(i, j, k)
    return answer
# a = [1,-1,-1,0]
# a = [3,0,-2,-1,1,2]
# a = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
# print(a)
# print("Sorted nums: ", sorted(a))
# print(threeSum(a))
    

def findMaxAverage(nums: list[int], k: int) -> float:
    maximum = 0
    length = len(nums)
    i = 0
    if length > k:
        j = k - 1
        running_average = sum(nums[i:j+1])
    else:
        j = k
        running_average = sum(nums[i:j])
    maximum = max(maximum, running_average)
    print(running_average)

    while j < length:
        maximum = max(maximum, running_average)
        if j + 1 < length:
            running_average += ((nums[j + 1] - nums[i]))
        print(maximum, running_average)
        i += 1
        j += 1
    return maximum/k

# print(findMaxAverage([5], 1))
def three_sum(nums: list[int]):
    right = len(nums) - 1
    nums.sort()
    answer = []

    for i, v in enumerate(nums):
        if i > 0 and v == nums[i - 1]:
            continue
        iner_target = 0 - v
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if nums[left] == nums[left - 1] and nums[right] == nums[right + 1]:
                continue
            if sum == iner_target:
                answer.append([v, nums[left], nums[right]])
                print(answer)
                left += 1
                right -= 1
            elif sum < iner_target:
                left += 1
            else:
                right -= 1
    return answer

# a = [-4, -3, -2, -1, -1, 0, 0, 1, 2, 3, 4]
# print(three_sum([-2,0,0,2,2]))
for i in range(4):
    if i == 2:
        print("Continue...")
        continue
    print(i)
