#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

import pytest

# pytest provides access to the fixture information on the requested object.


@pytest.fixture()
def fixture01(request):
    print("\nIn fixture01()...")
    print("Fixture Scope: " + str(request.scope))
    print("Function Name:" + str(request.function.__name__))
    print("Class Name: " + str(request.cls))
    print("Module Name: " + str(request.module.__name__))
    print("File Path: " + str(request.fspath))
    

@pytest.mark.usefixtures('fixture01')
def test_case01(request):
    print("\nI'm the test_case01()...")

    def fin():
        print("\nFinalized.")
    request.addfinalizer(fin)
