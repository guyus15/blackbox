## @file config_test.py
# @brief Contains tests to test the 'config' module.
# @author Guy Chamberlain-Webber

import unittest
import json
import src.config as config

this_config = dict()


## This test case test the 'config' module.
class TestConfig(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        global this_config

        with open(config.CONFIG_PATH) as fp:
            contents = fp.read()
            this_config = json.loads(contents)

    # Test 1
    def test_get_log_dir(self):
        # This test ensures that get_log_dir() returns the expected value.
        global this_config

        log_dir = config.get_log_dir()

        self.assertEqual(config.get_log_dir(), this_config["logging"]["log-directory"])
