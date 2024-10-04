def minSteps(s: str, t: str) -> int:
    """
    Calculate the minimum number of steps to convert "word2" into anagram of "word1" 
    Args:
        s: first word
        t: second word
    returns:
        count: minimum number of steps

    time complexity O(n)
    space complexity O(n)
    """
    # adds all the unique elements of word 's' with number of frequency of each alphabet in dictionary
    frequency = {x: s.count(x) for x in set(s)}
    counter = 0
    for i in set(t):
        # adds all the unique elements of word 't' with number of frequency of each alphabet in dictionary 
        # if alphabet was there decrease it's frequency with the new alphabet frequency

        if i not in frequency:
            frequency[i] = t.count(i)
        else:
            frequency[i] -= t.count(i)
    # sum all the absolute value of the dictionary
    for key in frequency:
        counter += abs(frequency[key])
        # divide it by two because we count 2 times 
        # example: s = abb, t = aab -> {a:1, b:2}, ...{a:1, b:-1}  1 + abs(-1) = 2
        # but, if we change t's a to b that all.
    return int(counter / 2)

# s, t = "aab", "abb"
# s, t = "leetcode", "practice"abs
# s, t = "listen", "silent"
