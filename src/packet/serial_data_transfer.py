## @file.py serial_data_transfer.py
# @brief Responsible for writing and reading data across a serial data transfer and
# setting up pyserial.
# @author Guy Chamberlain-Webber

import serial

import src.config as config
from src.clock import Clock
from src.packet.packet import ACK

RESEND_TIME = 5  # 5 seconds


class SerialDataTransfer:
    def __init__(self):
        self.serial = serial.Serial(port=config.get_com_port(),
                                    baudrate=config.get_baudrate(),
                                    timeout=config.get_timeout(),
                                    bytesize=config.get_bytesize(),
                                    parity=config.get_parity(),
                                    stopbits=config.get_stopbits()
                                    )

    def __del__(self):
        self.serial.close()

    ## Writes data across a serial communication port.
    def write(self, data: list):
        self.serial.write(data)

    ## Writes a single byte of data across a serial communication port.
    def write_byte(self, value):
        data = [value]

        self.serial.write(data)

    ## Reads data from a serial communication port.
    #
    # @return The data (if any) read from the serial communication port.
    def read(self, size: int):
        clock = Clock()

        ack_acquired = False

        # Reads the ACK, so it does not appear in final data.
        while not ack_acquired:
            data = self.serial.read(size=1)
            if int.from_bytes(data, "little") == ACK:
                ack_acquired = True

        while True:
            # If we have not received any data after a set time, don't bother trying to read,
            # we'll send another packet.
            if clock.time_elapsed(RESEND_TIME):
                print("No response from sent packet, moving on to next...")
                break

            response = self.serial.read(size=size)

            if len(response) == size:
                return response

        return None
