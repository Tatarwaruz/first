import tkinter as tk
from tkinter import ttk
from math import sqrt


class Calculator:
    def __init__ (self, master):
        self.master = master
        self.master.title("Калькулятор")
        self.master.geometry("380x140")

        self.number_enty = ttk.Entry(self.master, width=20)
        self.number_enty.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        self.button_1 = ttk.Button(self.master, text="1", command=lambda: self.button_click(1))
        self.button_2 = ttk.Button(self.master, text="2", command=lambda: self.button_click(2))
        self.button_3 = ttk.Button(self.master, text="3", command=lambda: self.button_click(3))
        self.button_4 = ttk.Button(self.master, text="4", command=lambda: self.button_click(4))
        self.button_5 = ttk.Button(self.master, text="5", command=lambda: self.button_click(5))
        self.button_6 = ttk.Button(self.master, text="6", command=lambda: self.button_click(6))
        self.button_7 = ttk.Button(self.master, text="7", command=lambda: self.button_click(7))
        self.button_8 = ttk.Button(self.master, text="8", command=lambda: self.button_click(8))
        self.button_9 = ttk.Button(self.master, text="9", command=lambda: self.button_click(9))
        self.button_0 = ttk.Button(self.master, text="0", command=lambda: self.button_click(0))
        self.button_clear = ttk.Button(self.master, text="C", command=self.button_clear)
        self.button_add = ttk.Button(self.master, text="+", command=self.button_add)
        self.button_equal = ttk.Button(self.master, text="=", command=self.button_equal)
        self.button_subtract = ttk.Button(self.master, text="-", command=self.button_subtract)
        self.button_multiply = ttk.Button(self.master, text="*", command=self.button_multiply)
        self.button_divide = ttk.Button(self.master, text="/", command=self.button_divide)
        self.button_floor_div = ttk.Button(self.master, text="//", command=self.button_floor_div)
        self.button_modulus = ttk.Button(self.master, text="%", command=self.button_modulus)
        self.button_sqrt = ttk.Button(self.master, text="√", command=self.button_sqrt)
        self.button_neg = ttk.Button(self.master, text="+/-", command=self.button_neg)

        self.button_1
        self.button_2
        self.button_3
        self.button_add
        self.button_floor_div

        self.button_4
        self.button_5
        self.button_6
        self.button_substract
        self.button_modulus

        self.button_7
        self.button_8
        self.button_9
        self.button_multiply
        self.button_sqrt

        self.button_clear
        self.button_0
        self.button_equal
        self.button_divide
        self.button_neg

        self.f_num = 0
        self.math = ""
