## @file main.py
# @brief The main entry point for the program.
# @author Guy Chamberlain-Webber

import serial
import src.config as config

from src.packet.packet import Packet
from src.packet.headers import LocalHeaderMX5
from src.packet.packet_ids import PacketID


def run():
    # Creating and sending a panel restart packet.
    header = LocalHeaderMX5(PacketID.RESTART_REQUEST,
                            channel=0x06,
                            destination_channel_address=0x1d,
                            source_channel_address=0x1d
                            )
    new_packet = Packet(header)

    new_packet.write()


if __name__ == "__main__":
    run()
    