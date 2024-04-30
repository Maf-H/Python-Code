#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu
import pytest

from calculator import Calculator


class TestClass01:
    def test_case01(self):
        calc = Calculator()
        result = calc.add(2, 2)
        assert 4 == result

    def test_case02(self):
        with pytest.raises(ValueError):
            result = Calculator().add(2, 'two')

    def test_case03(self):
        with pytest.raises(ValueError):
            result = Calculator().add('two', 2)

    def test_case04(self):
        with pytest.raises(ValueError):
            result = Calculator().add('two', 'two')

# Test-Driven Development with pytest
# ===================================
# Test-driven development (TDD) is a paradigm whereby you implement the new
# feature or requirement by writing the tests first, watch them fail, and then write the code to make the failed
# tests pass. Once the basic skeleton of the features is implemented this way, you then build on this by altering the
# tests and then changing the development code to accommodate the added functionality. You repeat this process as
# many times as needed to accommodate all new requirements.
