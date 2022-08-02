## @file byte_container.py
# @brief Contains interface IByteContainer used to enforce the presence specific byte-related functions
# inside a class.
# @author Guy Chamberlain-Webber

import abc


## An interface containing specific byte-related functions.
#
# Python does not officially support interfaces, so we use a NotImplemented
# exception to ensure that functions are defined elsewhere.
class IByteContainer(abc.ABC):
    ## Gets an object as an array of bytes.
    #
    # @return The containing object as an array of bytes.
    @abc.abstractmethod
    def get_byte_array(self):
        pass

    # Sets the parameter contained at 'key' to 'value'.
    @abc.abstractmethod
    def set_parameter(self, key, value):
        pass

    # Gets the parameter contained at 'key'
    #
    # @return The parameter contained at the specified key.
    @abc.abstractmethod
    def get_parameter(self, key):
        pass
    