#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu
def setup_module(module):
    print("\nIn setup_module()...")


def teardown_module(module):
    print("\nIn teardown_module()...")


def setup_function(function):
    print("\nIn setup_function()...")


def teardown_function(function):
    print("\nIn teardown_function()...")


def test_case01():
    print("\nIn test_case01()")


def test_case02():
    print("\nIn test_case02()")


class TestClass02:

    @classmethod
    def setup_class(cls):
        print("\nIn setup_class()...")

    @classmethod
    def teardown_class(cls):
        print("\nIn teardown_class()...")

    def setup_method(self):
        print("\nIn setup_method()...")

    def teardown_method(self):
        print("\nIn teardown_method()...")

    def test_case01(self):
        print("\nIn test_case01()...")

    def test_case02(self):
        print("\nIn test_case02()...")

    def test_case03(self):
        print("\nIn test_case03()...")

    def test_case04(self):
        print("\nIn test_case04()...")


