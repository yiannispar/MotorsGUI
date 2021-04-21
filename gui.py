#
# piezoelectric motor gui
# 
# author: I.Paraskevas
# date: Feb, 2021
#

import tkinter as tk
import commands
from tkinter import messagebox
import time
import tkinter.font as font
	
def exit_gui(device,window):
    commands.park_both_motors(device)
    window.destroy()

def run_gui(device):
    window = tk.Tk()
    window.title("Piezoelectric motor")
    window.geometry("700x750")
    tk.Label(text="Piezoelectric motor program", fg="white", bg="blue", font=("Arial", 25)).pack(pady=25) 

    #----------------buttons-------------------------#
    button_size=font.Font(size=15)

    b_park_motor_1  = tk.Button(window, text = 'Park motor 1', command = lambda: commands.park_motor(1,device))
    b_park_motor_1['font'] = button_size
    b_park_motor_1.place(x=20, y=100)

    b_park_motor_2  = tk.Button(window, text = 'Park motor 2', command = lambda: commands.park_motor(2,device))
    b_park_motor_2['font'] = button_size
    b_park_motor_2.place(x=170, y=100)
    
    b_park_both_motors = tk.Button(window, text = 'Park both motors', command = lambda: commands.park_both_motors(device))
    b_park_both_motors['font'] = button_size
    b_park_both_motors.place(x=320, y=100)

    b_unpark_motor_1  = tk.Button(window, text = 'Unpark motor 1', command = lambda: commands.unpark_motor(1,device))
    b_unpark_motor_1['font'] = button_size
    b_unpark_motor_1.place(x=20, y=150)

    b_unpark_motor_2  = tk.Button(window, text = 'Unpark motor 2', command = lambda: commands.unpark_motor(2,device))
    b_unpark_motor_2['font'] = button_size
    b_unpark_motor_2.place(x=170, y=150)
        
    b_unpark_both_motors = tk.Button(window, text = 'Unpark both motors', command = lambda: commands.unpark_both_motors(device))
    b_unpark_both_motors['font'] = button_size
    b_unpark_both_motors.place(x=320, y=150)

    label_distance = tk.Label(text="Distance to move motor(s) [mm] :")
    label_distance['font'] = button_size
    label_distance.place(x=20,y=200)
    entry = tk.Entry()
    entry['font'] = button_size
    entry.place(x=300, y=200)

    b_move_motor_1 = tk.Button(window, text = 'Move motor 1', command = lambda: commands.move_motor(1,entry.get(),device))
    b_move_motor_1['font'] = button_size
    b_move_motor_1.place(x=20, y=230)

    b_move_motor_2 = tk.Button(window, text = 'Move motor 2', command = lambda: commands.move_motor(2,entry.get(),device))
    b_move_motor_2['font'] = button_size
    b_move_motor_2.place(x=170, y=230)

    b_move_both_motors = tk.Button(window, text = 'Move both motors', command = lambda: commands.move_both_motors(entry.get(),device))
    b_move_both_motors['font'] = button_size
    b_move_both_motors.place(x=320, y=230)

    label_speed = tk.Label(text="Set speed to motor(s) [mm/s]:")
    label_speed['font'] = button_size
    label_speed.place(x=20,y=280)
    entry_speed = tk.Entry()
    entry_speed['font'] = button_size
    entry_speed.place(x=270, y=280)

    b_set_speed_motor_1 = tk.Button(window, text = 'Set speed to motor 1', command = lambda: commands.set_speed(1,entry_speed.get(),device))
    b_set_speed_motor_1['font'] = button_size
    b_set_speed_motor_1.place(x=20, y=310)

    b_set_speed_motor_2 = tk.Button(window, text = 'Set speed to motor 2', command = lambda: commands.set_speed(2,entry_speed.get(),device))
    b_set_speed_motor_2['font'] = button_size
    b_set_speed_motor_2.place(x=230, y=310)
    
    b_set_speed_both_motors  = tk.Button(window, text = 'Set speed to both motors', command = lambda: commands.set_speed_both_motors(entry_speed.get(),device))
    b_set_speed_both_motors['font'] = button_size
    b_set_speed_both_motors.place(x=440, y=310)

    label_send_command = tk.Label(text="Send command:")
    label_send_command['font'] = button_size
    label_send_command.place(x=20,y=360)
    entry_send_command = tk.Entry()
    entry_send_command['font'] = button_size
    entry_send_command.place(x=160, y=360)

    b_send_command  = tk.Button(window, text = 'Send command', command = lambda: commands.run_command(entry_send_command.get().split(),device))
    b_send_command['font'] = button_size
    b_send_command.place(x=380, y=360)

    b_get_position_1  = tk.Button(window, text = 'Get position of\n motor 1', command = lambda: commands.get_position(1,device))
    b_get_position_1['font'] = button_size
    b_get_position_1.place(x=20, y=410)

    b_get_position_2  = tk.Button(window, text = 'Get position of\n motor 2', command = lambda: commands.get_position(2,device))
    b_get_position_2['font'] = button_size
    b_get_position_2.place(x=180, y=410)

    b_get_position_both_motors  = tk.Button(window, text = 'Get position of\n both motors', command = lambda: commands.get_position_both_motors(device))
    b_get_position_both_motors['font'] = button_size
    b_get_position_both_motors.place(x=340, y=410)

    b_stop_motor_1  = tk.Button(window, text = 'Stop motor 1', command = lambda: commands.stop_motor(1,device),fg='red')
    stop_motor_button_font=font.Font(size=15,weight="bold")
    b_stop_motor_1['font'] = stop_motor_button_font
    b_stop_motor_1.place(x=20, y=480)

    b_stop_motor_2  = tk.Button(window, text = 'Stop motor 2', command = lambda: commands.stop_motor(2,device),fg='red')
    b_stop_motor_2['font'] = stop_motor_button_font
    b_stop_motor_2.place(x=180, y=480)

    b_stop_both_motors  = tk.Button(window, text = 'Stop both motors', command = lambda: commands.stop_both_motors(device),fg='red')
    b_stop_both_motors['font'] = stop_motor_button_font
    b_stop_both_motors.place(x=340, y=480)

    label_go_to_position = tk.Label(text="Move motor(s) to position :")
    label_go_to_position['font'] = button_size
    label_go_to_position.place(x=20,y=540)
    entry_go_to_position = tk.Entry()
    entry_go_to_position['font'] = button_size
    entry_go_to_position.place(x=250, y=540)

    b_move_motor_1_to_position  = tk.Button(window, text = 'Move motor 1\nto position', command = lambda: commands.move_motor_to_position(1,entry_go_to_position.get(),device))
    b_move_motor_1_to_position['font'] = button_size
    b_move_motor_1_to_position.place(x=20, y=580)

    b_move_motor_2_to_position  = tk.Button(window, text = 'Move motor 2\nto position', command = lambda: commands.move_motor_to_position(2,entry_go_to_position.get(),device))
    b_move_motor_2_to_position['font'] = button_size
    b_move_motor_2_to_position.place(x=180, y=580)

    b_set_current_position_as_home  = tk.Button(window, text = 'Set current\n position as home', command = lambda: commands.set_current_position_as_home(device))
    b_set_current_position_as_home['font'] = button_size
    b_set_current_position_as_home.place(x=20, y=660)

    b_go_to_home_position  = tk.Button(window, text = 'Go to home\nposition', command = lambda: commands.go_to_home_position(device))
    b_go_to_home_position['font'] = button_size
    b_go_to_home_position.place(x=200, y=660)

    b_get_relative_position  = tk.Button(window, text = 'Get relative\nposition', command = lambda: commands.get_relative_position(device))
    b_get_relative_position['font'] = button_size
    b_get_relative_position.place(x=340, y=660)

    b_exit_gui = tk.Button(window, text="Exit", command= lambda: exit_gui(device,window),bg='red')
    exit_button_font=font.Font(size=25,weight="bold")
    b_exit_gui['font'] = exit_button_font
    b_exit_gui.place(x=580, y=660)
    #------------------------------------------------#
    
    window.mainloop()

