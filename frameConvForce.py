# This will define the FrameConvForce class


import tkinter as tk


class FrameConvForce(tk.Frame):
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
        self.entry_N = tk.Entry(frame_main, width=entry_width)
        self.label_N = tk.Label(frame_main, width=label_width, text='N')
        self.entry_kN = tk.Entry(frame_main, width=entry_width)
        self.label_kN = tk.Label(frame_main, text='kN')
        self.entry_kg_f = tk.Entry(frame_main, width=entry_width)
        self.label_kg_f = tk.Label(frame_main, text='kg.f')
        self.entry_T_f = tk.Entry(frame_main, width=entry_width)
        self.label_T_f = tk.Label(frame_main, text='T.f')
        self.entry_lb_f = tk.Entry(frame_main, width=entry_width)
        self.label_lb_f = tk.Label(frame_main, text='lb.f')
        # And all their positions
        self.entry_N.grid(row=0, column=0, padx=(pad_ext, 0), pady=pad_ext)
        self.label_N.grid(row=0, column=1, padx=(0, 5*pad_ext), pady=pad_ext, sticky='w')
        self.entry_kN.grid(row=0, column=2, padx=pad_ext, pady=pad_ext)
        self.label_kN.grid(row=0, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_kg_f.grid(row=1, column=2, padx=pad_ext, pady=pad_ext)
        self.label_kg_f.grid(row=1, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_T_f.grid(row=2, column=2, padx=pad_ext, pady=pad_ext)
        self.label_T_f.grid(row=2, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_lb_f.grid(row=3, column=2, padx=pad_ext, pady=pad_ext)
        self.label_lb_f.grid(row=3, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        # Configurations for expansion
        frame_main.columnconfigure([0, 2], weight=1)
        # Bindings for each of the entries
        self.entry_N.bind('<KeyRelease>', lambda event: self.forceConversion('N', float(self.entry_N.get())))
        self.entry_kN.bind('<KeyRelease>', lambda event: self.forceConversion('kN', float(self.entry_kN.get())))
        self.entry_kg_f.bind('<KeyRelease>', lambda event: self.forceConversion('kg.f', float(self.entry_kg_f.get())))
        self.entry_T_f.bind('<KeyRelease>', lambda event: self.forceConversion('T.f', float(self.entry_T_f.get())))
        self.entry_lb_f.bind('<KeyRelease>', lambda event: self.forceConversion('lb.f', float(self.entry_lb_f.get())))
    

    def forceConversion(self, given_unit, quantity):  # To do all the converting on the window
        base = forceToN(given_unit, quantity)
        conversions = forceFromN(base)
        entries = {
            'N':self.entry_N, 
            'kN':self.entry_kN, 
            'kg.f':self.entry_kg_f, 
            'T.f':self.entry_T_f,
            'lb.f':self.entry_lb_f
            }
        del entries[given_unit]  # To remove the given unit from being edited
        
        for unit, entry in entries.items():
            conversion = conversions[unit]
            entry.delete(0, tk.END)
            entry.insert(0, f'{conversion:.3f}')


def forceToN(unit, quantity):  # This is to change to SI unit
    quantity = float(quantity)
    if unit == 'N':
        return quantity
    elif unit == 'kN':
        return quantity * 1000
    elif unit == 'kg.f':
        return quantity * 9.80665
    elif unit == 'T.f':
        return quantity * 9.80665 * 1000
    elif unit == 'lb.f':
        return quantity * 4.44822


def forceFromN(quantity):  # To give out all the conversions
    n = quantity
    kn = quantity / 1000
    kg_f = quantity / 9.80665
    T_f = quantity / 9.80665 / 1000
    lb_f = quantity / 4.44822
    return {'N':n, 'kN':kn, 'kg.f':kg_f, 'T.f':T_f, 'lb.f':lb_f}
