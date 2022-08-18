## @file main.py
# @brief The main entry point for the program.
# @author Guy Chamberlain-Webber

import src.config as config
import src.constants as constants

from src.clock import Clock
from src.packet.device_codes import devices_codes
from src.packet.packet_types import PointInformationRequestMX5


## The main program loop.
def run():
    # Get any existing points.
    points = find_valid_points()

    should_run = True
    time_period = config.get_time_period()
    clock = Clock(start_true=True)

    print("\n--- INFORMATION REQUESTS ---\n")

    while should_run:
        if clock.time_elapsed(time_period):
            for point in points:
                print(f"Requesting information for point {point}...")
                packet = PointInformationRequestMX5(point)
                packet.write()

                read_data = packet.read()
                if read_data.reply_successful():
                    print(devices_codes[read_data.get_parameter("pdevice_type")])

                print("\n")


## Looks through each of the points on the network and discovers those which actually exist. These are returned.
#
# @return A list of valid points in the network.
def find_valid_points() -> list:
    valid_points = []

    should_poll_points = True
    polling_time_period = config.get_polling_time_period()
    clock = Clock(start_true=True)

    current_point_number = 0

    print("--- POLLING ---\n")

    while should_poll_points:
        if clock.time_elapsed(polling_time_period):
            print(f"Polling point {current_point_number} for devices...")
            packet = PointInformationRequestMX5(current_point_number)
            packet.write()

            read_data = packet.read()
            if read_data.reply_successful():
                valid_points.append(current_point_number)

            current_point_number += 1

            if current_point_number > constants.MAXIMUM_POINT_NUMBER:
                should_poll_points = False

            print("\n")

    return valid_points


if __name__ == "__main__":
    run()
