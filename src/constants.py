## @file constants.py
# @brief Contains constants used throughout the program, and are modifiable if necessary.
# @author Guy Chamberlain-Webber

SOH = 0x01  # Start of frame
ACK = 0x06  # Acknowledge
SEQ_WRAP = 0x0f  # Number to wrap the SEQ
RESEND_TIME = 5  # Time to wait before resending a packet
