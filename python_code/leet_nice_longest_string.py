# class Solution:
#     def longestNiceSubstring(self, s: str) -> str:
#         """
#         Time Complexity O(n)
#         Space Complexity O(n)
#         Solved using divide and conquer
#         """
#         longest_nice_string = ''
#         def check_existence(start, end):
#             have_pair = True

#             for i, v in enumerate(s[start:end]):
#                 # checks if it has lower or upper case pair of letter
#                 if (v.islower() and (v.upper() in s[start:end + 1])) or (v.isupper() and (v.lower() in s[start:end + 1])):
#                     continue
#                 else:
#                     # if it doesn't have pair we need to check only it's left and right
#                     have_pair = False
#                     break
#             return have_pair

#         for start in range(len(s)):
#             for end in range(start + 1, len(s) + 1):
#                 if check_existence(start,end) and (len(longest_nice_string) < (end - start)):
#                     longest_nice_string = "".join(s[start:end])
#         return longest_nice_string

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        """
        Credit to "hynmj"
        Time Complexity O(n)
        Space Complexity O(n)
        Solved using divide and conquer
        """
        if len(s)<2:
            return ""
        have_pair=True # used to checks if character has "inverse case" pair of itself
        for i in range(len(s)):
            # checks if it has lower or upper case pair of letter
            if (s[i].islower() and (s[i].upper() in s)) or (s[i].isupper() and (s[i].lower() in s)):
                continue
            else:
                # if it doesn't have pair we need to check only it's left and right
                have_pair = False
                break
        # returns the string if it contains upper and lower case of character of the each element
        if have_pair:
            return s
        else:
            # check recursively every composition longest, and nice substring
            # when the for loop breaks the index 'i' value comes here to divide and conques the left and right sub-string
            left=self.longestNiceSubstring(s[:i]) # checks the sub-string left to the unique character
            right=self.longestNiceSubstring(s[i+1:]) # checks the sub-string, right to the unique characte
            

            #  If there are multiple, equal length: them  return the substring of the earliest occurrence.
            if len(left) >= len(right):
                return left
            else:
                return right 


# Test cases
def test_longestNiceSubstring():
    sol = Solution()

    # Test case 1: Example with nice substrings
    assert sol.longestNiceSubstring("YazaAay") == "aAa", "Test Case 1 Failed"
    
    # Test case 2: Entire string is nice
    assert sol.longestNiceSubstring("Bb") == "Bb", "Test Case 2 Failed"
    
    # Test case 3: No nice substring
    assert sol.longestNiceSubstring("abc") == "", "Test Case 3 Failed"
    
    # Test case 4: All characters are nice
    assert sol.longestNiceSubstring("aAaA") == "aAaA", "Test Case 4 Failed"
    
    # Test case 5: Complex case with multiple nice substrings
    assert sol.longestNiceSubstring("cChHJj") == "cChHJj", "Test Case 5 Failed"
    
    # Test case 6: Large string with all pairs
    assert sol.longestNiceSubstring("aAbBcCdDeEfFgGhH") == "aAbBcCdDeEfFgGhH", "Test Case 6 Failed"
    
    # Test case 7: Empty string input
    assert sol.longestNiceSubstring("") == "", "Test Case 7 Failed"
    
    # Test case 8: Single character (not nice)
    assert sol.longestNiceSubstring("A") == "", "Test Case 8 Failed"
    
    # Test case 9: String with only one nice pair
    assert sol.longestNiceSubstring("cB") == "", "Test Case 9 Failed"

    print("All test cases passed!")

# Run the tests
test_longestNiceSubstring()