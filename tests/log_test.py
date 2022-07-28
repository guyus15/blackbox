## @file log_test.py
# @brief Contains tests to test the 'log' module.
# @author Guy Chamberlain-Webber

import unittest
import os
import src.config as config
import src.log as log

from unittest.mock import patch
from io import StringIO


## This test case test the 'log' module.
class TestLog(unittest.TestCase):

    def setUp(self):
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

    # Test 2
    def test_create_log_dir_exist(self):
        # This test ensures that the create_log_dir() function correctly informs the
        # user which log directory is being used if already one exists.

        log_dir_name = config.get_log_dir()

        # Create a log directory
        log.create_log_dir()

        with patch("sys.stdout", new=StringIO()) as fake_output:
            log.create_log_dir()
            self.assertEqual(fake_output.getvalue(), "Logging to directory '{}'\n".format(log_dir_name))

    @classmethod
    def tearDownClass(cls) -> None:
        # Remove test log directory
        log_dir = config.get_log_dir()

        if os.path.exists(log_dir):
            os.rmdir(log_dir)
