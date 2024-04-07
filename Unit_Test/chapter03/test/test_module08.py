#  Copyright (c) 04-06/04/2024, 16:48.
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
