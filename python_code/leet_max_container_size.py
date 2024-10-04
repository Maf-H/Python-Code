"""
    The commented code is brute force approach but
    Time Complexity = O(n^2) 
    We need 3 senarios to increase container size
        1. maximum distance between left and right
        2. maximum height of left and right
        3. both 1 and 2
    """
def max_area_2loop(height: list[int]) -> int:
    """
    Brute force approach to find maximum area of a rectangle in a given array.
    time complexity O(N^2)
    """    
    maximum = 0

    for i, v1 in enumerate(height):
        for j, v2 in enumerate(height[i + 1:]):
            maximum = max(maximum, (min(v1, v2) * (j + 1)))
    return maximum

# height = [1,8,6,2,5,4,8,3,7]
# print(maxArea(height))

def max_area(height: list[int]) -> int:
    """
    The optimized code uses two pointers (i, j) to iterate through the array.
    It calculates the maximum area of a rectangle formed by the current pointers and updates the maximum area if necessary.
    Time Complexity = O(n)
    """
    i = 0
    j = len(height) - 1
    maximum_water = 0
    max_height = max(height)
    while i < j:
        maximum_water = max(maximum_water, min(height[i], height[j]) * (j - i))      
        if max_height * (j - i) <= maximum_water:
            break
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return maximum_water

print(max_area([1,8,6,2,5,4,8,3,7]))
