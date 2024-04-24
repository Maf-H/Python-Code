#  Copyright (c) 05-06/04/2024, 16:48.
#  @author Mesfin Haftu

import unittest
# When an exception is raised in a test case, the test case fails.
# The code shown below will raise an exception explicitly.


class TestClass14(unittest.TestCase):
    def test_case01(self):
        raise Exception
