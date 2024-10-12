#  Date & Time 27/04/2024, 17:10.
#  @author Mesfin Haftu
from itertools import permutations

def get_anagrams(word):
    # Get all permutations of the characters in the word
    perm = permutations(word)
    
    # Create a set to store unique anagrams
    anagrams = set()
    
    # Iterate through the permutations and join the characters to form words
    for p in perm:
        anagram = ''.join(p)
        anagrams.add(anagram)
    
    return anagrams

# Example usage
word = "abc"
result = get_anagrams(word)
for anagram in result:
    print(anagram)
