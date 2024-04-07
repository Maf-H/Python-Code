#  Copyright (c) 03/04/2024, 18:53.
#  Mesfin Haftu
#  All rights are reserved

import unittest


class Test_Class01(unittest.TestCase):
    """
    Demonstration of unit test
    It executes by test_case methods with alphabetical order.
    without checking the order of you write them.
    """
    def test_case01(self):
        my_str = "ASHEIN"
        my_int = 999
        # assertTrue checks if the argument passed is true
        self.assertTrue(isinstance(my_str, str))
        self.assertTrue(isinstance(my_int, int))

    def test_case02(self):
        my_pi = 3.14
        # assertFalse checks if the argument passed is false
        self.assertFalse(isinstance(my_pi, int))


if __name__ == '__main__':
    # If the argument meets the assert condition, the test case passes; otherwise, it fails.
    # unittest.main() is the test runner.
    unittest.main(verbosity=2)
