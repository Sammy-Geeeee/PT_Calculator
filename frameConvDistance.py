# This will define the FrameConvDistance class


import tkinter as tk


class FrameConvDistance(tk.Frame):
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
        self.entry_m = tk.Entry(frame_main, width=entry_width)
        self.label_m = tk.Label(frame_main, width=label_width, text='m')
        self.entry_mm = tk.Entry(frame_main, width=entry_width)
        self.label_mm = tk.Label(frame_main, text='mm')
        self.entry_cm = tk.Entry(frame_main, width=entry_width)
        self.label_cm = tk.Label(frame_main, text='cm')
        self.entry_km = tk.Entry(frame_main, width=entry_width)
        self.label_km = tk.Label(frame_main, text='km')
        self.entry_in = tk.Entry(frame_main, width=entry_width)
        self.label_in = tk.Label(frame_main, text='in')
        self.entry_ft = tk.Entry(frame_main, width=entry_width)
        self.label_ft = tk.Label(frame_main, text='ft')
        self.entry_yd = tk.Entry(frame_main, width=entry_width)
        self.label_yd = tk.Label(frame_main, text='yd')
        self.entry_mi = tk.Entry(frame_main, width=entry_width)
        self.label_mi = tk.Label(frame_main, text='mi')
        # And all their positions
        self.entry_m.grid(row=0, column=0, padx=(pad_ext, 0), pady=pad_ext)
        self.label_m.grid(row=0, column=1, padx=(0, 5*pad_ext), pady=pad_ext, sticky='w')
        self.entry_mm.grid(row=0, column=2, padx=pad_ext, pady=pad_ext)
        self.label_mm.grid(row=0, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_cm.grid(row=1, column=2, padx=pad_ext, pady=pad_ext)
        self.label_cm.grid(row=1, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_km.grid(row=2, column=2, padx=pad_ext, pady=pad_ext)
        self.label_km.grid(row=2, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_in.grid(row=3, column=2, padx=pad_ext, pady=pad_ext)
        self.label_in.grid(row=3, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_ft.grid(row=4, column=2, padx=pad_ext, pady=pad_ext)
        self.label_ft.grid(row=4, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_yd.grid(row=5, column=2, padx=pad_ext, pady=pad_ext)
        self.label_yd.grid(row=5, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_mi.grid(row=6, column=2, padx=pad_ext, pady=pad_ext)
        self.label_mi.grid(row=6, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        # Configurations for expansion
        frame_main.columnconfigure([0, 2], weight=1)
        # Bindings for each of the entries
        self.entry_m.bind('<KeyRelease>', lambda event: self.distanceConversion('m', float(self.entry_m.get())))
        self.entry_mm.bind('<KeyRelease>', lambda event: self.distanceConversion('mm', float(self.entry_mm.get())))
        self.entry_cm.bind('<KeyRelease>', lambda event: self.distanceConversion('cm', float(self.entry_cm.get())))
        self.entry_km.bind('<KeyRelease>', lambda event: self.distanceConversion('km', float(self.entry_km.get())))
        self.entry_in.bind('<KeyRelease>', lambda event: self.distanceConversion('in', float(self.entry_in.get())))
        self.entry_ft.bind('<KeyRelease>', lambda event: self.distanceConversion('ft', float(self.entry_ft.get())))
        self.entry_yd.bind('<KeyRelease>', lambda event: self.distanceConversion('yd', float(self.entry_yd.get())))
        self.entry_mi.bind('<KeyRelease>', lambda event: self.distanceConversion('mi', float(self.entry_mi.get())))
    

    def distanceConversion(self, given_unit, quantity):  # To do all the converting on the window
        base = distanceTom(given_unit, quantity)
        conversions = distanceFromm(base)
        entries = {
            'm':self.entry_m, 
            'mm':self.entry_mm, 
            'cm':self.entry_cm, 
            'km':self.entry_km, 
            'in':self.entry_in, 
            'ft':self.entry_ft, 
            'yd':self.entry_yd, 
            'mi':self.entry_mi
            }
        del entries[given_unit]  # To remove the given unit from being edited
        
        for unit, entry in entries.items():
            conversion = conversions[unit]
            entry.delete(0, tk.END)
            entry.insert(0, f'{conversion:.3f}')


def distanceTom(unit, quantity):  # This is to change to SI unit
    quantity = float(quantity)
    if unit == 'm':
        return quantity
    elif unit == 'mm':
        return quantity / 1000
    elif unit == 'cm':
        return quantity / 100
    elif unit == 'km':
        return quantity * 1000
    elif unit == 'in':
        return quantity / 39.3701
    elif unit == 'ft':
        return quantity / 3.28084
    elif unit == 'yd':
        return quantity / 1.09361
    elif unit == 'mi':
        return quantity * 1609.34


def distanceFromm(quantity):  # To give out all the conversions
    m = quantity
    mm = quantity * 1000
    cm = quantity * 100
    km = quantity / 1000
    inch = quantity * 39.3701
    ft = quantity * 3.2808
    yd = quantity * 1.09361
    mi = quantity / 1609.34
    return {'m':m, 'mm':mm, 'cm':cm, 'km':km, 'in':inch, 'ft':ft, 'yd':yd, 'mi':mi}
