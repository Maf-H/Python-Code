def two_sum(nums: list[int], target: int) -> list[int]:
    """
    first method
    Time Complexity O(n^2)
    Space Complexity O(1)

    second method
    Time Complexity O(n)
    Space Complexity O(n)
    """
    # for i, v1 in enumerate(nums):
    #     for j, v2 in enumerate(nums):
    #         if v1 + v2 == target:
    #             return [i, j]
    # return []

    nums_dict = {}
    for i, v in enumerate(nums):
        if target - v in nums_dict:
            return [nums_dict[target - v], i]
        nums_dict[v] = i
    return []

if __name__ == '__main__':
    a = [2,7,11,15]
    print(two_sum(a, 9))
