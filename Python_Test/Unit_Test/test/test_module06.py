#  Copyright (c) 03-06/04/2024, 16:48.
#  @author Mesfin Haftu

import unittest


class Test_Class07(unittest.TestCase):

    def test_case01(self):
        self.assertTrue("python".islower())
        print("\nIn test_case()")

# We can run a test without main using unittest module and the file without '.py'
# python3 -m unittest -v test_module06
