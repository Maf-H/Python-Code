def reverse_words(s):
    """
    :type s: str
    :rtype: str
    """
    s = s.strip(' ').split()
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ' '.join(s)
s = ["the sky      is blue", "  hello world  "]
print(reverse_words(s[0]))
