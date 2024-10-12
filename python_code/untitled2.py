
mark = input("Enter the student's mark: ")
# Check if the mark is greater than or equal to 50
if not isinstance(mark, float):
    try:
        mark = float(mark)
    except ValueError:
        print("You entered a non-numeric value.")
    else:
        if mark >= 50:
            print("Pass")
        else:
            print("Fail")


