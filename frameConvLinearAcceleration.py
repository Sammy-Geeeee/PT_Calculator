# This will define the FrameConvLinearAcceleration class


import tkinter as tk


class FrameConvLinearAcceleration(tk.Frame):
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
        self.entry_m_s_s = tk.Entry(frame_main, width=entry_width)
        self.label_m_s_s = tk.Label(frame_main, width=label_width, text='m/s/s')
        self.entry_m_s_min = tk.Entry(frame_main, width=entry_width)
        self.label_m_s_min = tk.Label(frame_main, text='m/s/min')
        self.entry_km_hr_s = tk.Entry(frame_main, width=entry_width)
        self.label_km_hr_s = tk.Label(frame_main, text='km/hr/s')
        self.entry_km_hr_min = tk.Entry(frame_main, width=entry_width)
        self.label_km_hr_min = tk.Label(frame_main, text='km/hr/min')
        self.entry_km_hr_hr = tk.Entry(frame_main, width=entry_width)
        self.label_km_hr_hr = tk.Label(frame_main, text='km/hr/hr')
        self.entry_ft_s_s = tk.Entry(frame_main, width=entry_width)
        self.label_ft_s_s = tk.Label(frame_main, text='ft/s/s')
        self.entry_ft_s_min = tk.Entry(frame_main, width=entry_width)
        self.label_ft_s_min = tk.Label(frame_main, text='ft/s/min')
        self.entry_mi_hr_s = tk.Entry(frame_main, width=entry_width)
        self.label_mi_hr_s = tk.Label(frame_main, text='mi/hr/s')
        self.entry_mi_hr_min = tk.Entry(frame_main, width=entry_width)
        self.label_mi_hr_min = tk.Label(frame_main, text='mi/hr/min')
        self.entry_mi_hr_hr = tk.Entry(frame_main, width=entry_width)
        self.label_mi_hr_hr = tk.Label(frame_main, text='mi/hr/hr')
        # And all their positions
        self.entry_m_s_s.grid(row=0, column=0, padx=(pad_ext, 0), pady=pad_ext)
        self.label_m_s_s.grid(row=0, column=1, padx=(0, 5*pad_ext), pady=pad_ext, sticky='w')
        self.entry_m_s_min.grid(row=0, column=2, padx=pad_ext, pady=pad_ext)
        self.label_m_s_min.grid(row=0, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_km_hr_s.grid(row=1, column=2, padx=pad_ext, pady=pad_ext)
        self.label_km_hr_s.grid(row=1, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_km_hr_min.grid(row=2, column=2, padx=pad_ext, pady=pad_ext)
        self.label_km_hr_min.grid(row=2, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_km_hr_hr.grid(row=3, column=2, padx=pad_ext, pady=pad_ext)
        self.label_km_hr_hr.grid(row=3, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_ft_s_s.grid(row=4, column=2, padx=pad_ext, pady=pad_ext)
        self.label_ft_s_s.grid(row=4, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_ft_s_min.grid(row=5, column=2, padx=pad_ext, pady=pad_ext)
        self.label_ft_s_min.grid(row=5, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_mi_hr_s.grid(row=6, column=2, padx=pad_ext, pady=pad_ext)
        self.label_mi_hr_s.grid(row=6, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_mi_hr_min.grid(row=7, column=2, padx=pad_ext, pady=pad_ext)
        self.label_mi_hr_min.grid(row=7, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        self.entry_mi_hr_hr.grid(row=8, column=2, padx=pad_ext, pady=pad_ext)
        self.label_mi_hr_hr.grid(row=8, column=3, padx=(0, pad_ext), pady=pad_ext, sticky='w')
        # Configurations for expansion
        frame_main.columnconfigure([0, 2], weight=1)
        # Bindings for each of the entries
        self.entry_m_s_s.bind('<KeyRelease>', lambda event: self.linearAccelerationConversion('m/s/s', float(self.entry_m_s_s.get())))
        self.entry_m_s_min.bind('<KeyRelease>', lambda event: self.linearAccelerationConversion('m/s/min', float(self.entry_m_s_min.get())))
        self.entry_km_hr_s.bind('<KeyRelease>', lambda event: self.linearAccelerationConversion('km/hr/s', float(self.entry_km_hr_s.get())))
        self.entry_km_hr_min.bind('<KeyRelease>', lambda event: self.linearAccelerationConversion('km/hr/min', float(self.entry_km_hr_min.get())))
        self.entry_km_hr_hr.bind('<KeyRelease>', lambda event: self.linearAccelerationConversion('km/hr/hr', float(self.entry_km_hr_hr.get())))
        self.entry_ft_s_s.bind('<KeyRelease>', lambda event: self.linearAccelerationConversion('ft/s/s', float(self.entry_ft_s_s.get())))
        self.entry_ft_s_min.bind('<KeyRelease>', lambda event: self.linearAccelerationConversion('ft/s/min', float(self.entry_ft_s_min.get())))
        self.entry_mi_hr_s.bind('<KeyRelease>', lambda event: self.linearAccelerationConversion('mi/hr/s', float(self.entry_mi_hr_s.get())))
        self.entry_mi_hr_min.bind('<KeyRelease>', lambda event: self.linearAccelerationConversion('mi/hr/min', float(self.entry_mi_hr_min.get())))
        self.entry_mi_hr_hr.bind('<KeyRelease>', lambda event: self.linearAccelerationConversion('mi/hr/hr', float(self.entry_mi_hr_hr.get())))
    

    def linearAccelerationConversion(self, given_unit, quantity):  # To do all the converting on the window
        base = linearAccelerationTomss(given_unit, quantity)
        conversions = linearAccelerationFrommss(base)
        entries = {
            'm/s/s':self.entry_m_s_s, 
            'm/s/min':self.entry_m_s_min, 
            'km/hr/s':self.entry_km_hr_s, 
            'km/hr/min':self.entry_km_hr_min, 
            'km/hr/hr':self.entry_km_hr_hr, 
            'ft/s/s':self.entry_ft_s_s, 
            'ft/s/min':self.entry_ft_s_min, 
            'mi/hr/s':self.entry_mi_hr_s, 
            'mi/hr/min':self.entry_mi_hr_min, 
            'mi/hr/hr':self.entry_mi_hr_hr
            }
        del entries[given_unit]  # To remove the given unit from being edited
        
        for unit, entry in entries.items():
            conversion = conversions[unit]
            entry.delete(0, tk.END)
            entry.insert(0, f'{conversion:.3f}')


def linearAccelerationTomss(unit, quantity):  # This is to change to SI unit
    quantity = float(quantity)
    if unit == 'm/s/s':
        return quantity
    elif unit == 'm/s/min':
        return quantity / 60
    elif unit == 'km/hr/s':
        return quantity / 3.6
    elif unit == 'km/hr/min':
        return quantity / 3.6 / 60
    elif unit == 'km/hr/hr':
        return quantity / 3.6 / 60 / 60
    elif unit == 'ft/s/s':
        return quantity / 3.28084
    elif unit == 'ft/s/min':
        return quantity / 3.28084 / 60
    elif unit == 'mi/hr/s':
        return quantity / 2.23694
    elif unit == 'mi/hr/min':
        return quantity / 2.23694 / 60
    elif unit == 'mi/hr/hr':
        return quantity / 2.23694 / 60 / 60


def linearAccelerationFrommss(quantity):  # To give out all the conversions
    m_s_s = quantity
    m_s_min = quantity * 60
    km_hr_s = quantity * 3.6
    km_hr_min = quantity * 3.6 * 60
    km_hr_hr = quantity * 3.6 * 60 * 60
    ft_s_s = quantity * 3.28084
    ft_s_min = quantity * 3.28084 * 60
    mi_hr_s = quantity * 2.23694
    mi_hr_min = quantity * 2.23694 * 60
    mi_hr_hr = quantity * 2.3694 * 60 * 60
    return {'m/s/s':m_s_s, 'm/s/min':m_s_min, 'km/hr/s':km_hr_s, 'km/hr/min':km_hr_min, 'km/hr/hr':km_hr_hr, 'ft/s/s':ft_s_s, 'ft/s/min':ft_s_min, 'mi/hr/s':mi_hr_s, 'mi/hr/min':mi_hr_min, 'mi/hr/hr':mi_hr_hr}
    