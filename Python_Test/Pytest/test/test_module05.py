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
    print("\n In fixture01()...")
          
@pytest.mark.usefixtures("fixture01")
def test_case01(fixture01):
    print("\n In test_case01()...")
    

# @pytest.fixture() 
# @pytest.mark.usefixtures("fixture01")  
# Both the above decorators have  the same functionality. 
# to run in terminal from Python_Test directory:
# py.test -vs Pytest/test/test_module05.py
# output=
        #  Pytest/test/test_module05.py::test_case01
        #  In fixture01()...

        #  In test_case01()...
        # PASSED

        # =============================== 1 passed in 0.01s ================================
