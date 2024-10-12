#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

try:
    num = int(input("Enter Natural Number:"))
    print(" Reciprocal of ", num, "= ", 1/num)
except ValueError:
    print("Enter A number")
except ZeroDivisionError:
    print("Zero doesn't have reciprocal")