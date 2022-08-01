## @file log.py
# @brief Contains logging utility functions.
# @author Guy Chamberlain-Webber

import os
import sys
import time
import src.config as config


## An exception raised when a platform type is not supported.
class UnsupportedPlatformException (Exception):
    pass


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


## Writes to a log entry within the log directory.
#
# This function determines whether to log on Windows or RPi, then will call
# the correct write log function, after pre-pending time and date to the
# log entry.
#
# @param entry The log entry.
# @param logfile The log file.
def write_log(entry: str, logfile: str):
    if not config.get_log_enabled():
        return

    current_time = time.strftime("%d/%m/%Y @ %H:%M:%S", time.gmtime())
    entry = "{} - {}\n".format(current_time, entry)

    plat = sys.platform

    if plat == "win32":
        # Log on Windows
        write_log_windows(entry, logfile);
    elif plat == "linux":
        # Log on Linux
        write_log_linux(entry, logfile);
    else:
        # Unsupported platform
        raise UnsupportedPlatformException("The blackbox does not support platforms of type '{}'.".format(plat))


## Writes to a log entry within the log directory on Windows.
#
# @param entry The log entry.
# @param logfile The log file.
def write_log_windows(entry: str, logfile: str):
    log_path = config.get_log_dir() + '/' + logfile

    with open(log_path, 'a') as fd:
        fd.write(entry)


## Writes to a log entry within the log directory on Linux.
#
# @param entry The log entry.
# @param logfile The log file.
def write_log_linux(entry: str, logfile: str):
    log_path = config.get_log_dir() + '/' + logfile

    with open(log_path, 'a') as fd:
        fd.write(entry)

    """
    TODO: Do a check here to see if the user has a USB connected. If so, write the logs
    there instead.
    
    TODO: Look at status LEDs, these can be configured to show progress of log entry writing.
    """
