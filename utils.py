#
# utils.py
#
# author: I.Paraskevas
# created: Sept, 2020
#

import serial

wfm_length = 0.0045 #mm
microsteps_in_wfm = 8192 #microsteps in one wfm
mm_per_count = 25.4/4000 

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
    print("\t\u2022 gp <address>: get position")
    print("\t\u2022 gpb : get positions of both motors")
    print("\t\u2022 go <address> <position> : move motor <address> to position <position>")

def mm_to_wfm(distance):
    return float(distance)/wfm_length

#mm/s to wfm/s
def convert_speed(speed):
    return str(round(mm_to_wfm(speed)))
    
def calculate_microsteps(wfm):
    return str(round(wfm * microsteps_in_wfm))

def convert_counts_to_mm(counts):
    return round(float(counts * mm_per_count),2)

def convert_mm_to_counts(mm):
    return float(mm * 1/mm_per_count)

def isRangeExceeded(posX,posY):
    isXwithinRange=True
    isYwithinRange=True
    if int(posX)>3000 or int(posX)<-3500:
        print("Position exceeded range: -3500 < motor 1 < 3000. Please enter a new value")
        isXwithinRange=False
    if int(posY)>3500 or int(posY)<-3000:
        print("Position exceeded range: -3000 < motor 2 < 3500. Please enter a new value")
        isYwithinRange=False

    if isXwithinRange and isYwithinRange:
        return False
    else: return True
