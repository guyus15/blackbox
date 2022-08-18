## @file loggable.py
# @brief Contains interface ILoggable used to enforce logging functionality on an object.
# @author Guy Chamberlain-Webber

import abc


## An interface used containing specific logging functions.
class ILoggable(abc.ABC):
    ## Returns an object as a series of comma-separated-values.
    @abc.abstractmethod
    def get_as_csv(self):
        pass
