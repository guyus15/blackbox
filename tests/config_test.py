## @file config_test.py
# @brief Contains tests to test the 'config' module.
# @author Guy Chamberlain-Webber

import unittest
import json
import src.config as config

this_config = dict()

# Override config path just for the tests.
config.CONFIG_PATH = "../config.json"


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

        self.assertEqual(config.get_log_dir(), this_config["logging"]["directory"])

    # Test 2
    def test_get_log_enabled(self):
        # This test ensures that get_log_enabled() returns the expected value.
        global this_config

        self.assertEqual(config.get_log_enabled(), this_config["logging"]["enabled"])

    # Test 3
    def test_get_mx_signature(self):
        # This test ensures that get_mx_signature() returns the expected value.
        global this_config

        self.assertEqual(config.get_mx_signature(), this_config["packets"]["mx-speak-signature"])

    # Test 4
    def test_get_packet_length(self):
        # This test ensures that when given a valid MXSpeakVersion, the get_packet_length()
        # function will return the correct value from the configuration file.
        global this_config

        self.assertEqual(config.get_packet_length(config.MXSpeakVersion.MX_SPEAK5),
                         this_config["packets"]["mx5-default-packet-length"])
        self.assertEqual(config.get_packet_length(config.MXSpeakVersion.MX_SPEAK6),
                         this_config["packets"]["mx6-default-packet-length"])

    # Test 5
    def test_get_packet_length_invalid_version(self):
        # This test ensures that when given an invalid MXSpeakVersion, the get_packet_length() function
        # will raise an AttributeError.

        with self.assertRaises(AttributeError) as cm:
            config.get_packet_length(10)

        exception = cm.exception
        self.assertIsNotNone(exception)

    # Test 6
    def test_get_test_start_directory(self):
        # This test ensures that the get_test_start_directory() function will return the
        # correct path of the start-directory from the configuration file.
        global this_config

        self.assertEqual(config.get_test_start_directory(), this_config["testing"]["start-directory"])

