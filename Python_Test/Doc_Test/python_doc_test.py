#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

import doctest

"""
python_doc_testing
sample doc testing.
"""


def mul(a, b):
    """

    """
    return a * b


def add(a, b):
    """

    """
    return a + b


if __name__ == "__main__":
    doctest.testmod()


# to  run the file in terminal
# python3 -m doctest -v python_doc_test.py
# python3 -m doctest -v test_data.txt
# -m stands for you get module after -m doctest
# -v stands for verbose used to console output of the test
