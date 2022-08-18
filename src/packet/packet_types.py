## @file packet_types.py
# @brief Contains concrete implementations of frequently used packets.
# @author Guy Chamberlain-Webber

import src.constants as constants

from src.packet.content import Content
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


## A class representing a point information reply packet (MX5).
class PointInformationReplyMX5(Content):
    def __init__(self, point_number: int, data: list, **kwargs):
        self.point_number = point_number
        self._data = data

        params = {
            "soh": self._data[constants.PIRMX5_SOH_INDEX],
            "seq": self._data[constants.PIRMX5_SEQ_INDEX],
            "hpacket_length": self._data[constants.PIRMX5_PACKET_LENGTH_INDEX],
            "hnetwork_node": self._data[constants.PIRMX5_NETWORK_NODE_INDEX],
            "hchannel": self._data[constants.PIRMX5_POINT_ADDRESS_CHANNEL_INDEX],
            "hdestination_channel_address": self._data[constants.PIRMX5_DESTINATION_CHANNEL_ADDRESS_INDEX],
            "hdestination_task": self._data[constants.PIRMX5_DESTINATION_TASK_INDEX],
            "hsource_channel_address": self._data[constants.PIRMX5_SOURCE_CHANNEL_ADDRESS_INDEX],
            "hsource_task": self._data[constants.PIRMX5_SOURCE_TASK_INDEX],
            "hmarker": self._data[constants.PIRMX5_MARKER_INDEX],
            "hpacket_id": self._data[constants.PIRMX5_PACKET_ID_INDEX],
            "preply_status": self._data[constants.PIRMX5_REPLY_STATUS_INDEX],
            "pflags": self._data[constants.PIRMX5_FLAGS_INDEX],
            "pnode": self._data[constants.PIRMX5_NODE_INDEX],
            "pchannel": self._data[constants.PIRMX5_POINT_ADDRESS_CHANNEL_INDEX],
            "pchannel_address": self._data[constants.PIRMX5_CHANNEL_ADDRESS_INDEX],
            "ppoint_category": self._data[constants.PIRMX5_POINT_CATEGORY_INDEX],
            "ppoint_number": self._data[constants.PIRMX5_POINT_NUMBER_INDEX],
            "plogical_point_number": self._data[constants.PIRMX5_LOGICAL_POINT_NUMBER_INDEX],
            "plogical_point_zone": self._data[constants.PIRMX5_LOGICAL_POINT_ZONE_INDEX],
            "pdevice_type": self._data[constants.PIRMX5_DEVICE_TYPE_INDEX],
            "pauxiliary_point_attributes": self._data[constants.PIRMX5_AUXILIARY_POINT_ATTRIBUTES_INDEX],
            "pgroup1": self._data[constants.PIRMX5_GROUP1_INDEX],
            "pgroup2": self._data[constants.PIRMX5_GROUP2_INDEX],
            "parea_type": self._data[constants.PIRMX5_AREA_TYPE_INDEX],
            "parea_number": self._data[constants.PIRMX5_AREA_NUMBER_INDEX],
            "psector_id": self._data[constants.PIRMX5_SECTOR_ID_INDEX],
            "ploop_type": self._data[constants.PIRMX5_LOOP_TYPE_INDEX],
            "praw_identity": self._data[constants.PIRMX5_RAW_IDENTITY_INDEX],
            "pactual_device_type": self._data[constants.PIRMX5_ACTUAL_DEVICE_TYPE_INDEX],
            "pmode_and_sensitivity": self._data[constants.PIRMX5_MODE_AND_SENSITIVITY_INDEX],
            "praw_analogue_values1": self._data[constants.PIRMX5_RAW_ANALOGUE_VALUES1_INDEX],
            "praw_analogue_values2": self._data[constants.PIRMX5_RAW_ANALOGUE_VALUES2_INDEX],
            "praw_analogue_values3": self._data[constants.PIRMX5_RAW_ANALOGUE_VALUES3_INDEX],
            "plta_flags": self._data[constants.PIRMX5_LTA_FLAGS_INDEX],
            "pdirtiness": self._data[constants.PIRMX5_DIRTINESS_INDEX],
            "punits_of_measure1": self._data[constants.PIRMX5_UNITS_OF_MEASURE1_INDEX],
            "punits_of_measure2": self._data[constants.PIRMX5_UNITS_OF_MEASURE2_INDEX],
            "punits_of_measure3": self._data[constants.PIRMX5_UNITS_OF_MEASURE3_INDEX],
            "pconverted_value1": self._data[constants.PIRMX5_CONVERTED_VALUE1_INDEX],
            "pconverted_value2": self._data[constants.PIRMX5_CONVERTED_VALUE2_INDEX],
            "pconverted_value3": self._data[constants.PIRMX5_CONVERTED_VALUE3_INDEX],
            "pinstantaneous_active_state": self._data[constants.PIRMX5_INSTANTANEOUS_ACTIVE_STATE_INDEX],
            "pinstantaneous_fault_state": self._data[constants.PIRMX5_INSTANTANEOUS_FAULT_STATE_INDEX],
            "pconfirmed_active_state": self._data[constants.PIRMX5_CONFIRMED_ACTIVE_STATE_INDEX],
            "pconfirmed_fault_state": self._data[constants.PIRMX5_CONFIRMED_FAULT_STATE_INDEX],
            "packnowledged_active_state": self._data[constants.PIRMX5_ACKNOWLEDGED_ACTIVE_STATE_INDEX],
            "packnowledged_fault_state": self._data[constants.PIRMX5_ACKNOWLEDGED_FAULT_STATE_INDEX],
            "poutput_forced_mode": self._data[constants.PIRMX5_OUTPUT_FORCED_MODE_INDEX],
            "poutput_unforced_state": self._data[constants.PIRMX5_OUTPUT_UNFORCED_STATE_INDEX],
            "poutput_forced_state": self._data[constants.PIRMX5_OUTPUT_FORCED_STATE_INDEX],
            "pclient_id1": self._data[constants.PIRMX5_CLIENT_ID1_INDEX],
            "pclient_id2": self._data[constants.PIRMX5_CLIENT_ID2_INDEX],
            "pposition_in_points_total1": self._data[constants.PIRMX5_POSITION_IN_POINTS_TOTAL1_INDEX],
            "pposition_in_points_total2": self._data[constants.PIRMX5_POSITION_IN_POINTS_TOTAL2_INDEX]
        }

        super().__init__(**params)

    ## Returns whether the reply packet has been successful in finding a device on the network.
    #
    # @return True is a device has been found at a particular point on the network, otherwise False.
    def reply_successful(self) -> bool:
        return self.get_parameter("preply_status") == 0

    def __str__(self):
        if self.reply_successful():
            return super().__str__()

        return f"No points found at address {self.point_number}."


