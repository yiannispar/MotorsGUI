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
    window.title("Piezoelectir motor")
    window.geometry("700x500")
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
    b_unpark_motor_1.place(x=20, y=150)

    b_unpark_motor_2  = tk.Button(window, text = 'Park motor 2', command = lambda: commands.unpark_motor(2,device))
    b_unpark_motor_2['font'] = button_size
    b_unpark_motor_2.place(x=170, y=150)
        
    b_unpark_both_motors = tk.Button(window, text = 'Unpark both motors', command = lambda: commands.unpark_both_motors(device))
    b_unpark_both_motors['font'] = button_size
    b_unpark_both_motors.place(x=320, y=150)

    label_distance = tk.Label(text="Distance to move motor(s) [mm] :")
    label_distance.place(x=20,y=200)
    entry = tk.Entry()
    entry.place(x=220, y=200)

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
    label_speed.place(x=20,y=270)
    entry_speed = tk.Entry()
    entry_speed.place(x=220, y=270)

    b_set_speed_motor_1 = tk.Button(window, text = 'Set speed to motor 1', command = lambda: commands.set_speed(1,entry_speed.get(),device))
    b_set_speed_motor_1['font'] = button_size
    b_set_speed_motor_1.place(x=20, y=300)

    b_set_speed_motor_2 = tk.Button(window, text = 'Set speed to motor 2', command = lambda: commands.set_speed(2,entry_speed.get(),device))
    b_set_speed_motor_2['font'] = button_size
    b_set_speed_motor_2.place(x=230, y=300)
    
    b_set_speed_both_motors  = tk.Button(window, text = 'Set speed to both motors', command = lambda: commands.set_speed_both_motors(entry_speed.get(),device))
    b_set_speed_both_motors['font'] = button_size
    b_set_speed_both_motors.place(x=440, y=300)

    label_send_command = tk.Label(text="Send command:")
    label_send_command.place(x=20,y=360)
    entry_send_command = tk.Entry()
    entry_send_command.place(x=130, y=360)

    b_send_command  = tk.Button(window, text = 'Send command', command = lambda: commands.run_command(entry_send_command.get().split(),device))
    b_send_command['font'] = button_size
    b_send_command.place(x=280, y=360)
    
    b_exit_gui = tk.Button(window, text="Exit", command= lambda: exit_gui(device,window),fg='red')
    exit_button_font=font.Font(size=25,weight="bold")
    b_exit_gui['font'] = exit_button_font
    b_exit_gui.place(x=310, y=420)
    #------------------------------------------------#
    
    window.mainloop()

