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
    window.geometry("700x860")
    tk.Label(text="2-D Translation Stage", fg="white", bg="blue", font=("Arial", 25)).pack(pady=25) 
    button_size=font.Font(size=15)

    #----------- Park ------------#
    b_park_both_motors = tk.Button(window, text = 'Park motors', command = lambda: commands.park_both_motors(device))
    b_park_both_motors['font'] = button_size
    b_park_both_motors.place(x=20, y=100)

    b_unpark_both_motors = tk.Button(window, text = 'Unpark  motors', command = lambda: commands.unpark_both_motors(device))
    b_unpark_both_motors['font'] = button_size
    b_unpark_both_motors.place(x=170, y=100)
    #-----------------------------#

    #----------- Move ------------#
    label_distance = tk.Label(text="Distance to move motor(s) [mm] :")
    label_distance['font'] = button_size
    label_distance.place(x=20,y=150)
    entry = tk.Entry(width=5)
    entry['font'] = button_size
    entry.place(x=300, y=150)

    b_move_motor_1 = tk.Button(window, text = 'Move x-axis', command = lambda: commands.move_motor(1,entry.get(),device))
    b_move_motor_1['font'] = button_size
    b_move_motor_1.place(x=20, y=180)

    b_move_motor_2 = tk.Button(window, text = 'Move y-axis', command = lambda: commands.move_motor(2,entry.get(),device))
    b_move_motor_2['font'] = button_size
    b_move_motor_2.place(x=170, y=180)

    b_move_both_motors = tk.Button(window, text = 'Move both axes', command = lambda: commands.move_both_motors(entry.get(),device))
    b_move_both_motors['font'] = button_size
    b_move_both_motors.place(x=320, y=180)
    #----------------------------#

    #------------Speed-----------#
    label_speed = tk.Label(text="Set speed to motors [mm/s]:")
    label_speed['font'] = button_size
    label_speed.place(x=20,y=240)
    entry_speed = tk.Entry(width=5)
    entry_speed['font'] = button_size
    entry_speed.place(x=270, y=240)

    b_set_speed_both_motors  = tk.Button(window, text = 'Set', command = lambda: commands.set_speed_both_motors(entry_speed.get(),device))
    b_set_speed_both_motors['font'] = button_size
    b_set_speed_both_motors.place(x=330, y=238)
    #----------------------------#

    #-------Send Command---------#
    label_send_command = tk.Label(text="Command:")
    label_send_command['font'] = button_size
    label_send_command.place(x=20,y=360)
    entry_send_command = tk.Entry()
    entry_send_command['font'] = button_size
    entry_send_command.place(x=120, y=360)
    
    b_send_command  = tk.Button(window, text = 'Send', command = lambda: commands.run_command(entry_send_command.get().split(),device))
    b_send_command['font'] = button_size
    b_send_command.place(x=350, y=360)
    #---------------------------#

    #-----------Stop------------#
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
    #---------------------------#

    #----------Absolute---------#
    label_x_abs = tk.Label(text="x")
    label_x_abs['font'] = button_size
    label_x_abs.place(x=340,y=527)
    label_y_abs = tk.Label(text="y")
    label_y_abs['font'] = button_size
    label_y_abs.place(x=400,y=527)   
    label_go_to_position = tk.Label(text="Move to ABSOLUTE position [counts]:")
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
    #----------------------------#

    #-------Home Position--------#
    b_set_current_position_as_home  = tk.Button(window, text = 'Set current\n position as home', command = lambda: commands.set_current_position_as_home(device))
    b_set_current_position_as_home['font'] = button_size
    b_set_current_position_as_home.place(x=20, y=470)

    b_go_to_home_position  = tk.Button(window, text = 'Go to home\nposition', command = lambda: commands.go_to_home_position(device))
    b_go_to_home_position['font'] = button_size
    b_go_to_home_position.place(x=200, y=470)

    b_get_home_position  = tk.Button(window, text = 'Get home\nposition', command = lambda: commands.get_home_position(device))
    b_get_home_position['font'] = button_size
    b_get_home_position.place(x=335, y=470)
    #----------------------------#

    #---------Relative-----------#
    label_x_rel = tk.Label(text="x")
    label_x_rel['font'] = button_size
    label_x_rel.place(x=340,y=627)
    label_y_rel = tk.Label(text="y")
    label_y_rel['font'] = button_size
    label_y_rel.place(x=400,y=627)   
    label_go_to_rel_position = tk.Label(text="Move to RELATIVE position [mm]:")
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
    #-----------------------------#

    #------------Scan-------------#
    label_scan_x = tk.Label(text="x-axis")
    label_scan_x['font'] = button_size
    label_scan_x.place(x=20,y=750)
    label_scan_y = tk.Label(text="y-axis")
    label_scan_y['font'] = button_size
    label_scan_y.place(x=20,y=785)
    label_scan_range_x_min = tk.Label(text="min [mm]")
    label_scan_range_x_min['font'] = button_size
    label_scan_range_x_min.place(x=79,y=729)
    label_scan_range_x_max = tk.Label(text="max [mm]")
    label_scan_range_x_max['font'] = button_size
    label_scan_range_x_max.place(x=172,y=729)
    label_scan_range_x_step = tk.Label(text="step [mm]")
    label_scan_range_x_step['font'] = button_size
    label_scan_range_x_step.place(x=265,y=729)
    entry_scan_range_x_min = tk.Entry(width=7)
    entry_scan_range_x_min['font'] = button_size
    entry_scan_range_x_min.place(x=80, y=750)
    entry_scan_range_x_min.insert(0, "0")
    entry_scan_range_x_max = tk.Entry(width=7)
    entry_scan_range_x_max['font'] = button_size
    entry_scan_range_x_max.place(x=175, y=750)
    entry_scan_range_x_max.insert(0, "0")
    entry_scan_range_x_step = tk.Entry(width=7)
    entry_scan_range_x_step['font'] = button_size
    entry_scan_range_x_step.place(x=270, y=750)
    entry_scan_range_x_step.insert(0, "0")

    entry_scan_range_y_min = tk.Entry(width=7)
    entry_scan_range_y_min['font'] = button_size
    entry_scan_range_y_min.place(x=80, y=785)
    entry_scan_range_y_min.insert(0, "0")
    entry_scan_range_y_max = tk.Entry(width=7)
    entry_scan_range_y_max['font'] = button_size
    entry_scan_range_y_max.place(x=175, y=785)
    entry_scan_range_y_max.insert(0, "0")
    entry_scan_range_y_step = tk.Entry(width=7)
    entry_scan_range_y_step['font'] = button_size
    entry_scan_range_y_step.place(x=270, y=785)
    entry_scan_range_y_step.insert(0, "0")

    b_scan  = tk.Button(window, text = 'Start\nscan', command = lambda: commands.scan(device,entry_scan_range_x_min.get(),entry_scan_range_x_max.get(),entry_scan_range_x_step.get(),entry_scan_range_y_min.get(),entry_scan_range_y_max.get(),entry_scan_range_y_step.get()),bg='green')
    scan_button_font=font.Font(size=25,weight="bold")
    b_scan['font'] = scan_button_font
    b_scan.place(x=365, y=740)

    label_note = tk.Label(text="Note: min & max values are relative to the home position")
    label_note['font'] = button_size
    label_note.place(x=20,y=820)
    #----------------------------------#

    #--------------Exit----------------#
    b_exit_gui = tk.Button(window, text="Exit", command= lambda: exit_gui(device,window))
    exit_button_font=font.Font(size=25,weight="bold")
    b_exit_gui['font'] = exit_button_font
    b_exit_gui.place(x=590, y=780)  
    #----------------------------------#
    
    window.mainloop()

