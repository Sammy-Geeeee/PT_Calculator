# This will define the FrameConvMass class


import tkinter as tk
from tkinter import ttk


class FrameConvMass(tk.Frame):
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
        self.entry_kg = tk.Entry(frame_main, width=entry_width)
        self.label_kg = tk.Label(frame_main, width=label_width, text='kg')
        self.entry_mg = tk.Entry(frame_main, width=entry_width)
        self.label_mg = tk.Label(frame_main, text='mg')
        self.entry_g = tk.Entry(frame_main, width=entry_width)
        self.label_g = tk.Label(frame_main, text='g')
        self.entry_T = tk.Entry(frame_main, width=entry_width)
        self.label_T = tk.Label(frame_main, text='T')
        self.entry_oz = tk.Entry(frame_main, width=entry_width)
        self.label_oz = tk.Label(frame_main, text='oz')
        self.entry_lb = tk.Entry(frame_main, width=entry_width)
        self.label_lb = tk.Label(frame_main, text='lb')
        self.entry_st = tk.Entry(frame_main, width=entry_width)
        self.label_st = tk.Label(frame_main, text='st')
        # And all their positions
        self.entry_kg.grid(row=0, column=0, padx=(pad_ext, 0), pady=pad_ext)
        self.label_kg.grid(row=0, column=1, padx=(0, 5*pad_ext), pady=pad_ext, sticky='w')
        self.entry_mg.grid(row=0, column=2, padx=pad_ext, pady=pad_ext)
        self.label_mg.grid(row=0, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_g.grid(row=1, column=2, padx=pad_ext, pady=pad_ext)
        self.label_g.grid(row=1, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_T.grid(row=2, column=2, padx=pad_ext, pady=pad_ext)
        self.label_T.grid(row=2, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_oz.grid(row=3, column=2, padx=pad_ext, pady=pad_ext)
        self.label_oz.grid(row=3, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_lb.grid(row=4, column=2, padx=pad_ext, pady=pad_ext)
        self.label_lb.grid(row=4, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_st.grid(row=5, column=2, padx=pad_ext, pady=pad_ext)
        self.label_st.grid(row=5, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        # Configurations for expansion
        frame_main.columnconfigure([0, 2], weight=1)
        # Bindings for each of the entries
        self.entry_kg.bind('<KeyRelease>', lambda event: self.massConversion('kg', float(self.entry_kg.get())))
        self.entry_mg.bind('<KeyRelease>', lambda event: self.massConversion('mg', float(self.entry_mg.get())))
        self.entry_g.bind('<KeyRelease>', lambda event: self.massConversion('g', float(self.entry_g.get())))
        self.entry_T.bind('<KeyRelease>', lambda event: self.massConversion('T', float(self.entry_T.get())))
        self.entry_oz.bind('<KeyRelease>', lambda event: self.massConversion('oz', float(self.entry_oz.get())))
        self.entry_lb.bind('<KeyRelease>', lambda event: self.massConversion('lb', float(self.entry_lb.get())))
        self.entry_st.bind('<KeyRelease>', lambda event: self.massConversion('st', float(self.entry_st.get())))
    

    def massConversion(self, given_unit, quantity):  # To do all the converting on the window
        base = massTokg(given_unit, quantity)
        conversions = massFromkg(base)
        entries = {
            'kg':self.entry_kg, 
            'mg':self.entry_mg, 
            'g':self.entry_g, 
            'T':self.entry_T, 
            'oz':self.entry_oz, 
            'lb':self.entry_lb, 
            'st':self.entry_st
            }
        del entries[given_unit]  # To remove the given unit from being edited
        
        for unit, entry in entries.items():
            conversion = conversions[unit]
            entry.delete(0, tk.END)
            entry.insert(0, f'{conversion:.3f}')


def massTokg(unit, quantity):  # This is to change to SI unit
    quantity = float(quantity)
    if unit == 'kg':
        return quantity
    elif unit == 'mg':
        return quantity / 1000**2
    elif unit == 'g':
        return quantity / 1000
    elif unit == 'T':
        return quantity * 1000
    elif unit == 'oz':
        return quantity / 35.274
    elif unit == 'lb':
        return quantity / 2.205
    elif unit == 'st':
        return quantity * 6.35029


def massFromkg(quantity):  # To give out all the conversions
    kg = quantity
    mg = quantity * 1000**2
    g = quantity * 1000
    T = quantity / 1000
    oz = quantity * 35.274
    lb = quantity * 2.205
    st = quantity / 6.35029
    return {'kg':kg, 'mg':mg, 'g':g, 'T':T, 'oz':oz, 'lb':lb, 'st':st}
