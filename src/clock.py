## @file clock.py
# @brief A simple Clock implementation, used to manage the timing of the control flow of the program.
# @author Guy Chamberlain-Webber

import time


class Clock:
    def __init__(self, start_true: bool = False):
        self.start_time = time.time()
        self.start_true = start_true

    ## Returns true if a number of elapsed 'seconds' have passed since the start
    # time.
    #
    # @return True if 'seconds' have passed since the start time, False if not.
    def time_elapsed(self, seconds: int) -> bool:
        if self.start_true:
            self.start_true = False
            return True

        current_time = time.time()
        elapsed_time = current_time - self.start_time

        if elapsed_time > seconds:
            # Reset the start time
            self.start_time = current_time
            return True

        return False
