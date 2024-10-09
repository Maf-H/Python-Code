def max_vowels(s: str, k: int) -> int:
    """
    Time Complexity O(n)
    space Complexity O(len(vowels))
    """
    vowels = set('aeiou')
    temp_counter = 0
    final_result = 0
    for c in s[:k]:
        if c in vowels:
            temp_counter += 1
    final_result = max(final_result, temp_counter)
    for char in range(k, len(s)):
        if final_result >= k:
            return k
        if s[char - k] in vowels and s[char] not in vowels:
            temp_counter -= 1
        elif s[char - k] not in vowels and s[char] in vowels:
            temp_counter += 1
        final_result = max(final_result, temp_counter)
    return final_result
inp = ["abciiidef", "tryhard", "leetcode"]
print(max_vowels(inp[0], 3))
# l e e t c o d e
#   ∆     ∆

# class Solution:
# def maxVowels(self, s: str, k: int) -› int:
# vowel = l'a', 'e', 'i', 'o', 'u'}
# 1, cnt, res = 0, 0, 0
# for r in range(len(s)):
# cnt += 1 if s[r] in vowel else 0
# if r - 1 + 1 > k:
# cnt -= 1 if s[1] in vowel else 0
# 1 += 1
# res = max(res, cnt)
# return res

