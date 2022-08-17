## @file config_test.py
# @brief Contains tests to test the 'config' module.
# @author Guy Chamberlain-Webber
import json
import sys
import unittest

import serial

import src.config as config
from src.exceptions.invalid_value import InvalidValueException

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
            # noinspection PyTypeChecker
            config.get_packet_length(10)

        exception = cm.exception
        self.assertIsNotNone(exception)

    # Test 6
    def test_get_test_start_directory(self):
        # This test ensures that the get_test_start_directory() function will return the
        # correct path of the start-directory from the configuration file.
        global this_config

        self.assertEqual(config.get_test_start_directory(), this_config["testing"]["start-directory"])

    # Test 7
    def test_get_test_discovery_pattern(self):
        # This test ensures that the get_test_discovery_pattern() function will return the
        # correct test discovery pattern specified in the configuration settings.
        global this_config

        self.assertEqual(config.get_test_discovery_pattern(), this_config["testing"]["discovery-pattern"])

    # Test 8
    def test_get_com_port_windows(self):
        # This test ensures that the get_com_port() function will return the correct
        # COM port name depending on the platform that the program is being run with.
        # In this case the function should return the "windows" COM port name from the
        # configuration.
        global this_config

        # Make a copy of sys.platform
        temp_plat = sys.platform

        # Hard coding for test purposes.
        sys.platform = "win32"

        self.assertEqual(config.get_com_port(), this_config["com"]["windows"])

        sys.platform = temp_plat

    # Test 9
    def test_get_com_port_linux(self):
        # This test ensures that the get_com_port() function will return the correct
        # COM port name depending on the platform that the program is being run with.
        # In this case the function should return the "linux" COM port name from the
        # configuration.
        global this_config

        # Make a copy of sys.platform
        temp_plat = sys.platform

        # Hard coding for test purposes.
        sys.platform = "linux"

        self.assertEqual(config.get_com_port(), this_config["com"]["linux"])

        sys.platform = temp_plat

    # Test 10
    def test_get_baudrate(self):
        # This test ensures that the get_baudrate() function will return the correct
        # baudrate specified in the configuration file.
        global this_config

        self.assertEqual(config.get_baudrate(), this_config["serial"]["baudrate"])

    # Test 11
    def test_get_timeout(self):
        # This test ensures that the get_timeout() function will return the correct
        # timeout value specified in the configuration file.
        global this_config

        self.assertEqual(config.get_timeout(), this_config["serial"]["timeout"])

    # Test 12
    def test_get_bytesize_valid(self):
        # This test ensures that when the get_bytesize() function is called, it will
        # return the correct serial enum value corresponding to that value.

        # Hard-coded for test purposes.
        config.config["serial"]["bytesize"] = 8

        self.assertEqual(config.get_bytesize(), serial.EIGHTBITS)

    # Test 13
    def test_get_bytesize_string(self):
        # This test ensures that when the get_bytesize() function is called when
        # a string is set to the bytesize value in the configuration file, an
        # InvalidValueException will be raised.

        # Hard-coded for test purposes.
        config.config["serial"]["bytesize"] = "some string"

        with self.assertRaises(InvalidValueException) as cm:
            config.get_bytesize()

        exception = cm.exception
        self.assertIsNotNone(exception)

    # Test 14
    def test_get_bytesize_out_of_range(self):
        # This test ensures that when the get_bytesize() function is called when
        # the bytesize value of the configuration file is set to an out of range
        # integer, an InvalidValueException will be raised.

        # Hard-coded for test purposes.
        config.config["serial"]["bytesize"] = 20

        with self.assertRaises(InvalidValueException) as cm:
            config.get_bytesize()

        exception = cm.exception
        self.assertIsNotNone(exception)

    # Test 15
    def test_get_parity(self):
        # This test ensures that when the get_parity() function is called, it will
        # return the correct serial enum value corresponding to that value.

        # Hard-coded for test purposes.
        config.config["serial"]["parity"] = "none"

        self.assertEqual(config.get_parity(), serial.PARITY_NONE)

    # Test 16
    def test_get_parity_invalid(self):
        # This test ensures that when the get_parity() function is called with an
        # invalid parity configuration, an InvalidValueException will be raised.

        # Hard-coded for test purposes.
        config.config["serial"]["parity"] = "some invalid parity"

        with self.assertRaises(InvalidValueException) as cm:
            config.get_parity()

        exception = cm.exception
        self.assertIsNotNone(exception)

    # Test 17
    def test_get_stopbits(self):
        # This test ensures that when the get_stopbits() function is called, it will
        # return the correct serial enum value corresponding to that value.

        # Hard-coded for test purposes.
        config.config["serial"]["stopbits"] = 1

        self.assertEqual(config.get_stopbits(), serial.STOPBITS_ONE)

    # Test 18
    def test_get_stopbits_string(self):
        # This test ensures that when the get_stopbits() function is called when the
        # stopbits configuration has been set to a string, an InvalidValueException will be
        # raised.

        # Hard-coded for test purposes.
        config.config["serial"]["stopbits"] = "some invalid stopbits value"

        with self.assertRaises(InvalidValueException) as cm:
            config.get_stopbits()

        exception = cm.exception
        self.assertIsNotNone(exception)

    # Test 19
    def test_get_stopbits_invalid(self):
        # This test ensures that when the get_stopbits() function is called with
        # an invalid stopbits configuration, an InvalidValueException will be raised.

        # Hard-coded for test purposes.
        config.config["serial"]["stopbits"] = 5

        with self.assertRaises(InvalidValueException) as cm:
            config.get_stopbits()

        exception = cm.exception
        self.assertIsNotNone(exception)

    # Test 20
    def test_get_time_period(self):
        # This test ensures that when the get_time_period() function is called,
        # it will return the correct value.
        global this_config

        self.assertEqual(config.get_time_period(), this_config["time-period"])

    # Test 21
    def test_get_polling_time_period(self):
        # This test ensures that when the get_polling_time_period() function is called,
        # it will return the correct value.
        global this_config

        self.assertEqual(config.get_polling_time_period(), this_config["polling-time-period"])

    @classmethod
    def tearDownClass(cls) -> None:
        with open(config.CONFIG_PATH) as fd:
            contents = fd.read()
            config.config = json.loads(contents)
