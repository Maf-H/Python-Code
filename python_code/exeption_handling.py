try:
    #  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

num = int(input("Enter Natural Number:"))
    print(" Reciprocal of ", num, "= ", 1/num)
except ValueError:
    print("Enter A number")
except ZeroDivisionError:
    print("Zero doesn't have reciprocal")