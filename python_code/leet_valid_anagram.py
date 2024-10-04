"""Given two strings s and t, return true if t is an 
anagram of s, and false otherwise.
"""
from collections import defaultdict
def is_anagram(s: str, t: str) -> bool:
    """
    1st. method
        sorting has nlogn time complexity
        Time Complexity O(nlog(n))
        Space Complexity O(1) 

    2nd. method
        Time Complexity O(n)
        Space Complexity O(n) 
    """
    # return sorted(s) == sorted(t)

    if len(s) != len(t):
        return False
    counter = defaultdict(int)
    for i, j in zip(s, t):
        counter[i] += 1
        counter[j] -= 1
    for v in counter.values():
        if v != 0:
            return False
    return True


a, b = "anagram", "gramana"
print(is_anagram(a, b))
