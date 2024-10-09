def reverse_vowels(s):
    """
    :type s: str
    :rtype: str
    """
    if len(s) == 1:
        return s
    vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U',}
    s = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] in vowel and s[right] in vowel:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        elif s[left] in vowel and s[right] not in vowel:
            right -= 1
        else:
            left += 1
    return ''.join(s)
s = "leetcode"
print(reverseVowels(s))
