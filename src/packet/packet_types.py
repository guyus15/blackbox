## @file packet_types.py
# @brief Contains concrete implementations of frequently used packets.
# @author Guy Chamberlain-Webber

from src.packet.headers import LocalHeaderMX5
from src.packet.headers import LocalHeaderMX6
from src.packet.packet import Packet
from src.packet.packet_ids import PacketID
from src.packet.writable import IWritable


## A class representing a restart panel packet (MX5).
class RestartPanelMX5(IWritable):
    def __init__(self):
        header = LocalHeaderMX5(PacketID.RESTART_REQUEST)
        self.packet = Packet(header)

    ## Writes to a serial communications port.
    def write(self):
        self.packet.write()


## A class representing a restart panel packet (MX6).
class RestartPanelMX6(IWritable):
    def __init__(self):
        header = LocalHeaderMX5(PacketID.RESTART_REQUEST)
        self.packet = Packet(header)

    ## Writes to a serial communication port.
    def write(self):
        self.packet.write()


## A class representing a panel information request (MX5).
class PanelDetailsRequestMX5(IWritable):
    def __init__(self):
        header = LocalHeaderMX5(PacketID.PANEL_DETAILS_REQUEST)
        self.packet = Packet(header)

    ## Writes to a serial communications port.
    def write(self):
        self.packet.write()


## A class representing a panel information request (MX6).
class PanelDetailsRequestMX6(IWritable):
    def __init__(self):
        header = LocalHeaderMX6(PacketID.PANEL_DETAILS_REQUEST)
        self.packet = Packet(header)

    # Writes to a serial communications port.
    def write(self):
        self.packet.write()
