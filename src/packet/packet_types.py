## @file packet_types.py
# @brief Contains concrete implementations of frequently used packets.
# @author Guy Chamberlain-Webber

from src.packet.packet import Packet
from src.packet.headers import LocalHeaderMX5, LocalHeaderMX6
from src.packet.packet_ids import PacketID
from src.packet.writable import IWritable


class RestartPanelMX5(IWritable):
    def __init__(self):
        header = LocalHeaderMX5(PacketID.RESTART_REQUEST,
                                channel=0x06,
                                destination_channel_address=0x1d,
                                source_channel_address=0x1d
                                )
        self.packet = Packet(header)

    ## Writes to a serial communications port.
    def write(self):
        self.packet.write()
