## @file run_test_suite.py
# @brief A test suite designed to run all existing test cases.
# @author Guy Chamberlain-Webber

import unittest
from unittest import TestLoader


## A concrete implementation of unittest.TestResult used to visualise test
# results more clearly.
class TestLog(unittest.TestResult):
    def __init__(self):
        super().__init__()

    def startTestRun(self) -> None:
        print("Running discovered tests...\n")

    def startTest(self, test: unittest.TestCase) -> None:
        print(f"\nTest: {test}")

    def addSuccess(self, test: unittest.TestCase) -> None:
        print("Result: PASSED")

    def addError(self, test: unittest.TestCase, err: tuple) -> None:
        error_type = err[0]
        error_value = err[1]

        print(f"ERROR: {error_type}\n{error_value}\n")

    def addFailure(self, test: unittest.TestCase, err: tuple) -> None:
        failure_type = err[0]
        failure_value = err[1]

        print(f"FAILURE: {failure_type}\n{failure_value}")


## Discovers existing tests and runs them, storing the result as a TestLog.
def run_tests():
    loader = TestLoader()
    result = TestLog()

    suite = loader.discover(start_dir="tests", pattern="*_test.py", top_level_dir=None)

    suite.run(result)


if __name__ == "__main__":
    run_tests()
