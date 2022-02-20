# This will define the FrameCalcsPTCalcs class


from FrameCalcsPTBelts import *
from FrameCalcsPTTeeth import *
from FrameCalcsPTGearbox import *
from units import *
import tkinter as tk
from tkinter import ttk


class FrameCalcsPTCalcs(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # Some base variables for the sizing of various things
        pad_ext = 10

        # To make the main sub frame
        frame_main = tk.Frame(master)
        frame_main.grid(row=0, column=0)
        # Configurations for expansion
        frame_main.columnconfigure([0, 1, 2, 3, 4], weight=1)
        

        # To make all the frames and separators for this section
        FrameCalcsPTBelts(frame_main)
        separator1 = ttk.Separator(frame_main)
        FrameCalcsPTTeeth(frame_main)
        separator2 = ttk.Separator(frame_main)
        FrameCalcsPTGearbox(frame_main)
        # And to put them in place, frame placement defined in their own classes
        separator1.grid(row=1, column=0, sticky='ew', padx=pad_ext, pady=3*pad_ext)
        separator2.grid(row=3, column=0, sticky='ew', padx=pad_ext, pady=3*pad_ext)
