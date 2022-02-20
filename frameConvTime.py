# This will define the FrameConvTime class


import tkinter as tk


class FrameConvTime(tk.Frame):
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
        self.entry_s = tk.Entry(frame_main, width=entry_width)
        self.label_s = tk.Label(frame_main, width=label_width, text='s')
        self.entry_ms = tk.Entry(frame_main, width=entry_width)
        self.label_ms = tk.Label(frame_main, text='ms')
        self.entry_min = tk.Entry(frame_main, width=entry_width)
        self.label_min = tk.Label(frame_main, text='min')
        self.entry_hr = tk.Entry(frame_main, width=entry_width)
        self.label_hr = tk.Label(frame_main, text='hr')
        # And all their positions
        self.entry_s.grid(row=0, column=0, padx=(pad_ext, 0), pady=pad_ext)
        self.label_s.grid(row=0, column=1, padx=(0, 5*pad_ext), pady=pad_ext, sticky='w')
        self.entry_ms.grid(row=0, column=2, padx=pad_ext, pady=pad_ext)
        self.label_ms.grid(row=0, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_min.grid(row=1, column=2, padx=pad_ext, pady=pad_ext)
        self.label_min.grid(row=1, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_hr.grid(row=2, column=2, padx=pad_ext, pady=pad_ext)
        self.label_hr.grid(row=2, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        # Configurations for expansion
        frame_main.columnconfigure([0, 2], weight=1)
        # Bindings for each of the entries
        self.entry_s.bind('<KeyRelease>', lambda event: self.timeConversion('s', float(self.entry_s.get())))
        self.entry_ms.bind('<KeyRelease>', lambda event: self.timeConversion('ms', float(self.entry_ms.get())))
        self.entry_min.bind('<KeyRelease>', lambda event: self.timeConversion('min', float(self.entry_min.get())))
        self.entry_hr.bind('<KeyRelease>', lambda event: self.timeConversion('hr', float(self.entry_hr.get())))
    

    def timeConversion(self, given_unit, quantity):  # To do all the converting on the window
        base = timeTos(given_unit, quantity)
        conversions = timeFroms(base)
        entries = {
            's':self.entry_s, 
            'ms':self.entry_ms, 
            'min':self.entry_min, 
            'hr':self.entry_hr
            }
        del entries[given_unit]  # To remove the given unit from being edited
        
        for unit, entry in entries.items():
            conversion = conversions[unit]
            entry.delete(0, tk.END)
            entry.insert(0, f'{conversion:.3f}')


def timeTos(unit, quantity):  # This is to change to SI unit
    quantity = float(quantity)
    if unit == 's':
        return quantity
    elif unit == 'ms':
        return quantity / 1000
    elif unit == 'min':
        return quantity * 60
    elif unit == 'hr':
        return quantity * 60**2


def timeFroms(quantity):  # To give out all the conversions
    s = quantity
    ms = quantity * 1000
    min = quantity / 60
    hr = quantity / 60**2
    return {'s':s, 'ms':ms, 'min':min, 'hr':hr}
