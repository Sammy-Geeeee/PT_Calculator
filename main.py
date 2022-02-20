# PT Calculator Program

"""
This program is to put a bunch of basic Power Transmission calculations in one program.
This will include the ability to do basic unit conversions as well as actual calculations
"""

from frameCalcsFundamentals import *
from frameCalcsPTCalcs import *
from frameConvMass import *
from frameConvTime import *
from frameConvDistance import *
from frameConvLinearSpeed import *
from frameConvRotationalSpeed import *
from frameConvLinearAcceleration import *
from frameConvForce import *
from frameConvTorque import *
from frameConvPower import *
import tkinter as tk
from tkinter import ttk


class Window:
    def __init__(self, root, title, geometry):
        # This will set all the base information to make the main window
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)
        # Universal variables
        pad_ext = 5


        # This will create the main notebook for the entire program
        notebook_main = ttk.Notebook(master=root)
        notebook_main.pack(expand=1, fill='both', padx=pad_ext, pady=pad_ext)
        # To create the frames for each main section
        frame_conversions = tk.Frame(master=notebook_main)
        frame_calculations = tk.Frame(master=notebook_main)
        # Adding some configurations to allow expansion
        frame_conversions.columnconfigure([0], weight=1)
        frame_calculations.columnconfigure([0], weight=1)
        # And to add them to the main notebook
        notebook_main.add(frame_conversions, text='Conversions')
        notebook_main.add(frame_calculations, text='Calculations')


        # To make the parts for the Conversion frame
        notebook_conversions = ttk.Notebook(master=frame_conversions)
        notebook_conversions.pack(expand=1, fill='both', padx=pad_ext, pady=pad_ext)
        # All the frame creation
        frame_mass = tk.Frame(master=notebook_conversions)
        frame_time = tk.Frame(master=notebook_conversions)
        frame_distance = tk.Frame(master=notebook_conversions)
        frame_lin_speed = tk.Frame(master=notebook_conversions)
        frame_rot_speed = tk.Frame(master=notebook_conversions)
        frame_lin_accel = tk.Frame(master=notebook_conversions)
        frame_force = tk.Frame(master=notebook_conversions)
        frame_torque = tk.Frame(master=notebook_conversions)
        frame_power = tk.Frame(master=notebook_conversions)
        # Configs to allow for expansion
        frame_mass.columnconfigure([0], weight=1)
        frame_time.columnconfigure([0], weight=1)
        frame_distance.columnconfigure([0], weight=1)
        frame_lin_speed.columnconfigure([0], weight=1)
        frame_rot_speed.columnconfigure([0], weight=1)
        frame_lin_accel.columnconfigure([0], weight=1)
        frame_force.columnconfigure([0], weight=1)
        frame_torque.columnconfigure([0], weight=1)
        frame_power.columnconfigure([0], weight=1)
        # And adding them to their notebook
        notebook_conversions.add(frame_mass, text='Mass')
        notebook_conversions.add(frame_time, text='Time')
        notebook_conversions.add(frame_distance, text='Distance')
        notebook_conversions.add(frame_lin_speed, text='Linear Speed')
        notebook_conversions.add(frame_rot_speed, text='Rotational Speed')
        notebook_conversions.add(frame_lin_accel, text='Linear Acceleration')
        notebook_conversions.add(frame_force, text='Force')
        notebook_conversions.add(frame_torque, text='Torque')
        notebook_conversions.add(frame_power, text='Power')


        # To make the Calculation frame
        notebook_calculations = ttk.Notebook(master=frame_calculations)
        notebook_calculations.pack(expand=1, fill='both', padx=pad_ext, pady=pad_ext)
        # All the frame creation
        frame_fundamentals = tk.Frame(master=notebook_calculations)
        frame_pt_calcs = tk.Frame(master=notebook_calculations)
        # Configurations for expansion
        frame_fundamentals.columnconfigure([0], weight=1)
        frame_pt_calcs.columnconfigure([0], weight=1)
        # And adding them to their notebook
        notebook_calculations.add(frame_fundamentals, text='Fundamentals')
        notebook_calculations.add(frame_pt_calcs, text='PT Calculations')


        # Adding each of the frames for each part to their section
        FrameConvMass(frame_mass)
        FrameConvTime(frame_time)
        FrameConvDistance(frame_distance)
        FrameConvLinearSpeed(frame_lin_speed)
        FrameConvRotationalSpeed(frame_rot_speed)
        FrameConvLinearAcceleration(frame_lin_accel)
        FrameConvForce(frame_force)
        FrameConvTorque(frame_torque)
        FrameConvPower(frame_power)

        FrameCalcsFundamentals(frame_fundamentals)
        FrameCalcsPTCalcs(frame_pt_calcs)


        self.root.mainloop()  # To actually run the program loop


def main():
    window = Window(tk.Tk(), 'Power Transmission Calculator', '1000x850')  # Main window defined here
    

main()
