#  Copyright (c) 05/04/2024, 13:23.
#  Mesfin Haftu
#  All rights are reserved
import unittest
"""To fail a test use fail() method."""


class TestClass12(unittest.TestCase):
    def test_case(self):
        """This is test method."""
        print(self.id())
        self.fail()
