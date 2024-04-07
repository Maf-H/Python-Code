#  Copyright (c) 05-06/04/2024, 16:48.
#  @author Mesfin Haftu

import unittest


class TestClass11(unittest.TestCase):
    def test_case01(self):
        """This is test method."""
        print("\nIn test_case01()")
        print(self.id())
        print(self.shortDescription())


