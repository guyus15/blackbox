## @file main.py
# @brief The main entry point for the program.
# @author Guy Chamberlain-Webber

from src.clock import Clock
from src.packet.packet_types import PointInformationRequestMX5


def run():
    should_run = True
    clock = Clock(start_true=True)

    current_point_number = 0

    while should_run:
        if clock.time_elapsed(5):
            print(f"Requesting information for point {current_point_number}...")
            packet = PointInformationRequestMX5(current_point_number)
            packet.write()

            read_data = packet.read()
            if read_data:
                print(read_data)

            # Increment point number
            current_point_number += 1

            print("\n")


if __name__ == "__main__":
    run()
