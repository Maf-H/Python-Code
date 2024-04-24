#  Copyright (c) 05-06/04/2024, 16:48.
#  @author Mesfin Haftu
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

    @unittest.skipIf(sys.platform is not "windows", "The system is not Windows")
    def test_case04(self):
        # windows specific testing code
        pass
#

