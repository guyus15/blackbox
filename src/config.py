## @file config.py
# @brief Contains utility functions for reading configuration information from the configuration file.
# @author Guy Chamberlain-Webber

import json

CONFIG_PATH = "config.json"

# The configuration dictionary
config = dict()


## Loads the configuration contained within the configuration file.
#
# Looks for a directory named in the configuration files
# to store log files in. If it can't find this, it will
# create one.
def load_config():
    global config

    # Don't bother loading configuration if it is already loaded.
    if len(config.keys()) > 0:
        return

    with open(CONFIG_PATH) as fd:
        contents = fd.read()
        config = json.loads(contents)


## Returns logging enabled.
#
# This function returns true if the 'enabled' variable is set to true
# in the configuration file. Otherwise, it will return false.
#
# @return True if logging is enabled, False if it is not.
def get_log_enabled() -> bool:
    global config
    load_config()

    return config["logging"]["enabled"]


## Returns the path to the log directory.
#
# @return The path to the log directory.
def get_log_dir() -> str:
    global config
    load_config()

    return config["logging"]["directory"]
