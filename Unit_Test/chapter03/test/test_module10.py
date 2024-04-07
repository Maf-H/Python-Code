#  Copyright (c) 05/04/2024, 13:11.
#  Mesfin Haftu
#  All rights are reserved

import unittest


class TestClass11(unittest.TestCase):
    def test_case01(self):
        """This is test method."""
        print("\nIn test_case01()")
        print(self.id())
        print(self.shortDescription())


