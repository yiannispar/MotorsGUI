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
    window.title("2-D Translation Stage")
    window.geometry("700x800")
    tk.Label(text="2-D Translation Stage", fg="white", bg="blue", font=("Arial", 25)).pack(pady=25) 

    #----------------buttons-------------------------#
    button_size=font.Font(size=15)

    #b_park_motor_1  = tk.Button(window, text = 'Park motor 1', command = lambda: commands.park_motor(1,device))
    #b_park_motor_1['font'] = button_size
    #b_park_motor_1.place(x=20, y=100)

    #b_park_motor_2  = tk.Button(window, text = 'Park motor 2', command = lambda: commands.park_motor(2,device))
    #b_park_motor_2['font'] = button_size
    #b_park_motor_2.place(x=170, y=100)
    
    b_park_both_motors = tk.Button(window, text = 'Park motors', command = lambda: commands.park_both_motors(device))
    b_park_both_motors['font'] = button_size
    b_park_both_motors.place(x=20, y=100)

    #b_unpark_motor_1  = tk.Button(window, text = 'Unpark motor 1', command = lambda: commands.unpark_motor(1,device))
    #b_unpark_motor_1['font'] = button_size
    #b_unpark_motor_1.place(x=20, y=150)

    #b_unpark_motor_2  = tk.Button(window, text = 'Unpark motor 2', command = lambda: commands.unpark_motor(2,device))
    #b_unpark_motor_2['font'] = button_size
    #b_unpark_motor_2.place(x=170, y=150)
        
    b_unpark_both_motors = tk.Button(window, text = 'Unpark  motors', command = lambda: commands.unpark_both_motors(device))
    b_unpark_both_motors['font'] = button_size
    b_unpark_both_motors.place(x=170, y=100)

    label_distance = tk.Label(text="Distance to move motor(s) [mm] :")
    label_distance['font'] = button_size
    label_distance.place(x=20,y=150)
    entry = tk.Entry(width=5)
    entry['font'] = button_size
    entry.place(x=300, y=150)

    b_move_motor_1 = tk.Button(window, text = 'Move x-axis', command = lambda: commands.move_motor(1,entry.get(),device))
    b_move_motor_1['font'] = button_size
    b_move_motor_1.place(x=20, y=190)

    b_move_motor_2 = tk.Button(window, text = 'Move y-axis', command = lambda: commands.move_motor(2,entry.get(),device))
    b_move_motor_2['font'] = button_size
    b_move_motor_2.place(x=170, y=190)

    b_move_both_motors = tk.Button(window, text = 'Move both axes', command = lambda: commands.move_both_motors(entry.get(),device))
    b_move_both_motors['font'] = button_size
    b_move_both_motors.place(x=320, y=190)

    label_speed = tk.Label(text="Set speed to motor(s) [mm/s]:")
    label_speed['font'] = button_size
    label_speed.place(x=20,y=280)
    entry_speed = tk.Entry(width=5)
    entry_speed['font'] = button_size
    entry_speed.place(x=270, y=280)

    b_set_speed_motor_1 = tk.Button(window, text = 'Set speed to x-axis', command = lambda: commands.set_speed(1,entry_speed.get(),device))
    b_set_speed_motor_1['font'] = button_size
    b_set_speed_motor_1.place(x=20, y=310)

    b_set_speed_motor_2 = tk.Button(window, text = 'Set speed to y-axis', command = lambda: commands.set_speed(2,entry_speed.get(),device))
    b_set_speed_motor_2['font'] = button_size
    b_set_speed_motor_2.place(x=230, y=310)
    
    b_set_speed_both_motors  = tk.Button(window, text = 'Set speed to both axes', command = lambda: commands.set_speed_both_motors(entry_speed.get(),device))
    b_set_speed_both_motors['font'] = button_size
    b_set_speed_both_motors.place(x=440, y=310)

    label_send_command = tk.Label(text="Command:")
    label_send_command['font'] = button_size
    label_send_command.place(x=20,y=360)
    entry_send_command = tk.Entry()
    entry_send_command['font'] = button_size
    entry_send_command.place(x=120, y=360)

    b_send_command  = tk.Button(window, text = 'Send', command = lambda: commands.run_command(entry_send_command.get().split(),device))
    b_send_command['font'] = button_size
    b_send_command.place(x=350, y=360)

    #b_get_position_1  = tk.Button(window, text = 'Get position of\n motor 1', command = lambda: commands.get_position(1,device))
    #b_get_position_1['font'] = button_size
    #b_get_position_1.place(x=20, y=410)

    #b_get_position_2  = tk.Button(window, text = 'Get position of\n motor 2', command = lambda: commands.get_position(2,device))
    #b_get_position_2['font'] = button_size
    #b_get_position_2.place(x=180, y=410)


    b_stop_motor_1  = tk.Button(window, text = 'Stop x-axis', command = lambda: commands.stop_motor(1,device),fg='red')
    stop_motor_button_font=font.Font(size=15,weight="bold")
    b_stop_motor_1['font'] = stop_motor_button_font
    b_stop_motor_1.place(x=20, y=420)

    b_stop_motor_2  = tk.Button(window, text = 'Stop y-axis', command = lambda: commands.stop_motor(2,device),fg='red')
    b_stop_motor_2['font'] = stop_motor_button_font
    b_stop_motor_2.place(x=180, y=420)

    b_stop_both_motors  = tk.Button(window, text = 'Stop both axes', command = lambda: commands.stop_both_motors(device),fg='red')
    b_stop_both_motors['font'] = stop_motor_button_font
    b_stop_both_motors.place(x=340, y=420)

    label_go_to_position = tk.Label(text="Move to ABSOLUTE position (x,y):")
    label_go_to_position['font'] = button_size
    label_go_to_position.place(x=20,y=550)
    entry_go_to_position_x = tk.Entry(width=5)
    entry_go_to_position_x.insert(0, "0")
    entry_go_to_position_x['font'] = button_size
    entry_go_to_position_x.place(x=320, y=550)
    entry_go_to_position_y = tk.Entry(width=5)
    entry_go_to_position_y.insert(0, "0")
    entry_go_to_position_y['font'] = button_size
    entry_go_to_position_y.place(x=380, y=550)
    b_move_to_position  = tk.Button(window, text = 'Go', command = lambda: commands.move_motor_to_position(entry_go_to_position_x.get(),entry_go_to_position_y.get(),device))
    b_move_to_position['font'] = button_size
    b_move_to_position.place(x=440, y=548)
    
    b_get_position_both_motors  = tk.Button(window, text = 'Get absolute position', command = lambda: commands.get_position_both_motors(device))
    b_get_position_both_motors['font'] = button_size
    b_get_position_both_motors.place(x=20, y=580)

    b_set_current_position_as_home  = tk.Button(window, text = 'Set current\n position as home', command = lambda: commands.set_current_position_as_home(device))
    b_set_current_position_as_home['font'] = button_size
    b_set_current_position_as_home.place(x=20, y=470)

    b_go_to_home_position  = tk.Button(window, text = 'Go to home\nposition', command = lambda: commands.go_to_home_position(device))
    b_go_to_home_position['font'] = button_size
    b_go_to_home_position.place(x=200, y=470)

    b_get_home_position  = tk.Button(window, text = 'Get home\nposition', command = lambda: commands.get_home_position(device))
    b_get_home_position['font'] = button_size
    b_get_home_position.place(x=335, y=470)

    label_go_to_rel_position = tk.Label(text="Move to RELATIVE position (x,y):")
    label_go_to_rel_position['font'] = button_size
    label_go_to_rel_position.place(x=20,y=650)
    entry_go_to_rel_position_x = tk.Entry(width=5)
    entry_go_to_rel_position_x.insert(0, "0")
    entry_go_to_rel_position_x['font'] = button_size
    entry_go_to_rel_position_x.place(x=320, y=650)
    entry_go_to_rel_position_y = tk.Entry(width=5)
    entry_go_to_rel_position_y.insert(0, "0")
    entry_go_to_rel_position_y['font'] = button_size
    entry_go_to_rel_position_y.place(x=380, y=650)
    
    b_go_to_relative_position  = tk.Button(window, text = 'Go', command = lambda: commands.go_to_relative_position(entry_go_to_rel_position_x.get(),entry_go_to_rel_position_y.get(),device))   
    b_go_to_relative_position['font'] = button_size
    b_go_to_relative_position.place(x=440, y=648)

    b_get_relative_position  = tk.Button(window, text = 'Get relative position', command = lambda: commands.get_relative_position(device))
    b_get_relative_position['font'] = button_size
    b_get_relative_position.place(x=20, y=680)
    
    b_scan  = tk.Button(window, text = 'Start scan', command = lambda: commands.scan(device),bg='green')
    scan_button_font=font.Font(size=25,weight="bold")
    b_scan['font'] = scan_button_font
    b_scan.place(x=20, y=740)

    b_exit_gui = tk.Button(window, text="Exit", command= lambda: exit_gui(device,window))
    exit_button_font=font.Font(size=25,weight="bold")
    b_exit_gui['font'] = exit_button_font
    b_exit_gui.place(x=580, y=740)
    #------------------------------------------------#
    
    window.mainloop()

