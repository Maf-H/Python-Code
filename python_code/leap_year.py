'''The function below determines if a year is leap or not.'''
def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False

#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")