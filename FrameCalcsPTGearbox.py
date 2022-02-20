# This will define the FrameCalcsPTGearbox class


from units import *
from frameConvDistance import *
from frameConvPower import *
from frameConvRotationalSpeed import *
from frameConvTorque import *
import tkinter as tk
from tkinter import StringVar, ttk
from sympy import symbols, solve


class FrameCalcsPTGearbox(tk.Frame):
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
        frame_main.columnconfigure([0, 2, 4, 6, 7], weight=1)
        

        # Widgets for this part
        labelGearbox = tk.Label(frame_main, width=5*label_width, text='Gearbox Outputs')
        label_t = tk.Label(frame_main, width=label_width, text='Torque')
        label_p = tk.Label(frame_main, width=label_width, text='Power')
        label_rs = tk.Label(frame_main, width=label_width, text='Rotational Speed')
        label_r = tk.Label(frame_main, width=label_width, text='Ratio (x:1)')
        label_e = tk.Label(frame_main, width=label_width, text='Efficiency (%)')
        self.entry_t = tk.Entry(frame_main, width=entry_width)
        self.entry_p = tk.Entry(frame_main, width=entry_width)
        self.entry_rs = tk.Entry(frame_main, width=entry_width)
        self.entry_r = tk.Entry(frame_main, width=entry_width)
        self.entry_e = tk.Entry(frame_main, width=entry_width)
        sv_t, sv_p, sv_rs = StringVar(), StringVar(), StringVar()
        options_t = ttk.OptionMenu(frame_main, sv_t, Units().torque[0], *Units().torque)
        options_p = ttk.OptionMenu(frame_main, sv_p, Units().power[0], *Units().power)
        options_rs = ttk.OptionMenu(frame_main, sv_rs, Units().rotational_speed[0], *Units().rotational_speed)
        # Positioning all of these widgets
        labelGearbox.grid(row=0, column=0, columnspan=6, padx=pad_ext, pady=pad_ext)
        label_t.grid(row=1, column=0, columnspan=2, padx=pad_ext, pady=(pad_ext, 0))
        label_p.grid(row=1, column=2, columnspan=2, padx=pad_ext, pady=(pad_ext, 0))
        label_rs.grid(row=1, column=4, columnspan=2, padx=pad_ext, pady=(pad_ext, 0))
        label_r.grid(row=1, column=6, padx=pad_ext, pady=(pad_ext, 0))
        label_e.grid(row=1, column=7, padx=pad_ext, pady=(pad_ext, 0))
        self.entry_t.grid(row=2, column=0, padx=pad_ext, pady=pad_ext)
        self.entry_p.grid(row=2, column=2, padx=pad_ext, pady=pad_ext)
        self.entry_rs.grid(row=2, column=4, padx=pad_ext, pady=pad_ext)
        self.entry_r.grid(row=2, column=6, padx=pad_ext, pady=pad_ext)
        self.entry_e.grid(row=2, column=7, padx=pad_ext, pady=pad_ext)
        options_t.grid(row=2, column=1, padx=(0, 2*pad_ext), pady=pad_ext)
        options_p.grid(row=2, column=3, padx=(0, 2*pad_ext), pady=pad_ext)
        options_rs.grid(row=2, column=5, padx=(0, 2*pad_ext), pady=pad_ext)
        # Bindings for the Entries
        self.entry_t.bind('<Return>', lambda event: self.gearboxDisplay('T', self.entry_t.get(), sv_t.get(), self.entry_p.get(), sv_p.get(), self.entry_rs.get(), sv_rs.get(), self.entry_r.get(), self.entry_e.get()))
        self.entry_p.bind('<Return>', lambda event: self.gearboxDisplay('P', self.entry_t.get(), sv_t.get(), self.entry_p.get(), sv_p.get(), self.entry_rs.get(), sv_rs.get(), self.entry_r.get(), self.entry_e.get()))
        self.entry_rs.bind('<Return>', lambda event: self.gearboxDisplay('RS', self.entry_t.get(), sv_t.get(), self.entry_p.get(), sv_p.get(), self.entry_rs.get(), sv_rs.get(), self.entry_r.get(), self.entry_e.get()))
        self.entry_r.bind('<Return>', lambda event: self.gearboxDisplay('R', self.entry_t.get(), sv_t.get(), self.entry_p.get(), sv_p.get(), self.entry_rs.get(), sv_rs.get(), self.entry_r.get(), self.entry_e.get()))
        self.entry_e.bind('<Return>', lambda event: self.gearboxDisplay('E', self.entry_t.get(), sv_t.get(), self.entry_p.get(), sv_p.get(), self.entry_rs.get(), sv_rs.get(), self.entry_r.get(), self.entry_e.get()))


    def gearboxDisplay(self, entry, t_qty, t_unit, p_qty, p_unit, rs_qty, rs_unit, r_qty, e_qty):
        # To provide a dummy value for the calculations to be performed
        if entry == 'T':
            t_qty = 1
        if entry == 'P':
            p_qty = 1
        if entry == 'RS':
            rs_qty = 1
        if entry == 'R':
            r_qty = 1
        if entry == 'E':
            e_qty = 1

        answers = gearboxCalculations(t_qty, t_unit, p_qty, p_unit, rs_qty, rs_unit, r_qty, e_qty)

        if entry == 'T':
            self.entry_t.delete(0, tk.END)
            self.entry_t.insert(0, f"{answers['T']:.3f}")
        if entry == 'P':
            self.entry_p.delete(0, tk.END)
            self.entry_p.insert(0, f"{answers['P']:.3f}")
        if entry == 'RS':
            self.entry_rs.delete(0, tk.END)
            self.entry_rs.insert(0, f"{answers['RS']:.3f}")
        if entry == 'R':
            self.entry_r.delete(0, tk.END)
            self.entry_r.insert(0, f"{answers['R']:.3f}")
        if entry == 'E':
            self.entry_e.delete(0, tk.END)
            self.entry_e.insert(0, f"{answers['E']:.3f}")


