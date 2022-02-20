# This will define the FrameConvLinearSpeed class


import tkinter as tk


class FrameConvLinearSpeed(tk.Frame):
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
        self.entry_m_s = tk.Entry(frame_main, width=entry_width)
        self.label_m_s = tk.Label(frame_main, width=label_width, text='m/s')
        self.entry_m_min = tk.Entry(frame_main, width=entry_width)
        self.label_m_min = tk.Label(frame_main, text='m/min')
        self.entry_mm_s = tk.Entry(frame_main, width=entry_width)
        self.label_mm_s = tk.Label(frame_main, text='mm/s')
        self.entry_mm_min = tk.Entry(frame_main, width=entry_width)
        self.label_mm_min = tk.Label(frame_main, text='mm/min')
        self.entry_km_hr = tk.Entry(frame_main, width=entry_width)
        self.label_km_hr = tk.Label(frame_main, text='km/hr')
        self.entry_ft_s = tk.Entry(frame_main, width=entry_width)
        self.label_ft_s = tk.Label(frame_main, text='ft/s')
        self.entry_mi_h = tk.Entry(frame_main, width=entry_width)
        self.label_mi_h = tk.Label(frame_main, text='mi/hr')
        # And all their positions
        self.entry_m_s.grid(row=0, column=0, padx=(pad_ext, 0), pady=pad_ext)
        self.label_m_s.grid(row=0, column=1, padx=(0, 5*pad_ext), pady=pad_ext, sticky='w')
        self.entry_m_min.grid(row=0, column=2, padx=pad_ext, pady=pad_ext)
        self.label_m_min.grid(row=0, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_mm_s.grid(row=1, column=2, padx=pad_ext, pady=pad_ext)
        self.label_mm_s.grid(row=1, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_mm_min.grid(row=2, column=2, padx=pad_ext, pady=pad_ext)
        self.label_mm_min.grid(row=2, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_km_hr.grid(row=3, column=2, padx=pad_ext, pady=pad_ext)
        self.label_km_hr.grid(row=3, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_ft_s.grid(row=4, column=2, padx=pad_ext, pady=pad_ext)
        self.label_ft_s.grid(row=4, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_mi_h.grid(row=5, column=2, padx=pad_ext, pady=pad_ext)
        self.label_mi_h.grid(row=5, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        # Configurations for expansion
        frame_main.columnconfigure([0, 2], weight=1)
        # Bindings for each of the entries
        self.entry_m_s.bind('<KeyRelease>', lambda event: self.linearSpeedConversion('m/s', float(self.entry_m_s.get())))
        self.entry_m_min.bind('<KeyRelease>', lambda event: self.linearSpeedConversion('m/min', float(self.entry_m_min.get())))
        self.entry_mm_s.bind('<KeyRelease>', lambda event: self.linearSpeedConversion('mm/s', float(self.entry_mm_s.get())))
        self.entry_mm_min.bind('<KeyRelease>', lambda event: self.linearSpeedConversion('mm/min', float(self.entry_mm_min.get())))
        self.entry_km_hr.bind('<KeyRelease>', lambda event: self.linearSpeedConversion('km/hr', float(self.entry_km_hr.get())))
        self.entry_ft_s.bind('<KeyRelease>', lambda event: self.linearSpeedConversion('ft/s', float(self.entry_ft_s.get())))
        self.entry_mi_h.bind('<KeyRelease>', lambda event: self.linearSpeedConversion('mi/hr', float(self.entry_mi_h.get())))
    

    def linearSpeedConversion(self, given_unit, quantity):  # To do all the converting on the window
        base = linearSpeedToms(given_unit, quantity)
        conversions = linearSpeedFromms(base)
        entries = {
            'm/s':self.entry_m_s, 
            'm/min':self.entry_m_min, 
            'mm/s':self.entry_mm_s, 
            'mm/min':self.entry_mm_min, 
            'km/hr':self.entry_km_hr, 
            'ft/s':self.entry_ft_s, 
            'mi/hr':self.entry_mi_h
            }
        del entries[given_unit]  # To remove the given unit from being edited
        
        for unit, entry in entries.items():
            conversion = conversions[unit]
            entry.delete(0, tk.END)
            entry.insert(0, f'{conversion:.3f}')


def linearSpeedToms(unit, quantity):  # This is to change to SI unit
    quantity = float(quantity)
    if unit == 'm/s':
        return quantity
    elif unit == 'm/min':
        return quantity / 60
    elif unit == 'mm/s':
        return quantity / 1000
    elif unit == 'mm/min':
        return quantity / 1000 / 60
    elif unit == 'km/hr':
        return quantity / 3.6
    elif unit == 'ft/s':
        return quantity / 3.28084
    elif unit == 'mi/hr':
        return quantity / 2.23694


def linearSpeedFromms(quantity):  # To give out all the conversions
    m_s = quantity
    m_min = quantity * 60
    mm_s = quantity * 1000
    mm_min = quantity * 60 * 1000
    km_hr = quantity * 3.6
    ft_s = quantity * 3.2808
    mi_hr = quantity * 2.23694
    return {'m/s':m_s, 'm/min':m_min, 'mm/s':mm_s, 'mm/min':mm_min, 'km/hr':km_hr, 'ft/s':ft_s, 'mi/hr':mi_hr}
