## @file.py readable.py
# @brief Contains interface IReadable used to enforce reading functionality on an object.
# @author Guy Chamberlain-Webber

import abc


## An interface containing specific reading functions.
class IReadable(abc.ABC):
    ## Reads from a serial communications port.
    @abc.abstractmethod
    def read(self):
        pass
