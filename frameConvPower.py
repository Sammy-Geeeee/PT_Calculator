# This will define the FrameConvPower class


import tkinter as tk


class FrameConvPower(tk.Frame):
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
        self.entry_W = tk.Entry(frame_main, width=entry_width)
        self.label_W = tk.Label(frame_main, width=label_width, text='W')
        self.entry_kW = tk.Entry(frame_main, width=entry_width)
        self.label_kW = tk.Label(frame_main, text='kW')
        self.entry_hp = tk.Entry(frame_main, width=entry_width)
        self.label_hp = tk.Label(frame_main, text='hp')
        # And all their positions
        self.entry_W.grid(row=0, column=0, padx=(pad_ext, 0), pady=pad_ext)
        self.label_W.grid(row=0, column=1, padx=(0, 5*pad_ext), pady=pad_ext, sticky='w')
        self.entry_kW.grid(row=0, column=2, padx=pad_ext, pady=pad_ext)
        self.label_kW.grid(row=0, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_hp.grid(row=1, column=2, padx=pad_ext, pady=pad_ext)
        self.label_hp.grid(row=1, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        # Configurations for expansion
        frame_main.columnconfigure([0, 2], weight=1)
        # Bindings for each of the entries
        self.entry_W.bind('<KeyRelease>', lambda event: self.powerConversion('W', float(self.entry_W.get())))
        self.entry_kW.bind('<KeyRelease>', lambda event: self.powerConversion('kW', float(self.entry_kW.get())))
        self.entry_hp.bind('<KeyRelease>', lambda event: self.powerConversion('hp', float(self.entry_hp.get())))
        

    def powerConversion(self, given_unit, quantity):  # To do all the converting on the window
        base = powerToW(given_unit, quantity)
        conversions = powerFromW(base)
        entries = {
            'W':self.entry_W, 
            'kW':self.entry_kW, 
            'hp':self.entry_hp
            }
        del entries[given_unit]  # To remove the given unit from being edited
        
        for unit, entry in entries.items():
            conversion = conversions[unit]
            entry.delete(0, tk.END)
            entry.insert(0, f'{conversion:.3f}')


def powerToW(unit, quantity):  # This is to change to SI unit
    quantity = float(quantity)
    if unit == 'W':
        return quantity
    elif unit == 'kW':
        return quantity * 1000
    elif unit == 'hp':
        return quantity * 745.7


def powerFromW(quantity):  # To give out all the conversions
    W = quantity
    kW = quantity / 1000
    hp = quantity / 745.7
    return {'W': W, 'kW': kW, 'hp': hp}
