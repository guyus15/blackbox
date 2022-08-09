## @file main.py
# @brief The main entry point for the program.
# @author Guy Chamberlain-Webber

from src.packet.packet_types import RestartPanelMX5


def run():
    # Creating and sending a panel restart packet.
    packet = RestartPanelMX5()
    packet.write()


if __name__ == "__main__":
    run()
    