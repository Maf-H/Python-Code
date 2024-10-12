#  Date & Time 20/05/2024, 12:53.
#  @author Mesfin Haftu

def calPoints(ops) -> int:

    """
    Constraints:
    • 1 <= ops.length <= 1000
    • ops (i] is "C", "D, "+", or a string representing an integer in the range 1-3 * 104, 3 * 104] .
        C = clear the last element
        D = double the last element
        + = add the last two elements
    • For operation "+", there will always be at least two previous scores on the record.
    • For operations "C" and "D", there will always be at least one previous score on the record.
    :type ops: List[str] - List of operations
    :rtype: int-Sum of scores after performing all operations
    """
    temp = []
    operators = ["C", "D", "+"]
    numbers = [str(num) for num in range(-312, 312)]

    for value in ops:
        if value in numbers:
            temp.append(int(value))
        elif value in operators:
            if value == "+":
                if len(temp) >= 2:
                    temp.append(temp[-1] + temp[-2])
                else:
                    return
            elif value == "C":
                if len(temp) >=1:
                    del temp [-1]
                else:
                    return
            elif value == "D":
                if len(temp) >= 1:
                    temp.append(temp[-1] * 2)
                else:
                    return
            else:
                return
        else:
            print("Unknown input")
            break

    result = sum(temp)
    return result


if __name__ == '__main__':
    line = input()
    if len(line) <= 1000:
        # line = "5 4 C D +"
        ops = line.strip().split()
        print(calPoints(ops))
    else:
        print("Ops length is greater than 1000")
