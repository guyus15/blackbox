## @file headers_test.py
# @brief Contains tests to test the 'headers' file and classes.
# @author Guy Chamberlain-Webber

import unittest
from src.packet.headers import LocalHeaderMX5, LocalHeaderMX6
from src.exceptions.parameter_not_found import ParameterNotFoundException
from src.exceptions.invalid_value import InvalidValueException


## This test case tests the 'headers' file and classes.
class TestHeaders(unittest.TestCase):
    # Test 1
    def test_mx5_header_contents(self):
        # This test ensures that after creating an MX Speak 5 packet header,
        # it contains the correct values.

        # MX Speak packet header, ID of 0.
        mx5_header = LocalHeaderMX5(0)

        expected_value = [9, 0, 0, 0, 0, 0, 0, 0, 0]

        self.assertEqual(mx5_header.get_byte_array(), expected_value)

    # Test 2
    def test_mx6_header_contents(self):
        # This test ensures that after creating an MX Speak 6 packet header,
        # it contains the correct values.

        # MX Speak packet header, ID of 0.
        mx6_header = LocalHeaderMX6(0)

        expected_value = [11, 228, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.assertEqual(mx6_header.get_byte_array(), expected_value)

    # Test 3
    def test_mx5_override_default_contents(self):
        # This test ensures that it is possible to override an MX5 header's contents
        # if further arguments are provided in the initialiser.

        mx5_header = LocalHeaderMX5(182,
                                    network_node=10,
                                    channel=5,
                                    destination_task=1
                                    )

        expected_value = [9, 10, 5, 0, 1, 0, 0, 0, 182]

        self.assertEqual(mx5_header.get_byte_array(), expected_value)

    # Test 4
    def test_mx5_override_non_existent_attr(self):
        # This test ensures that it is not possible to add new values to the MX5 header
        # by adding additional arguments. A ParameterNotFoundException should be raised.

        with self.assertRaises(ParameterNotFoundException) as cm:
            mx5_header = LocalHeaderMX5(182, non_existent=10, another=15, yet_another=20)

        exception = cm.exception
        self.assertIsNotNone(exception)

    # Test 5
    def test_mx6_override_default_contents(self):
        # This test ensures that it is possible to override an MX6 header's contents
        # if further arguments are provided to the initialiser.

        mx6_header = LocalHeaderMX6(149,
                                    network_node=1,
                                    channel=10,
                                    destination_task=5
                                    )

        expected_value = [11, 228, 1, 10, 0, 5, 0, 0, 0, 149, 0]

        self.assertEqual(mx6_header.get_byte_array(), expected_value)

    # Test 6
    def test_mx6_override_speak_signature(self):
        # This test ensures that it is not possible to override the MX6 Speak Signature,
        # if it is attempted, an InvalidValueException will be raised.

        with self.assertRaises(InvalidValueException) as cm:
            mx6_header = LocalHeaderMX6(150,
                                        mx_speak_signature=200
                                        )

        exception = cm.exception
        self.assertIsNotNone(exception)

    # Test 7
    def test_mx6_override_non_existent_attr(self):
        # This test ensures that it is not possible to add new values to the MX6 header
        # by adding additional arguments. A ParameterNotFoundException should be raised.

        with self.assertRaises(ParameterNotFoundException) as cm:
            mx6_header = LocalHeaderMX6(150, non_existent=10, another=15, yet_anothe=20)

        exception = cm.exception
        self.assertIsNotNone(exception)
