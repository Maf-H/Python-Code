#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

import pytest

@pytest.fixture()
def fixture01():
    print("\nIn fixture01()...")
    
    
@pytest.mark.usefixtures('fixture01')
class TestClass03:
    def test_case01(self):
        print("I am test_case01()...")
        
    def test_case02(self):
        print("I am test_case02()...")