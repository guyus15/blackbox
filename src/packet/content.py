## @file content.py
# @brief An abstraction of the contents of a packet.
# @author Guy Chamberlain-Webber

## A class specifying a packet contents object, which contains relevant functions
# to load a packet with data.
class Content:
    def __init__(self, **kwargs):
        self._params = dict()

        # Loads given attributes into _params.
        for attr in kwargs:
            self._params[attr] = kwargs[attr]

    ## Returns the content object as a string.
    #
    # @return The string representation of the content object.
    def __str__(self):
        string = "Packet contents:\n"

        for attr in self._params:
            string += "{}: {}\n".format(attr, self._params[attr])

        return string
