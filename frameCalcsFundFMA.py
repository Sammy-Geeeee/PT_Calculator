# This will define the FrameCalcsFundFMA class


from units import *
from frameConvMass import *
from frameConvLinearAcceleration import *
from frameConvForce import *
import tkinter as tk
from tkinter import StringVar, ttk
from sympy import symbols, solve


class FrameCalcsFundFMA(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # Some base variables for the sizing of various things
        pad_ext = 10
        entry_width = 1000
        label_width = 15
        # To make the main sub frame, just so I can grid everything
        frame_main = tk.Frame(master)
        frame_main.grid(row=0, column=0)
        # Configurations for expansion
        frame_main.columnconfigure([0, 2, 4], weight=1)
        

        # Widgets for this part
        label_FMA = tk.Label(frame_main, width=5*label_width, text='Force, Mass, Acceleration')
        label_F = tk.Label(frame_main, width=label_width, text='Force')
        label_M = tk.Label(frame_main, width=label_width, text='Mass')
        label_A = tk.Label(frame_main, width=label_width, text='Acceleration')
        self.entry_F = tk.Entry(frame_main, width=entry_width)
        self.entry_M = tk.Entry(frame_main, width=entry_width)
        self.entry_A = tk.Entry(frame_main, width=entry_width)
        sv_F, sv_M, sv_A = StringVar(), StringVar(), StringVar()
        options_F = ttk.OptionMenu(frame_main, sv_F, Units().force[0], *Units().force)
        options_M = ttk.OptionMenu(frame_main, sv_M, Units().mass[0], *Units().mass)
        options_A = ttk.OptionMenu(frame_main, sv_A, Units().linear_acceleration[0], *Units().linear_acceleration)
        # Positioning all of these widgets
        label_FMA.grid(row=0, column=0, columnspan=6, padx=pad_ext, pady=pad_ext)
        label_F.grid(row=1, column=0, columnspan=2, padx=pad_ext, pady=(pad_ext, 0))
        label_M.grid(row=1, column=2, columnspan=2, padx=pad_ext, pady=(pad_ext, 0))
        label_A.grid(row=1, column=4, columnspan=2, padx=pad_ext, pady=(pad_ext, 0))
        self.entry_F.grid(row=2, column=0, padx=pad_ext, pady=pad_ext)
        self.entry_M.grid(row=2, column=2, padx=pad_ext, pady=pad_ext)
        self.entry_A.grid(row=2, column=4, padx=pad_ext, pady=pad_ext)
        options_F.grid(row=2, column=1, padx=(0, 2*pad_ext), pady=pad_ext)
        options_M.grid(row=2, column=3, padx=(0, 2*pad_ext), pady=pad_ext)
        options_A.grid(row=2, column=5, padx=(0, 2*pad_ext), pady=pad_ext)
        # Bindings for the Entries
        self.entry_F.bind('<Return>', lambda event: self.fmaDisplay('F', self.entry_F.get(), sv_F.get(), self.entry_M.get(), sv_M.get(), self.entry_A.get(), sv_A.get()))
        self.entry_M.bind('<Return>', lambda event: self.fmaDisplay('M', self.entry_F.get(), sv_F.get(), self.entry_M.get(), sv_M.get(), self.entry_A.get(), sv_A.get()))
        self.entry_A.bind('<Return>', lambda event: self.fmaDisplay('A', self.entry_F.get(), sv_F.get(), self.entry_M.get(), sv_M.get(), self.entry_A.get(), sv_A.get()))



    def fmaDisplay(self, entry, f_qty, f_unit, m_qty, m_unit, a_qty, a_unit):
        # To provide a dummy value for the calculations to be performed
        if entry == 'F':
            f_qty = 1
        if entry == 'M':
            m_qty = 1
        if entry == 'A':
            a_qty = 1

        answers = fmaCalculations(f_qty, f_unit, m_qty, m_unit, a_qty, a_unit)

        if entry == 'F':
            self.entry_F.delete(0, tk.END)
            self.entry_F.insert(0, f"{answers['F']:.3f}")
        if entry == 'M':
            self.entry_M.delete(0, tk.END)
            self.entry_M.insert(0, f"{answers['M']:.3f}")
        if entry == 'A':
            self.entry_A.delete(0, tk.END)
            self.entry_A.insert(0, f"{answers['A']:.3f}")


def fmaCalculations(f_qty, f_unit, m_qty, m_unit, a_qty, a_unit):
    # To convert all the given units into their S.I unit equivalents
    f_si = forceToN(f_unit, f_qty)
    m_si = massTokg(m_unit, m_qty)
    a_si = linearAccelerationTomss(a_unit, a_qty)

    # To make a symbolic equation for this
    F, M, A = symbols('F M A')
    equation = -F + M*A

    # To make different equations for each variable
    f_eq = solve(equation, F)[0]
    m_eq = solve(equation, M)[0]
    a_eq = solve(equation, A)[0]

    # To sub the given values into each equation
    f_calc = f_eq.subs({M:m_si, A:a_si})
    m_calc = m_eq.subs({F:f_si, A:a_si})
    a_calc = a_eq.subs({F:f_si, M:m_si})

    # To change the values back into the user selected unit
    f_conv = forceFromN(f_calc)[f_unit]
    m_conv = massFromkg(m_calc)[m_unit]
    a_conv = linearAccelerationFrommss(a_calc)[a_unit]

    return {'F':f_conv, 'M':m_conv, 'A':a_conv}
