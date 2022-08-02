## @file config.py
# @brief Contains utility functions for reading configuration information from the configuration file.
# @author Guy Chamberlain-Webber

import json
import enum

CONFIG_PATH = "config.json"

# The configuration dictionary
config = dict()


## An enum used to represents different version of the MX Speak specification.
class MXSpeakVersion(enum.Enum):
    MX_SPEAK5 = 0
    MX_SPEAK6 = 1


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


## Returns the path to the test start directory.
#
# @returns The path to the test start directory.
def get_test_start_directory() -> str:
    global config
    load_config()

    return config["testing"]["start-directory"]


## Returns MX Speak Signature.
#
# @return The MX Speak Signature for data packets.
def get_mx_signature() -> int:
    global config
    load_config()

    return config["packets"]["mx-speak-signature"]


## Returns the default packet header length of a protocol's local header.
#
# A packet length will be returned depending on the enum type passed into the function.
#
# @return The default packet header length.
def get_packet_length(mx_version: MXSpeakVersion) -> int:
    global config
    load_config()

    if mx_version is MXSpeakVersion.MX_SPEAK5:
        return config["packets"]["mx5-default-packet-length"]
    elif mx_version is MXSpeakVersion.MX_SPEAK6:
        return config["packets"]["mx6-default-packet-length"]

    raise AttributeError(f"No default packet length found for {mx_version}")
