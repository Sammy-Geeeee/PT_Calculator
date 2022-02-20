# This will define the FrameCalcsFundPTR class


from units import *
from frameConvPower import *
from frameConvTorque import *
from frameConvRotationalSpeed import *
import tkinter as tk
from tkinter import StringVar, ttk
from sympy import symbols, solve


class FrameCalcsFundPTR(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # Some base variables for the sizing of various things
        pad_ext = 10
        entry_width = 1000
        label_width = 15
        # To make the main sub frame, just so I can grid everything
        frame_main = tk.Frame(master)
        frame_main.grid(row=6, column=0)
        # Configurations for expansion
        frame_main.columnconfigure([0, 2, 4], weight=1)
        

        # Widgets for this part
        label_PTR = tk.Label(frame_main, width=5*label_width, text='Power, Torque, Rotational Speed')
        label_P = tk.Label(frame_main, width=label_width, text='Power')
        label_T = tk.Label(frame_main, width=label_width, text='Torque')
        label_R = tk.Label(frame_main, width=label_width, text='Rotational Speed')
        self.entry_P = tk.Entry(frame_main, width=entry_width)
        self.entry_T = tk.Entry(frame_main, width=entry_width)
        self.entry_R = tk.Entry(frame_main, width=entry_width)
        sv_P, sv_T, sv_R = StringVar(), StringVar(), StringVar()
        options_P = ttk.OptionMenu(frame_main, sv_P, Units().power[0], *Units().power)
        options_T = ttk.OptionMenu(frame_main, sv_T, Units().torque[0], *Units().torque)
        options_R = ttk.OptionMenu(frame_main, sv_R, Units().rotational_speed[0], *Units().rotational_speed)
        # Positioning all of these widgets
        label_PTR.grid(row=0, column=0, columnspan=6, padx=pad_ext, pady=pad_ext)
        label_P.grid(row=1, column=0, columnspan=2, padx=pad_ext, pady=(pad_ext, 0))
        label_T.grid(row=1, column=2, columnspan=2, padx=pad_ext, pady=(pad_ext, 0))
        label_R.grid(row=1, column=4, columnspan=2, padx=pad_ext, pady=(pad_ext, 0))
        self.entry_P.grid(row=2, column=0, padx=pad_ext, pady=pad_ext)
        self.entry_T.grid(row=2, column=2, padx=pad_ext, pady=pad_ext)
        self.entry_R.grid(row=2, column=4, padx=pad_ext, pady=pad_ext)
        options_P.grid(row=2, column=1, padx=(0, 2*pad_ext), pady=pad_ext)
        options_T.grid(row=2, column=3, padx=(0, 2*pad_ext), pady=pad_ext)
        options_R.grid(row=2, column=5, padx=(0, 2*pad_ext), pady=pad_ext)
        # Bindings for the Entries
        self.entry_P.bind('<Return>', lambda event: self.ptrDisplay('P', self.entry_P.get(), sv_P.get(), self.entry_T.get(), sv_T.get(), self.entry_R.get(), sv_R.get()))
        self.entry_T.bind('<Return>', lambda event: self.ptrDisplay('T', self.entry_P.get(), sv_P.get(), self.entry_T.get(), sv_T.get(), self.entry_R.get(), sv_R.get()))
        self.entry_R.bind('<Return>', lambda event: self.ptrDisplay('R', self.entry_P.get(), sv_P.get(), self.entry_T.get(), sv_T.get(), self.entry_R.get(), sv_R.get()))


    def ptrDisplay(self, entry, p_qty, p_unit, t_qty, t_unit, r_qty, r_unit):
        # To provide a dummy value for the calculations to be performed
        if entry == 'P':
            l_qty = 1
        if entry == 'T':
            d_qty = 1
        if entry == 'R':
            r_qty = 1

        answers = ptrCalculations(p_qty, p_unit, t_qty, t_unit, r_qty, r_unit)

        if entry == 'P':
            self.entry_P.delete(0, tk.END)
            self.entry_P.insert(0, f"{answers['P']:.3f}")
        if entry == 'T':
            self.entry_T.delete(0, tk.END)
            self.entry_T.insert(0, f"{answers['T']:.3f}")
        if entry == 'R':
            self.entry_R.delete(0, tk.END)
            self.entry_R.insert(0, f"{answers['R']:.3f}")


def ptrCalculations(p_qty, p_unit, t_qty, t_unit, r_qty, r_unit):
    # To convert all the given units into their S.I unit equivalents
    p_si = powerToW(p_unit, p_qty)
    t_si = torqueToNm(t_unit, t_qty)
    r_si = rotationalSpeedTorads(r_unit, r_qty)

    # To make a symbolic equation for this
    P, T, R = symbols('P T R')
    equation = -P + T*R

    # To make different equations for each variable
    p_eq = solve(equation, P)[0]
    t_eq = solve(equation, T)[0]
    r_eq = solve(equation, R)[0]

    # To sub the given values into each equation
    p_calc = p_eq.subs({T:t_si, R:r_si})
    t_calc = t_eq.subs({P:p_si, R:r_si})
    r_calc = r_eq.subs({P:p_si, T:t_si})

    # To change the values back into the user selected unit
    p_conv = powerFromW(p_calc)[p_unit]
    t_conv = torqueFromNm(t_calc)[t_unit]
    r_conv = rotationalSpeedFromrads(r_calc)[r_unit]

    return {'P':p_conv, 'T':t_conv, 'R':r_conv}
