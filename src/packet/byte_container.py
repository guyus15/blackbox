## @file byte_container.py
# @brief Contains interface IByteContainer used to enforce the presence specific byte-related functions
# inside a class.
# @author Guy Chamberlain-Webber

## An interface containing specific byte-related functions.
#
# Python does not officially support interfaces, so we use a NotImplemented
# exception to ensure that functions are defined elsewhere.
class IByteContainer:
    ## Gets an object as an array of bytes.
    #
    # @return The containing object as an array of bytes.
    def get_byte_array(self):
        raise NotImplementedError("@get_byte_array has not been implemented.")

    # Sets the parameter contained at 'key' to 'value'.
    def set_parameter(self, key, value):
        raise NotImplementedError("@set_parameter has not been implemented.")

    # Gets the parameter contained at 'key'
    #
    # @return The parameter contained at the specified key.
    def get_parameter(self, key):
        raise NotImplementedError("@get_parameter has not been implemented.")