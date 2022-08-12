## @file main.py
# @brief The main entry point for the program.
# @author Guy Chamberlain-Webber

from src.clock import Clock
from src.packet.packet_types import PointInformationRequestMX6


def run():
    should_run = True
    clock = Clock(start_true=True)

    while should_run:
        if clock.time_elapsed(5):
            packet = PointInformationRequestMX6()
            packet.write()

            read_data = packet.read()
            if read_data:
                print(read_data)


if __name__ == "__main__":
    run()
