## @file headers.py
# @brief Contains a collection of headers used for packet construction.
# @author Guy Chamberlain-Webber

from src.packet.content import Content


## Base header class.
class BaseHeader(Content):
    ## Gets an object as an array of bytes.
    #
    # @return The containing object as an array of bytes.
    def get_byte_array(self) -> list:
        data = list()

        for param in self._params.keys():
            data.append(self.get_parameter(param))

        return data


## An MX Speak 5 Local Header, which is used when connected to the panel's COM2 serial port.
class LocalHeaderMX5(BaseHeader):
    def __init__(self, packet_id: int):
        params = {
            "packet_length":                0x09,  # Default length
            "network_node":                 0x00,
            "channel":                      0x00,
            "destination_channel_address":  0x00,
            "destination_task":             0x00,
            "source_channel_address":       0x00,
            "source_task":                  0x00,
            "marker":                       0x00,
            "packet_id":                    packet_id
        }

        super().__init__(**params)


## An MX Speak 6 Local Header, which is used when connected to the panel's COM2 serial port.
class LocalHeaderMX6(BaseHeader):
    def __init__(self, packet_id: int):
        params = {
            "packet_length":                0x0b,  # Default length (11)
            "mx_speak_signature":           0xe4,  # (228)
            "network_node":                 0x00,
            "channel":                      0x00,
            "destination_channel_address":  0x00,
            "destination_task":             0x00,
            "source_channel_address":       0x00,
            "source_task":                  0x00,
            "marker":                       0x00,
            "packet_id":                    packet_id,
            "reserved":                     0x00
        }

        super().__init__(**params)