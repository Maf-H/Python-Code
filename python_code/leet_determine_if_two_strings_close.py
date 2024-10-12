from collections import Counter
def close_strings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
            return False

    w1 = Counter(word1)         # "abbzccca"-{a:2,b:2,c:2,z:1}
    w2 = Counter(word2)         # "babzzczc"-{a:2,b:2,c:2,z:1}
    unique_char = list(w1.keys())
    # checks if the element in word1 exists in word2 and vice-versal
    for char in unique_char:
        if (char in w1 and char not in w2) or (char in w2 and char not in w1):
            return False

    v1 = list(w1.values()) # [2,2,2,1]
    v2 = list(w2.values()) # [1,2,1,3]
    v1.sort() # [1,2,2,2]
    v2.sort() # [1,1,2,3]
    if v1 != v2:
        return False
    return True

words = ["abbzzca", "babzzcz"]
print(close_strings(words[0], words[1]))
