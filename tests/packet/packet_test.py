## @file packet_test.py
# @brief Contains tests to test the 'packet' file and class.
# @author Guy Chamberlain-Webber

import unittest

from src.constants import SEQ_WRAP
from src.packet.headers import LocalHeaderMX5, LocalHeaderMX6
from src.packet.packet import Packet
from src.packet.packet_ids import PacketID

this_packet = None


## This test case tests the 'packet' file and class.
class TestPacket(unittest.TestCase):
    def setUp(self) -> None:
        global this_packet

        header = LocalHeaderMX5(PacketID.INVALID)

        this_packet = Packet(
            header,
            value1=1,
            value2=2,
            value3=3
        )

        # Reset the SEQ number between tests.
        Packet.seq = 0x01

    # Test 1
    def test_mx5_packet_size(self):
        # This test ensures that the size of a packet with a header type of MX Speak 5 with no
        # contents will be 9.

        header = LocalHeaderMX5(PacketID.INVALID)
        mx5_packet = Packet(header)

        self.assertEqual(len(mx5_packet._params), 9)

    # Test 2
    def test_mx6_packet_size(self):
        # This test ensures that the size of a packet with a header type of MX Speak 6 with no
        # contents will be 11.

        header = LocalHeaderMX6(PacketID.NET_VERSION_REQUEST)
        mx6_packet = Packet(header)

        self.assertEqual(len(mx6_packet._params), 11)

    # Test 3
    # noinspection PyUnresolvedReferences
    def test_packet_contents(self):
        # This test ensures that the constructor of the Packet class behaves as expected by correctly merging
        # together the parameters of the header and contents.
        global this_packet

        expected_contents = [0x01, 0x01, 0x0c,
                             0x00, 0x00, 0x00,
                             0x00, 0x00, 0x00,
                             0x00, 0x00, 0x01,
                             0x02, 0x03, 0x13]

        self.assertEqual(this_packet.get_byte_array(), expected_contents)

    # Test 4
    def test_seq_number_start(self):
        # This test ensures that the starting sequence number is 1.
        self.assertEqual(Packet.seq, 0x01)

    # Test 5
    # noinspection PyUnresolvedReferences
    def test_increment_seq_number(self):
        # This test ensures that each time a packet is written to the serial communications port,
        # the sequence number (SEQ) is incremented accordingly.
        global this_packet

        # Writing three times should increment the SEQ by three.
        this_packet.write()
        this_packet.write()
        this_packet.write()

        # 0x01 + 3 = 0x04
        self.assertEqual(Packet.seq, 0x04)

    # Test 6
    # noinspection PyUnresolvedReferences
    def test_increment_seq_wrap(self):
        # This test ensures that when the sequence number reaches a certain threshhold, it will
        # wrap back round to its starting value.
        global this_packet

        for i in range(SEQ_WRAP):
            this_packet.write()

        self.assertEqual(Packet.seq, 0x01)
