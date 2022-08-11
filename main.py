## @file main.py
# @brief The main entry point for the program.
# @author Guy Chamberlain-Webber

from src.clock import Clock
from src.packet.packet_types import PanelDetailsRequestMX5


def run():
    should_run = True
    clock = Clock(start_true=True)

    while should_run:
        if clock.can_run_after(5):
            packet = PanelDetailsRequestMX5()
            packet.write()

            read_data = packet.read()
            if read_data:
                print(read_data)


if __name__ == "__main__":
    run()
