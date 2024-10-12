#  Date & Time 20/05/2024, 16:00.
#  @author Mesfin Haftu
"""
def min_people_in_meeting_hall(asked):
    # minimum number of people in meeting hall
    min_people = 0
    # list of unique numbers in asked list
    unique_number = list(set(asked))
    # iterate over each unique number in asked list and
    # return the minimum number of people in meeting hall including themselves
    for num in unique_number:
        # update the  min_people number which has the same T-shirt number including themselves
        min_people += (num + 1)
    # return the minimum number of people in meeting hall including themselves
    return min_people


# Example Usage
asked1 = [1, 4, 1]
print(min_people_in_meeting_hall(asked1))  # Output: 7

asked2 = [30, 30, 30]
print(min_people_in_meeting_hall(asked2))  # Output: 31

"""

def min_people_in_meeting_hall(asked):
  # minimum number of people in meeting hall
  min_people = 0
  # list of unique numbers in asked list
  unique_number = list(set(asked))
  # iterate over each unique number in asked list and
  # return the minimum number of people in meeting hall including themselves
  for num in unique_number:
    # update the  min_people number which has the same T-shirt number including themselves
    min_people += (num + 1)
  # return the minimum number of people in meeting hall including themselves
  return min_people

# Example Usage
asked1 = [1, 4, 1]
print(min_people_in_meeting_hall(asked1))  # Output: 7

asked2 = [30, 30, 30]
print(min_people_in_meeting_hall(asked2))  # Output: 31
