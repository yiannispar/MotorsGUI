#
# utils.py
#
# author: I.Paraskevas
# created: Sept, 2020
#

import serial

wfm_length = 0.0045 #mm
microsteps_in_wfm = 8192 #microsteps in one wfm

def print_commands():
    print("\t\u2022 mv <address> <distance [mm]>: move motor")
    print("\t\u2022 mvb <distance [mm]>: move both motors")
    print("\t\u2022 ss <address> <speed [mm/s]>: set speed")
    print("\t\u2022 ssb <speed [mm/s]>: set speed to both motors")
    print("\t\u2022 p <address>: park motor")
    print("\t\u2022 pb : park both motors")
    print("\t\u2022 up <address> : unpark motor")
    print("\t\u2022 upb : unpark both motors")
    print("\t\u2022 st <address> : stop motor")
    print("\t\u2022 stb : stop both motors")

def mm_to_wfm(distance):
    return float(distance)/wfm_length

#mm/s to wfm/s
def convert_speed(speed):
    return str(round(mm_to_wfm(speed)))
    
def calculate_microsteps(wfm):
    return str(round(wfm * microsteps_in_wfm))
