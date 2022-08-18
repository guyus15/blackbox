## @file writable.py
# @brief Contains interface IWritable used to enforce writing functionality on an object.
# @author Guy Chamberlain-Webber

import abc


## An interface containing specific writing functions.
class IWritable(abc.ABC):
    ## Writes to a serial communications port.
    @abc.abstractmethod
    def write(self):
        pass
