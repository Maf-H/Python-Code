def bad_fun(n):
    """
    This code demonstrates exception inside a function
    """
    try:
        return 1/n
    except ZeroDivisionError as err:
        print(err, "from inside.")
        raise  # 'raise; can be with or with ot parameter
        raise (NameError, TypeError)

    """
    This code demonstrates exception outside a function
    """


try:
    bad_fun(0)
except ArithmeticError :
    print("Arithmetic Error from Outside")
except NameError as #  Copyright (c) 2024. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

err:
    print(err)
except TypeError as err:
    print(err)





