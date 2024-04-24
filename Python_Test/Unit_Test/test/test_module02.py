#  Copyright (c) 03-06/04/2024, 16:48.
#  @author Mesfin Haftu
import unittest
import inspect


class TestClass02(unittest.TestCase):

        def test_case02(self):
            print("\nRunning Test Method : " + inspect.stack()[0][3])

        def test_case01(self):
            # inspect.stack()[0][3] prints the name of the current test method
            print("\nRunning Test Method : " + inspect.stack()[0][3])


if __name__ == '__main__':
    unittest.main(verbosity=2)
