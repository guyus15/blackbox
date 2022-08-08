## @file content.py
# @brief An abstraction of the contents of a packet.
# @author Guy Chamberlain-Webber

from src.packet.byte_container import IByteContainer


## A class specifying a packet contents object, which contains relevant functions
# to load a packet with data.
class Content(IByteContainer):
    def __init__(self, **kwargs):
        self._params = dict()

        # Loads given attributes into _params.
        for attr in kwargs:
            self._params[attr] = kwargs[attr]

    ## Checks whether 'key' exists in the content parameters.
    #
    # @return True if 'key' exists, False if it doesn't.
    def check_exists(self, key: str) -> bool:
        for attr in self._params:
            if attr == key:
                return True

        return False

    ## Gets an object as an array of bytes.
    #
    # @return The containing object as an array of bytes.
    def get_byte_array(self) -> list:
        byte_array = []

        for attr in self._params.values():
            if type(attr) == int:
                byte_array.append(attr)
            elif type(attr) == str:
                for char in attr:
                    char_to_byte = bytes(char, encoding='utf-8')
                    byte_to_int = int.from_bytes(char_to_byte, 'little')
                    byte_array.append(byte_to_int)

        return byte_array

    ## Sets the parameter contained at 'key' to 'value'.
    def set_parameter(self, key: str, value):
        if not self.check_exists(key):
            raise AttributeError(f"'{key}' can not be found in content parameters.")

        self._params[key] = value

    ## Gets the parameter contained at 'key'.
    #
    # @return The parameter contained at the specified key.
    def get_parameter(self, key: str):
        if not self.check_exists(key):
            raise AttributeError(f"'{key}' can not be found in content parameters.")

        return self._params[key]

    ## Gets all the content parameters
    #
    # @return The parameters of the content object.
    def get_parameters(self) -> dict:
        return self._params

    ## Returns the content object as a string.
    #
    # @return The string representation of the content object.
    def __str__(self) -> str:
        string = "Packet contents:\n"

        for attr in self._params:
            string += "{}: {}\n".format(attr, self._params[attr])

        return string
