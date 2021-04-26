#
# commands.py
#
# author: I.Paraskevas
# created: Sept, 2020
#

import protocol
import serial.rs485
import math
import utils
import time

motor1_home_position=0
motor2_home_position=0

def move_motor(address,distance,device):
    print("Moving motor ", address,", ", distance, " mm")
    abs_distance = abs(float(distance))
    distance_wfm = utils.mm_to_wfm(abs_distance)
    round_down_wfm = math.floor(distance_wfm)
    remainder = distance_wfm - round_down_wfm
    microsteps = utils.calculate_microsteps(remainder)
    if float(distance) < 0: round_down_wfm = -round_down_wfm
    command = "X" + str(address) + protocol.jog + str(round_down_wfm) + "," + microsteps + protocol.CR
    device.write(command.encode())
    print("Rx:", device.readline().decode())
    
def park_both_motors(device):
    print("Parking both motors")
    park_motor(1,device)
    park_motor(2,device)

def unpark_both_motors(device):
    print("Unparking both motors")
    unpark_motor(1,device)
    unpark_motor(2,device)

#unpark and set an initial speed (1 mm/s)    
def init_both_motors(device):
    unpark_both_motors(device)
    speed = 1 #mm/s
    set_speed_both_motors(speed,device)
    reverse_encoder_axis(2,device) #reverse axis for motor 2 (necessary)

def set_speed(address,speed,device):
    print("Setting speed of ", speed, " mm/s to motor ", address)
    command = "X" + str(address) + protocol.speed + utils.convert_speed(speed) + protocol.CR
    device.write(command.encode())
    print("Rx:", device.readline().decode())

def park_motor(address,device):
    print("Parking motor ", address)
    command = "X" + str(address) + protocol.park + protocol.CR
    device.write(command.encode())
    print("Rx:", device.readline().decode())
    
def unpark_motor(address,device):
    print("Unparking motor ", address)
    command = "X" + str(address) + protocol.unpark + protocol.CR
    device.write(command.encode())
    print("Rx:", device.readline().decode())

def move_both_motors(distance,device):
    print("Moving both motors ", distance, " mm")
    move_motor(1,distance,device)
    move_motor(2,distance,device)

def set_speed_both_motors(speed,device):
    print("Setting speed of ", speed, " mm/s to both motors")
    set_speed(1,speed,device)
    set_speed(2,speed,device)

def stop_motor(address,device):
    print("Stopping motor ", address)
    command = "X" + str(address) + protocol.stop + protocol.CR
    device.write(command.encode())
    print("Rx:", device.readline().decode())

def stop_both_motors(device):
    print("Stopping both motors")
    stop_motor(1,device)
    stop_motor(2,device)

def get_position(address,device):
    print("Getting position of motor ", address)
    command = "X" + str(address) + protocol.get_position + protocol.CR
    device.write(command.encode())
    print("Rx:", device.readline().decode())

def get_position_both_motors(device):
    print("Getting positions of both motors")
    get_position(1,device)
    get_position(2,device)

def move_motor_to_position(position_x,position_y,device):
    if int(position_y)<-6500 or int(position_y)>500:
        print("Position exceeded range: -6500 < motor 2 < 500. Please enter a new value")
        return
    if int(position_x)>4500 or int(position_x)<-2000:
        print("Position exceeded range: -2000 < motor 1 < 4500. Please enter a new value")
        return
    print("Moving motors to absolute position ", position_x,",",position_y )
    command = "X" + str(1) + protocol.go_to_position + position_x + protocol.CR
    device.write(command.encode())
    print("Rx:", device.readline().decode())
    command = "X" + str(2) + protocol.go_to_position + position_y + protocol.CR
    device.write(command.encode())
    print("Rx:", device.readline().decode())
                                 
def reverse_encoder_axis(address,device):
    print("Reversing encoder axis for motor ", address)
    command = "X" + str(address) + "Y6,1" + protocol.CR
    device.write(command.encode())
    print("Rx:", device.readline().decode())

def return_motor_position(address,device):
    command = "X" + str(address) + protocol.get_position + protocol.CR
    device.write(command.encode())
    return device.readline().decode()[4:]

def set_current_position_as_home(device):
    print("Setting current position as home")
    global motor1_home_position
    global motor2_home_position
    motor1_home_position=return_motor_position(1,device)
    motor2_home_position=return_motor_position(2,device)
    print("Home position set")
    print("Motor 1 = ",motor1_home_position)
    print("Motor 2 = ",motor2_home_position)
    
def go_to_home_position(device):
    print("Moving motors to home positon")
    motor1_home_pos=motor1_home_position[:-1]
    motor2_home_pos=motor2_home_position[:-1]
    move_motor_to_position(str(motor1_home_pos),str(motor2_home_pos),device)

def get_relative_position(device):
    print("Getting relative position")
    posX=int(return_motor_position(1,device))-int(motor1_home_position)
    posY=int(return_motor_position(2,device))-int(motor2_home_position)
    print("Motor 1 relative position = ",posX)
    print("Motor 2 relative position = ",posY)

def go_to_relative_position(position_x,position_y,device):
    print("Moving motors to relative positon x,y ", position_x, ",",position_y)
    rel_pos1=int(motor1_home_position)+int(position_x)
    rel_pos2=int(motor2_home_position)+int(position_y)
    move_motor_to_position(str(rel_pos1),str(rel_pos2),device)

def scan(device):
    print("Scanning in progress")
    for pos in range(-1000,1200,500):
        go_to_relative_position(pos,0,device)
        time.sleep(10)
    for pos in range(-1000,1200,500):
        go_to_relative_position(0,pos,device)
        time.sleep(10)
    print("Scan completed!")

def run_command(args,device):
    command = args[0]
    if command =="mv":
        if len(args) != 3: return
        move_motor(args[1], args[2],device)
    elif command =="mvb":
        if len(args) != 2: return
        move_both_motors(args[1],device)
    elif command =="ss":
        if len(args) != 3: return
        set_speed(args[1], args[2],device)
    elif command =="ssb":
        if len(args) != 2: return
        set_speed_both_motors(args[1],device)
    elif command =="p":
        if len(args) != 2: return
        park_motor(args[1],device)
    elif command =="pb":
        if len(args) !=1: return
        park_both_motors(device)
    elif command =="up":
        if len(args) != 2: return
        unpark_motor(args[1],device)
    elif command =="upb":
        if len(args) !=1: return
        unpark_both_motors(device)
    elif command =="st":
        if len(args) !=2: return
        stop_motor(args[1],device)
    elif command =="stb":
        if len(args) !=1: return
        stop_both_motors(device)
    elif command =="gp":
        if len(args) != 2: return
        get_position(args[1],device)
    elif command =="gpb":
        if len(args) !=1: return
        get_position_both_motors(device)
    elif command =="go":
        if len(args) != 3: return
        move_motor_to_position(args[1], args[2],device)
    else:
        command = command + protocol.CR
        device.write(command.encode())
        print("Rx:", device.readline().decode())


