try:
    #  Copyright (c) 2024-06/04/2024, 16:48.
#  @author Mesfin Haftu

num = int(input("Enter Natural Number:"))
    print(" Reciprocal of ", num, "= ", 1/num)
except ValueError:
    print("Enter A number")
except ZeroDivisionError:
    print("Zero doesn't have reciprocal")