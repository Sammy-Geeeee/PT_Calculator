# This will define the FrameConvTorque class


import tkinter as tk


class FrameConvTorque(tk.Frame):
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
        self.entry_N_m = tk.Entry(frame_main, width=entry_width)
        self.label_N_m = tk.Label(frame_main, width=label_width, text='N.m')
        self.entry_kN_m = tk.Entry(frame_main, width=entry_width)
        self.label_kN_m = tk.Label(frame_main, text='kN.m')
        self.entry_kg_f_m = tk.Entry(frame_main, width=entry_width)
        self.label_kg_f_m = tk.Label(frame_main, text='kg.f.m')
        self.entry_lb_f_ft = tk.Entry(frame_main, width=entry_width)
        self.label_lb_f_ft = tk.Label(frame_main, text='lb.f.ft')
        # And all their positions
        self.entry_N_m.grid(row=0, column=0, padx=(pad_ext, 0), pady=pad_ext)
        self.label_N_m.grid(row=0, column=1, padx=(0, 5*pad_ext), pady=pad_ext, sticky='w')
        self.entry_kN_m.grid(row=0, column=2, padx=pad_ext, pady=pad_ext)
        self.label_kN_m.grid(row=0, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_kg_f_m.grid(row=1, column=2, padx=pad_ext, pady=pad_ext)
        self.label_kg_f_m.grid(row=1, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_lb_f_ft.grid(row=2, column=2, padx=pad_ext, pady=pad_ext)
        self.label_lb_f_ft.grid(row=2, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        # Configurations for expansion
        frame_main.columnconfigure([0, 2], weight=1)
        # Bindings for each of the entries
        self.entry_N_m.bind('<KeyRelease>', lambda event: self.torqueConversion('N.m', float(self.entry_N_m.get())))
        self.entry_kN_m.bind('<KeyRelease>', lambda event: self.torqueConversion('kN.m', float(self.entry_kN_m.get())))
        self.entry_kg_f_m.bind('<KeyRelease>', lambda event: self.torqueConversion('kg.f.m', float(self.entry_kg_f_m.get())))
        self.entry_lb_f_ft.bind('<KeyRelease>', lambda event: self.torqueConversion('lb.f.ft', float(self.entry_lb_f_ft.get())))
        

    def torqueConversion(self, given_unit, quantity):  # To do all the converting on the window
        base = torqueToNm(given_unit, quantity)
        conversions = torqueFromNm(base)
        entries = {
            'N.m':self.entry_N_m, 
            'kN.m':self.entry_kN_m, 
            'kg.f.m':self.entry_kg_f_m, 
            'lb.f.ft':self.entry_lb_f_ft
            }
        del entries[given_unit]  # To remove the given unit from being edited
        
        for unit, entry in entries.items():
            conversion = conversions[unit]
            entry.delete(0, tk.END)
            entry.insert(0, f'{conversion:.3f}')


def torqueToNm(unit, quantity):  # This is to change to SI unit
    quantity = float(quantity)
    if unit == 'N.m':
        return quantity
    elif unit == 'kN.m':
        return quantity * 1000
    elif unit == 'kg.f.m':
        return quantity * 9.80665
    elif unit == 'lb.f.ft':
        return quantity * 1.35582


def torqueFromNm(quantity):  # To give out all the conversions
    n_m = quantity
    kn_m = quantity / 1000
    kg_f_m = quantity / 9.80665
    lb_f_ft = quantity / 1.35582
    return {'N.m': n_m, 'kN.m': kn_m, 'kg.f.m': kg_f_m, 'lb.f.ft': lb_f_ft}