## A class representing a point information reply packet (MX6).
class PointInformationReplyMX6(Content):
    def __init__(self, point_number: int, data: list, **kwargs):
        self.point_number = point_number
        self._data = data

        params = {
            "soh": self._data[constants.PIRMX6_SOH_INDEX],
            "seq": self._data[constants.PIRMX6_SEQ_INDEX],
            "hpacket_length": self._data[constants.PIRMX6_PACKET_LENGTH_INDEX],
            "hmx_speak_signature": self._data[constants.PIRMX6_MX6_SPEAKSIGNATURE_INDEX],
            "hnetwork_node": self._data[constants.PIRMX6_NETWORK_NODE_INDEX],
            "hchannel": self._data[constants.PIRMX6_POINT_ADDRESS_CHANNEL_INDEX],
            "hdestination_channel_address": self._data[constants.PIRMX6_DESTINATION_CHANNEL_ADDRESS_INDEX],
            "hdestination_task": self._data[constants.PIRMX6_DESTINATION_TASK_INDEX],
            "hsource_channel_address": self._data[constants.PIRMX6_SOURCE_CHANNEL_ADDRESS_INDEX],
            "hsource_task": self._data[constants.PIRMX6_SOURCE_TASK_INDEX],
            "hmarker": self._data[constants.PIRMX6_MARKER_INDEX],
            "hpacket_id": self._data[constants.PIRMX6_PACKET_ID_INDEX],
            "preply_status": self._data[constants.PIRMX6_REPLY_STATUS_INDEX],
            "pflags": self._data[constants.PIRMX6_FLAGS_INDEX],
            "pnode": self._data[constants.PIRMX6_NODE_INDEX],
            "pchannel": self._data[constants.PIRMX6_POINT_ADDRESS_CHANNEL_INDEX],
            "pchannel_address": self._data[constants.PIRMX6_CHANNEL_ADDRESS_INDEX],
            "ppoint_category": self._data[constants.PIRMX6_POINT_CATEGORY_INDEX],
            "ppoint_number": self._data[constants.PIRMX6_POINT_NUMBER_INDEX],
            "plogical_point_number": self._data[constants.PIRMX6_LOGICAL_POINT_NUMBER_INDEX],
            "plogical_point_zone": self._data[constants.PIRMX6_LOGICAL_POINT_ZONE_INDEX],
            "pdevice_type": self._data[constants.PIRMX6_DEVICE_TYPE_INDEX],
            "pauxiliary_point_attributes": self._data[constants.PIRMX6_AUXILIARY_POINT_ATTRIBUTES_INDEX],
            "pgroup1": self._data[constants.PIRMX6_GROUP1_INDEX],
            "pgroup2": self._data[constants.PIRMX6_GROUP2_INDEX],
            "parea_type": self._data[constants.PIRMX6_AREA_TYPE_INDEX],
            "parea_number": self._data[constants.PIRMX6_AREA_NUMBER_INDEX],
            "psector_id": self._data[constants.PIRMX6_SECTOR_ID_INDEX],
            "ploop_type": self._data[constants.PIRMX6_LOOP_TYPE_INDEX],
            "praw_identity": self._data[constants.PIRMX6_RAW_IDENTITY_INDEX],
            "pactual_device_type": self._data[constants.PIRMX6_ACTUAL_DEVICE_TYPE_INDEX],
            "pmode_and_sensitivity": self._data[constants.PIRMX6_MODE_AND_SENSITIVITY_INDEX],
            "praw_analogue_values1": self._data[constants.PIRMX6_RAW_ANALOGUE_VALUES1_INDEX],
            "praw_analogue_values2": self._data[constants.PIRMX6_RAW_ANALOGUE_VALUES2_INDEX],
            "praw_analogue_values3": self._data[constants.PIRMX6_RAW_ANALOGUE_VALUES3_INDEX],
            "plta_flags": self._data[constants.PIRMX6_LTA_FLAGS_INDEX],
            "pdirtiness": self._data[constants.PIRMX6_DIRTINESS_INDEX],
            "punits_of_measure1": self._data[constants.PIRMX6_UNITS_OF_MEASURE1_INDEX],
            "punits_of_measure2": self._data[constants.PIRMX6_UNITS_OF_MEASURE2_INDEX],
            "punits_of_measure3": self._data[constants.PIRMX6_UNITS_OF_MEASURE3_INDEX],
            "pconverted_value1": self._data[constants.PIRMX6_CONVERTED_VALUE1_INDEX],
            "pconverted_value2": self._data[constants.PIRMX6_CONVERTED_VALUE2_INDEX],
            "pconverted_value3": self._data[constants.PIRMX6_CONVERTED_VALUE3_INDEX],
            "pinstantaneous_active_state": self._data[constants.PIRMX6_INSTANTANEOUS_ACTIVE_STATE_INDEX],
            "pinstantaneous_fault_state": self._data[constants.PIRMX6_INSTANTANEOUS_FAULT_STATE_INDEX],
            "pconfirmed_active_state": self._data[constants.PIRMX6_CONFIRMED_ACTIVE_STATE_INDEX],
            "pconfirmed_fault_state": self._data[constants.PIRMX6_CONFIRMED_FAULT_STATE_INDEX],
            "packnowledged_active_state": self._data[constants.PIRMX6_ACKNOWLEDGED_ACTIVE_STATE_INDEX],
            "packnowledged_fault_state": self._data[constants.PIRMX6_ACKNOWLEDGED_FAULT_STATE_INDEX],
            "poutput_forced_mode": self._data[constants.PIRMX6_OUTPUT_FORCED_MODE_INDEX],
            "poutput_unforced_state": self._data[constants.PIRMX6_OUTPUT_UNFORCED_STATE_INDEX],
            "poutput_forced_state": self._data[constants.PIRMX6_OUTPUT_FORCED_STATE_INDEX],
            "pclient_id1": self._data[constants.PIRMX6_CLIENT_ID1_INDEX],
            "pclient_id2": self._data[constants.PIRMX6_CLIENT_ID2_INDEX],
            "pposition_in_points_total1": self._data[constants.PIRMX6_POSITION_IN_POINTS_TOTAL1_INDEX],
            "pposition_in_points_total2": self._data[constants.PIRMX6_POSITION_IN_POINTS_TOTAL2_INDEX]
        }

        super().__init__(**params)

    def reply_successful(self) -> bool:
        return self.get_parameter("preply_status") == 0

    def __str__(self):
        if self.reply_successful():
            return super().__str__()

        return f"No points found at address {self.point_number}."


