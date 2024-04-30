#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

# test fixtures are the set of steps performed before and after the tests.

import unittest


def setUpModule():
    """called once before anything else in this module."""
    print("In setUpModule()...")


def tearDownModule():
    """called once after anything else in this module."""
    print("In tearDownModule()...")


class test_module06(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """called once before any test."""
        print("In setUpClass()...")

    @classmethod
    def tearDownClass(cls):
        """called once after all tests, if set_up_class successful."""
        print("In tearDownClass()...")

    def setUp(self):
        """called multiple times, before every test method"""
        print("\nIn setUp()...")

    def tearDown(self):
        """called multiple times, after every test method"""
        print("In tearDown()...")

    def test_case01(self):
        self.assertTrue("PYTHON".isupper())
        print("In test_case01()")

    def test_case02(self):
        self.assertFalse("python".isupper())
        print("In test_case02()")


if __name__ == '__main__':
    unittest.main(verbosity=2)
