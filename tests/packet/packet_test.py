## @file packet_test.py
# @brief Contains tests to test the 'packet' file and class.
# @author Guy Chamberlain-Webber

import unittest
from src.packet.packet import Packet
from src.packet.headers import LocalHeaderMX5, LocalHeaderMX6

this_packet = None


## This test case tests the 'packet' file and class.
class TestPacket(unittest.TestCase):
    def setUp(self) -> None:
        global this_packet

        header = LocalHeaderMX5(0)

        this_packet = Packet(
            header,
            value1=1,
            value2=2,
            value3=3
        )

    # Test 1
    def test_mx5_packet_size(self):
        # This test ensures that the size of a packet with a header type of MX Speak 5 with no
        # contents will be 9.

        header = LocalHeaderMX5(0)
        mx5_packet = Packet(header)

        self.assertEqual(len(mx5_packet._params), 9)

    # Test 2
    def test_mx6_packet_size(self):
        # This test ensures that the size of a packet with a header type of MX Speak 6 with no
        # contents will be 11.

        header = LocalHeaderMX6(11)
        mx6_packet = Packet(header)

        self.assertEqual(len(mx6_packet._params), 11)

    # Test 3
    # noinspection PyUnresolvedReferences
    def test_packet_contents(self):
        # This test ensures that the constructor of the Packet class behaves as expected by correctly merging
        # together the parameters of the header and contents.

        global this_packet

        expected_contents = [b'\x09', b'\x00', b'\x00',
                             b'\x00', b'\x00', b'\x00',
                             b'\x00', b'\x00', b'\x00',
                             b'\x01', b'\x02', b'\x03']

        self.assertEqual(this_packet.get_byte_array(), expected_contents)
