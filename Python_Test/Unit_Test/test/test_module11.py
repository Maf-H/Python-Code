#  Copyright (c) 05-06/04/2024, 16:48.
#  @author Mesfin Haftu
import unittest
"""To fail a test use fail() method."""


class TestClass12(unittest.TestCase):
    def test_case(self):
        """This is test method."""
        print(self.id())
        self.fail()
