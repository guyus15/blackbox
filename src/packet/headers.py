## @file headers.py
# @brief Contains a collection of headers used for packet construction.
# @author Guy Chamberlain-Webber

from src.packet.content import Content


## An MX Speak 5 Local Header, which is used when connected to the panel's COM2 serial port.
class LocalHeaderMX5(Content):
    def __init__(self, packet_id: int):
        params = {
            "packet_length":                0x09,
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
