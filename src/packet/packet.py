## @file packet.py
# @brief Contains definition for the Packet class.
# @author Guy Chamberlain-Webber

from src.packet.byte_container import IByteContainer
from src.packet.headers import BaseHeader
from src.packet.content import Content


## Provides an abstraction of a data packet, which will be able to be transmitted to, and received
# from the panel.
class Packet(Content):
    def __init__(self, header: BaseHeader, content: Content):
        if not isinstance(header, BaseHeader):
            raise AttributeError(f"'{type(header)}' is not of expected type, BaseHeader.")
        if not isinstance(content, Content):
            raise AttributeError(f"'{type(header)}' is not of expected type, Content.")

        self._header = header
        self._content = content

        # Combine parameters of header and content together
        self._params = header.get_parameters()
        self._params.update(content.get_parameters())

    def get_byte_array(self) -> list:
        header_array = self._header.get_byte_array()
        content_array = self._content.get_byte_array()

        return header_array + content_array
