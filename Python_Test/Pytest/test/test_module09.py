#  Copyright (c) 12/04/2024, 14:16.
#  @author Mesfin Haftu
#  Scope of pytest fixtures

import pytest


def test_case01():
    with pytest.raises(Exception):  # Fails if the code x doesn't raise exception.
        x = 1 / 0


def test_case02():
    with pytest.raises(Exception):
        x = 1 / 1


#  we can run it in terminal:
#  python3 -m pytest -vs test_module09.py
#  Stopping After the First (or N) Failures
#  =========================================
#  py.test -x   stop execution after 1 failure
#  py.test --maxfail=3   stop execution after N = 3 failures
#  Profiling Test Execution Duration shows the N = 10 slowest test
#  =================================
#  py.test --durations=10
#  JUnit-Style Logs can be generated:
#  =================================
#  py.test --junitxml=result.xml
#  Plain Results can be generated:
#  ===============================
#  py.test --resultlog=result.log
#  Sending a Test Report to Online pastebin Service
#  ================================================
#  py.test -v --pastebin=all



