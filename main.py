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

    with serial.Serial(port=config.get_com_port(),
                       baudrate=config.get_baudrate(),
                       timeout=config.get_timeout(),
                       bytesize=config.get_bytesize(),
                       parity=config.get_parity(),
                       stopbits=config.get_stopbits()) as ser:

        ser.write(new_packet.get_byte_array())


if __name__ == "__main__":
    run()
    