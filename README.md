# Piezoelectric motor code v1.0
This repository contains the code that controls the motors on the 2-D translation stage. (piezomotor company)  
Author: Ioannis Paraskevas <ioannis.paraskevas.13@ucl.ac.uk>  
Last update: May,2021

main.py 
--------
main code

command.py
----------
user defined commands

protocol.py
-----------
communication protocol from manual

utils.py
-------
useful functions

config.py
--------
configuration file

gui.py
------
GUI interface

How to run on Linux (tested on Windows 10 Subsystem for Linux)
----------
1) Power on the board and connect it to the PC using the USB cable
2) Open "config.py" and make sure you have the correct port
3) python3 main.py  
*Optional (recommended): python3 main -g (to open GUI)

Requirements:
1) python3
2) pySerial (https://pyserial.readthedocs.io/en/latest/pyserial.html)
3) TKinter (for GUI)

How to run on Windows (tested on Windows 10)
---------------------
Open config.py and change port name "dev/ttyS#" to "COM#" (# represents the port number)  
Note: The GUI might appear differently
