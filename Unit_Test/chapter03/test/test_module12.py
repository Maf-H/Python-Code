#  Copyright (c) 05/04/2024, 13:32.
#  Mesfin Haftu
#  All rights are reserved
import sys
import unittest

"""Use @unittest.skip() decorator to skip a testing a method."""


class TestClass12(unittest.TestCase):
    @unittest.skip("Demonstrating unconditional skipping")
    def test_case01(self):
        self.fail("FATAL")

    @unittest.skipUnless(sys.platform.startswith("dar"), "requires mac Os")
    def test_case02(self):
        #  MacOs specific testing code
        pass

    @unittest.skipUnless(sys.platform.startswith("linux"), "requires Linux")
    def test_case03(self):
        # Linux specific testing code
        pass
