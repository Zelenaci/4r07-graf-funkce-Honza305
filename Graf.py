#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:00:39 2019

@author: mah35070
"""

import tkinter as tk
from tkinter import LabelFrame, Radiobutton, Label, 



class Application(tk.Tk):
    name = 'Grafy'

    def __init__(self):
        super().__init__(className=self.name)
        
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        
        self.lblffce = LabelFrame(self, text="Graf matematické funkce", padx=5, pady=5)
        self.lblffce.grid(column = 1, row = 1)
        
        self.lblfce = Label(self.lblffce)
        self.lblfce.grid(row= 1, column = 1)
        
        self.v = IntVar()
        
        self.radsin = Radiobutton(self.lblfce, text="sin" , variable=self.v, value=0)
        self.radsin.grid(column=1, row=1)
        
        self.radlog = Radiobutton(self.lblfce, text="log" , variable=self.v, value=1)
        self.radlog.grid(column=1, row=2)
        
        self.radexp = Radiobutton(self.lblfce, text="exp" , variable=self.v, value=2)
        self.radexp.grid(column=1, row=3)
        
        self.lblod = Label(self.lblffce)
        self.lbod.grid(row=1, column = 2)
        
        self.msgo = Message(self.lblod, text = "Od")
        self.msgo.grid(row = 1 , column = 1)
        
        
        
        
        