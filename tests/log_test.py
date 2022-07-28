## @file log_test.py
# @brief Contains tests to test the 'log' module.
# @author Guy Chamberlain-Webber

import unittest
import os
import src.config as config
import src.log as log


## This test case test the 'log' module.
class TestLog(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Remove any test log directories if they exist.
        log_dir = config.get_log_dir()

        if os.path.exists(log_dir):
            os.rmdir(log_dir)

    # Test 1
    def test_create_log_dir_no_exist(self):
        # This test ensures that the create_log_dir() function correctly creates a
        # log directory if one doesn't exist.

        log_dir = config.get_log_dir()

        self.assertFalse(os.path.exists(log_dir))
        log.create_log_dir()
        self.assertTrue(os.path.exists(log_dir))
