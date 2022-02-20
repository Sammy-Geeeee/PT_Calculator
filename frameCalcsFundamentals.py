# This will define the FrameCalcsFundamentals class


from frameCalcsFundFMA import *
from frameCalcsFundTFD import *
from frameCalcsFundLDR import *
from frameCalcsFundPTR import *
from units import *
import tkinter as tk
from tkinter import ttk


class FrameCalcsFundamentals(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # Some base variables for the sizing of various things
        pad_ext = 10

        # To make the main sub frame
        frame_main = tk.Frame(master)
        frame_main.grid(row=0, column=0)
        # Configurations for expansion
        frame_main.columnconfigure([0, 1, 2, 3, 4, 5, 6], weight=1)
        

        # To make all the frames and separators for this section
        FrameCalcsFundFMA(frame_main)
        separator1 = ttk.Separator(frame_main)
        FrameCalcsFundTFD(frame_main)
        separator2 = ttk.Separator(frame_main)
        FrameCalcsFundLDR(frame_main)
        separator3 = ttk.Separator(frame_main)
        FrameCalcsFundPTR(frame_main)
        # And to put them in place, frame placement defined in their own classes
        separator1.grid(row=1, column=0, sticky='ew', padx=pad_ext, pady=3*pad_ext)
        separator2.grid(row=3, column=0, sticky='ew', padx=pad_ext, pady=3*pad_ext)
        separator3.grid(row=5, column=0, sticky='ew', padx=pad_ext, pady=3*pad_ext)
