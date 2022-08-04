## @file packet.py
# @brief Contains definition for the Packet class.
# @author Guy Chamberlain-Webber

from src.packet.byte_container import IByteContainer
from src.packet.headers import BaseHeader
from src.packet.content import Content


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
