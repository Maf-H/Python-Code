#  Copyright (c) 04/04/2024, 18:57.
#  Mesfin Haftu
#  All rights are reserved

import unittest
import test_me


class TestClass09(unittest.TestCase):

    def test_case01(self):
        self.assertEqual(test_me.add(2, 3), 5)
        print("\n In test_case01()")

    def test_case02(self):
        self.assertEqual(test_me.mul(2, 3), 6)
        print("\n In test_case02()")
