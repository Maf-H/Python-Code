# If you want to run a block of code after the test with a fixture has run, 
# you have to add a finalizer function to the fixture

import pytest


@pytest.fixture()
def fixture01(request):
    print("\nIn fixture01()...")
    
    def fin():
        print("\nFinalyzed.")
          
    request.addfinalizer(fin)
@pytest.mark.usefixtures("fixture01")
def test_case01(fixture01):
    print("I am the test_case01()...")