## @file run_test_suite.py
# @brief A test suite designed to run all existing test cases.
# @author Guy Chamberlain-Webber

import unittest
from unittest import TestLoader


## Runs tests found in the 'test' directory configured in config.json
def run_tests():
    loader = TestLoader()
    suite = loader.discover(start_dir="tests/", pattern="*_test.py", top_level_dir=None)

    unittest.TextTestRunner().run(suite)


if __name__ == "__main__":
    run_tests()
