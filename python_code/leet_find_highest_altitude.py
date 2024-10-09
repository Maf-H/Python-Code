def largest_altitude(gain: list[int]) -> int:
    prefix = 0
    highest = 0
    for i in gain:
        prefix += i
        highest = max(highest, prefix)
    return highest

gain = [[-5,1,5,0,-7], [-4,-3,-2,-1,4,3,2]]
print(largest_altitude(gain[1]))       
