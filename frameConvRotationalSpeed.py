# This will define the FrameConvRotational class


import tkinter as tk
from math import pi


class FrameConvRotationalSpeed(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # Some base variables for the sizing of various things
        pad_ext = 10
        entry_width = 1000
        label_width = 5

        # To make the main sub frame, just so I can grid everything
        frame_main = tk.Frame(master)
        frame_main.pack(expand=1, fill='both')
        
        # To make all the widgets within this frame
        self.entry_rad_s = tk.Entry(frame_main, width=entry_width)
        self.label_rad_s = tk.Label(frame_main, width=label_width, text='rad/s')
        self.entry_rad_min = tk.Entry(frame_main, width=entry_width)
        self.label_rad_min = tk.Label(frame_main, text='rad/min')
        self.entry_deg_s = tk.Entry(frame_main, width=entry_width)
        self.label_deg_s = tk.Label(frame_main, text='deg/s')
        self.entry_deg_min = tk.Entry(frame_main, width=entry_width)
        self.label_deg_min = tk.Label(frame_main, text='deg/min')
        self.entry_rev_s = tk.Entry(frame_main, width=entry_width)
        self.label_rev_s = tk.Label(frame_main, text='rev/s')
        self.entry_rev_min = tk.Entry(frame_main, width=entry_width)
        self.label_rev_min = tk.Label(frame_main, text='rev/min')
        self.entry_rev_hr = tk.Entry(frame_main, width=entry_width)
        self.label_rev_hr = tk.Label(frame_main, text='rev/hr')
        # And all their positions
        self.entry_rad_s.grid(row=0, column=0, padx=(pad_ext, 0), pady=pad_ext)
        self.label_rad_s.grid(row=0, column=1, padx=(0, 5*pad_ext), pady=pad_ext, sticky='w')
        self.entry_rad_min.grid(row=0, column=2, padx=pad_ext, pady=pad_ext)
        self.label_rad_min.grid(row=0, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_deg_s.grid(row=1, column=2, padx=pad_ext, pady=pad_ext)
        self.label_deg_s.grid(row=1, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_deg_min.grid(row=2, column=2, padx=pad_ext, pady=pad_ext)
        self.label_deg_min.grid(row=2, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_rev_s.grid(row=3, column=2, padx=pad_ext, pady=pad_ext)
        self.label_rev_s.grid(row=3, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_rev_min.grid(row=4, column=2, padx=pad_ext, pady=pad_ext)
        self.label_rev_min.grid(row=4, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_rev_hr.grid(row=5, column=2, padx=pad_ext, pady=pad_ext)
        self.label_rev_hr.grid(row=5, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        # Configurations for expansion
        frame_main.columnconfigure([0, 2], weight=1)
        # Bindings for each of the entries
        self.entry_rad_s.bind('<KeyRelease>', lambda event: self.rotationalSpeedConversion('rad/s', float(self.entry_rad_s.get())))
        self.entry_rad_min.bind('<KeyRelease>', lambda event: self.rotationalSpeedConversion('rad/min', float(self.entry_rad_min.get())))
        self.entry_deg_s.bind('<KeyRelease>', lambda event: self.rotationalSpeedConversion('deg/s', float(self.entry_deg_s.get())))
        self.entry_deg_min.bind('<KeyRelease>', lambda event: self.rotationalSpeedConversion('deg/min', float(self.entry_deg_min.get())))
        self.entry_rev_s.bind('<KeyRelease>', lambda event: self.rotationalSpeedConversion('rev/s', float(self.entry_rev_s.get())))
        self.entry_rev_min.bind('<KeyRelease>', lambda event: self.rotationalSpeedConversion('rev/min', float(self.entry_rev_min.get())))
        self.entry_rev_hr.bind('<KeyRelease>', lambda event: self.rotationalSpeedConversion('rev/hr', float(self.entry_rev_hr.get())))
    

    def rotationalSpeedConversion(self, given_unit, quantity):  # To do all the converting on the window
        base = rotationalSpeedTorads(given_unit, quantity)
        conversions = rotationalSpeedFromrads(base)
        entries = {
            'rad/s':self.entry_rad_s, 
            'rad/min':self.entry_rad_min, 
            'deg/s':self.entry_deg_s, 
            'deg/min':self.entry_deg_min, 
            'rev/s':self.entry_rev_s, 
            'rev/min':self.entry_rev_min, 
            'rev/hr':self.entry_rev_hr}
        del entries[given_unit]  # To remove the given unit from being edited
        
        for unit, entry in entries.items():
            conversion = conversions[unit]
            entry.delete(0, tk.END)
            entry.insert(0, f'{conversion:.3f}')


def rotationalSpeedTorads(unit, quantity):  # This is to change to SI unit
    quantity = float(quantity)
    if unit == 'rad/s':
        return quantity
    elif unit == 'rad/min':
        return quantity / 60
    elif unit == 'deg/s':
        return quantity * (pi/180)
    elif unit == 'deg/min':
        return quantity * (pi/180) / 60
    elif unit == 'rev/s':
        return quantity * (2*pi)
    elif unit == 'rev/min':
        return quantity * (2*pi) / 60
    elif unit == 'rev/hr':
        return quantity * (2*pi) / 60**2


def rotationalSpeedFromrads(quantity):  # To give out all the conversions
    rad_s = quantity
    rad_min = quantity * 60
    deg_s = quantity / (pi/180)
    deg_min = quantity / (pi/180) * 60
    rev_s = quantity / (2*pi)
    rev_min = quantity / (2*pi) * 60
    rev_hr = quantity / (2*pi) * 60**2
    return {'rad/s': rad_s, 'rad/min': rad_min, 'deg/s': deg_s, 'deg/min': deg_min, 'rev/s': rev_s, 'rev/min': rev_min, 'rev/hr': rev_hr}
