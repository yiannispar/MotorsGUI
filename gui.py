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
    time.sleep(4)
    window.destroy()

def run_gui(device):
    window = tk.Tk()
    window.geometry("550x700")
    tk.Label(text="Piezoelectric motor program", fg="white", bg="blue", font=("Arial", 25)).pack(pady=20) 

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

    b_unpark_motor_1  = tk.Button(window, text = 'Park motor 1', command = lambda: commands.unpark_motor(1,device))
    b_unpark_motor_1['font'] = button_size
    b_unpark_motor_1.place(x=20, y=200)

    b_unpark_motor_2  = tk.Button(window, text = 'Park motor 2', command = lambda: commands.unpark_motor(2,device))
    b_unpark_motor_2['font'] = button_size
    b_unpark_motor_2.place(x=170, y=200)
        
    b_unpark_both_motors = tk.Button(window, text = 'Unpark both motors', command = lambda: commands.unpark_both_motors(device))
    b_unpark_both_motors['font'] = button_size
    b_unpark_both_motors.place(x=320, y=200)

    label_distance = tk.Label(text="Distance to move motor(s)[mm] :")
    label_distance.place(x=20,y=300)
    entry = tk.Entry()
    entry.place(x=220, y=300)

    b_move_motor_1 = tk.Button(window, text = 'Move motor 1', command = lambda: commands.move_motor(1,entry.get(),device))
    b_move_motor_1['font'] = button_size
    b_move_motor_1.place(x=20, y=350)

    b_move_motor_2 = tk.Button(window, text = 'Move motor 2', command = lambda: commands.move_motor(2,entry.get(),device))
    b_move_motor_2['font'] = button_size
    b_move_motor_2.place(x=170, y=350)

    b_move_both_motors = tk.Button(window, text = 'Move both motors', command = lambda: commands.move_both_motors(entry.get(),device))
    b_move_both_motors['font'] = button_size
    b_move_both_motors.place(x=320, y=350)

    label_speed = tk.Label(text="Set speed to motor(s) [mm/s]:")
    label_speed.place(x=20,y=450)
    entry_speed = tk.Entry()
    entry_speed.place(x=220, y=450)

    b_set_speed_motor_1 = tk.Button(window, text = 'Set speed to motor 1', command = lambda: commands.set_speed(1,entry_speed.get(),device))
    b_set_speed_motor_1['font'] = button_size
    b_set_speed_motor_1.place(x=20, y=500)

    b_set_speed_motor_2 = tk.Button(window, text = 'Set speed to motor 2', command = lambda: commands.set_speed(2,entry_speed.get(),device))
    b_set_speed_motor_2['font'] = button_size
    b_set_speed_motor_2.place(x=190, y=500)
    
    b_set_speed_both_motors  = tk.Button(window, text = 'Set speed to both motors', command = lambda: commands.set_speed_both_motors(entry_speed.get(),device))
    b_set_speed_both_motors['font'] = button_size
    b_set_speed_both_motors.place(x=320, y=500)

    b_exit_gui = tk.Button(window, text="Exit", command= lambda: exit_gui(device,window))
    b_exit_gui['font'] = button_size
    b_exit_gui.place(x=190, y=600)
    #------------------------------------------------#
    
    window.mainloop()

