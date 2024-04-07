#  Copyright (c) 03-06/04/2024, 16:48.
#  @author Mesfin Haftu

import unittest
import inspect


def add(a, b):
    print("We're in custom made function : " + inspect.stack()[0][3])
    return a + b


class Test_Class03(unittest.TestCase):

    def test_case01(self):
        print("\nRunning Test Method : " + inspect.stack()[0][3])
        self.assertEqual(add(2, 3), 5)

    def test_case02(self):
        print("\nRunning Test Method : " + inspect.stack()[0][3])
        my_var = 3.14
        self.assertTrue(isinstance(my_var, float))

    def test_case03(self):
        print("\nRunning Test Method : " + inspect.stack()[0][3])
        self.assertEqual(add(2, 2), 5)

    def test_case04(self):
        print("\nRunning Test Method : " + inspect.stack()[0][3])
        my_var = 3.14
        self.assertTrue(isinstance(my_var, int))


if __name__ == '__main__':
    unittest.main(verbosity=2)
