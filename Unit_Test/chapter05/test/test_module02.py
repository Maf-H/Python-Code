#  Copyright (c) 06/04/2024, 22:26.
#  @author Mesfin Haftu


class TestClass01:
    def test_case01(self):
        assert "Python".upper() == 'PYTHON'

    def test_case02(self):
        assert "Python".lower() == 'python'

# we can run specific class or specific method using the following command
# py.test -v test_module02.py::TestClass01
# py.test -v test_module02.py::TestClass01::test_case01
# Run the following command in the project directory to initiate automated test discovery:
# py.test -v
