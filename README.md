# Piezoelectric motor code v1.0
This repository contains the code to control the motor. (piezomotor company)  
Author: Ioannis Paraskevas  
Last update: April,2021

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

How to run
----------
1) Power on the board and connect it to the PC using the USB cable
2) Open "config.py" and make sure you have the correct port
3) python3 main.py
4) OPTIONAL (recommended): python3 main -g (to open GUI)

Requirements:
1) python3
2) pySerial (https://pyserial.readthedocs.io/en/latest/pyserial.html)
3) TKinter