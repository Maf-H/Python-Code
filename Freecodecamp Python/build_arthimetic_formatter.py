def arithmetic_arranger(problems, show_answers=False):
    """_summary_

    Args:
        problems (_type_): _description_
        show_answers (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """
    top = []
    bottom = []
    dashes = []
    answer = []
    justifier = 0
    

    for problem in problems:
        num1, op, num2 = problem.split()
        if op not in "+-":
            return "Error: Operator must be '+' or '-'."
        if not num1.isdigit() or not num2.isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        justifier = (max(len(num1), len(num2)) + 2)
        top.append(num1.rjust(justifier))
        bottom.append(op + num2.rjust(justifier - 1))
        dashes.append('-'*justifier)

        if show_answers:
            if op =='+':
                tempo = str(int(num1) + int(num2))
                answer.append(str(tempo).rjust(justifier))
            else:
                tempo = str(int(num1) - int(num2))
                answer.append(tempo.rjust(justifier))
    final_value = '    '.join(top) + '\n' + '    '.join(bottom) + '\n' + '    '.join(dashes)
    if show_answers:
        return final_value + '\n' + '    '.join(answer)
    else:
        return final_value
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))

p = [["3801 - 2", "123 + 49"],
["1 + 2", "1 - 9380"],
["3 + 855", "3801 - 2", "45 + 43", "123 + 49"],
["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"],
["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"],
["3 / 855", "3801 - 2", "45 + 43", "123 + 49"],
["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"],
["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"],
["3 + 855", "988 + 40"],
["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"]
]
for i in p:
    print(f'{arithmetic_arranger(i)}')
