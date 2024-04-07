#  Copyright (c) 04/04/2024, 01:36.
#  Mesfin Haftu
#  All rights are reserved

import unittest


class TestClass08(unittest.TestCase):
    def test_case01(self):
        self.assertTrue("PYTHON".isupper())
        print("\nIn test_case1()")

    def test_case02(self):
        self.assertTrue("Python".isupper())
        print("\nIn test_case2()")

    def test_case03(self):
        self.assertTrue(True)
        print("\nIn test_case3()")

# python3 -m unittest -f test_module07
# -f stands for failsafe:to stop on first fail
# -q stands for quiet when error happened.
