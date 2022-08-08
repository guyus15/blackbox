## @file packet.py
# @brief Contains definition for the Packet class.
# @author Guy Chamberlain-Webber

from src.packet.headers import BaseHeader
from src.packet.content import Content

soh = 0x01
seq = 0x01


## Provides an abstraction of a data packet, which will be able to be transmitted to, and received
# from the panel.
class Packet(Content):
    def __init__(self, header: BaseHeader, **kwargs):
        super().__init__(**kwargs)
        if not isinstance(header, BaseHeader):
            raise AttributeError(f"'{type(header)}' is not of expected type, BaseHeader.")

        self._header = header

        # Combine parameters of header and kwargs together
        _params_copy = self._params
        self._params = header.get_parameters()
        self._params.update(_params_copy)

    ## Gets an object as an array of bytes.
    #
    # The packet will provide SOH and SEQ numbers to the byte array, as well
    # as a checksum at the end based on all previous bytes.
    #
    # @return The containing object as an array of bytes.
    def get_byte_array(self) -> list:
        default_array = super().get_byte_array()

        checksum = 0
        for byte in default_array:
            checksum += byte

        # Modulus operation to ensure checksum can be contained within one byte.
        checksum %= 255

        default_array.insert(0, soh)
        default_array.insert(1, seq)
        default_array.append(checksum)

        return default_array
