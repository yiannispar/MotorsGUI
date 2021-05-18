#
# piezoelectric motor code (Piezomotor company)
#
# author: I.Paraskevas
# created: Sept, 2020
#

import config
import serial.rs485
import commands
import utils
import protocol
import gui
import sys
import argparse

if __name__ == "__main__":

    print("-------------------------------------")
    print("    2-D Translation Stage Program    ")
    print("-------------------------------------")

    parser = argparse.ArgumentParser()
    parser.add_argument('-g','-gui', action='store_true',help="opens GUI")
    args = parser.parse_args()

    device = serial.rs485.RS485(config.port, baudrate=config.baudrate, bytesize=config.bytesize, stopbits=config.stopbits, parity=config.parity, timeout=config.timeout)
    device.rs485_mode = serial.rs485.RS485Settings(True,True)

    commands.init_both_motors(device)

    if args.g:
        gui.run_gui(device)
        device.close()
        sys.exit(0)
    
    print("Type a command or exit. Available commands:")
    utils.print_commands()

    while True:
        user_input = input("Tx: ")
        if user_input=="": continue

        args =  user_input.split()
        if args[0] == "exit": break
        commands.run_command(args,device)

    commands.park_both_motors(device)
    device.close()




        

