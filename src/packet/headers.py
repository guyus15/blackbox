## @file headers.py
# @brief Contains a collection of headers used for packet construction.
# @author Guy Chamberlain-Webber

import src.config as config
from src.config import MXSpeakVersion
from src.packet.content import Content
from src.exceptions.parameter_not_found import ParameterNotFoundException
from src.exceptions.invalid_value import InvalidValueException

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
    def __init__(self, packet_id: int, **kwargs):
        params = {
            "packet_length":                config.get_packet_length(MXSpeakVersion.MX_SPEAK5),
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

        # Override defaults if they have been provided.
        for attr in kwargs:
            if self.check_exists(attr):
                self._params[attr] = kwargs[attr]
            else:
                raise ParameterNotFoundException(f"Given parameter '{attr}' does not exist in header.")


## An MX Speak 6 Local Header, which is used when connected to the panel's COM2 serial port.
class LocalHeaderMX6(BaseHeader):
    def __init__(self, packet_id: int, **kwargs):
        params = {
            "packet_length":                config.get_packet_length(MXSpeakVersion.MX_SPEAK6),
            "mx_speak_signature":           config.get_mx_signature(),
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

        # Override defaults if they have been provided.
        for attr in kwargs:
            if attr == "mx_speak_signature":
                raise InvalidValueException(f"Invalid value '{attr}': Cannot modify MX Speak Signature value.")

            if self.check_exists(attr):
                self._params[attr] = kwargs[attr]
            else:
                raise ParameterNotFoundException(f"Given parameter '{attr}' does not exist in header.")
