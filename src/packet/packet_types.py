## @file packet_types.py
# @brief Contains concrete implementations of frequently used packets.
# @author Guy Chamberlain-Webber

from src.packet.headers import LocalHeaderMX5
from src.packet.headers import LocalHeaderMX6
from src.packet.packet import Packet
from src.packet.packet_ids import PacketID
from src.packet.writable import IWritable


## A class to be used as the base class for all writable packets.
class PacketImplementation(IWritable):
    def __init__(self):
        header = LocalHeaderMX5(PacketID.INVALID)
        self.packet = Packet(header)

    ## Writes to a serial communication port.
    def write(self):
        self.packet.write()

    # Reads data from a communications port by calling the underlying
    # packet read method.
    #
    # @return The data read (if any).
    def read(self) -> list:
        # noinspection PyTypeChecker
        # Due to it being the base class, when used by child classes, type will change.
        return self.packet.read(response_sizes.get(type(self)))


## A class representing a restart panel packet (MX5).
class RestartPanelMX5(PacketImplementation):
    def __init__(self):
        super().__init__()
        header = LocalHeaderMX5(PacketID.RESTART_REQUEST)
        self.packet = Packet(header)


## A class representing a restart panel packet (MX6).
class RestartPanelMX6(PacketImplementation):
    def __init__(self):
        super().__init__()
        header = LocalHeaderMX5(PacketID.RESTART_REQUEST)
        self.packet = Packet(header)


## A class representing a panel information request (MX5).
class PanelDetailsRequestMX5(PacketImplementation):
    def __init__(self):
        super().__init__()
        header = LocalHeaderMX5(PacketID.PANEL_DETAILS_REQUEST)
        self.packet = Packet(header)


## A class representing a panel information request (MX6).
class PanelDetailsRequestMX6(PacketImplementation):
    def __init__(self):
        super().__init__()
        header = LocalHeaderMX6(PacketID.PANEL_DETAILS_REQUEST)
        self.packet = Packet(header)


# A dictionary containing concrete packets respective to their expected response packet's size (i.e. you send
# a MX5 Panel Details request, you expected a response of size 29).
response_sizes = {
    RestartPanelMX5: 0,
    RestartPanelMX6: 0,
    PanelDetailsRequestMX5: 30,
    PanelDetailsRequestMX6: 31
}
