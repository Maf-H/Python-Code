"""
function used to compres string and return the length of the string
"""
def compress_2loops(chars: list[str]) -> int:
    """
    Compress the given list of characters by replacing the character and
    how many times its repetition if it is occured more than 1.
    then, return the number of compressed characters.
        Time Complexity O(n^2)
        Space Complexity O(1)
    """
    if not chars or len(chars) == 1:
        return len(chars)
    i = 0
    j = 0
    length = len(chars)

    while i < length:
        count = 1
        # counts the number repeated characters
        while i < length - 1 and chars[i] == chars[i + 1]:
            count += 1
            i += 1
        # appends the character to chars
        chars[j] = chars[i]
        j += 1
        if count > 1:
            # adds a counter to the chars
            for c in str(count):
                chars[j] = c
                j += 1
        i += 1
    print(chars[:j])
    return j

def compress_1loop(chars: list[str]) -> int:
    """
    Time Complexity O(n^2) --Worst case if all elements are the same
    Space Complexity O(1)
    """
    if not chars or len(chars) == 1:
        return len(chars)

    length = len(chars)
    j = 0
    count = 1

    for i in range(1, length + 1):
        if i < length and chars[i] == chars[i - 1]:
            count += 1
        else:
            # adds a character to chars to index of j
            chars[j] = chars[i - 1]
            j += 1
            # if count > (1 digit) it adds each digit as a string to chars[j] else add the digit as string
            if count > 1:
                for c in str(count):
                    chars[j] = c
                    j += 1
            count = 1
    print(chars[:j])
    return j

chs = [
    [],
    ['a'],
    ['a', 'a'],
    ['a', 'b', 'c'],
    ['a', 'b', 'b', 'c', 'c', 'c'],
    ['a', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c']
]
print(chs[4])
print(compress_2loops(chs[4]))
print(chs[5])
print(compress_1loop(chs[5]))
# print(compress(['a', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c']))
