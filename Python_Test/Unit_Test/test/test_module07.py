#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

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
