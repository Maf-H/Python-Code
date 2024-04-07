#  Copyright (c) 05/04/2024, 13:57.
#  Mesfin Haftu
#  All rights are reserved

import unittest
# When an exception is raised in a test case, the test case fails.
# The code shown below will raise an exception explicitly.


class TestClass14(unittest.TestCase):
    def test_case01(self):
        raise Exception
