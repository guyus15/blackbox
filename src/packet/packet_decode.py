## @file.py packet_decode.py
# @brief Provides functions to decode a series of bytes into a human-readable format.
# @author Guy Chamberlain-Webber

import src.constants as constants
from src.packet.device_codes import devices_codes

# Dictionaries defining the meaning of packet contents.

reply_status = {
    0: "Success",
    1: "Failure"
}

flags = {
    0: "Input Forced",
    1: "Point Untested or Failed",
    2: "Input Isolated",
    4: "Output Isolated",
    8: "Out of Compensation",
    16: "Point Type",
    32: "Loop Fault",
    64: "Output Under Test"
}

channel = {
    0: "MP CPU/Software Channel",
    1: "RBus (Remote Bus)",
    2: "COM1",
    3: "COM2",
    4: "COM3 (Network Port)",
    5: "LNet (Local Ethernet)",
    6: "Service Bus",
    7: "All Channels",
    12: "MP Loop",
    13: "MP Non-Loop",
    14: "Comm Ports Statuses",
    15: "Comm Nodes Statuses"
}

channel_address = {
    255: "All"
}

point_category = {
    0: "Real",
    1: "Pseudo",
    2: "XBus (Expansion Bus)",
    3: "Timer",
    4: "Menu",
    5: "Isolate",
    6: "User",
    254: "Not a Point",
    255: "All"
}

point_number = {
    253: "No Physical Address Provided",
    255: "All"
}

logical_point_zone = {
    254: "Zone N/A"
}

auxiliary_point_attributes = {
    0: "The point supports input",
    1: "The point supports output",
    2: "The point is a 'Solo' conventional detector interface",
    4: "Base of split device",
    8: "Part of split device",
    16: "Unused",
    32: "The point raising this event is classified as a sounder",
    64: "Is isolation of point allowed"
}

sector_id = {
    254: "Not in Sector"
}

loop_type = {
    0: "Thorn",
    1: "MX Digital",
    2: "Not Loop",
    3: "Zetfas",
    4: "STI"
}

lta_flags = {
    0: "LTA Available",
    1: "Dirtiness Available"
}

unit_of_measurement = {
    0: "Invalid",
    1: "Degrees C",
    2: "Degrees F",
    3: "ppm (parts per million)",
    4: "%/ft obscuration",
    5: "%/m obscuration",
    6: "Y value",
    7: "Amps",
    8: "Volts",
    9: "Not Installed",
    10: "mA"
}

instantaneous_active_state = {
    0: "Clear",
    1: "Pre-Alarm",
    2: "Alarm Verifying",
    3: "Active",
    4: "Resetting",
    5: "Test"
}

confirmed_active_state = {
    6: "Activate Warning"
}

output_forced_mode = {
    0: "Currently Unforced",
    1: "Currently Forced"
}

output_unforced_state = {
    0: "Off",
    1: "On",
    2: "Pulse 1 (pulsing mode 1)",
    3: "Pulse 2 (pulsing mode 2)",
    4: "Point With No Output"
}

output_forced_state = {
    0: "Off",
    1: "On",
    2: "Pulse 1 (pulsing mode 1)",
    3: "Pulse 2 (pulsing mode 2)",
    4: "Point With No Output"
}


