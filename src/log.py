## @file log.py
# @brief Contains logging utility functions.
# @author Guy Chamberlain-Webber

import os
import src.config as config


## Creates a directory to store log files.
#
# Looks for a directory named in the configuration files
# to store log files in. If it can't find this, it will
# create one.
def create_log_dir():
    log_path = config.get_log_dir()

    if os.path.exists(log_path):
        print("Logging to directory '{}'".format(log_path))
    else:
        print("Directory '{}' does not exist: creating...".format(log_path))
        os.mkdir(log_path)
