""" 
You have a long flowerbed in which some of the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, 
where 0 means empty and 1 means not empty, 
and an integer n, return true if n new flowers can be planted in the flowerbed 
without violating the no-adjacent-flowers rule and false otherwise."""

def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    """ 
    time complexity O(n)
    """
    length = len(flowerbed)
    for i in range(length):
        # if i is the 1st element or the last element
        # no further checking is_left = is_right = True
        is_left_empty = ((i == 0) or (i < length and flowerbed[i - 1] == 0))
        is_right_empty = ((i == length - 1) or (flowerbed[i + 1] == 0))

        print(f"{i}: {flowerbed} n:{n}")
        print(is_left_empty and is_right_empty)
        if is_left_empty and not flowerbed[i] and is_right_empty:
            flowerbed[i] = 1
            n -= 1
            print(f"Inner->{i}: {flowerbed} n:{n}")
            if n == 0:
                return True
    return False
f_bed = [[1,0,0,0,1], [1,0,0,0,0]]
print(can_place_flowers(f_bed[1], 2))