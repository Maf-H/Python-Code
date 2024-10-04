def pivotArray(nums, pivot: int):
        pivoted = []
        current = 0
        for i in range(len(nums)):
            if nums[i] < pivot:
                pivoted.insert(current, nums[i])
                current += 1
            elif nums[i] == pivot:
                pivoted.insert(current, nums[i])
            else:
                pivoted.append(nums[i])
            print(pivoted)

        return pivoted
nums = [-3,2,4,3]# [9,12,5,10,14,3,10]
print(pivotArray(nums, 10))