def gearboxCalculations(t_qty, t_unit, p_qty, p_unit, rs_qty, rs_unit, r_qty, e_qty):
    # To convert all the given units into their S.I unit equivalents
    t_si = torqueToNm(t_unit, t_qty)
    p_si = powerToW(p_unit, p_qty)
    rs_si = rotationalSpeedTorads(rs_unit, rs_qty)
    r_si = r_qty
    e_si = e_qty

    # To make a symbolic equation for this
    T, P, RS, R, E = symbols('T P RS R E')
    equation = -T + (P * R * (E/100))/RS

    # To make different equations for each variable
    t_eq = solve(equation, T)[0]
    p_eq = solve(equation, P)[0]
    rs_eq = solve(equation, RS)[0]
    r_eq = solve(equation, R)[0]
    e_eq = solve(equation, E)[0]

    # To sub the given values into each equation
    t_calc = t_eq.subs({P:p_si, RS:rs_si, R:r_si, E:e_si})
    p_calc = p_eq.subs({T:t_si, RS:rs_si, R:r_si, E:e_si})
    rs_calc = rs_eq.subs({T:t_si, P:p_si, R:r_si, E:e_si})
    r_calc = r_eq.subs({T:t_si, P:p_si, RS:rs_si, E:e_si})
    e_calc = e_eq.subs({T:t_si, P:p_si, RS:rs_si, R:r_si})

    # To change the values back into the user selected unit
    t_conv = torqueFromNm(t_calc)[t_unit]
    p_conv = powerFromW(p_calc)[p_unit]
    rs_conv = rotationalSpeedFromrads(rs_calc)[rs_unit]
    r_conv = r_calc
    e_conv = e_calc

    return {'T':t_conv, 'P':p_conv, 'RS':rs_conv, 'R':r_conv, 'E':e_conv}
