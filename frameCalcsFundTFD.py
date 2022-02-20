# This will define the FrameCalcsFundTFD class


from units import *
from frameConvDistance import *
from frameConvForce import *
from frameConvTorque import *
import tkinter as tk
from tkinter import StringVar, ttk
from sympy import symbols, solve


class FrameCalcsFundTFD(tk.Frame):
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
        frame_main.columnconfigure([0, 2, 4], weight=1)
        

        # Widgets for this part
        label_TFD = tk.Label(frame_main, width=5*label_width, text='Torque, Force, Diameter')
        label_T = tk.Label(frame_main, width=label_width, text='Torque')
        label_F = tk.Label(frame_main, width=label_width, text='Force')
        label_D = tk.Label(frame_main, width=label_width, text='Diameter')
        self.entry_T = tk.Entry(frame_main, width=entry_width)
        self.entry_F = tk.Entry(frame_main, width=entry_width)
        self.entry_D = tk.Entry(frame_main, width=entry_width)
        sv_T, sv_F, sv_D = StringVar(), StringVar(), StringVar()
        options_T = ttk.OptionMenu(frame_main, sv_T, Units().torque[0], *Units().torque)
        options_F = ttk.OptionMenu(frame_main, sv_F, Units().force[0], *Units().force)
        options_D = ttk.OptionMenu(frame_main, sv_D, Units().distance[0], *Units().distance)
        # Positioning all of these widgets
        label_TFD.grid(row=0, column=0, columnspan=6, padx=pad_ext, pady=pad_ext)
        label_T.grid(row=1, column=0, columnspan=2, padx=pad_ext, pady=(pad_ext, 0))
        label_F.grid(row=1, column=2, columnspan=2, padx=pad_ext, pady=(pad_ext, 0))
        label_D.grid(row=1, column=4, columnspan=2, padx=pad_ext, pady=(pad_ext, 0))
        self.entry_T.grid(row=2, column=0, padx=pad_ext, pady=pad_ext)
        self.entry_F.grid(row=2, column=2, padx=pad_ext, pady=pad_ext)
        self.entry_D.grid(row=2, column=4, padx=pad_ext, pady=pad_ext)
        options_T.grid(row=2, column=1, padx=(0, 2*pad_ext), pady=pad_ext)
        options_F.grid(row=2, column=3, padx=(0, 2*pad_ext), pady=pad_ext)
        options_D.grid(row=2, column=5, padx=(0, 2*pad_ext), pady=pad_ext)
        # Bindings for the Entries
        self.entry_T.bind('<Return>', lambda event: self.tfdDisplay('T', self.entry_T.get(), sv_T.get(), self.entry_F.get(), sv_F.get(), self.entry_D.get(), sv_D.get()))
        self.entry_F.bind('<Return>', lambda event: self.tfdDisplay('F', self.entry_T.get(), sv_T.get(), self.entry_F.get(), sv_F.get(), self.entry_D.get(), sv_D.get()))
        self.entry_D.bind('<Return>', lambda event: self.tfdDisplay('D', self.entry_T.get(), sv_T.get(), self.entry_F.get(), sv_F.get(), self.entry_D.get(), sv_D.get()))



    def tfdDisplay(self, entry, t_qty, t_unit, f_qty, f_unit, d_qty, d_unit):
        # To provide a dummy value for the calculations to be performed
        if entry == 'T':
            t_qty = 1
        if entry == 'F':
            f_qty = 1
        if entry == 'D':
            d_qty = 1

        answers = tfdCalculations(t_qty, t_unit, f_qty, f_unit, d_qty, d_unit)

        if entry == 'T':
            self.entry_T.delete(0, tk.END)
            self.entry_T.insert(0, f"{answers['T']:.3f}")
        if entry == 'F':
            self.entry_F.delete(0, tk.END)
            self.entry_F.insert(0, f"{answers['F']:.3f}")
        if entry == 'D':
            self.entry_D.delete(0, tk.END)
            self.entry_D.insert(0, f"{answers['D']:.3f}")


def tfdCalculations(t_qty, t_unit, f_qty, f_unit, d_qty, d_unit):
    # To convert all the given units into their S.I unit equivalents
    t_si = torqueToNm(t_unit, t_qty)
    f_si = forceToN(f_unit, f_qty)
    d_si = distanceTom(d_unit, d_qty)

    # To make a symbolic equation for this
    T, F, D = symbols('T F D')
    equation = -T + F*D/2

    # To make different equations for each variable
    t_eq = solve(equation, T)[0]
    f_eq = solve(equation, F)[0]
    d_eq = solve(equation, D)[0]

    # To sub the given values into each equation
    t_calc = t_eq.subs({F:f_si, D:d_si})
    f_calc = f_eq.subs({T:t_si, D:d_si})
    d_calc = d_eq.subs({T:t_si, F:f_si})

    # To change the values back into the user selected unit
    t_conv = torqueFromNm(t_calc)[t_unit]
    f_conv = forceFromN(f_calc)[f_unit]
    d_conv = distanceFromm(d_calc)[d_unit]

    return {'T':t_conv, 'F':f_conv, 'D':d_conv}