## A class representing a point information request (MX5).
class PointInformationRequestMX5(PacketImplementation):
    def __init__(self, point_number: int):
        super().__init__()

        self.point_number = point_number

        header = LocalHeaderMX5(PacketID.POINT_INFO_REQUEST)
        params = {
            "pnode": 0,  # D+0
            "pchannel": 0,  # D+1
            "pchannel_address": 1,  # D+2
            "ppoint_category": 0,  # D+3
            "ppoint_number": self.point_number,  # D+4
            "plogical_point_number": 253,  # D+5
            "plogical_point_zone": 254,  # D+6
            "pdevice_category": 0,  # D+7
            "pgroup0": 0,  # D+8
            "pgroup1": 1,  # D+9
            "poutput_point_state_store": 3,  # D+10
            "preserved0": 0,  # D+11
            "preserved1": 0,  # D+12
            "pmulti-area_type": 3,  # D+13
            "pareas0": 0,  # D+14
            "pareas1": 0,  # D+15
            "pareas2": 0,  # D+16
            "pareas3": 0,  # D+17
            "pareas4": 0,  # D+18
            "pareas5": 0,  # D+19
            "pareas6": 0,  # D+20
            "pareas7": 0,  # D+21
            "pareas8": 0,  # D+22
            "pareas9": 0,  # D+23
            "pareas10": 0,  # D+24
            "pareas11": 0,  # D+25
            "pareas12": 0,  # D+26
            "pareas13": 0,  # D+27
            "pareas14": 0,  # D+28
            "pareas15": 0,  # D+29
            "pareas16": 0,  # D+30
            "pareas17": 0,  # D+31
            "pareas18": 0,  # D+32
            "pareas19": 0,  # D+33
            "pareas20": 0,  # D+34
            "pareas21": 0,  # D+35
            "pareas22": 0,  # D+36
            "pareas23": 0,  # D+37
            "pareas24": 0,  # D+38
            "pareas25": 0,  # D+39
            "pareas26": 0,  # D+40
            "pareas27": 0,  # D+41
            "pareas28": 0,  # D+42
            "pareas29": 0,  # D+43
            "parea240": 0,  # D+44
            "pdevice_type": 127,  # D+45
            "prequest_type": 0,  # D+46
            "psearch_type": 10  # D+47
        }

        self.packet = Packet(header=header, **params)
        print(f"Point Information Request Packet: {self.packet.get_byte_array()}")

    # Reads data from a communications port by calling the underlying
    # packet read method.
    #
    # @return The data in the form of a PointInformationReplyMX6.
    def read(self) -> PointInformationReplyMX5:
        data = self.packet.read(response_sizes.get(type(self)))
        print(f"Read data: {data}")

        return PointInformationReplyMX5(self.point_number, data)


