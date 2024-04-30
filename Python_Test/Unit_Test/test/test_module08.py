#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

import unittest
import test_me


class TestClass09(unittest.TestCase):

    def test_case01(self):
        self.assertEqual(test_me.add(2, 3), 5)
        print("\n In test_case01()")

    def test_case02(self):
        self.assertEqual(test_me.mul(2, 3), 6)
        print("\n In test_case02()")
