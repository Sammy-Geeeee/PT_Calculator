# This will define the FrameCalcsPTTeeth class


from units import *
from frameConvDistance import *
import tkinter as tk
from tkinter import StringVar, ttk
from sympy import symbols, solve
from math import pi


class FrameCalcsPTTeeth(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # Some base variables for the sizing of various things
        pad_ext = 10
        entry_width = 1000
        label_width = 15
        # To make the main sub frame, just so I can grid everything
        frame_main = tk.Frame(master)
        frame_main.grid(row=2, column=0)
        # Configurations for expansion
        frame_main.columnconfigure([0, 2, 4, 6], weight=1)
        

        # Widgets for this part
        labelTeeth = tk.Label(frame_main, width=5*label_width, text='PCD, Pitch, Number of Teeth')
        label_PCD = tk.Label(frame_main, width=label_width, text='PCD')
        label_P = tk.Label(frame_main, width=label_width, text='Pitch')
        label_T = tk.Label(frame_main, width=label_width, text='Teeth (n)')
        self.entry_PCD = tk.Entry(frame_main, width=entry_width)
        self.entry_P = tk.Entry(frame_main, width=entry_width)
        self.entry_T = tk.Entry(frame_main, width=entry_width)
        sv_PCD, sv_P = StringVar(), StringVar()
        options_PCD = ttk.OptionMenu(frame_main, sv_PCD, Units().distance[0], *Units().distance)
        options_P = ttk.OptionMenu(frame_main, sv_P, Units().distance[0], *Units().distance)
        # Positioning all of these widgets
        labelTeeth.grid(row=0, column=0, columnspan=6, padx=pad_ext, pady=pad_ext)
        label_PCD.grid(row=1, column=0, columnspan=2, padx=pad_ext, pady=(pad_ext, 0))
        label_P.grid(row=1, column=2, columnspan=2, padx=pad_ext, pady=(pad_ext, 0))
        label_T.grid(row=1, column=4, columnspan=2, padx=pad_ext, pady=(pad_ext, 0))
        self.entry_PCD.grid(row=2, column=0, padx=pad_ext, pady=pad_ext)
        self.entry_P.grid(row=2, column=2, padx=pad_ext, pady=pad_ext)
        self.entry_T.grid(row=2, column=4, padx=pad_ext, pady=pad_ext)
        options_PCD.grid(row=2, column=1, padx=(0, 2*pad_ext), pady=pad_ext)
        options_P.grid(row=2, column=3, padx=(0, 2*pad_ext), pady=pad_ext)
        # Bindings for the Entries
        self.entry_PCD.bind('<Return>', lambda event: self.teethDisplay('PCD', self.entry_PCD.get(), sv_PCD.get(), self.entry_P.get(), sv_P.get(), self.entry_T.get()))
        self.entry_P.bind('<Return>', lambda event: self.teethDisplay('P', self.entry_PCD.get(), sv_PCD.get(), self.entry_P.get(), sv_P.get(), self.entry_T.get()))
        self.entry_T.bind('<Return>', lambda event: self.teethDisplay('T', self.entry_PCD.get(), sv_PCD.get(), self.entry_P.get(), sv_P.get(), self.entry_T.get()))


    def teethDisplay(self, entry, pcd_qty, pcd_unit, p_qty, p_unit, t_qty):
        # To provide a dummy value for the calculations to be performed
        if entry == 'PCD':
            pcd_qty = 1
        if entry == 'P':
            p_qty = 1
        if entry == 'T':
            t_qty = 1

        answers = teethCalculations(pcd_qty, pcd_unit, p_qty, p_unit, t_qty)

        if entry == 'PCD':
            self.entry_PCD.delete(0, tk.END)
            self.entry_PCD.insert(0, f"{answers['PCD']:.3f}")
        if entry == 'P':
            self.entry_P.delete(0, tk.END)
            self.entry_P.insert(0, f"{answers['P']:.3f}")
        if entry == 'T':
            self.entry_T.delete(0, tk.END)
            self.entry_T.insert(0, f"{answers['T']:.3f}")


def teethCalculations(pcd_qty, pcd_unit, p_qty, p_unit, t_qty):
    # To convert all the given units into their S.I unit equivalents
    pcd_si = distanceTom(pcd_unit, pcd_qty)
    p_si = distanceTom(p_unit, p_qty)
    t_si = t_qty

    # To make a symbolic equation for this
    PCD, P, T = symbols('PCD P T')
    equation = -PCD + (P * T)/pi

    # To make different equations for each variable
    pcd_eq = solve(equation, PCD)[0]
    p_eq = solve(equation, P)[0]
    t_eq = solve(equation, T)[0]

    # To sub the given values into each equation
    pcd_calc = pcd_eq.subs({P:p_si, T:t_si})
    p_calc = p_eq.subs({PCD:pcd_si, T:t_si})
    t_calc = t_eq.subs({PCD:pcd_si, P:p_si})

    # To change the values back into the user selected unit
    pcd_conv = distanceFromm(pcd_calc)[pcd_unit]
    p_conv = distanceFromm(p_calc)[p_unit]
    t_conv = t_calc

    return {'PCD':pcd_conv, 'P':p_conv, 'T':t_conv}
