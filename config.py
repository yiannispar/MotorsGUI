#
# config.py
# 
# author: I.Paraskevas
# created: Sept, 2020
#

import serial

port = "/dev/ttyS3"
baudrate = 115200
bytesize = serial.EIGHTBITS
stopbits = serial.STOPBITS_ONE
parity = serial.PARITY_NONE
timeout=2

x_home_pos=0
y_home_pos=2500
