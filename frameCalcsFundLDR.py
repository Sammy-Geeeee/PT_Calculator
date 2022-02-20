# This will define the FrameCalcsFundLDR class


from units import *
from frameConvLinearSpeed import *
from frameConvDistance import *
from frameConvRotationalSpeed import *
import tkinter as tk
from tkinter import StringVar, ttk
from sympy import symbols, solve


class FrameCalcsFundLDR(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # Some base variables for the sizing of various things
        pad_ext = 10
        entry_width = 1000
        label_width = 15
        # To make the main sub frame, just so I can grid everything
        frame_main = tk.Frame(master)
        frame_main.grid(row=4, column=0)
        # Configurations for expansion
        frame_main.columnconfigure([0, 2, 4], weight=1)
        

        # Widgets for this part
        label_LDR = tk.Label(frame_main, width=5*label_width, text='Linear and Rotational Speed')
        label_L = tk.Label(frame_main, width=label_width, text='Linear Speed')
        label_D = tk.Label(frame_main, width=label_width, text='Diameter')
        label_R = tk.Label(frame_main, width=label_width, text='Rotational Speed')
        self.entry_L = tk.Entry(frame_main, width=entry_width)
        self.entry_D = tk.Entry(frame_main, width=entry_width)
        self.entry_R = tk.Entry(frame_main, width=entry_width)
        sv_L, sv_D, sv_R = StringVar(), StringVar(), StringVar()
        options_L = ttk.OptionMenu(frame_main, sv_L, Units().linear_speed[0], *Units().linear_speed)
        options_D = ttk.OptionMenu(frame_main, sv_D, Units().distance[0], *Units().distance)
        options_R = ttk.OptionMenu(frame_main, sv_R, Units().rotational_speed[0], *Units().rotational_speed)
        # Positioning all of these widgets
        label_LDR.grid(row=0, column=0, columnspan=6, padx=pad_ext, pady=pad_ext)
        label_L.grid(row=1, column=0, columnspan=2, padx=pad_ext, pady=(pad_ext, 0))
        label_D.grid(row=1, column=2, columnspan=2, padx=pad_ext, pady=(pad_ext, 0))
        label_R.grid(row=1, column=4, columnspan=2, padx=pad_ext, pady=(pad_ext, 0))
        self.entry_L.grid(row=2, column=0, padx=pad_ext, pady=pad_ext)
        self.entry_D.grid(row=2, column=2, padx=pad_ext, pady=pad_ext)
        self.entry_R.grid(row=2, column=4, padx=pad_ext, pady=pad_ext)
        options_L.grid(row=2, column=1, padx=(0, 2*pad_ext), pady=pad_ext)
        options_D.grid(row=2, column=3, padx=(0, 2*pad_ext), pady=pad_ext)
        options_R.grid(row=2, column=5, padx=(0, 2*pad_ext), pady=pad_ext)
        # Bindings for the Entries
        self.entry_L.bind('<Return>', lambda event: self.ldrDisplay('L', self.entry_L.get(), sv_L.get(), self.entry_D.get(), sv_D.get(), self.entry_R.get(), sv_R.get()))
        self.entry_D.bind('<Return>', lambda event: self.ldrDisplay('D', self.entry_L.get(), sv_L.get(), self.entry_D.get(), sv_D.get(), self.entry_R.get(), sv_R.get()))
        self.entry_R.bind('<Return>', lambda event: self.ldrDisplay('R', self.entry_L.get(), sv_L.get(), self.entry_D.get(), sv_D.get(), self.entry_R.get(), sv_R.get()))


    def ldrDisplay(self, entry, l_qty, l_unit, d_qty, d_unit, r_qty, r_unit):
        # To provide a dummy value for the calculations to be performed
        if entry == 'L':
            l_qty = 1
        if entry == 'D':
            d_qty = 1
        if entry == 'R':
            r_qty = 1

        answers = ldrCalculations(l_qty, l_unit, d_qty, d_unit, r_qty, r_unit)

        if entry == 'L':
            self.entry_L.delete(0, tk.END)
            self.entry_L.insert(0, f"{answers['L']:.3f}")
        if entry == 'D':
            self.entry_D.delete(0, tk.END)
            self.entry_D.insert(0, f"{answers['D']:.3f}")
        if entry == 'R':
            self.entry_R.delete(0, tk.END)
            self.entry_R.insert(0, f"{answers['R']:.3f}")


def ldrCalculations(l_qty, l_unit, d_qty, d_unit, r_qty, r_unit):
    # To convert all the given units into their S.I unit equivalents
    l_si = linearSpeedToms(l_unit, l_qty)
    d_si = distanceTom(d_unit, d_qty)
    r_si = rotationalSpeedTorads(r_unit, r_qty)

    # To make a symbolic equation for this
    L, D, R = symbols('L D R')
    equation = -L + (D/2) * R

    # To make different equations for each variable
    l_eq = solve(equation, L)[0]
    d_eq = solve(equation, D)[0]
    r_eq = solve(equation, R)[0]

    # To sub the given values into each equation
    l_calc = l_eq.subs({D:d_si, R:r_si})
    d_calc = d_eq.subs({L:l_si, R:r_si})
    r_calc = r_eq.subs({L:l_si, D:d_si})

    # To change the values back into the user selected unit
    l_conv = linearSpeedFromms(l_calc)[l_unit]
    d_conv = distanceFromm(d_calc)[d_unit]
    r_conv = rotationalSpeedFromrads(r_calc)[r_unit]

    return {'L':l_conv, 'D':d_conv, 'R':r_conv}
