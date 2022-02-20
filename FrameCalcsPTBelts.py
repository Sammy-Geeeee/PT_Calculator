# This will define the FrameCalcsPTBelts class


from units import *
from frameConvDistance import *
import tkinter as tk
from tkinter import StringVar, ttk
from sympy import symbols, solve
from math import pi


class FrameCalcsPTBelts(tk.Frame):
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
        frame_main.columnconfigure([0, 2, 4, 6], weight=1)
        

        # Widgets for this part
        labelBelts = tk.Label(frame_main, width=5*label_width, text='Belt Length & Centres')
        label_L = tk.Label(frame_main, width=label_width, text='Belt Length')
        label_CD = tk.Label(frame_main, width=label_width, text='Centre Distance')
        label_D1 = tk.Label(frame_main, width=label_width, text='Diameter 1')
        label_D2 = tk.Label(frame_main, width=label_width, text='Diameter 2')
        self.entry_L = tk.Entry(frame_main, width=entry_width)
        self.entry_CD = tk.Entry(frame_main, width=entry_width)
        self.entry_D1 = tk.Entry(frame_main, width=entry_width)
        self.entry_D2 = tk.Entry(frame_main, width=entry_width)
        sv_L, sv_CD, sv_D1, sv_D2 = StringVar(), StringVar(), StringVar(), StringVar()
        options_L = ttk.OptionMenu(frame_main, sv_L, Units().distance[0], *Units().distance)
        options_CD = ttk.OptionMenu(frame_main, sv_CD, Units().distance[0], *Units().distance)
        options_D1 = ttk.OptionMenu(frame_main, sv_D1, Units().distance[0], *Units().distance)
        options_D2 = ttk.OptionMenu(frame_main, sv_D2, Units().distance[0], *Units().distance)
        # Positioning all of these widgets
        labelBelts.grid(row=0, column=0, columnspan=6, padx=pad_ext, pady=pad_ext)
        label_L.grid(row=1, column=0, columnspan=2, padx=pad_ext, pady=(pad_ext, 0))
        label_CD.grid(row=1, column=2, columnspan=2, padx=pad_ext, pady=(pad_ext, 0))
        label_D1.grid(row=1, column=4, columnspan=2, padx=pad_ext, pady=(pad_ext, 0))
        label_D2.grid(row=1, column=6, columnspan=2, padx=pad_ext, pady=(pad_ext, 0))
        self.entry_L.grid(row=2, column=0, padx=pad_ext, pady=pad_ext)
        self.entry_CD.grid(row=2, column=2, padx=pad_ext, pady=pad_ext)
        self.entry_D1.grid(row=2, column=4, padx=pad_ext, pady=pad_ext)
        self.entry_D2.grid(row=2, column=6, padx=pad_ext, pady=pad_ext)
        options_L.grid(row=2, column=1, padx=(0, 2*pad_ext), pady=pad_ext)
        options_CD.grid(row=2, column=3, padx=(0, 2*pad_ext), pady=pad_ext)
        options_D1.grid(row=2, column=5, padx=(0, 2*pad_ext), pady=pad_ext)
        options_D2.grid(row=2, column=7, padx=(0, 2*pad_ext), pady=pad_ext)
        # Bindings for the Entries
        self.entry_L.bind('<Return>', lambda event: self.beltsDisplay('L', self.entry_L.get(), sv_L.get(), self.entry_CD.get(), sv_CD.get(), self.entry_D1.get(), sv_D1.get(), self.entry_D2.get(), sv_D2.get()))
        self.entry_CD.bind('<Return>', lambda event: self.beltsDisplay('CD', self.entry_L.get(), sv_L.get(), self.entry_CD.get(), sv_CD.get(), self.entry_D1.get(), sv_D1.get(), self.entry_D2.get(), sv_D2.get()))
        self.entry_D1.bind('<Return>', lambda event: self.beltsDisplay('D1', self.entry_L.get(), sv_L.get(), self.entry_CD.get(), sv_CD.get(), self.entry_D1.get(), sv_D1.get(), self.entry_D2.get(), sv_D2.get()))
        self.entry_D2.bind('<Return>', lambda event: self.beltsDisplay('D2', self.entry_L.get(), sv_L.get(), self.entry_CD.get(), sv_CD.get(), self.entry_D1.get(), sv_D1.get(), self.entry_D2.get(), sv_D2.get()))


    def beltsDisplay(self, entry, l_qty, l_unit, cd_qty, cd_unit, d1_qty, d1_unit, d2_qty, d2_unit):
        # To provide a dummy value for the calculations to be performed
        if entry == 'L':
            l_qty = 1
        if entry == 'CD':
            cd_qty = 1
        if entry == 'D1':
            d1_qty = 1
        if entry == 'D2':
            d2_qty = 1

        answers = beltsCalculations(l_qty, l_unit, cd_qty, cd_unit, d1_qty, d1_unit, d2_qty, d2_unit)

        if entry == 'L':
            self.entry_L.delete(0, tk.END)
            self.entry_L.insert(0, f"{answers['L']:.3f}")
        if entry == 'CD':
            self.entry_CD.delete(0, tk.END)
            self.entry_CD.insert(0, f"{answers['CD']:.3f}")
        if entry == 'D1':
            self.entry_D1.delete(0, tk.END)
            self.entry_D1.insert(0, f"{answers['D1']:.3f}")
        if entry == 'D2':
            self.entry_D2.delete(0, tk.END)
            self.entry_D2.insert(0, f"{answers['D2']:.3f}")


def beltsCalculations(l_qty, l_unit, cd_qty, cd_unit, d1_qty, d1_unit, d2_qty, d2_unit):
    # To convert all the given units into their S.I unit equivalents
    cd_si = distanceTom(cd_unit, cd_qty)
    l_si = distanceTom(l_unit, l_qty)
    d1_si = distanceTom(d1_unit, d1_qty)
    d2_si = distanceTom(d2_unit, d2_qty)

    # To make a symbolic equation for this
    CD, L, D1, D2 = symbols('CD L D1 D2')
    equation = (-L) + (2*CD) + (pi*((D2+D1)/2)) + (((D2-D1)**2)/(4*CD))

    # To make different equations for each variable
    cd_eq = solve(equation, CD)[1]
    l_eq = solve(equation, L)[0]
    d1_eq = solve(equation, D1)[1]
    d2_eq = solve(equation, D2)[1]

    # To sub the given values into each equation
    cd_calc = cd_eq.subs({L:l_si, D1:d1_si, D2:d2_si})
    l_calc = l_eq.subs({CD:cd_si, D1:d1_si, D2:d2_si})
    d1_calc = d1_eq.subs({CD:cd_si, L:l_si, D2:d2_si})
    d2_calc = d2_eq.subs({CD:cd_si, L:l_si, D1:d1_si})

    # To change the values back into the user selected unit
    cd_conv = distanceFromm(cd_calc)[cd_unit]
    l_conv = distanceFromm(l_calc)[l_unit]
    d1_conv = distanceFromm(d1_calc)[d1_unit]
    d2_conv = distanceFromm(d2_calc)[d2_unit]

    return {'CD':cd_conv, 'L':l_conv, 'D1':d1_conv, 'D2':d2_conv}