## Decodes an MX6 Point Information Request packet.
def decode_pirmx5(data: dict):
    new_data = dict()

    # Reply status
    new_data[constants.PNAME_REPLY_STATUS] = reply_status[data[constants.PNAME_REPLY_STATUS]]

    # Flags
    new_data[constants.PNAME_FLAGS] = flags[data[constants.PNAME_FLAGS]]

    # Node
    new_data[constants.PNAME_NODE] = data[constants.PNAME_NODE]

    # Channel
    new_data[constants.PNAME_CHANNEL] = channel[data[constants.PNAME_CHANNEL]]

    # Channel address
    try:
        new_data[constants.PNAME_CHANNEL_ADDRESS] = channel_address[data[constants.PNAME_CHANNEL_ADDRESS]]
    except KeyError:
        new_data[constants.PNAME_CHANNEL_ADDRESS] = data[constants.PNAME_CHANNEL_ADDRESS]

    # Point category
    new_data[constants.PNAME_POINT_CATEGORY] = point_category[data[constants.PNAME_POINT_CATEGORY]]

    # Point number (physical)
    try:
        new_data[constants.PNAME_POINT_NUMBER] = channel_address[data[constants.PNAME_POINT_NUMBER]]
    except KeyError:
        new_data[constants.PNAME_POINT_NUMBER] = data[constants.PNAME_POINT_NUMBER]

    # Logical point number
    new_data[constants.PNAME_LOGICAL_POINT_NUMBER] = data[constants.PNAME_LOGICAL_POINT_NUMBER]

    # Logical point zone
    try:
        new_data[constants.PNAME_LOGICAL_POINT_ZONE] = logical_point_zone[data[constants.PNAME_LOGICAL_POINT_ZONE]]
    except KeyError:
        new_data[constants.PNAME_LOGICAL_POINT_ZONE] = data[constants.PNAME_LOGICAL_POINT_ZONE]

    # Device type
    new_data[constants.PNAME_DEVICE_TYPE] = devices_codes[data[constants.PNAME_DEVICE_TYPE]]

    # Auxiliary point attributes
    new_data[constants.PNAME_AUXILIARY_POINT_ATTRIBUTES] = data[constants.PNAME_AUXILIARY_POINT_ATTRIBUTES]

    # Group
    group1 = data[constants.PNAME_GROUP1]
    group2 = data[constants.PNAME_GROUP2]
    group = (group1 << 8) + group2

    new_data[constants.PNAME_GROUP] = group

    # Area type
    new_data[constants.PNAME_AREA_TYPE] = data[constants.PNAME_AREA_TYPE]

    # Area number
    new_data[constants.PNAME_AREA_NUMBER] = data[constants.PNAME_AREA_NUMBER]

    # Sector ID
    try:
        new_data[constants.PNAME_SECTOR_ID] = sector_id[data[constants.PNAME_SECTOR_ID]]
    except KeyError:
        new_data[constants.PNAME_SECTOR_ID] = data[constants.PNAME_SECTOR_ID]

    # Loop type
    new_data[constants.PNAME_LOOP_TYPE] = loop_type[data[constants.PNAME_LOOP_TYPE]]

    # Raw identity
    new_data[constants.PNAME_RAW_IDENTITY] = loop_type[data[constants.PNAME_RAW_IDENTITY]]

    # Actual device type
    new_data[constants.PNAME_ACTUAL_DEVICE_TYPE] = data[constants.PNAME_ACTUAL_DEVICE_TYPE]

    # Mode & sensitivity
    new_data[constants.PNAME_MODE_AND_SENSITIVITY] = data[constants.PNAME_MODE_AND_SENSITIVITY]

    # Raw analogue values
    new_data[constants.PNAME_RAW_ANALOGUE_VALUES1] = data[constants.PNAME_RAW_ANALOGUE_VALUES1]
    new_data[constants.PNAME_RAW_ANALOGUE_VALUES2] = data[constants.PNAME_RAW_ANALOGUE_VALUES2]
    new_data[constants.PNAME_RAW_ANALOGUE_VALUES3] = data[constants.PNAME_RAW_ANALOGUE_VALUES3]

    # LTA flags
    try:
        new_data[constants.PNAME_LTA_FLAGS] = lta_flags[data[constants.PNAME_LTA_FLAGS]]
    except KeyError:
        new_data[constants.PNAME_LTA_FLAGS] = data[constants.PNAME_LTA_FLAGS]

    # Raw LTA
    new_data[constants.PNAME_RAW_IDENTITY] = data[constants.PNAME_RAW_LTA]

    # Dirtiness
    new_data[constants.PNAME_DIRTINESS] = data[constants.PNAME_DIRTINESS]

    # Units of measurement
    new_data[constants.PNAME_UNITS_OF_MEASURE1] = unit_of_measurement[data[constants.PNAME_UNITS_OF_MEASURE1]]
    new_data[constants.PNAME_UNITS_OF_MEASURE2] = unit_of_measurement[data[constants.PNAME_UNITS_OF_MEASURE2]]
    new_data[constants.PNAME_UNITS_OF_MEASURE3] = unit_of_measurement[data[constants.PNAME_UNITS_OF_MEASURE3]]

    # Converted values
    new_data[constants.PNAME_CONVERTED_VALUES1] = data[constants.PNAME_CONVERTED_VALUES1]
    new_data[constants.PNAME_CONVERTED_VALUES2] = data[constants.PNAME_CONVERTED_VALUES2]
    new_data[constants.PNAME_CONVERTED_VALUES3] = data[constants.PNAME_CONVERTED_VALUES3]

    # Instantaneous states
    new_data[constants.PNAME_INSTANTANEOUS_ACTIVE_STATE] = instantaneous_active_state[
        data[constants.PNAME_INSTANTANEOUS_ACTIVE_STATE]]
    new_data[constants.PNAME_INSTANTANEOUS_FAULT_STATE] = data[constants.PNAME_INSTANTANEOUS_FAULT_STATE]

    # Confirmed states
    try:
        new_data[constants.PNAME_CONFIRMED_ACTIVE_STATE] = confirmed_active_state[
            data[constants.PNAME_CONFIRMED_ACTIVE_STATE]]
    except KeyError:
        new_data[constants.PNAME_CONFIRMED_ACTIVE_STATE] = data[constants.PNAME_CONFIRMED_ACTIVE_STATE]
        
    new_data[constants.PNAME_CONFIRMED_FAULT_STATE] = data[constants.PNAME_INSTANTANEOUS_FAULT_STATE]

    # Acknowledged states
    new_data[constants.PNAME_ACKNOWLEDGED_ACTIVE_STATE] = data[constants.PNAME_ACKNOWLEDGED_ACTIVE_STATE]
    new_data[constants.PNAME_ACKNOWLEDGED_FAULT_STATE] = data[constants.PNAME_ACKNOWLEDGED_FAULT_STATE]

    # Output forced mode
    new_data[constants.PNAME_OUTPUT_FORCED_MODE] = output_forced_mode[data[constants.PNAME_OUTPUT_FORCED_MODE]]

    # Output states
    new_data[constants.PNAME_OUTPUT_UNFORCED_STATE] = output_unforced_state[data[constants.PNAME_OUTPUT_UNFORCED_STATE]]
    new_data[constants.PNAME_OUTPUT_FORCED_STATE] = output_forced_state[data[constants.PNAME_OUTPUT_FORCED_STATE]]

    return new_data
