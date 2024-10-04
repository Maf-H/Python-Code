"""
There are n kids with candies. You are given an integer array candies, 
where each candies[i] represents the number of candies the ith kid has, 
and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, 
after giving the ith kid all the extraCandies, they will have the greatest number of candies
 among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies."""
def kids_with_candies(candies: list[int], extra_candies: int) -> list[bool]:
    """ 
    time Complexity O(N)
    """
    maximum = max(candies)
    length = len(candies)
    result = [False] * length

    for i in range(length):
        if candies[i] + extra_candies >= maximum:
            result[i] = True

    return result

print(kids_with_candies([2, 3, 5, 1, 3], 3))  # [true, true, true, false, true]
