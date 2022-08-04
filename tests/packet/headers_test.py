## @file headers_test.py
# @brief Contains tests to test the 'headers' file and classes.
# @author Guy Chamberlain-Webber

import unittest
from src.packet.headers import LocalHeaderMX5, LocalHeaderMX6


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
