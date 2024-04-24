# pytest fixtures
import pytest


@pytest.fixture()
def fixture01():
    print("\n In fixture01()...")


def test_case01(fixture01):
    print("\n In test_case01()...")