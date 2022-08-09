## @file.py serial_data_transfer.py
# @brief Responsible for writing and reading data across a serial data transfer and
# setting up pyserial.
# @author Guy Chamberlain-Webber

import serial
import src.config as config


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