## A class representing a point information request (MX6).
class PointInformationRequestMX6(PacketImplementation):
    def __init__(self, point_number: int):
        super().__init__()

        self.point_number = point_number

        header = LocalHeaderMX6(PacketID.POINT_INFO_REQUEST)
        params = {
            "pnode": 0,  # D+0
            "pchannel": 0,  # D+1
            "pchannel_address": 1,  # D+2
            "ppoint_category": 0,  # D+3
            "ppoint_number": self.point_number,  # D+4
            "plogical_point_number": 253,  # D+5
            "plogical_point_zone": 254,  # D+6
            "pdevice_category": 0,  # D+7
            "pgroup0": 0,  # D+8
            "pgroup1": 1,  # D+9
            "poutput_point_state_store": 3,  # D+10
            "preserved0": 0,  # D+11
            "preserved1": 0,  # D+12
            "pmulti-area_type": 3,  # D+13
            "pareas0": 0,  # D+14
            "pareas1": 0,  # D+15
            "pareas2": 0,  # D+16
            "pareas3": 0,  # D+17
            "pareas4": 0,  # D+18
            "pareas5": 0,  # D+19
            "pareas6": 0,  # D+20
            "pareas7": 0,  # D+21
            "pareas8": 0,  # D+22
            "pareas9": 0,  # D+23
            "pareas10": 0,  # D+24
            "pareas11": 0,  # D+25
            "pareas12": 0,  # D+26
            "pareas13": 0,  # D+27
            "pareas14": 0,  # D+28
            "pareas15": 0,  # D+29
            "pareas16": 0,  # D+30
            "pareas17": 0,  # D+31
            "pareas18": 0,  # D+32
            "pareas19": 0,  # D+33
            "pareas20": 0,  # D+34
            "pareas21": 0,  # D+35
            "pareas22": 0,  # D+36
            "pareas23": 0,  # D+37
            "pareas24": 0,  # D+38
            "pareas25": 0,  # D+39
            "pareas26": 0,  # D+40
            "pareas27": 0,  # D+41
            "pareas28": 0,  # D+42
            "pareas29": 0,  # D+43
            "parea240": 0,  # D+44
            "pdevice_type": 127,  # D+45
            "prequest_type": 0,  # D+46
            "psearch_type": 10,  # D+47
        }

        self.packet = Packet(header=header, **params)
        print(f"Point Information Request Packet: {self.packet.get_byte_array()}")

    # Reads data from a communications port by calling the underlying
    # packet read method.
    #
    # @return The data in the form of a PointInformationReplyMX6.
    def read(self) -> PointInformationReplyMX6:
        data = self.packet.read(response_sizes.get(type(self)))
        print(f"Read data: {data}")

        return PointInformationReplyMX6(self.point_number, data)


# A dictionary containing concrete packets respective to their expected response packet's size (i.e. you send
# a MX5 Panel Details request, you expected a response of size 29).
response_sizes = {
    RestartPanelMX5: 0,
    RestartPanelMX6: 0,
    PanelDetailsRequestMX5: 30,
    PanelDetailsRequestMX6: 31,
    PointInformationRequestMX5: 55,
    PointInformationRequestMX6: 55
}
