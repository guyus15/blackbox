## @file run_test_suite.py
# @brief A test suite designed to run all existing test cases.
# @author Guy Chamberlain-Webber

import src.config as config
import unittest
from unittest import TestLoader


## Runs tests found in the 'test' directory configured in config.json
def run_tests():
    loader = TestLoader()

    start_directory = config.get_test_start_directory()
    discovery_pattern = config.get_test_discovery_pattern()

    suite = loader.discover(start_dir=start_directory, pattern=discovery_pattern, top_level_dir=None)

    unittest.TextTestRunner().run(suite)


if __name__ == "__main__":
    run_tests()
