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


## A class representing a point information request (MX5).
class PointInformationRequestMX5(PacketImplementation):
    def __init__(self):
        super().__init__()
        header = LocalHeaderMX5(PacketID.POINT_INFO_REQUEST)
        params = {
            "node": 0,  # D+0
            "channel": 0,  # D+1
            "channel_address": 1,  # D+2
            "point_category": 0,  # D+3
            "point_number": 4,  # D+4
            "logical_point_number": 253,  # D+5
            "logical_point_zone": 254,  # D+6
            "device_category": 0,  # D+7
            "group0": 0,  # D+8
            "group1": 1,  # D+9
            "output_point_state_store": 3,  # D+10
            "reserved0": 0,  # D+11
            "reserved1": 0,  # D+12
            "multi-area_type": 3,  # D+13
            "areas0": 0,  # D+14
            "areas1": 0,  # D+15
            "areas2": 0,  # D+16
            "areas3": 0,  # D+17
            "areas4": 0,  # D+18
            "areas5": 0,  # D+19
            "areas6": 0,  # D+20
            "areas7": 0,  # D+21
            "areas8": 0,  # D+22
            "areas9": 0,  # D+23
            "areas10": 0,  # D+24
            "areas11": 0,  # D+25
            "areas12": 0,  # D+26
            "areas13": 0,  # D+27
            "areas14": 0,  # D+28
            "areas15": 0,  # D+29
            "areas16": 0,  # D+30
            "areas17": 0,  # D+31
            "areas18": 0,  # D+32
            "areas19": 0,  # D+33
            "areas20": 0,  # D+34
            "areas21": 0,  # D+35
            "areas22": 0,  # D+36
            "areas23": 0,  # D+37
            "areas24": 0,  # D+38
            "areas25": 0,  # D+39
            "areas26": 0,  # D+40
            "areas27": 0,  # D+41
            "areas28": 0,  # D+42
            "areas29": 0,  # D+43
            "area240": 0,  # D+44
            "device_type": 127,  # D+45
            "request_type": 0,  # D+46
            "search_type": 10  # D+47
        }

        self.packet = Packet(header=header, **params)


## A class representing a point information request (MX6).
class PointInformationRequestMX6(PacketImplementation):
    def __init__(self):
        super().__init__()
        header = LocalHeaderMX6(PacketID.POINT_INFO_REQUEST)
        params = {
            "node": 0,  # D+0
            "channel": 0,  # D+1
            "channel_address": 1,  # D+2
            "point_category": 0,  # D+3
            "point_number": 4,  # D+4
            "logical_point_number": 253,  # D+5
            "logical_point_zone": 254,  # D+6
            "device_category": 0,  # D+7
            "group0": 0,  # D+8
            "group1": 1,  # D+9
            "output_point_state_store": 3,  # D+10
            "reserved0": 0,  # D+11
            "reserved1": 0,  # D+12
            "multi-area_type": 3,  # D+13
            "areas0": 0,  # D+14
            "areas1": 0,  # D+15
            "areas2": 0,  # D+16
            "areas3": 0,  # D+17
            "areas4": 0,  # D+18
            "areas5": 0,  # D+19
            "areas6": 0,  # D+20
            "areas7": 0,  # D+21
            "areas8": 0,  # D+22
            "areas9": 0,  # D+23
            "areas10": 0,  # D+24
            "areas11": 0,  # D+25
            "areas12": 0,  # D+26
            "areas13": 0,  # D+27
            "areas14": 0,  # D+28
            "areas15": 0,  # D+29
            "areas16": 0,  # D+30
            "areas17": 0,  # D+31
            "areas18": 0,  # D+32
            "areas19": 0,  # D+33
            "areas20": 0,  # D+34
            "areas21": 0,  # D+35
            "areas22": 0,  # D+36
            "areas23": 0,  # D+37
            "areas24": 0,  # D+38
            "areas25": 0,  # D+39
            "areas26": 0,  # D+40
            "areas27": 0,  # D+41
            "areas28": 0,  # D+42
            "areas29": 0,  # D+43
            "area240": 0,  # D+44
            "device_type": 127,  # D+45
            "request_type": 0,  # D+46
            "search_type": 10  # D+47
        }

        self.packet = Packet(header=header, **params)


# A dictionary containing concrete packets respective to their expected response packet's size (i.e. you send
# a MX5 Panel Details request, you expected a response of size 29).
response_sizes = {
    RestartPanelMX5: 0,
    RestartPanelMX6: 0,
    PanelDetailsRequestMX5: 30,
    PanelDetailsRequestMX6: 31,
    PointInformationRequestMX5: 56,
    PointInformationRequestMX6: 56
}
